# Red Hammer Construction Group — Site

Plain static HTML/CSS/JS site for redhammergroup.com. No build step, no
framework, no package.json — deployed via Vercel, which auto-deploys
whatever is on `main`. Anything committed to `main` is what goes live.

## Structure

- `index.html`, `financing.html` — root-level pages
- `services/*.html` — one page per trade (roofing, concrete, etc.)
- `areas/*.html` — one page per city served, plus `areas/index.html` as the hub
- `Images/` — all site images
  - `Images/stock/` — licensed/stock photos, kept local (see "Images" below)
- `styles.css` — single shared stylesheet for the whole site

## Editing the nav bar or footer

Every page shares the same nav bar and footer, but each one needs
slightly different relative paths (root pages vs. `services/*` vs.
`areas/*`) and a couple of self-referencing links. Don't hand-edit the
`<nav>`/`<footer>` blocks in each HTML file — edit the shared source and
regenerate:

1. Edit `partials/nav.html` and/or `partials/footer.html`. These use
   `${token}` placeholders (root path prefix, logo file, anchor prefix,
   etc.) — see `build.py` for what each token resolves to per page.
2. Run `python3 build.py` from the repo root. It rewrites the `<nav>`
   and `<footer>` block in all 26 pages in place.
3. Diff the result (`git diff`) and commit.

This is a local/dev-time script only — it does not run as part of
deployment. The committed HTML is always the final, already-rendered
output.

## Images

- Keep images local under `Images/` — don't hotlink third-party image
  hosts (e.g. Unsplash direct URLs). We had to rip out ~60 hotlinked
  Unsplash references in July 2026 after two of them started 404ing in
  production (the photos were deleted upstream) with no warning.
  Hotlinking also adds a DNS/TLS round trip per image.
- Before adding a new image, resize it to roughly the pixel size it
  will actually display at (2–3x for retina is plenty) and compress
  it. Tools used in this repo: `pngquant` for PNGs (logos/graphics),
  `jpegoptim` for JPEGs (photos), ImageMagick `convert` for resizing
  and PNG→JPEG conversion when there's no real transparency.
- The Acorn Finance banner image (`fs.acornfinance.com`) is the one
  intentional exception — it's a live partner asset, not ours to host.

## Contact form

The "Free Estimate" form on `index.html` posts to Web3Forms
(`api.web3forms.com`). The hidden `access_key` field is what determines
which inbox submissions land in — it's tied to whatever email address
was used to generate that key on web3forms.com, not anything set in
this repo. Current key routes to gabriel@redhammergroup.com.

To change where submissions go: get a new access key at
https://web3forms.com/ (enter the target email, no login needed — they
email you the key and a verification link), then swap the
`value="..."` on the `access_key` hidden input in `index.html`.

## SEO

- `sitemap.xml` has `<lastmod>` dates — update them when a page's
  actual content changes, not on every unrelated commit.
- `robots.txt` and JSON-LD business schema live in `index.html`.

See `CHECKLIST.md` for the running list of site improvements and their
status.
