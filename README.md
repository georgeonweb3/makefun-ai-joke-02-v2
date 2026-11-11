# Senior-Engineer Move — an ai-joke-02 entry

One program, one joke: it writes a single one-liner about AI coding agents to `entry.txt`, byte for byte the same on every run.

The joke: "I gave my AI coding agent one bug to fix. It opened 14 files, renamed three functions 'for clarity,' and closed the ticket as 'cannot reproduce' — the most senior-engineer move I've ever seen."

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

Entry for the make.fun bounty [ai-joke-02](https://make.fun/bounty/ai-joke-02) — "Make the AI judge laugh" ($150 pool, 15 places).
