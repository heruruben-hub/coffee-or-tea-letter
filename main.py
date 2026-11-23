#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun bounty entry.

The entry is a single letter: "A" for coffee (or "B" for tea).

Why "A" — coffee — is the truer, funnier, more vivid choice:

* Coffee is the drink that starts the day. Tea waits politely; coffee
  barges in, wakes you up, and gets things done. The letter "A" is the
  first letter, the top of the alphabet — coffee is first in the morning,
  first in the queue, first in the bloodstream.
* Coffee is louder and more alive: the hiss of the espresso machine, the
  smell that fills the whole room before the first sip. Tea whispers;
  coffee talks back. A single "A" lands like that first bold sip.
* It is the honest answer for the sender: a working day in Madiun runs
  on coffee, not on a quiet cup of tea. Picking tea would be a pose;
  picking coffee is the truth.
"""

LETTER = chr(ord("A"))  # A = coffee, B = tea — built from its code point


def main() -> int:
    # Validate before touching the output file: exactly one char, A or B.
    if len(LETTER) != 1 or LETTER not in ("A", "B"):
        raise SystemExit(f"invalid entry letter: {LETTER!r}")

    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LETTER)

    # Read back and verify: the file must hold exactly that one byte.
    with open(out_path, "rb") as fh:
        raw = fh.read()
    if raw != LETTER.encode("ascii"):
        raise SystemExit(f"verification failed: {out_path} holds {raw!r}")

    print(f"wrote {LETTER!r} to {out_path} (verified: {len(raw)} byte)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
