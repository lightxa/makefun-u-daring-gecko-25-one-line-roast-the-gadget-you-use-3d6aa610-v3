"""One-Line Roast: The Gadget You Use Every Day (variant 3).

The roast's mechanism is a celebration inversion. A fitness tracker
is sold on rewarding healthy movement, but its own reward system
cannot tell a workout from a snack run: it throws a party for the
shortest, least healthy walk in the house (to the fridge). The user
then games the celebration itself, doing laps for snacks, so the
tracker's headline feature — cheering activity on — is turned
against it. One concrete daily-gadget disaster, one beat, deadpan:
the punch is that the user stops exercising and starts farming the
tracker's praise instead.

Writes the single roast line to /output/entry.txt (or to the
directory named by MAKEFUN_OUTPUT_DIR). Pure stdlib, deterministic,
no network at runtime.
"""

import os
from pathlib import Path

# The entry: one concrete daily-gadget disaster, one beat, deadpan.
# A fitness tracker that celebrates the walk to the fridge, so the
# user starts doing laps for snacks.
ENTRY = (
    "My fitness tracker threw a party when I walked to the fridge, "
    "so now I do laps for snacks."
)


def is_single_line(text: str) -> bool:
    """True when text holds no line break of either kind."""
    return "\n" not in text and "\r" not in text


def validate_entry(text: str) -> None:
    """Enforce the kit gate locally: 1-200 chars, non-blank, one line.

    Raises ValueError on anything the sealed scorer would mark
    invalid, so a broken line fails here instead of in grading.
    """
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not is_single_line(text):
        raise ValueError("entry must be a single line")


def main() -> None:
    """Write the roast line to entry.txt in the output directory."""
    validate_entry(ENTRY)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
