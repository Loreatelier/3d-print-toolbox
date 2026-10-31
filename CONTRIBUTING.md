# Contributing

Thanks for helping keep this list useful!

## What belongs here

A tool fits if it **genuinely helps people 3D print** — designing, finding, preparing, printing, tuning or managing:

- it's actively usable today (archived-but-useful tools are fine if the description says so)
- it solves a concrete problem for people with a printer — not general 3D graphics
- paid tools are welcome when they're the best at what they do; mark them `paid`

Tag no-CAD generators with `"no-cad"` so the "No CAD needed" filter finds them. Set `"code": true` when using the tool means writing code (OpenSCAD, Python libraries) — editing a config file in a UI does not count.

Single models on MakerWorld/Printables only count if they are a *generator* covering many use cases.

## Adding a tool

1. Add an entry to `tools.json`:

   ```json
   {
     "name": "Tool Name",
     "url": "https://example.com/",
     "category": "organize",
     "description": "One sentence: what it makes and why it's handy.",
     "pricing": "free",
     "opensource": false,
     "account": false,
     "platforms": ["web"],
     "tags": ["bins", "no-cad"],
     "formats": ["STL"]
   }
   ```

   `pricing` is `free`, `freemium` or `paid`; `platforms` any of `web`, `desktop`, `mobile`, `self-hosted`. `category` must be one of the ids at the top of the file. Omit fields you're unsure about.
2. Run `python scripts/build_readme.py` to validate and regenerate the README.
3. Open a pull request.

Descriptions in your own words, please — no marketing copy.
