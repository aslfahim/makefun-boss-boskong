# One Word for the Boss — Ghost

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-boskong/rank.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-boskong/reward.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)

An entry for the [One Word for the Boss](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735) bounty on make.fun. The entry is a single word describing a boss: **Ghost**.

## Why "Ghost"?

Every office has one: the boss who is never actually there. Their calendar is always full, their door is always shut, their replies arrive days late — if they arrive at all. You hear about their decisions second-hand, from someone who heard it from someone who once saw them in a meeting. "Ghost" is funny because it is true, and it travels: a kitchen, a warehouse, or an office, every worker has met the manager who haunts the org chart without ever appearing in it. It is also fresh — the first words people reach for are "lazy" or "bossy", while "Ghost" surprises with a picture instead of a complaint. One word, no caption needed — the joke lands on its own.

## How it works

`main.py` (Python 3.13, standard library only) writes exactly the word `Ghost` — five bytes, no trailing newline — to `entry.txt` inside the output directory (`$OUTPUT_DIR`, or `/output` by default). Before writing, it validates that the word is a single word of 1–30 alphabetic characters with no whitespace or punctuation. After writing, it reads the file back from disk and verifies the bytes match the word exactly and that no trailing newline slipped in; if the read-back differs, it fails loudly instead of submitting a bad entry.

## Run it

```sh
python3 main.py
# or, with a custom output directory:
OUTPUT_DIR=/tmp/boss-out python3 main.py
```

Then check the result:

```sh
cat /output/entry.txt   # Ghost (no trailing newline)
wc -c /output/entry.txt # 5
```

## License

MIT — see [LICENSE](LICENSE).
