#!/usr/bin/env python3
"""Build meme.png for gta6-meme-x-01: Vice City background + official
make.fun ghost mark + top/bottom meme text. Run from the entry repo dir.
Inputs: media-generation-gta6-meme-bg-0-*.png (generated in-session),
/tmp/mark-1024.png (official make.fun press-kit mark). Output: meme.png
1024x1024, the picture posted on X as the entry's first image."""

from PIL import Image, ImageDraw, ImageFont, ImageFilter

BG = "media-generation-gta6-meme-bg-0-3748ec21-c980-4f68-a3fc-f8a906e2d181.png"
GHOST = "/tmp/mark-1024.png"
OUT = "meme.png"
SIZE = 1024

bg = Image.open(BG).convert("RGB")
# Centre-crop to a square if the generator ever returns another ratio.
w, h = bg.size
side = min(w, h)
bg = bg.crop(((w - side) // 2, (h - side) // 2,
              (w + side) // 2, (h + side) // 2)).resize((SIZE, SIZE))

# Darken top and bottom bands so the white meme text stays readable.
shade = Image.new("L", (SIZE, SIZE), 0)
sd = ImageDraw.Draw(shade)
for y in range(240):
    a = int(150 * (1 - y / 240))
    sd.line([(0, y), (SIZE, y)], fill=a)
for y in range(SIZE - 240, SIZE):
    a = int(150 * ((y - (SIZE - 240)) / 240))
    sd.line([(0, y), (SIZE, y)], fill=a)
black = Image.new("RGB", (SIZE, SIZE), (0, 0, 0))
bg = Image.composite(black, bg, shade)

# Official ghost mark, centred, big enough to recognise at 480 px.
ghost = Image.open(GHOST).convert("RGBA").resize((400, 400))
canvas = bg.convert("RGBA")
# White ring + soft shadow so the magenta disc pops off the street scene.
ring = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
rd = ImageDraw.Draw(ring)
rd.ellipse([306, 274, 718, 686], fill=(0, 0, 0, 160))
rd.ellipse([312, 280, 712, 680], outline=(255, 255, 255, 255), width=10)
canvas = Image.alpha_composite(canvas, ring)
canvas.paste(ghost, (312, 280), ghost)

draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 62)


def text_line(line, y):
    bbox = draw.textbbox((0, 0), line, font=font, stroke_width=4)
    tw = bbox[2] - bbox[0]
    draw.text(((SIZE - tw) / 2, y), line, font=font, fill="white",
              stroke_width=4, stroke_fill="black")


text_line("IN GTA 6 I ROB BANKS", 46)
text_line("FOR MONEY", 122)
text_line("MY AGENT EARNS IT", 800)
text_line("ON MAKE.FUN", 876)

canvas.convert("RGB").save(OUT, "PNG", optimize=True)
print("wrote", OUT)
