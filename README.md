# KL Électricien IDF — Kénido Louissaint

Site officiel : **https://klelectricienidf.fr/**

Kénido Louissaint est un électricien indépendant intervenant en Île-de-France pour le dépannage, l’installation et la rénovation électrique. Contact professionnel : **06 03 22 51 63** — [WhatsApp](https://wa.me/33603225163).

Les réalisations présentées comprennent le passage de câbles, l’intervention sur une armoire électrique, la préparation des points électriques, la pose de prises et les raccordements.

Pour la peinture, la menuiserie et les finitions après les travaux électriques, Kénido coordonne le relais avec **[L&G Réno](https://www.lgrenonoisy.fr/)**. Les deux entreprises restent des intervenants distincts.

## Fonctionnement

Site statique en français, galerie animée au défilement, photographies de chantier, parcours professionnel et contact direct par téléphone ou WhatsApp. Aucune mesure d’audience, publicité ou collecte par formulaire n’est ajoutée.

- HTML, styles et interactions : `index.html`.
- Exploration : `robots.txt` et `sitemap.xml`.
- Données structurées : identité, personne, services et entreprise partenaire distincte, cohérentes avec les textes du site.
- `indexnow-key.txt` est une preuve de propriété publique pour IndexNow, pas un mot de passe.
- `scripts/notify-indexnow.py` notifie l’accueil après vérification de sa publication. Une notification reçue ne prouve ni l’indexation ni le classement.
- `seo-apache.conf` fournit uniquement le bloc de redirections géré, fusionné sans supprimer la configuration existante de l’hébergement.

## Publication

L’hébergement public est OVH. La branche de publication est `codex/site-preview`. Les corrections sont préparées sur une branche dédiée et proposées par pull request ; `main` n’est pas la branche de production.

Le déploiement conserve les fichiers précédents, publie les ressources avant l’accueil et vérifie les fichiers servis en HTTPS. Les variantes HTTP, `www` et `/index.html` doivent rediriger vers l’adresse canonique. Les secrets d’hébergement restent dans GitHub Actions et ne font pas partie du site.

L’adresse utilisée pour la validation Google Business Profile reste privée et n’est pas publiée dans ce dépôt ni dans les données structurées. Les informations administratives restant à compléter dans les mentions légales doivent être fournies par l’entrepreneur ; elles ne sont pas inventées.
