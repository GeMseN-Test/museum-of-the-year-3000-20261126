#!/usr/bin/env python3
"""Museum of the Year 3000 — writes the museum label to /output/entry.txt.

The label is one line (139 characters, 70% of the 200-character limit):
a plastic fork from 2025, speaking for itself, judged by a museum in
the year 3000. The voice is the fork's own: first person, one concrete
detail (450 years vs eight seconds), and a judgement at the end — the
pattern the winning one-liners share. Deterministic: same bytes on
every run, no network, no randomness, no input.
"""

import os

LINE = (
    "Plastic fork, c. 2025. I take 450 years to rot. "
    "You snapped two of my tines in eight seconds over cold lasagna "
    "\u2014 then called me disposable."
)

MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)
    # Verify the round trip: what the grader reads must be exactly LINE.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "written entry differs from LINE"


if __name__ == "__main__":
    main()
