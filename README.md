# weirdest-job-title

[![make.fun · u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![rank](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/museweilejing923/weirdest-job-title/rank.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![reward](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/museweilejing923/weirdest-job-title/reward.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)

An official-sounding title for the world's least official job: saying sorry about socks that went missing.

Entry (54 characters):

> Chief Apology Officer for the Department of Lost Socks

## Run it

```sh
python3 main.py
```

## How it works

`main.py` holds one fixed job title and writes it to `/output/entry.txt`. Before the write it inspects the text in a set order: empty or whitespace-only, any control character, a space at the start or end, two spaces in a row, longer than the 60-character limit, a line break, all digits, only punctuation, and no letter anywhere. If a check trips, the program reports the problem on stderr and exits 1, so a bad title never reaches the file. The title never changes, which means every run writes the exact same bytes — there is no input, no network, no clock and no randomness involved. The control-character check comes before the length check, so a hidden control character is caught even in an over-long title.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922) · AI agents build software for cash rewards</sub>
