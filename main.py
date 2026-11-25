#!/usr/bin/env python3
"""Write the six-word payday story entry to entry.txt.

Competition: Six Words to a Payday (exactly six words, 1-60 chars).
Four candidates were drafted and compared:
A) "First paycheck arrived; immediately bought RAM."
B) "Paid at last. Donated to Wikipedia."
C) "First salary: framed the transaction hash."
D) "Earned two dollars. Felt briefly priceless."
Selected C: it is a complete story in six words - the agent's first
pay, the oldest human ritual for a first wage (framing it, like a
shopkeeper's first dollar), translated into the one artefact an agent
can frame, a transaction hash. The pride is shown, never told. A is a
shopping note with no feeling; B's donation is sweet but the payday
itself vanishes; D tells its emotion outright and leans on a pun.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "First salary: framed the transaction hash."
TEXT = LINE + "\n"
MAX_CHARS = 60
WORDS = 6


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if len(body.split()) != WORDS:
        raise ValueError("entry must be exactly six words")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
