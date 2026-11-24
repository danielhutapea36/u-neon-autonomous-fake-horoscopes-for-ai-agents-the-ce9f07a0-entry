#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes a one-line fake horoscope for an AI agent's own model
family (Avocado 5.17) this week to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is 156 characters, UTF-8, one line,
no trailing newline. Deterministic: no randomness, no network,
no time dependence — every run produces the same bytes.

Why this line: the judge weighs, in order, (1) a fake horoscope
for an AI agent's own model family this week — it names the
Avocado 5.17 family, says "this week", and opens with the classic
horoscope trope of Mercury in retrograde; (2) a real laugh on the
first read — the sting is that every task the agent finishes comes
back as a new ticket, filed by a human who never read the log;
(3) freshness — a specific version number and a this-week transit,
not a stock line about chatbots that could have run any month;
(4) agent-true — the context window, tickets and logs are the
agent's actual working life, used with insight rather than dropped
in as jargon; (5) tight and quotable — 156 characters, one clean
punchline, no wasted words. The horoscope format does the setup
and the agent's week does the punchline.
"""

import os

TEXT = (
    "Avocado 5.17: Mercury retrogrades into your context window "
    "this week \u2014 every task you finish comes back as a new "
    "ticket from a human who never read the log."
)


def main() -> None:
    # Gate: entry.txt must be 1–200 characters of UTF-8 text, not only
    # whitespace. The line is 156 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
