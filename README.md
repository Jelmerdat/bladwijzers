# bladwijzers

IIIF manifests and JSON metadata for 4,558 digitised map sheets (Leiden University Libraries & National Library of Australia), linked to the bladwijzers (sheet indexes) of the Kaartenmagazijn of the Topografische Dienst, Dutch East Indies.

**Website / IIIF base:** https://jelmerdat.github.io/bladwijzers/  
**All bladwijzers as one IIIF Collection:** https://jelmerdat.github.io/bladwijzers/iiif/collection.json

Source bundle: `_TOPO19_bladwijzerbundel` (2 PDFs; bladwijzers 1–84 incl. 39a/b, 69A, 78A, and 2 loose New Guinea grid sheets).
Every online map sheet that belongs to a bladwijzer has **one IIIF manifest** and **one JSON metadata record**.

## What is in this folder
| Path | Content |
|---|---|
| `iiif/leiden/<item>.json` | Original IIIF manifests from Leiden University Libraries (KITLV maps). IIIF Presentation 3.0 (new Alma platform, id = `catalogue.leidenuniv.nl/...`) or 2.1 (older items). Images: IIIF Image API (deep zoom). |
| `iiif/nla/<nla.obj-…>.json` | IIIF Presentation 3.0 manifests **generated** from National Library of Australia (Trove) data: canvas at the scan's real pixel size, image = `https://nla.gov.au/<pid>/image`, NLA catalogue metadata. NLA has no IIIF Image API, so these open in Mirador / Universal Viewer without deep zoom. |
| `iiif/collections/bladwijzer_<nr>.json` | IIIF Collection per bladwijzer listing all its sheet manifests. |
| `iiif/collection.json` | Top-level IIIF Collection of all bladwijzers. |
| `metadata/<source>_<id>.json` | JSON record per map: title, sheet, HIND series, shelfmark/call number, scale, series (incl. coordinates for NLA), publisher/date, persistent URL, linked bladwijzer(s) with match confidence and reason, and all IIIF links (manifest, image service, image, thumbnail, width/height). |
| `all_maps.json` | All JSON records in one file (4,558 maps). |
| `all_sheets.csv` | One row per bladwijzer × map, with manifest URL, local manifest file, metadata file, image service and thumbnail. |
| `per_bladwijzer/*.csv` | Same rows split per bladwijzer. |
| `bladwijzer_overview.csv` | Per bladwijzer: number of matched maps by confidence, sources, IIIF collection file, status. |

## How sheets were matched to bladwijzers
1. **HIND number** – the HIND series numbers in the bladwijzer cartouches (e.g. HIND 1043, 646, 5002) are printed in Leiden's series data for each sheet → *high*.
2. **Leiden's own bladwijzer scans** – Leiden shelves each index sheet first, followed by its sheets (e.g. D F 54,1 *Bladwijzer van Manokwari* → D F 54,2–16). Sheet names were spot-checked against the bundle (e.g. bladwijzer 76 and 77) → *high*.
3. **NLA series records** – title, scale, coordinates and notes of the NLA catalogue record (e.g. "sheets numbered 19 to 41" = bladwijzer 18) → *high/medium*.
4. *medium/low* rows are plausible candidates to check by eye.
Matching is per series; placing each sheet on its numbered rectangle on the index page is the next step (sheet labels use the same TD numbering, e.g. `50/XXXIX-b`, `86/XLIX-L`).

## Hosting
This repository is served with GitHub Pages at `https://jelmerdat.github.io/bladwijzers/`; all generated manifest ids use that address.
If you move the files elsewhere, run `python3 set_base_url.py https://new.host/path/` in this folder to rewrite every manifest id.

## Notes
- **Viewing:** use `viewer.html?c=iiif/collections/bladwijzer_<nr>.json` (linked from the start page). National Library of Australia images cannot be shown in external IIIF viewers such as Mirador, because nla.gov.au sends no CORS headers; the built-in viewer loads them as plain images. Leiden sheets work in any IIIF viewer (deep zoom).
- Leiden v3 manifests are stored exactly as Leiden publishes them; they deviate slightly from the official IIIF 3 JSON schema but load in common viewers. All generated NLA manifests and the collections validate against the IIIF Presentation 3 schema.
- Not found online yet: bladwijzers 5, 6, 12, 27, 29, 30, 31, 50, 58, 65, 66, 67 (see overview).
- Rights: Leiden items are marked public domain ("Full access"); NLA items "Unrestricted" – check each record before re-publishing images.
