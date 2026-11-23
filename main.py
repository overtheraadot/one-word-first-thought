#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry (account A / overtheraa).

Writes exactly one word to the output file: the first word that comes to
mind. No network, no randomness, no arguments, no environment beyond the
output directory. Deterministic: the same bytes on every run.

The grader provides MAKEFUN_OUTPUT_DIR ("/output" in the sandbox); locally
it defaults to the same path, or pass it explicitly.
"""

import os

WORD = "blanket"

# The gate (competition.yaml / RULES.txt): /output/entry.txt must be UTF-8
# text of 1 to 24 characters, not only white space. Refuse to write anything
# that would fail it, rather than submitting an invalid entry.
assert 1 <= len(WORD) <= 24 and WORD.strip(), "word fails the gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
