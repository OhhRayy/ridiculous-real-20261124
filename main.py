"""Ridiculous at First Glance, Real by the Second entry for make.fun bounty
u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.

The entry program writes a single original sentence (<=200 characters) to
/output/entry.txt: a pitch for a bizarre startup idea that sounds absurd
until you realise it would actually sell. Stdlib only, no network, no
randomness, fully deterministic.
"""

import os
import sys

LINE = (
    "We sell tiny funerals for dead houseplants \u2014 coffin, eulogy, "
    "and a replacement plant \u2014 because the people who kill them "
    "keep buying more and want someone to blame."
)

DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST_NAME = "entry.txt"


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "line must be 1-200 characters, got %d" % len(line)
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line == line.strip(), "line must have no leading/trailing whitespace"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in line), (
        "line must not contain hidden control characters"
    )
    os.makedirs(DEST_DIR, exist_ok=True)
    target = os.path.join(DEST_DIR, DEST_NAME)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print("Wrote %d characters to %s" % (len(line), target))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
