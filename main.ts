// gta6-meme-x-01: "In GTA 6 I rob banks for money. My agent earns it on make.fun."
// Node 22, standard library only. The entry is the X post itself: this
// program copies POST.json from the repository root to /output/POST.json,
// where the gate reads it. That is all it has to do — the house reads the
// post from X (its first picture, then its text) and hands that to the judge.
// Nothing this program writes about the post is judged.
//
// Local check:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const src = join(BOT_DIR, 'POST.json');
const post = JSON.parse(readFileSync(src, 'utf8'));

if (typeof post !== 'object' || post === null || Array.isArray(post)) {
  throw new Error('POST.json must be a JSON object');
}
if (typeof post.url !== 'string' || !post.url.startsWith('https://')) {
  throw new Error('POST.json must name the post with an https url');
}
// The gate reads only an X post address: x.com or twitter.com, /status/<id>.
const X_POST = /^https:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\/[^/]+\/status\/\d+/;
if (!X_POST.test(post.url)) {
  throw new Error(`POST.json url is not an X post address: ${post.url}`);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
const outPath = join(OUTPUT_DIR, 'POST.json');
copyFileSync(src, outPath);

// Read the output back: a partial or corrupted write must fail loudly.
const written = readFileSync(outPath, 'utf8');
if (written !== readFileSync(src, 'utf8')) {
  throw new Error('output POST.json does not match POST.json after writing');
}

console.log(`wrote POST.json for ${post.url}`);
