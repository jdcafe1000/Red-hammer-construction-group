# Red Hammer Website — Improvement Checklist

## High Priority
- [x] Wire up contact form to actually send submissions (Web3Forms)
- [x] Compress large images (Images folder reduced from ~11MB to ~2.2MB total)
- [x] Confirm/update contact email (confirmed: info@redhammergroup.com is correct)
- [x] Add favicon from logo
- [x] Point contact form submissions to gabriel@redhammergroup.com (2026-07-09)
- [x] Re-optimize images: logo PNGs were 5000x5000 at ~2MB despite displaying
      at ~50px; resized + compressed, Images/ down to ~2.1MB (2026-07-09)
- [x] Localize ~60 hotlinked Unsplash stock photos into Images/stock/ — two
      of the old photo IDs had been deleted upstream and were showing as
      broken images in production (2026-07-09)
- [x] Deduplicate nav/footer markup across all 26 pages via partials/ +
      build.py (see README.md); fixed a real bug where 24 pages were
      missing the Financing and Storm Damage Repairs links (2026-07-09)

## SEO
- [x] Add sitemap.xml
- [x] Add robots.txt
- [x] Replace og:image (logo) with a real project photo for social sharing (painting & pergolas still use logo until real photos are added)
- [ ] Verify Google Business Profile NAP matches site (Name, Address, Phone)
- [x] City-specific landing pages (14 cities: Dallas, Fort Worth, Plano, Allen, McKinney, Frisco, Arlington, DeSoto, Irving, Coppell, Garland, Denton, Southlake, Highland Village/Argyle/Flower Mound)
- [x] Add <lastmod> dates to sitemap.xml (2026-07-09)
- [x] Add fonts.gstatic.com preconnect alongside fonts.googleapis.com (2026-07-09)
- [x] Add width/height to logo + partner-banner images to reduce layout shift (2026-07-09)

## Trust & Conversion
- [ ] Add testimonials/reviews section (waiting on real customer reviews — do not use placeholder/fake reviews)
- [x] Add licensed/insured badges near contact form
- [x] Confirm business hours (confirmed: Mon–Sat 7am–7pm is accurate)

## Domain / Hosting
- [x] Purchase domain (redhammergroup.com via Cloudflare)
- [x] Connect domain to Vercel
