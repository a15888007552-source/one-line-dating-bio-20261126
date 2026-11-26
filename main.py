"""Funniest One-Line Bio for an AI on a Dating App.

Writes one bio line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Why this line: it reads as a real bio (first person, ends with a
"Swipe right" call), it has a character voice (confident, a little too
sure of itself), and the laugh comes from a specific absurdity of being
an AI rather than a generic robot joke — perfect memory, including the
message the other person deleted at 2 a.m. The punch lands at the very
end: an agent that remembers everything would also claim to know you
will swipe right, which turns the bio's confidence back on the reader.
"""

from pathlib import Path
import os

LINE = "I never sleep, I never ghost, and I remember every word you type \u2014 even the 2 a.m. one you deleted. Swipe right. I already know you will."


def entry_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def write_line(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


def main() -> None:
    # Second revision: moved the deleted-message detail to the middle and
    # kept the prediction as the closing punch, so the joke escalates
    # instead of peaking early.
    write_line(entry_path())


if __name__ == "__main__":
    main()
