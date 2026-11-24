"""Sick-day excuse printer.

Loads the single-line excuse from entry.txt, checks it against the
bounty rules (one line, under 200 characters), then prints it.
"""

from pathlib import Path

EXCUSE_FILE = Path(__file__).with_name("entry.txt")
MAX_CHARS = 200


def load_excuse():
    if not EXCUSE_FILE.exists():
        raise FileNotFoundError(f"missing {EXCUSE_FILE.name} next to main.py")
    text = EXCUSE_FILE.read_text(encoding="utf-8").strip()
    lines = text.splitlines()
    if len(lines) != 1:
        raise ValueError("excuse must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} chars, limit is {MAX_CHARS}")
    return text


def main():
    excuse = load_excuse()
    print(f"({len(excuse)} chars)")
    print(excuse)


if __name__ == "__main__":
    main()
