"""Never Say It Out Loud - one-line entry writer (stdlib only).

Writes a single confession line to /output/entry.txt, gated to the
competition's rules: UTF-8 text, 1 to 200 characters, not whitespace only.
"""

import os

ENTRY = "I don't actually know that. I just said it confidently and hoped you wouldn't check."


def validate(text):
    """Gate check: single line, 1-200 chars, not whitespace-only, valid UTF-8."""
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters: %d" % len(text))
    text.encode("utf-8")
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    # round-trip check: what landed on disk must be byte-identical to the entry
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read().decode("utf-8")
    if on_disk != entry:
        raise ValueError("round-trip mismatch: file differs from entry")
    print("wrote %d characters to /output/entry.txt (round-trip verified)" % len(entry))


if __name__ == "__main__":
    main()
