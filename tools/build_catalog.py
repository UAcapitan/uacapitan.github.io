"""Regenerate the static, no-JavaScript game cards from the shared app catalog."""
from pathlib import Path
import html, json
from urllib.parse import urlparse
root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "games.json").read_text())
cards = []
for game in catalog["games"]:
    if not game.get("enabled"):
        continue
    name = html.escape(game["name"])
    tags = game.get("tags", [])
    genre = "idle" if "IDLE" in tags else "arcade" if "ARCADE" in tags or "ACTION" in tags else "puzzle"
    color = {"idle":"mint", "arcade":"lavender", "puzzle":"peach"}[genre]
    icon = urlparse(game["icon"]).path.lstrip("/")
    assert (root / icon).is_file(), f"Missing game artwork: {icon}"
    url = game["google_play"]
    assert url.startswith("https://play.google.com/store/apps/details?id="), "Invalid store link"
    labels = " · ".join(t.title() for t in tags if t not in ["FREE", "CASUAL", "OFFLINE"])
    cards.append(f'''<article class="game-card" data-genre="{genre}" data-search="{html.escape(game['name'].lower(), quote=True)}"><a class="game-art {color}" href="{html.escape(url, quote=True)}" target="_blank" rel="noopener" aria-label="Get {name} on Google Play"><img src="{icon}" alt="" width="160" height="160" loading="lazy"><span class="game-launch" aria-hidden="true">↗</span></a><div class="game-meta"><span>{html.escape(labels)}</span><span>Android</span></div><h3><a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener">{name}</a></h3><p>{html.escape(game['description'])}</p><a class="game-store" href="{html.escape(url, quote=True)}" target="_blank" rel="noopener">Get it on Google Play <span aria-hidden="true">↗</span></a></article>''')
page = root / "index.html"
content = page.read_text()
start, end = "<!-- GAMES:START -->", "<!-- GAMES:END -->"
content = content.split(start)[0] + start + "\n" + "\n".join(cards) + "\n" + end + content.split(end)[1]
page.write_text(content)
print(f"Generated {len(cards)} published game cards.")
