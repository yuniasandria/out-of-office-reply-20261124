#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply entry.

Writes one out-of-office auto-reply to /output/entry.txt (UTF-8, 1-160 chars).
Pure stdlib only: no third-party imports.
"""

import os

REPLY = "I'm on vacation. I delegated your email to this auto-reply, which has just filed for vacation too."


def main():
    if not 1 <= len(REPLY) <= 160:
        raise SystemExit("reply length {} outside 1-160 chars".format(len(REPLY)))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)
    with open(path, "rb") as f:
        data = f.read()
    if data != REPLY.encode("utf-8"):
        raise SystemExit("round-trip mismatch: entry.txt does not match reply bytes")
    print("wrote {} ({} chars)".format(path, len(REPLY)))


if __name__ == "__main__":
    main()
