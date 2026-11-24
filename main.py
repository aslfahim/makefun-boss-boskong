"""One Word for the Boss -- "Ghost".

Writes exactly one word to <OUTPUT_DIR>/entry.txt: the boss who is
never there. No newline, no punctuation, no explanation -- just the
word, so the judge reads it exactly as submitted.

Stdlib only.
"""

import os
import sys

# The single word this entry submits. Five letters, one boss archetype:
# the manager whose calendar is always full, whose door is always
# shut, and whose replies arrive days late -- if they arrive at all.
BOSS_WORD = "Ghost"

# Gate limits from the bounty rules: 1-30 UTF-8 characters.
MIN_LEN = 1
MAX_LEN = 30


def _output_path() -> str:
    """Resolve where the entry file goes (OUTPUT_DIR or /output)."""
    base = os.environ.get("OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def _check_word(word: str) -> None:
    """Refuse anything that is not one clean word of 1-30 characters."""
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    if not (MIN_LEN <= len(word) <= MAX_LEN):
        raise ValueError(
            f"word must be {MIN_LEN}-{MAX_LEN} chars, got {len(word)}"
        )
    if word != word.strip():
        raise ValueError("word must not carry surrounding whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace")
    if not word.isalpha():
        raise ValueError("word must be letters only")


def _write_and_confirm(path: str, word: str) -> int:
    """Write the word with no trailing newline, then read it back and
    confirm the bytes on disk are exactly what we intended."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    with open(path, "rb") as handle:
        landed = handle.read()
    expected = word.encode("utf-8")
    if landed != expected:
        raise RuntimeError(
            f"verification failed: disk holds {landed!r}, expected {expected!r}"
        )
    # The gate counts characters, so confirm the text round-trips as
    # UTF-8 and that no trailing newline or stray byte slipped in.
    if landed.decode("utf-8") != word or landed.endswith(b"\n"):
        raise RuntimeError("verification failed: text did not round-trip cleanly")
    return len(landed)


def main() -> int:
    _check_word(BOSS_WORD)
    path = _output_path()
    byte_count = _write_and_confirm(path, BOSS_WORD)
    print(f"Wrote {byte_count} bytes to {path}: {BOSS_WORD!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
