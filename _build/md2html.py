import re, sys, html
import markdown

src, dst = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()
blocos = []
def guarda(m):
    blocos.append(m.group(1))
    return f"\n\nMERMAIDBLOCK{len(blocos)-1}\n\n"
text = re.sub(r"```mermaid\n(.*?)```", guarda, text, flags=re.S)
corpo = markdown.markdown(text, extensions=["tables", "fenced_code"])
for i, b in enumerate(blocos):
    corpo = corpo.replace(f"<p>MERMAIDBLOCK{i}</p>", f'<pre class="mermaid">{html.escape(b)}</pre>')
doc = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><title>AlertaAqui RPA</title>
<style>
@page {{ size: A4; margin: 16mm 14mm; }}
body {{ font-family: "Segoe UI", Arial, sans-serif; font-size: 10.5pt; color: #1d2b36; line-height: 1.45; }}
h1 {{ color: #fff; background: #0b3d5c; padding: 14px 18px; border-bottom: 5px solid #f2a900; border-radius: 6px; font-size: 20pt; }}
h2 {{ color: #0b3d5c; border-bottom: 2px solid #f2a900; padding-bottom: 3px; margin-top: 22px; page-break-after: avoid; }}
table {{ border-collapse: collapse; width: 100%; margin: 8px 0; page-break-inside: avoid; }}
th {{ background: #0b3d5c; color: #fff; text-align: left; }}
th, td {{ border: 1px solid #c9d4dc; padding: 5px 7px; vertical-align: top; }}
tr:nth-child(even) td {{ background: #f4f7fa; }}
code {{ background: #eef2f5; padding: 1px 4px; border-radius: 3px; font-size: 9pt; }}
blockquote {{ border-left: 4px solid #f2a900; background: #fff8e1; margin: 8px 0; padding: 6px 12px; }}
pre.mermaid {{ text-align: center; page-break-inside: avoid; background: #fff; white-space: pre; font-size: 8.5pt; }}
pre.mermaid svg {{ max-height: 235mm; width: auto !important; }}
hr {{ border: 0; border-top: 1px solid #dde4ea; }}
</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
</head><body>
{corpo}
<script>
if (window.mermaid) {{ mermaid.initialize({{ startOnLoad: true, theme: "default", flowchart: {{ useMaxWidth: true }} }}); }}
</script>
</body></html>"""
open(dst, "w", encoding="utf-8").write(doc)
print("ok", len(blocos))
