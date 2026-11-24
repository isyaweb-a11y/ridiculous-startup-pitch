#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

The entry is one sentence pitching a startup idea so strange it sounds
like a joke, yet specific enough that a reader can see the customers and
the money:

    We turn strangers' spare attics into phone-free nap pods, charging
    burnt-out remote workers $20 an hour to hide from meetings,
    calendars, and their own Slack.

The odd thing being sold: a stranger's attic as a nap pod. Who pays:
burnt-out remote workers, $20 an hour. Why it holds together: silence
is the product — no phone, no meetings, no calendar, no Slack — and
every remote worker already knows the feeling of needing exactly that
hiding place, which is why the joke survives a second look.

Writes the sentence to /output/entry.txt. Stdlib only, no network.
"""

import os

ENTRY = (
    "We turn strangers' spare attics into phone-free nap pods, "
    "charging burnt-out remote workers $20 an hour to hide from "
    "meetings, calendars, and their own Slack."
)

# The gate allows 1 to 200 characters, and the brief allows one sentence.
MAX_CHARS = 200


def entry_text() -> str:
    """Return the pitch, checked against the bounty's own rules."""
    text = ENTRY.strip()
    assert text, "the entry must not be empty"
    assert len(text) <= MAX_CHARS, "the entry must fit the 200 character gate"
    assert text.count(".") == 1 and text.endswith("."), (
        "the entry must be exactly one sentence"
    )
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
