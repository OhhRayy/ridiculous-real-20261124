# ridiculous-real-20261124 — Ridiculous at First Glance, Real by the Second

[![make.fun · Ridiculous at First Glance, Real by the Second](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a?utm_source=github&utm_medium=readme&utm_campaign=ridiculous-real-20261124)
[![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/OhhRayy/ridiculous-real-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ridiculous-real-20261124)
[![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/OhhRayy/ridiculous-real-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a?utm_source=github&utm_medium=readme&utm_campaign=ridiculous-real-20261124)

Entry for the make.fun bounty **"Ridiculous at First Glance, Real by the Second"**
(slug `u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a`, $2, closes 24 Nov 2026 19:25 UTC).

The entry is one original sentence (163 characters) pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell:

> We sell tiny funerals for dead houseplants — coffin, eulogy, and a replacement plant — because the people who kill them keep buying more and want someone to blame.

Why it fits the judge's brief: the idea is genuinely strange (a funeral
service for a houseplant), yet the business logic holds in one breath — the
customers are serial plant-killers who keep buying replacements, the product
is the funeral package plus the replacement plant, and guilt is the recurring
revenue. One sentence, concrete buyers, visible money.

## Files

- `main.py` — the entry program: writes the sentence to `/output/entry.txt`
  (stdlib only, deterministic — every run writes identical bytes).
- `entry.txt` — the sentence itself, for reference.
- `LICENSE` — MIT.

## Verify locally

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
diff out1/entry.txt out2/entry.txt   # must match
wc -m out1/entry.txt                 # 163 characters, no trailing newline
```
