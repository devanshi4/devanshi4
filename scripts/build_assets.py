"""Build the SVG images used by the profile README.

Run from the repository root:  python scripts/build_assets.py
Every image is written twice, assets/<name>-light.svg and assets/<name>-dark.svg,
so the README can switch with the viewer's GitHub theme. Edit the data below
(PROJECTS, STATS, TOOLBOX) and re-run to update the profile.
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

THEMES = {
    "light": dict(bg="#ffffff", surface="#ffffff", subtle="#f6f8fa", ink="#0c0d12", muted="#59636e",
                  faint="#818b98", line="#d1d9e0", accent="#3347e0", accent_soft="#eef0fd",
                  warn="#b45309", warn_soft="#fdf3e5", good="#1a7f37", dot="#d1d9e0"),
    "dark": dict(bg="#0d1117", surface="#0d1117", subtle="#151b23", ink="#f0f6fc", muted="#9198a1",
                 faint="#6e7681", line="#3d444d", accent="#8e9dff", accent_soft="#1b2040",
                 warn="#f2b05e", warn_soft="#2d2313", good="#3fb950", dot="#262c36"),
}
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"


def wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    if cur:
        lines.append(cur)
    return lines


def write(name, theme, svg):
    (OUT / f"{name}-{theme}.svg").write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------- header
STATS = [
    ("~37K", "orphaned projects found", "in an Oracle audit"),
    ("~91%", "agreement for a local", "Llama 3.1 log classifier"),
    ("70→20", "error categories", "consolidated for the classifier"),
    ("10K+", "telecom sites monitored", "for activation health"),
]


def header(t):
    c = THEMES[t]
    stats = ""
    for i, (num, l1, l2) in enumerate(STATS):
        x = 56 + i * 280
        stats += f"""
  <g class="rise" style="animation-delay:{0.15 * i + 0.2:.2f}s">
    <text x="{x}" y="372" class="num">{escape(num)}</text>
    <text x="{x}" y="398" class="lbl">{escape(l1)}</text>
    <text x="{x}" y="417" class="lbl">{escape(l2)}</text>
  </g>"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="460" viewBox="0 0 1200 460" role="img" aria-labelledby="t d">
  <title id="t">Devanshi Pandya, Data Engineer</title>
  <desc id="d">Data engineer in New York who builds pipelines, dbt models and data-quality checks. Animated diagram of three source systems flowing through matching and tests into one trusted table.</desc>
  <defs>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.2" fill="{c['dot']}"/></pattern>
    <linearGradient id="fade" x1="0" x2="1" y1="0" y2="0"><stop offset="0.35" stop-color="{c['surface']}" stop-opacity="1"/><stop offset="1" stop-color="{c['surface']}" stop-opacity="0"/></linearGradient>
    <clipPath id="card"><rect x="1" y="1" width="1198" height="458" rx="16"/></clipPath>
  </defs>
  <style>
    text{{font-family:{SANS};fill:{c['ink']}}}
    .mono{{font-family:{MONO}}}
    .role{{font-size:17px;fill:{c['muted']};font-weight:500}}
    .name{{font-size:58px;font-weight:700;letter-spacing:-2.2px}}
    .tag{{font-size:21px;fill:{c['muted']}}}
    .tag tspan.hl{{fill:{c['ink']};font-weight:600}}
    .num{{font-size:32px;font-weight:700;letter-spacing:-1px}}
    .lbl{{font-size:14px;fill:{c['muted']}}}
    .node{{fill:{c['subtle']};stroke:{c['line']};stroke-width:1.3}}
    .node.out{{fill:{c['accent_soft']};stroke:{c['accent']}}}
    .node.rev{{fill:{c['warn_soft']};stroke:{c['warn']}}}
    .nt{{font-family:{MONO};font-size:13px;fill:{c['ink']}}}
    .ns{{font-family:{MONO};font-size:11px;fill:{c['faint']}}}
    .edge{{fill:none;stroke:{c['line']};stroke-width:2}}
    .flow{{fill:none;stroke:{c['accent']};stroke-width:2.2;stroke-linecap:round;stroke-dasharray:2 12;animation:flow 1.2s linear infinite}}
    .flow.rev{{stroke:{c['warn']}}}
    .open circle{{fill:{c['good']}}}
    .open .ring{{fill:none;stroke:{c['good']};stroke-width:2;transform-origin:63px 50px;transform-box:view-box;animation:ping 2.4s ease-out infinite}}
    .glow{{fill:none;stroke:{c['accent']};stroke-width:2;opacity:0;animation:glow 2.8s ease-in-out infinite}}
    .rise{{animation:rise .8s cubic-bezier(.2,.8,.2,1) both}}
    @keyframes flow{{to{{stroke-dashoffset:-28}}}}
    @keyframes ping{{0%{{transform:scale(.6);opacity:.9}}80%,100%{{transform:scale(2.4);opacity:0}}}}
    @keyframes glow{{0%,100%{{opacity:0}}50%{{opacity:.55}}}}
    @keyframes rise{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
    @media (prefers-reduced-motion: reduce){{.flow,.ring,.glow,.rise{{animation:none}}.glow{{opacity:0}}}}
  </style>
  <g clip-path="url(#card)">
    <rect width="1200" height="460" fill="{c['surface']}"/>
    <rect x="600" width="600" height="320" fill="url(#dots)"/>
    <rect x="560" width="260" height="320" fill="url(#fade)"/>
  </g>
  <rect x="1" y="1" width="1198" height="458" rx="16" fill="none" stroke="{c['line']}"/>

  <g class="open"><circle cx="63" cy="50" r="5"/><circle class="ring" cx="63" cy="50" r="5"/></g>
  <text x="78" y="56" class="role">Data Engineer · New York, NY · open to data engineering roles</text>
  <text x="54" y="132" class="name">Devanshi Pandya</text>
  <text class="tag"><tspan x="56" y="182">I build the <tspan class="hl">pipelines, dbt models and data-quality</tspan></tspan><tspan x="56" y="211"><tspan class="hl">checks</tspan> that catch wrong data before anyone</tspan><tspan x="56" y="240">reports on it.</tspan></text>

  <g transform="translate(700 40)">
    <path class="edge" d="M150 30 C180 30 180 112 212 112"/><path class="flow" d="M150 30 C180 30 180 112 212 112"/>
    <path class="edge" d="M150 124 L212 124"/><path class="flow" d="M150 124 L212 124" style="animation-delay:-.4s"/>
    <path class="edge" d="M150 218 C180 218 180 136 212 136"/><path class="flow" d="M150 218 C180 218 180 136 212 136" style="animation-delay:-.8s"/>
    <path class="edge" d="M320 116 C340 116 340 74 362 74"/><path class="flow" d="M320 116 C340 116 340 74 362 74"/>
    <path class="edge" d="M320 132 C340 132 340 178 362 178"/><path class="flow rev" d="M320 132 C340 132 340 178 362 178"/>
    <rect class="node" x="0" y="8" width="150" height="44" rx="8"/><text class="nt" x="14" y="27">inventory.csv</text><text class="ns" x="14" y="43">1 row per site</text>
    <rect class="node" x="0" y="102" width="150" height="44" rx="8"/><text class="nt" x="14" y="121">rf_plan.json</text><text class="ns" x="14" y="137">per plan version</text>
    <rect class="node" x="0" y="196" width="150" height="44" rx="8"/><text class="nt" x="14" y="215">field_ops.parquet</text><text class="ns" x="14" y="231">per work order</text>
    <rect class="node" x="212" y="94" width="108" height="60" rx="8"/><text class="nt" x="226" y="119">match +</text><text class="nt" x="226" y="137">dbt tests</text>
    <rect class="glow" x="358" y="48" width="132" height="52" rx="11"/>
    <rect class="node out" x="362" y="52" width="124" height="44" rx="8"/><text class="nt" x="376" y="71">dim_site</text><text class="ns" x="376" y="87">24 canonical</text>
    <rect class="node rev" x="362" y="160" width="124" height="36" rx="8"/><text class="nt" x="376" y="183">review_queue</text>
  </g>

  <line x1="56" x2="1144" y1="322" y2="322" stroke="{c['line']}"/>{stats}
</svg>
"""


# ---------------------------------------------------------------- project cards
PROJECTS = [
    dict(slug="entity-resolution", kind="Entity resolution", status=("In progress", "warn"),
         title="Cell-Site Entity Resolution",
         desc="Three telecom systems describe the same towers with no shared ID, matched on evidence into one table.",
         result="78 records → 24 canonical sites", stack=["Spark SQL", "Iceberg", "S3", "EMR"]),
    dict(slug="spark-lab", kind="Spark performance", status=("Code on request", "muted"),
         title="Spark Performance Lab",
         desc="A skewed join reproduced on a real cluster, diagnosed in the Spark UI, with every fix measured.",
         result="Join stage 12.7 s → 2.4 s, spill → 0", stack=["PySpark 4.0", "Spark UI", "AQE"]),
    dict(slug="market-pulse", kind="Streaming", status=None,
         title="Market Pulse",
         desc="Trades captured with Debezium CDC and streamed through Kafka with live prices into Iceberg and dbt.",
         result="No lost or double-counted trades", stack=["Debezium", "Kafka", "Iceberg", "dbt", "BigQuery"]),
    dict(slug="lakehouse", kind="Lakehouse on AWS", status=None,
         title="E-commerce Lakehouse",
         desc="Kinesis clickstream and daily batch orders move through bronze, silver and gold PySpark layers on S3.",
         result="6 gold tables, queryable in Athena", stack=["Kinesis", "Lambda", "PySpark", "Glue", "Athena"]),
    dict(slug="weather", kind="Batch ELT", status=None,
         title="Weather Data Platform",
         desc="Lambda lands hourly weather in S3, Airflow loads Snowflake and dbt builds an incremental star schema.",
         result="Safe to re-run: no duplicates at any layer", stack=["Lambda", "S3", "Snowflake", "dbt", "Airflow"]),
    dict(slug="yelp", kind="Analytics engineering", status=None,
         title="Yelp Reviews Analytics",
         desc="Staging, intermediate and mart dbt models over 2,000+ reviews, with tests, lineage and a SQL health score.",
         result="3 tested marts with documented lineage", stack=["dbt", "PostgreSQL", "Python"]),
    dict(slug="text-to-sql", kind="GenAI", status=None,
         title="Natural-Language SQL Assistant",
         desc="A LangChain agent turns plain-English questions into SQL, runs it on Postgres and fixes its errors.",
         result="Answers questions needing 5-table joins", stack=["LangChain", "OpenAI", "PostgreSQL", "Streamlit"]),
    dict(slug="churn", kind="Machine learning", status=None,
         title="Customer Churn Prediction",
         desc="XGBoost flags telecom customers likely to cancel; SHAP explains each prediction for the retention team.",
         result="ROC-AUC 0.82 on 7,043 customers", stack=["XGBoost", "SHAP", "pandas", "Streamlit"]),
]


def card(p, t):
    c = THEMES[t]
    W, H = 480, 236
    lines = wrap(p["desc"], 54)
    assert len(lines) <= 2, f"{p['title']}: description needs {len(lines)} lines; keep it to 2 (about 100 characters)"
    desc = "".join(f'<tspan x="24" y="{104 + i * 21}">{escape(l)}</tspan>' for i, l in enumerate(lines))
    status = ""
    if p["status"]:
        label, tone = p["status"]
        col = c["warn"] if tone == "warn" else c["muted"]
        bg = c["warn_soft"] if tone == "warn" else c["subtle"]
        w = len(label) * 7.1 + 30
        x = W - 24 - w
        pulse = '<circle class="pulse" cx="{0}" cy="31" r="3.5" fill="{1}"/>'.format(x + 13, col) if tone == "warn" else f'<circle cx="{x + 13}" cy="31" r="3.5" fill="{col}"/>'
        status = f'<rect x="{x:.1f}" y="20" width="{w:.1f}" height="22" rx="11" fill="{bg}" stroke="{c["line"]}"/>{pulse}<text x="{x + 22:.1f}" y="35" class="pill" fill="{col}">{escape(label)}</text>'
    chips, cx = "", 24
    for s in p["stack"]:
        w = len(s) * 7.25 + 16
        if cx + w > W - 24:
            break
        chips += f'<rect x="{cx:.1f}" y="190" width="{w:.1f}" height="24" rx="6" fill="{c["subtle"]}" stroke="{c["line"]}"/><text x="{cx + 8:.1f}" y="206" class="chip">{escape(s)}</text>'
        cx += w + 6
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(p['title'])}: {escape(p['result'])}">
  <defs>
    <linearGradient id="sheen" x1="0" x2="1"><stop offset="0" stop-color="{c['accent']}" stop-opacity="0"/><stop offset=".5" stop-color="{c['accent']}" stop-opacity=".16"/><stop offset="1" stop-color="{c['accent']}" stop-opacity="0"/></linearGradient>
    <clipPath id="res"><rect x="24" y="142" width="{W - 48}" height="34" rx="8"/></clipPath>
  </defs>
  <style>
    text{{font-family:{SANS}}}
    .kind{{font-size:13px;font-weight:600;fill:{c['accent']}}}
    .title{{font-size:21px;font-weight:700;letter-spacing:-.4px;fill:{c['ink']}}}
    .desc{{font-size:14.5px;fill:{c['muted']}}}
    .res{{font-size:14.5px;font-weight:600;fill:{c['ink']}}}
    .reslbl{{font-size:12px;font-weight:600;fill:{c['accent']}}}
    .chip{{font-family:{MONO};font-size:12px;fill:{c['muted']}}}
    .pill{{font-size:12px;font-weight:600}}
    .sweep{{animation:sweep 5s ease-in-out infinite}}
    .pulse{{animation:pulse 1.6s ease-in-out infinite}}
    @keyframes sweep{{0%,55%{{transform:translateX(-200px)}}100%{{transform:translateX({W}px)}}}}
    @keyframes pulse{{50%{{opacity:.25}}}}
    @media (prefers-reduced-motion: reduce){{.sweep,.pulse{{animation:none}}.sweep{{opacity:0}}}}
  </style>
  <rect x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="{c['surface']}" stroke="{c['line']}" stroke-width="1.5"/>
  <text x="24" y="36" class="kind">{escape(p['kind'])}</text>{status}
  <text x="24" y="74" class="title">{escape(p['title'])}</text>
  <text class="desc">{desc}</text>
  <rect x="24" y="142" width="{W - 48}" height="34" rx="8" fill="{c['accent_soft']}"/>
  <g clip-path="url(#res)"><rect class="sweep" x="0" y="142" width="200" height="34" fill="url(#sheen)"/></g>
  <text x="38" y="164" class="reslbl">Result</text><text x="92" y="164" class="res">{escape(p['result'])}</text>
  {chips}
</svg>
"""


# ---------------------------------------------------------------- toolbox
TOOLBOX = [
    ("Core, daily", ["SQL", "Python", "PySpark", "dbt", "Snowflake", "Airflow", "Dagster"], True),
    ("Streaming & lakehouse", ["Kafka", "Debezium CDC", "Structured Streaming", "Iceberg", "Delta Lake", "Parquet"], False),
    ("Cloud & platform", ["AWS S3", "EMR", "Glue", "Kinesis", "Lambda", "Athena", "IAM", "GCP", "Terraform", "Docker", "CI/CD"], False),
    ("Warehouses & BI", ["BigQuery", "Redshift", "Databricks", "Trino", "PostgreSQL", "Oracle", "Looker (LookML)", "Tableau", "Power BI"], False),
    ("GenAI & ML", ["Llama", "Mistral", "LLM evaluation", "LangChain", "XGBoost", "SHAP", "Feature pipelines"], False),
]


def toolbox(t):
    c = THEMES[t]
    W, colw, pad = 1200, 216, 24
    body, maxy = "", 0
    for i, (head, items, core) in enumerate(TOOLBOX):
        x0 = pad + i * (colw + 9)
        body += f'<text x="{x0}" y="44" class="h{" core" if core else ""}">{escape(head)}</text>'
        x, y = x0, 62
        for s in items:
            w = len(s) * 7.6 + 18
            if x + w > x0 + colw:
                x, y = x0, y + 34
            fill = c["accent_soft"] if core else c["subtle"]
            stroke = c["accent"] if core else c["line"]
            body += f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="26" rx="7" fill="{fill}" stroke="{stroke}" stroke-opacity="{0.55 if core else 1}"/><text x="{x + 9:.1f}" y="{y + 17.5}" class="chip{" core" if core else ""}">{escape(s)}</text>'
            x += w + 6
        maxy = max(maxy, y + 26)
    H = maxy + 24
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Toolbox: {escape('; '.join(h + ': ' + ', '.join(it) for h, it, _ in TOOLBOX))}">
  <style>
    text{{font-family:{SANS}}}
    .h{{font-size:14px;font-weight:600;fill:{c['muted']}}}
    .h.core{{fill:{c['accent']}}}
    .chip{{font-family:{MONO};font-size:12.5px;fill:{c['ink']}}}
    .chip.core{{font-weight:600}}
  </style>
  <rect x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="{c['surface']}" stroke="{c['line']}" stroke-width="1.5"/>
  {body}
</svg>
"""


for theme in THEMES:
    write("header", theme, header(theme))
    write("toolbox", theme, toolbox(theme))
    for p in PROJECTS:
        write(f"card-{p['slug']}", theme, card(p, theme))
print("wrote", len(list(OUT.glob("*.svg"))), "SVG files to", OUT)
