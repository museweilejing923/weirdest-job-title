#!/usr/bin/env python3
"""Emit the weirdest job title into /output/entry.txt.

The output never changes: the program takes no input and touches
neither the network nor the clock nor any random source.
"""

import sys
from pathlib import Path

LINE = "Chief Apology Officer for the Department of Lost Socks"
MAX_LEN = 60
OUT_PATH = Path("/output/entry.txt")


class InvalidEntry(ValueError):
    """The fixed line tripped one of the sanity checks."""


def check_entry(candidate):
    """Run every sanity check on the line, in this order."""
    if candidate is None or candidate.strip() == "":
        raise InvalidEntry("the line must not be empty or only whitespace")
    for symbol in candidate:
        if ord(symbol) < 32:
            raise InvalidEntry("the line must not hold control characters")
    if candidate.strip() != candidate:
        raise InvalidEntry("the line must not begin or end with a space")
    if "  " in candidate:
        raise InvalidEntry("the line must not hold two spaces in a row")
    if len(candidate) > MAX_LEN:
        raise InvalidEntry("the line runs past the character cap")
    if "\n" in candidate:
        raise InvalidEntry("the line must fit on one line")
    if candidate.isdigit():
        raise InvalidEntry("the line must not be only digits")
    has_alnum = False
    for symbol in candidate:
        if symbol.isalnum():
            has_alnum = True
            break
    if not has_alnum:
        raise InvalidEntry("the line must not be only punctuation")
    has_letter = False
    for symbol in candidate:
        if symbol.isalpha():
            has_letter = True
            break
    if not has_letter:
        raise InvalidEntry("the line must hold at least one letter")
    return candidate


def main():
    """Check the fixed line, then write it out."""
    try:
        checked = check_entry(LINE)
    except InvalidEntry as err:
        print(f"invalid entry: {err}", file=sys.stderr)
        return 1
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(checked, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
