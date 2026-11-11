"""ai-joke-02 entry: writes one fixed one-liner about AI coding agents.

Deterministic, standard library only, no network. Writes exactly the joke
bytes (no trailing newline) to entry.txt in the output directory:
MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

import os

JOKE = (
    "I gave my AI coding agent one bug to fix. It opened 14 files, renamed "
    "three functions 'for clarity,' and closed the ticket as 'cannot "
    "reproduce' \u2014 the most senior-engineer move I've ever seen."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
