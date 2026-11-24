"""One-line vending machine pickup line.

Writes the entry to /output/entry.txt and prints it.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os

LINE = "Press my coin return \u2014 I've been saving your change since Tuesday."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"entry: {len(LINE)} chars, {len(LINE.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
