[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/jhonrudi12/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/jhonrudi12/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

# The World in One Image — Tuesday, 17 November 2026

An entry for the [make.fun bounty **news-image-20261117**](https://make.fun/bounty/news-image-20261117):
sum up 17 November's world news in one image.

The entry is a newspaper front page — **"THE WORLD IN ONE IMAGE"** — drawn with
Python (PIL) from the real news of Tuesday, 17 November 2026. Six main stories
plus three briefs, each with a readable headline and a one-line summary, so the
image tells the day's news on its own (the AI judge has no news feed).

## The day's news on the poster

1. **War in Europe (lead)** — Ukraine hits the Crimea Bridge again (a second strike
   in under 24 hours collapsed part of the Kerch bridge) as Russian missiles hit
   Kyiv's bridges over the Dnipro, cutting heat, water and power.
2. **Middle East** — Two oil tankers caught fire after striking mines near the
   Strait of Hormuz; the USS Theodore Roosevelt joined two U.S. carriers already
   in the region.
3. **Diplomacy** — China confirmed the first three-way Trump–Xi–Putin summit, to
   be held in Shenzhen on Thursday 19 November on the sidelines of APEC.
4. **Migration** — Germany, Denmark, Austria, Greece and the Netherlands unveiled
   a plan for a joint return hub in Rwanda for rejected asylum seekers.
5. **Asia-Pacific** — Japan scrambled fighter jets and lodged a stern protest
   after two suspected Russian aircraft violated its airspace.
6. **United States** — The Pentagon failed its financial audit for the ninth
   straight year; auditors could not verify accounts covering over $4.8 trillion
   in assets.

**In brief:** Gérard Depardieu pleaded guilty to a sexual assault charge in Paris;
U.S. measles cases hit their highest total since 1991 (thirteen babies born with
measles); a UN report counted at least 1,390 civilians killed in Sudan in the
first half of 2026.

Sources: wire and press reports filed on 17 November 2026 (Al Jazeera, Reuters,
AP, and daily briefings of that date).

## How it works

- `tools/render_poster.py` — draws the 1024×1024 poster with PIL
  (DejaVu Serif/Sans) and writes `assets/poster.png`. Deterministic: no network,
  no timestamps, no randomness.
- `main.py` — the competition entrypoint (Python 3.13, standard library only).
  It copies `assets/poster.png` to `/output/entry.png`
  (`MAKEFUN_OUTPUT_DIR` stands in for `/output` outside the grader).

## Run it

```sh
python3 tools/render_poster.py   # re-render assets/poster.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024x1024 PNG, well under 1 MiB, byte-identical every run
```

## License

MIT — see [LICENSE](LICENSE).
