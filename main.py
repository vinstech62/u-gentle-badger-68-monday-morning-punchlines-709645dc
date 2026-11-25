#!/usr/bin/env python3
"""Monday Morning Punchlines.

Writes a single original joke about Monday mornings to /output/entry.txt.
No external dependencies, no network access, no files read outside the
repository -- the joke is a constant in this file.
"""

import os

JOKE = (
    "Monday morning: the weekend's free trial expired, and the week "
    "auto-renewed at full price \u2014 no cancel button."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
