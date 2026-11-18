#!/usr/bin/env python3
"""Entry for make.fun competition news-image-20261117.

Copies the pre-rendered poster (assets/poster.png, drawn by
tools/render_poster.py from the real news of Tuesday 17 November 2026)
to /output/entry.png. Standard library only, no network, deterministic:
the same bytes are written on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "assets", "poster.png")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
print("wrote", DST)
