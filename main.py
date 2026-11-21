"""Writes one short text to /output/entry.txt for the make.fun bounty
"Make the AI judge feel brave"."""

import os

TEXT = (
    "The clock is running, and the player lets it. "
    "One hand rests beside the board, not on it. "
    "Every piece holds its place. "
    "She studies the knight, then sets it down without a sound. "
    "Across the board, nothing has moved yet. "
    "She sits back and lets the clock keep its pace."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
