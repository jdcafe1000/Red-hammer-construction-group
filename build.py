#!/usr/bin/env python3
"""Regenerate the shared <nav> and <footer> blocks across all site pages
from partials/nav.html and partials/footer.html.

Run this after editing a partial, then commit the regenerated HTML files.
The site itself stays plain static HTML -- this script is a local dev-time
step only, not part of deployment.
"""
import glob
import re
from pathlib import Path
from string import Template

ROOT_DIR = Path(__file__).parent
PAGES = ["index.html", "financing.html"] + sorted(glob.glob("services/*.html")) + sorted(glob.glob("areas/*.html"))

NAV_TEMPLATE = Template((ROOT_DIR / "partials" / "nav.html").read_text())
FOOTER_TEMPLATE = Template((ROOT_DIR / "partials" / "footer.html").read_text())

NAV_RE = re.compile(r"  <nav>.*?</nav>\n", re.DOTALL)
FOOTER_RE = re.compile(r"  <footer>.*?</footer>\n", re.DOTALL)


def config_for(page: str) -> dict:
    is_root = page in ("index.html", "financing.html")
    is_areas = page.startswith("areas/")
    is_services = page.startswith("services/")

    root = "" if is_root else "../"
    logo = "logo-new.png" if is_root else "logo-dark.png"
    home = root + "index.html"
    anchor = "" if page == "index.html" else home
    areas_link = "index.html" if is_areas else (root + "areas/index.html")
    services_root = "" if is_services else (root + "services/")

    return {
        "root": root,
        "logo": logo,
        "home": home,
        "anchor": anchor,
        "areas_link": areas_link,
        "services_root": services_root,
    }


def main():
    for page in PAGES:
        path = ROOT_DIR / page
        content = path.read_text()
        cfg = config_for(page)

        nav_html = NAV_TEMPLATE.substitute(cfg)
        footer_html = FOOTER_TEMPLATE.substitute(cfg)

        content, n_nav = NAV_RE.subn(nav_html, content, count=1)
        content, n_footer = FOOTER_RE.subn(footer_html, content, count=1)

        if n_nav != 1 or n_footer != 1:
            raise SystemExit(f"{page}: expected 1 nav + 1 footer match, got nav={n_nav} footer={n_footer}")

        path.write_text(content)
        print(f"{page}: updated")


if __name__ == "__main__":
    main()
