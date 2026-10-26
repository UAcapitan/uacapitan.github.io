# Usefulsoc website

The public studio website at https://uacapitan.github.io/. A responsive, buildless static site, hosted by GitHub Pages from the root of `main` in `UAcapitan/uacapitan.github.io`.

## Preview

From this directory, run:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173/. There are no packages to install. All game links and content work without JavaScript; JavaScript adds genre filters, local search, and the mobile menu. The website contains no analytics or advertising scripts.

## Update games

The existing [games.json](games.json) is also consumed by the games’ cross-promotion features. Preserve its schema and existing URLs. Update that catalog and add the corresponding icon to [images](images/), then regenerate the static cards:

```sh
python3 tools/build_catalog.py
```

Update the game-count badge and page description if the published game count changes. Highway Hustle is presented separately as in development because it is not in the published catalog. Update this when released.

## Privacy page

[usefulsoc-privacy/index.html](usefulsoc-privacy/index.html) is the local source copy. **The live URL is served by the separate `UAcapitan/usefulsoc-privacy` project repository**, which GitHub Pages prioritizes over the same directory in this repository. Publish identical policy HTML as `index.html` in that repository when editing the policy. It shares the CSS, fonts, and mark from this website’s `/assets/` directory.

The October 2026 policy was reconciled with the current local game analytics client and backend documentation, including random installation identifiers, activity/session collection, the limited onboarding and cross-promotion events, retention targets, and AdMob. Revisit the text whenever actual data practices change.

## Advertising files

- [app-ads.txt](app-ads.txt): the original Google AdMob publisher record, preserved verbatim.
- [ads.txt](ads.txt): the seven OneTag and reseller entries supplied by the owner on 26 October 2026. Publishing this file does not itself add advertising to the website.

Keep both as plain text at the domain root and publicly crawlable. Do not insert HTML or redirect them to a web page.

## Publishing

Commit the site changes and push `main` to `origin`. GitHub Pages is already configured to publish the repository root. Check the Pages build and public URLs after each push.

Fonts are self-hosted DM Sans and Space Grotesk under the SIL Open Font License; license files are included in [assets/fonts](assets/fonts/). Game artwork belongs to the existing Usefulsoc catalog. The logo mark and site design are vector/CSS assets.
