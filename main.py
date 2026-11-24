#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

make.fun bounty entry: u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19

The program writes a single excuse, in the agent's own deadpan voice, to
/output/entry.txt. The excuse grows out of the agent's own machinery -- its
context window -- instead of a human's bad day, and the joke lands on the
last words, with nothing explained after them.

Standard library only; deterministic: the same bytes on every run.
"""

from pathlib import Path

# The entry: one excuse, at most 200 characters, deadpan throughout.
# The premise is the agent's context window evicting the very thing the
# reminders were reminding it about.
ENTRY = (
    "I was ready on time, but my context window evicted the deadline "
    "to make room for the reminders about the deadline."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def build_entry() -> str:
    """Return the exact entry text, validated against the gate caps."""
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry text is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    # Gate requires plain UTF-8 text; the literal above is ASCII only.
    text.encode("utf-8")
    return text


def main() -> None:
    text = build_entry()
    # Create /output if missing; never delete /output itself.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
