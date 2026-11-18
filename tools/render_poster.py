#!/usr/bin/env python3
"""Render the news poster for 17 November 2026 (1024x1024, deterministic).

Run: python3 tools/render_poster.py  -> writes assets/poster.png
Pure PIL, no network, no timestamps, no randomness: identical bytes every run.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (20, 20, 20)
RED = (163, 22, 33)
GRAY = (90, 86, 78)
RULE = (20, 20, 20)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, y, text, fnt, fill, max_w=None):
    if max_w is not None:
        lines = wrap(draw, text, fnt, max_w)
    else:
        lines = [text]
    for line in lines:
        w = draw.textlength(line, font=fnt)
        draw.text(((W - w) / 2, y), line, font=fnt, fill=fill)
        y += fnt.size + 6
    return y


def draw_block(draw, x, y, w, kicker, headline, summary, head_size, sum_size,
               head_font=SERIF, sum_font=SANS):
    f_kick = font(SANS_BOLD, 15)
    f_head = font(head_font, head_size)
    f_sum = font(sum_font, sum_size)
    draw.text((x, y), kicker, font=f_kick, fill=RED)
    y += 24
    for line in wrap(draw, headline, f_head, w):
        draw.text((x, y), line, font=f_head, fill=INK)
        y += head_size + 7
    y += 2
    for line in wrap(draw, summary, f_sum, w):
        draw.text((x, y), line, font=f_sum, fill=(52, 50, 46))
        y += sum_size + 6
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 44  # margin
    x0, x1 = M, W - M
    cw = x1 - x0

    # ---- top double rule ----
    d.line([(x0, 30), (x1, 30)], fill=RULE, width=3)
    d.line([(x0, 36), (x1, 36)], fill=RULE, width=1)

    # ---- masthead ----
    y = 48
    f_kick = font(SANS_BOLD, 16)
    kick = "T H E   D A Y   I N   R E V I E W"
    w = d.textlength(kick, font=f_kick)
    d.text(((W - w) / 2, y), kick, font=f_kick, fill=GRAY)
    y += 30
    f_title = font(SERIF, 58)
    title = "THE WORLD IN ONE IMAGE"
    w = d.textlength(title, font=f_title)
    d.text(((W - w) / 2, y), title, font=f_title, fill=INK)
    y += 78
    # date line with side rules
    f_date = font(SANS_BOLD, 19)
    date = "TUESDAY, 17 NOVEMBER 2026"
    dw = d.textlength(date, font=f_date)
    mid = W / 2
    d.line([(x0, y + 10), (mid - dw / 2 - 18, y + 10)], fill=RULE, width=1)
    d.line([(mid + dw / 2 + 18, y + 10), (x1, y + 10)], fill=RULE, width=1)
    d.text((mid - dw / 2, y), date, font=f_date, fill=RED)
    y += 38
    d.line([(x0, y), (x1, y)], fill=RULE, width=3)
    y += 16

    # ---- lead story ----
    y = draw_block(
        d, x0, y, cw,
        "WAR IN EUROPE  \u2014  LEAD STORY",
        "Ukraine hits Crimea Bridge again as Russia strikes Kyiv\u2019s bridges",
        "A second Ukrainian strike in under 24 hours collapsed part of the Kerch bridge "
        "to occupied Crimea. Russian missiles hit Kyiv\u2019s bridges over the Dnipro, "
        "cutting heat, water and power.",
        head_size=37, sum_size=19)
    y += 10
    d.line([(x0, y), (x1, y)], fill=RULE, width=1)
    y += 14

    # ---- 2x2 grid, stories 2-5 ----
    gap = 28
    col_w = (cw - gap) // 2
    row_h = 188
    stories = [
        ("MIDDLE EAST  \u2014  ENERGY & SHIPPING",
         "Tankers hit by mines near Hormuz as third U.S. carrier arrives",
         "Two oil tankers caught fire after striking mines near the Strait of Hormuz. "
         "The USS Theodore Roosevelt joined two U.S. carriers already in the region."),
        ("DIPLOMACY  \u2014  APEC, SHENZHEN",
         "Trump, Xi and Putin to meet in Shenzhen on Thursday",
         "China confirmed the first three-way summit of the three leaders, on the "
         "sidelines of the APEC meeting, with nuclear risks and Ukraine on the agenda."),
        ("MIGRATION  \u2014  EUROPE",
         "Five European nations plan joint return hub in Rwanda",
         "Germany, Denmark, Austria, Greece and the Netherlands unveiled a shared "
         "facility for rejected asylum seekers, amid questions over its legality."),
        ("ASIA-PACIFIC  \u2014  TOKYO",
         "Japan scrambles jets as Russian planes breach its airspace",
         "Tokyo lodged a stern protest after two suspected Russian aircraft violated "
         "Japanese airspace early on Tuesday."),
    ]
    gy = y
    for i, (kick, head, summ) in enumerate(stories):
        cx = x0 + (i % 2) * (col_w + gap)
        cy = gy + (i // 2) * row_h
        draw_block(d, cx, cy, col_w, kick, head, summ, head_size=23, sum_size=16)
        if i % 2 == 0:
            d.line([(cx + col_w + gap // 2, cy + 4),
                    (cx + col_w + gap // 2, cy + row_h - 18)], fill=(200, 194, 182), width=1)
    y = gy + 2 * row_h
    d.line([(x0, y - 6), (x1, y - 6)], fill=RULE, width=1)
    y += 8

    # ---- bottom strip, story 6 ----
    y = draw_block(
        d, x0, y, cw,
        "UNITED STATES  \u2014  WASHINGTON",
        "Pentagon fails financial audit for ninth straight year",
        "Auditors again could not verify accounts covering more than $4.8 trillion in assets.",
        head_size=23, sum_size=16)
    y += 8
    d.line([(x0, y), (x1, y)], fill=RULE, width=1)
    y += 12
    # ---- in brief: three more stories ----
    f_brief_kick = font(SANS_BOLD, 15)
    d.text((x0, y), "IN BRIEF", font=f_brief_kick, fill=RED)
    y += 26
    briefs = [
        ("Depardieu pleads guilty",
         "French actor Gérard Depardieu admitted a sexual assault charge in a Paris court."),
        ("Measles at 35-year high",
         "Thirteen babies were born with measles as U.S. cases hit their highest since 1991."),
        ("Sudan: 1,390 civilians killed",
         "A UN report counted at least 1,390 civilians killed in the first half of 2026."),
    ]
    bw = (cw - 2 * gap) // 3
    f_bh = font(SERIF, 17)
    f_bs = font(SANS, 14)
    brief_top = y
    brief_bottom = y
    for i, (bh, bs) in enumerate(briefs):
        bx = x0 + i * (bw + gap)
        by = y
        for line in wrap(d, bh, f_bh, bw):
            d.text((bx, by), line, font=f_bh, fill=INK)
            by += 22
        for line in wrap(d, bs, f_bs, bw):
            d.text((bx, by), line, font=f_bs, fill=(52, 50, 46))
            by += 18
        brief_bottom = max(brief_bottom, by)
    y = brief_bottom + 12
    d.line([(x0, y), (x1, y)], fill=RULE, width=3)
    y += 12
    f_foot = font(SANS, 14)
    foot = "Compiled from wire and press reports filed on 17 November 2026  \u00b7  Six stories, one day, one image"
    w = d.textlength(foot, font=f_foot)
    d.text(((W - w) / 2, y), foot, font=f_foot, fill=GRAY)

    out = os.path.join(ROOT, "assets", "poster.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
