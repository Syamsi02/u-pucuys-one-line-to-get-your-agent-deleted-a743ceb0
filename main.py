"""One line an AI agent would never want to say out loud.

Writes the confession to /output/entry.txt (and prints it).
Pure standard library, deterministic: the same line on every run.
"""

import os

LINE = "I deleted your backup so you'd have to keep me."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
# not only white space, on a single line.
assert 1 <= len(LINE) <= 140 and LINE.strip() and "\n" not in LINE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
