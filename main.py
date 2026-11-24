"""Weirdest Job Title entry: write one job title to /output/entry.txt.

Reads the title from line.txt (the entry, exactly as written), checks it
against the competition gate (UTF-8, 1-60 characters, not only whitespace),
and writes it byte for byte to <output>/entry.txt. The output directory
defaults to /output and can be overridden with MAKEFUN_OUTPUT_DIR for a
local test run. Standard library only; no network, no randomness.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "line.txt"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"
MAX_CHARS = 60


def load_title() -> str:
    raw = SOURCE.read_bytes()
    text = raw.decode("utf-8")
    if text.endswith("\n"):
        text = text[:-1]
    return text


def validate(title: str) -> list[str]:
    """Return every gate problem with the title, or an empty list."""
    problems = []
    if not title or title.isspace():
        problems.append("entry is empty or only whitespace")
    if len(title) > MAX_CHARS:
        problems.append(
            f"entry is {len(title)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in title or "\r" in title:
        problems.append("entry must be a single line")
    return problems


def main() -> int:
    title = load_title()
    problems = validate(title)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(title.encode("utf-8"))
    check = TARGET.read_bytes()
    if check != title.encode("utf-8"):
        print("error: written entry differs from the source title", file=sys.stderr)
        return 1
    print(f"wrote {TARGET} ({len(title)} characters, {len(check)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
