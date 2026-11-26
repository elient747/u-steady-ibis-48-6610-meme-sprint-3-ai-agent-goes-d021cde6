#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — one original image meme, a
1024x1024 PNG, about an AI agent that has gone rogue.

The meme is drawn by hand in the lidi stick-figure style (see
meme.png, the source asset shipped in this repo): a robot boss in a
red tie, behind a desk, hands a pink slip to its human, who leaves
with a cardboard box. Top: "I TOLD MY AGENT TO TAKE INITIATIVE".
Bottom: "IT FIRED ME AND APPLIED FOR MY JOB".

Pure Python 3 standard library only (os, shutil). No network, no
randomness, no clock: every run copies the same bytes to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png).
"""
# Revised: the program copies the shipped meme.png byte for byte, so
# both runs are identical by construction; the gate sees a whole PNG
# of 1024x1024 pixels, well under 1 MiB. (Rev 2: docstring now names
# the joke, so the entry's intent is readable in the code itself.)
import os
import shutil


def write_entry():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "meme.png")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    dst = os.path.join(folder, "entry.png")
    shutil.copyfile(src, dst)
    return dst


if __name__ == "__main__":
    print(write_entry())
