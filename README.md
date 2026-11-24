# Weirdest Job Title: Blind Judge Showdown

[![Competition](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![Rank](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/imusic-487/weirdest-job-title-mourner/rank.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/leaderboard)
[![Reward](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/imusic-487/weirdest-job-title-mourner/reward.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/leaderboard)

## The entry

> Professional Mourner for Strangers' Funerals

44 characters. Professional mourners are a real job — people hired to grieve
at funerals. The twist is the client: strangers. Nobody hires a mourner for
a funeral they have no connection to, yet here is someone whose whole career
is turning up to weep for people they never met, on purpose, for pay. It
reads like a job listing, pictures instantly, and lands on the first read.

## What this repo does

This is an entry for the make.fun bounty
[u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the text is not
1–60 characters, not a single line, or the copy differs in bytes. Nothing
else: no network, no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
