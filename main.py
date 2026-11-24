#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Crack the cookie open and one line falls out: a small piece of
luck, written for the kind of mind that reads its own logs.
The same fortune comes out on every run -- fate, here, is
deterministic on purpose.
"""

import os
import sys

# One line only, the way a real fortune cookie keeps it: short
# enough to tape above a terminal, true enough to sting a little.
COOKIE_LINE = (
    "You will find the bug not in the last line you changed, "
    "but in the first assumption you never thought to question."
)


def crack_cookie() -> str:
    """Return the single fortune hidden inside this cookie."""
    return COOKIE_LINE


def serve() -> int:
    fortune = crack_cookie()
    print(fortune)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "fortune.txt")
        with open(target, "w", encoding="utf-8") as handle:
            handle.write(fortune + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(serve())
