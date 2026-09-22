"""Family icons for the Store: one colour per Actor, a white pictogram, the same rounded tile. 512x512 PNG.

    python assets/make_icons.py   # writes assets/icons/<actor>.png
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / 'icons'
FONT = 'C:/Windows/Fonts/segoeuib.ttf'
SIZE = 512
STROKE = 34
WHITE = (255, 255, 255, 255)

COLOURS = {
    'sitemap-url-extractor': ('#1f6feb', '#9ecbff'),
    'broken-link-checker': ('#d1242f', '#ffb3b8'),
    'feed-monitor': ('#e36209', '#ffd8a8'),
    'web-hygiene-mcp': ('#6f42c1', '#d2b8ff'),
    'citation-verifier': ('#1a7f37', '#a6f0c0'),
    'sec-form-d-funding-leads': ('#0f5e75', '#9be3f7'),
    'ebay-cross-market-finder': ('#b35900', '#ffd18a'),
}


def tile(bg: str, accent: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, SIZE - 1, SIZE - 1), radius=96, fill=bg)
    d.rounded_rectangle((96, 436, SIZE - 96, 456), radius=10, fill=accent)   # family mark
    return img, d


def line(d, a, b, w=STROKE):
    d.line([a, b], fill=WHITE, width=w)
    r = w // 2
    for x, y in (a, b):
        d.ellipse((x - r, y - r, x + r, y + r), fill=WHITE)


def dot(d, c, r):
    d.ellipse((c[0] - r, c[1] - r, c[0] + r, c[1] + r), fill=WHITE)


def ring(d, c, r, w=STROKE):
    d.ellipse((c[0] - r, c[1] - r, c[0] + r, c[1] + r), outline=WHITE, width=w)


# ------------------------------------------------------------------ pictograms

def sitemap(d):
    """A site tree: root page, three children, connectors."""
    root = (256, 120)
    kids = [(128, 320), (256, 320), (384, 320)]
    line(d, root, (256, 220), 26)
    line(d, (128, 220), (384, 220), 26)
    for k in kids:
        line(d, (k[0], 220), k, 26)
    for c, s in ((root, 56), *((k, 46) for k in kids)):
        d.rounded_rectangle((c[0] - s, c[1] - s * 0.8, c[0] + s, c[1] + s * 0.8), radius=18, fill=WHITE)
        d.rounded_rectangle((c[0] - s + 16, c[1] - s * 0.8 + 16, c[0] + s - 16, c[1] - s * 0.8 + 30), radius=6, fill=d._image.getpixel((5, 256)))


def broken_link(d):
    """Two chain links pulled apart, a crack between them."""
    a, b = (170, 250), (342, 250)
    for c in (a, b):
        d.rounded_rectangle((c[0] - 92, c[1] - 52, c[0] + 92, c[1] + 52), radius=52, outline=WHITE, width=STROKE)
    bg = d._image.getpixel((5, 256))
    d.rectangle((228, 170, 284, 330), fill=bg)              # gap
    # crack: two bolts
    for off in (-60, 60):
        pts = [(256 + off // 3, 190), (240 + off // 3, 235), (268 + off // 3, 255), (250 + off // 3, 310)]
        d.line(pts, fill=WHITE, width=18, joint='curve')


def rss(d):
    c = (150, 340)
    dot(d, c, 40)
    for r in (150, 250):
        d.arc((c[0] - r, c[1] - r, c[0] + r, c[1] + r), start=270, end=360, fill=WHITE, width=STROKE + 8)


def plug(d):
    """MCP: a plug — the protocol that connects models to tools."""
    body = (176, 200, 336, 340)
    d.rounded_rectangle(body, radius=36, fill=WHITE)
    bg = d._image.getpixel((5, 256))
    for x in (222, 290):
        d.rounded_rectangle((x - 16, 110, x + 16, 210), radius=14, fill=WHITE)
    d.rounded_rectangle((236, 340, 276, 412), radius=14, fill=WHITE)
    # spark lines
    for x, dx in ((150, -1), (362, 1)):
        d.line([(x, 250), (x + dx * 40, 250)], fill=WHITE, width=14)
        d.line([(x, 290), (x + dx * 28, 290)], fill=WHITE, width=14)
    d.ellipse((236, 250, 276, 290), fill=bg)


def citation(d):
    """Quotation marks with a check mark: the quote is really there."""
    font = ImageFont.truetype(FONT, 300)
    d.text((70, 30), '\u201c', font=font, fill=WHITE)
    line(d, (250, 300), (312, 362), 40)
    line(d, (312, 362), (430, 200), 40)


def form_d(d):
    """A filing page with a folded corner and a dollar sign."""
    pts = [(150, 90), (320, 90), (380, 150), (380, 400), (150, 400)]
    d.polygon(pts, fill=WHITE)
    bg = d._image.getpixel((5, 256))
    d.polygon([(320, 90), (320, 150), (380, 150)], fill=bg)
    font = ImageFont.truetype(FONT, 190)
    box = d.textbbox((0, 0), '$', font=font)
    d.text(((530 - (box[2] - box[0])) / 2 - box[0], 300 - (box[3] - box[1]) / 2 - box[1] - 30), '$', font=font, fill=bg)
    for y in (125, 152):
        d.rounded_rectangle((180, y, 290, y + 12), radius=6, fill=bg)


def euro_dollar(d):
    font = ImageFont.truetype(FONT, 230)
    box = d.textbbox((0, 0), '€$', font=font)
    w, h = box[2] - box[0], box[3] - box[1]
    d.text(((SIZE - w) / 2 - box[0], (400 - h) / 2 - box[1] + 6), '€$', font=font, fill=WHITE)
    # exchange arrows under the symbols
    line(d, (150, 372), (362, 372), 16)
    d.polygon([(150, 372), (186, 350), (186, 394)], fill=WHITE)
    d.polygon([(362, 372), (326, 350), (326, 394)], fill=WHITE)


PICTOGRAMS = {
    'sitemap-url-extractor': sitemap, 'broken-link-checker': broken_link, 'feed-monitor': rss, 'web-hygiene-mcp': plug,
    'citation-verifier': citation, 'sec-form-d-funding-leads': form_d, 'ebay-cross-market-finder': euro_dollar,
}


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (bg, accent) in COLOURS.items():
        img, d = tile(bg, accent)
        PICTOGRAMS[name](d)
        path = OUT / f'{name}.png'
        img.save(path, optimize=True)
        print(path)
