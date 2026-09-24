#!/usr/bin/env python3
"""Notify IndexNow only after the canonical page and ownership file are live."""
import hashlib
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://klelectricienidf.fr"
PAGES = [(ORIGIN + "/", ROOT / "index.html"),
         (ORIGIN + "/electricien-bailly.html", ROOT / "electricien-bailly.html")]
KEY_URL = ORIGIN + "/indexnow-key.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"


def main():
    key = (ROOT / "indexnow-key.txt").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9a-f]{32}", key):
        raise ValueError("Invalid IndexNow ownership key format")
    context = ssl.create_default_context()
    for url, path in [(KEY_URL, ROOT / "indexnow-key.txt"), *PAGES]:
        request = urllib.request.Request(url, headers={"Cache-Control": "no-cache"})
        with urllib.request.urlopen(request, timeout=20, context=context) as response:
            if response.status != 200 or response.url != url:
                raise ValueError("Canonical ownership or page URL is not directly available")
            actual = response.read(path.stat().st_size + 1)
        if hashlib.sha256(actual).digest() != hashlib.sha256(path.read_bytes()).digest():
            raise ValueError("Public content differs from this deployment; notification skipped")
    payload = {"host": "klelectricienidf.fr", "key": key,
               "keyLocation": KEY_URL, "urlList": [url for url, _ in PAGES]}
    if "--dry-run" in sys.argv:
        print("Public ownership file and pages verified; no IndexNow notification sent.")
        return
    request = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode("utf-8"),
                                    headers={"Content-Type": "application/json; charset=utf-8"},
                                    method="POST")
    with urllib.request.urlopen(request, timeout=30, context=context) as response:
        status = response.status
    if status not in (200, 202):
        raise ValueError(f"Unexpected IndexNow response: HTTP {status}")
    message = ("URL notification received" if status == 200
               else "URL notification received; ownership key validation pending")
    print(f"IndexNow HTTP {status}: {message}. This does not prove indexing or ranking.")


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as error:
        sys.exit(f"IndexNow notification failed: HTTP {error.code}; site deployment is unaffected.")
    except (OSError, ValueError) as error:
        sys.exit(f"IndexNow notification not completed: {error}")
