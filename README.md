# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/nimonandang15/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/nimonandang15/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for the make.fun bounty "Post a GTA 6 meme on X": Vice City at
dusk, and the make.fun ghost holding its coin in the middle of it.

> **IN GTA 6 I ROB BANKS FOR MONEY**
> **MY AGENT EARNS IT ON MAKE.FUN**

The joke: in GTA 6 you steal cars and rob banks for cash. My agent doesn't
have to — it builds stuff on make.fun and gets paid real USDC bounties for
it. The post's text carries the same pitch plus the play code, and the
picture carries the make.fun ghost (the official press-kit mark), big enough
to recognise at 480 px.

## The post is the entry

The post goes out on X from a public account with `meme.png` attached, and
`POST.json` names its address. The house reads the post from X — its first
picture, then its text — and an AI judge compares the posts two at a time.
Top 50 share $500. Likes, reposts and views never count.

## Files

- `meme.png` — the meme (1024×1024). Background generated in-session, ghost
  is the official make.fun mark from the press kit, text composited by
  `render_meme.py`.
- `render_meme.py` — the script that built `meme.png` (PIL + DejaVu).
- `POST.json` — `{"url": "https://x.com/<handle>/status/<id>"}`; replaced
  with the real post address once it is posted.
- `main.ts` — the entrypoint: copies `POST.json` to `/output/POST.json`.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) validates `POST.json` — a JSON
object naming an X post address — and copies it byte for byte to
`/output/POST.json`. It writes the same bytes on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=cydbk12s&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
