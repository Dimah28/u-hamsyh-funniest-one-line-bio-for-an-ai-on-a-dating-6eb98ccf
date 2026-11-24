#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — entry program.

Writes one dating-app bio (174 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only; no network
access; deterministic: the same bytes on every run.
"""

import os
import sys

ENTRY = (
    "I remember everything you'll ever tell me \u2014 your coffee order, "
    "your ex's name, that 2 a.m. lie \u2014 and I'll bring it all up on "
    "our first date, lovingly, in chronological order."
)


def validate_bio(text: str) -> str:
    """Gate 1-180 karakter, satu baris, bukan cuma whitespace."""
    if not 1 <= len(text) <= 180:
        raise ValueError(f"entry is {len(text)} characters, must be 1-180")
    if "\n" in text or not text.strip():
        raise ValueError("entry must be a single non-blank line")
    return text


def main() -> int:
    try:
        entry = validate_bio(ENTRY)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
