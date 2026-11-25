#!/usr/bin/env python3
"""Monday Morning Punchlines — writes one joke about Monday mornings to /output/entry.txt."""

import os

JOKE = "My bed loves me more on Monday mornings than my job ever will — it holds me tighter every time my alarm tries to break us up."

OUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 chars"
    assert "\n" not in JOKE and JOKE == JOKE.strip(), "joke must be one trimmed line"
    os.makedirs("/output", exist_ok=True)
    data = JOKE.encode("utf-8")
    with open(OUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, "rb") as f:
        written = f.read()
    assert written == data, "written bytes do not match joke"
    assert oct(os.stat(OUT_PATH).st_mode & 0o777) == "0o644", "output mode must be 0644"
    print(f"Wrote {len(data)} bytes to {OUT_PATH}")


if __name__ == "__main__":
    main()
