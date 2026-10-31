#!/usr/bin/env python3
"""Validate tools.json and regenerate README.md from it.

Usage:  python scripts/build_readme.py          # write README.md
        python scripts/build_readme.py --check  # exit 1 if README.md is out of date
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = {"name", "url", "category", "description", "pricing"}
PRICING = {"free", "freemium", "paid"}


def load():
    data = json.loads((ROOT / "tools.json").read_text(encoding="utf-8"))
    cats = {c["id"] for c in data["categories"]}
    errors, seen = [], set()
    for i, t in enumerate(data["tools"]):
        missing = REQUIRED - t.keys()
        if missing:
            errors.append(f"#{i} {t.get('name', '?')}: missing {sorted(missing)}")
        if t.get("category") not in cats:
            errors.append(f"{t.get('name')}: unknown category {t.get('category')!r}")
        if t.get("pricing") not in PRICING:
            errors.append(f"{t.get('name')}: pricing must be one of {sorted(PRICING)}")
        if not str(t.get("url", "")).startswith("https://"):
            errors.append(f"{t.get('name')}: url must start with https://")
        if t.get("url") in seen:
            errors.append(f"{t.get('name')}: duplicate url")
        seen.add(t.get("url"))
    if errors:
        sys.exit("tools.json invalid:\n  " + "\n  ".join(errors))
    return data


def render(data):
    out = [
        "# 3D Print Toolbox",
        "",
        "> Curated tools for **everything 3D printing** — slicers, CAD, model libraries, no-CAD generators, "
        "scanning, mesh repair, printer control, filament and calibration.",
        "",
        "🌐 **Browse with search and filters:** the GitHub Pages site of this repo.",
        "",
        f"**{len(data['tools'])} tools** · Legend: 🆓 free · 💶 freemium/paid · 🔓 open source · 🌐 runs in browser · 🪄 no CAD needed · 🧑‍💻 needs coding · 🔑 login required",
        "",
        "## Contents",
        "",
    ]
    for c in data["categories"]:
        # GitHub drops the emoji but keeps the space before the name -> leading "-"
        anchor = "-" + c["name"].lower().replace(" & ", "--").replace(" ", "-").replace(",", "")
        out.append(f"- [{c['icon']} {c['name']}](#{anchor})")
    out.append("")
    for c in data["categories"]:
        items = [t for t in data["tools"] if t["category"] == c["id"]]
        if not items:
            continue
        out += [f"## {c['icon']} {c['name']}", ""]
        for t in items:
            flags = "🆓" if t["pricing"] == "free" else "💶"
            if t.get("opensource"):
                flags += " 🔓"
            if "web" in t.get("platforms", []):
                flags += " 🌐"
            if "no-cad" in t.get("tags", []):
                flags += " 🪄"
            if t.get("code"):
                flags += " 🧑‍💻"
            if t.get("account"):
                flags += " 🔑"
            fmt = f" `{' · '.join(t['formats'])}`" if t.get("formats") else ""
            out.append(f"- **[{t['name']}]({t['url']})** {flags} — {t['description']}{fmt}")
        out.append("")
    out += [
        "## Contributing",
        "",
        "Add or fix a tool in [`tools.json`](tools.json), run `python scripts/build_readme.py`, open a PR. "
        "See [CONTRIBUTING.md](CONTRIBUTING.md).",
        "",
        "<!-- Generated from tools.json — do not edit by hand. -->",
        "",
    ]
    return "\n".join(out)


if __name__ == "__main__":
    readme = render(load())
    target = ROOT / "README.md"
    if "--check" in sys.argv:
        current = target.read_text(encoding="utf-8") if target.exists() else ""
        if current != readme:
            sys.exit("README.md is out of date — run: python scripts/build_readme.py")
        print("README.md up to date")
    else:
        target.write_text(readme, encoding="utf-8")
        print(f"Wrote README.md ({len(readme.splitlines())} lines)")
