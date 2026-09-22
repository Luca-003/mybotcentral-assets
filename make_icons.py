"""Family icons for the Store: one colour per Actor, a bold monogram, the same rounded tile. 512x512 PNG.

    python assets/make_icons.py   # writes assets/icons/<actor>.png
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / 'icons'
FONT = 'C:/Windows/Fonts/segoeuib.ttf'
# actor -> (monogram, background hex, accent hex)
ICONS = {
    'sitemap-url-extractor': ('SM', '#1f6feb', '#9ecbff'),
    'broken-link-checker': ('BL', '#d1242f', '#ffb3b8'),
    'feed-monitor': ('RSS', '#e36209', '#ffd8a8'),
    'web-hygiene-mcp': ('MCP', '#6f42c1', '#d2b8ff'),
    'citation-verifier': ('CV', '#1a7f37', '#a6f0c0'),
    'sec-form-d-funding-leads': ('FD', '#0f5e75', '#9be3f7'),
    'ebay-cross-market-finder': ('€$', '#b35900', '#ffd18a'),
}


def make(name: str, text: str, bg: str, accent: str) -> Path:
    size = 512
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, size - 1, size - 1), radius=96, fill=bg)
    # family mark: a thin accent bar at the bottom, same on every icon
    d.rounded_rectangle((96, 420, size - 96, 444), radius=12, fill=accent)
    font_size = 250 if len(text) <= 2 else 190
    font = ImageFont.truetype(FONT, font_size)
    box = d.textbbox((0, 0), text, font=font)
    w, h = box[2] - box[0], box[3] - box[1]
    d.text(((size - w) / 2 - box[0], (400 - h) / 2 - box[1] + 10), text, font=font, fill='white')
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f'{name}.png'
    img.save(path, optimize=True)
    return path


if __name__ == '__main__':
    for name, (text, bg, accent) in ICONS.items():
        print(make(name, text, bg, accent))
