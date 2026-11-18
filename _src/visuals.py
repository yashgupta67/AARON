"""SVG visuals for the Arron site. All return markup strings."""
import math

FONT = 'font-family="Manrope,sans-serif"'


def _defs(uid):
    return f'''<defs>
<linearGradient id="g{uid}" x1="0" x2="1"><stop offset="0" stop-color="#ff6b78"/><stop offset="1" stop-color="#6aa3ff"/></linearGradient>
<linearGradient id="f{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6aa3ff" stop-opacity=".4"/><stop offset="1" stop-color="#6aa3ff" stop-opacity="0"/></linearGradient>
</defs>'''


GLASS = 'fill="rgba(255,255,255,.07)" stroke="rgba(255,255,255,.2)"'


# ------------------------------------------------------------------ AI
def v_ai():
    layers = [4, 6, 6, 3]
    xs = [60, 205, 355, 500]
    pts = []
    for li, n in enumerate(layers):
        top, bot = 70, 330
        ys = [top + (bot - top) * (i / (n - 1)) for i in range(n)] if n > 1 else [200]
        pts.append([(xs[li], y) for y in ys])
    edges = []
    for li in range(len(layers) - 1):
        for a in pts[li]:
            for b in pts[li + 1]:
                edges.append(f'<line x1="{a[0]}" y1="{a[1]:.0f}" x2="{b[0]}" y2="{b[1]:.0f}" stroke="rgba(150,190,255,.16)"/>')
    path_nodes = [pts[0][1], pts[1][2], pts[2][3], pts[3][1]]
    path2 = [pts[0][3], pts[1][4], pts[2][2], pts[3][2]]
    path3 = [pts[0][0], pts[1][1], pts[2][1], pts[3][0]]

    def path(p):
        return "M" + " L".join(f"{x},{y:.0f}" for x, y in p)

    flows = ''.join(
        f'<path d="{path(p)}" fill="none" stroke="url(#gai)" stroke-width="2.2" class="sv-flow" style="animation-delay:{i*.4}s"/>'
        for i, p in enumerate([path_nodes, path2, path3]))
    dots = ''.join(
        f'<circle r="5" fill="#fff"><animateMotion dur="{4+i}s" begin="{i*1.1}s" repeatCount="indefinite" path="{path(p)}"/></circle>'
        for i, p in enumerate([path_nodes, path2, path3]))
    nodes = ''
    for li, layer in enumerate(pts):
        for ni, (x, y) in enumerate(layer):
            hot = (li, ni) in [(0, 1), (1, 2), (2, 3), (3, 1), (0, 3), (1, 4), (2, 2), (3, 2), (0, 0), (1, 1), (2, 1), (3, 0)]
            fill = '#ff6b78' if hot and li == 3 else ('#6aa3ff' if hot else '#10306b')
            nodes += f'<circle cx="{x}" cy="{y:.0f}" r="{9 if hot else 7}" fill="{fill}" stroke="rgba(255,255,255,.55)" stroke-width="1.5"/>'
    labels = ''.join(
        f'<text x="{x}" y="372" text-anchor="middle" fill="#9fb3e0" font-size="12" font-weight="700" letter-spacing="2">{t}</text>'
        for x, t in zip(xs, ["DATA", "REASON", "DECIDE", "ACT"]))
    return f'''<svg viewBox="0 0 560 390" {FONT} aria-label="Neural network">
<defs><linearGradient id="gai" x1="0" x2="1"><stop offset="0" stop-color="#ff6b78"/><stop offset="1" stop-color="#6aa3ff"/></linearGradient></defs>
{''.join(edges)}{flows}{nodes}{dots}{labels}</svg>'''


# ------------------------------------------------------------------ ERP
def _spark(x, y, w, h, seed):
    import random
    r = random.Random(seed)
    vals = [r.random() * .6 + .2 for _ in range(7)]
    vals = sorted(vals[:3]) + vals[3:]
    pts = " ".join(f"{x + i * w / 6:.0f},{y + h - v * h:.0f}" for i, v in enumerate(vals))
    return f'<polyline points="{pts}" fill="none" stroke="#6aa3ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'


def v_erp():
    tiles = [("Finance", 20, 18), ("Supply Chain", 215, 18), ("Manufacturing", 410, 18),
             ("Procurement", 20, 308), ("HR & Payroll", 215, 308), ("Sales & CRM", 410, 308)]
    lines = ''
    cx, cy = 280, 195
    for i, (n, x, y) in enumerate(tiles):
        tx, ty = x + 65, (y + 84 if y < 100 else y)
        lines += f'<path d="M{cx},{cy} C{cx},{(cy+ty)/2} {tx},{(cy+ty)/2} {tx},{ty}" fill="none" stroke="url(#gerp)" stroke-width="2" class="sv-flow" style="animation-delay:{i*.3}s"/>'
    tl = ''
    for i, (n, x, y) in enumerate(tiles):
        tl += f'''<g><rect x="{x}" y="{y}" width="130" height="84" rx="16" {GLASS}/>
<text x="{x+16}" y="{y+28}" fill="#fff" font-size="12" font-weight="800">{n}</text>
<circle cx="{x+118}" cy="{y+24}" r="4" fill="#4ade80" class="sv-pulse"/>
{_spark(x+16, y+40, 98, 28, i+3)}</g>'''
    return f'''<svg viewBox="0 0 560 410" {FONT} aria-label="ERP modules">
<defs><linearGradient id="gerp" x1="0" x2="1"><stop offset="0" stop-color="#ff6b78"/><stop offset="1" stop-color="#6aa3ff"/></linearGradient>
<radialGradient id="cerp"><stop offset="0" stop-color="#2563d8"/><stop offset="1" stop-color="#0a2457"/></radialGradient></defs>
{lines}
<circle cx="{cx}" cy="{cy}" r="78" fill="none" stroke="rgba(255,255,255,.18)" stroke-dasharray="3 7" class="spin"/>
<circle cx="{cx}" cy="{cy}" r="58" fill="url(#cerp)" stroke="rgba(255,255,255,.4)" stroke-width="1.5"/>
<text x="{cx}" y="{cy-2}" text-anchor="middle" fill="#fff" font-size="22" font-weight="800">ERP</text>
<text x="{cx}" y="{cy+18}" text-anchor="middle" fill="#bcd0f7" font-size="10.5" letter-spacing="1.5">CORE</text>
{tl}</svg>'''


# ------------------------------------------------------------------ ITSM
def v_itsm():
    cols = [("NEW", 8), ("AI TRIAGE", 146), ("IN PROGRESS", 284), ("RESOLVED", 422)]
    out = ''
    for t, x in cols:
        out += f'<rect x="{x}" y="14" width="130" height="224" rx="14" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.14)"/>'
        out += f'<text x="{x+14}" y="38" fill="#9fb3e0" font-size="10.5" font-weight="800" letter-spacing="1.6">{t}</text>'

    def card(x, y, c):
        return f'<g><rect x="{x}" y="{y}" width="102" height="44" rx="10" fill="rgba(255,255,255,.1)" stroke="rgba(255,255,255,.2)"/><rect x="{x}" y="{y+8}" width="4" height="28" rx="2" fill="{c}"/><rect x="{x+16}" y="{y+13}" width="56" height="6" rx="3" fill="rgba(255,255,255,.7)"/><rect x="{x+16}" y="{y+26}" width="38" height="5" rx="2.5" fill="rgba(255,255,255,.3)"/></g>'
    static = card(22, 52, "#ff6b78") + card(22, 106, "#6aa3ff") + card(160, 106, "#6aa3ff") + card(298, 52, "#6aa3ff") + card(298, 106, "#ff6b78") + card(436, 52, "#4ade80") + card(436, 106, "#4ade80") + card(436, 160, "#4ade80")
    moving = f'''<g><animateTransform attributeName="transform" type="translate" values="0 0;138 0;276 0;414 0;414 0" keyTimes="0;.25;.5;.75;1" dur="8s" repeatCount="indefinite"/>
{card(22,160,"#ff6b78")}</g>'''
    donut = '<circle cx="86" cy="326" r="40" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="10"/><circle cx="86" cy="326" r="40" fill="none" stroke="#4ade80" stroke-width="10" stroke-linecap="round" stroke-dasharray="238 252" transform="rotate(-90 86 326)"/><text x="86" y="331" text-anchor="middle" fill="#fff" font-size="18" font-weight="800">SLA</text>'
    bars = ''.join(f'<rect x="{200+i*34}" y="{380-h}" width="20" height="{h}" rx="5" fill="{"#6aa3ff" if i<5 else "#ff6b78"}" opacity="{.5+i*.07:.2f}"/>' for i, h in enumerate([86, 78, 70, 60, 48, 36, 28]))
    labels = '<text x="200" y="274" fill="#fff" font-size="13" font-weight="800">Open tickets per day</text><text x="200" y="292" fill="#9fb3e0" font-size="11">Trending down since AI triage</text>'
    return f'''<svg viewBox="0 0 560 410" {FONT} aria-label="Service workflow">{out}{static}{moving}
<rect x="8" y="256" width="544" height="146" rx="14" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.14)"/>
{donut}<text x="86" y="384" text-anchor="middle" fill="#9fb3e0" font-size="11">Targets met</text>{labels}{bars}</svg>'''


# ------------------------------------------------------------------ CX
def v_cx():
    return f'''<svg viewBox="0 0 560 410" {FONT} aria-label="Customer journey">
<defs><linearGradient id="gcx" x1="0" x2="1"><stop offset="0" stop-color="#6aa3ff"/><stop offset="1" stop-color="#ff6b78"/></linearGradient>
<linearGradient id="fcx" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6aa3ff" stop-opacity=".4"/><stop offset="1" stop-color="#6aa3ff" stop-opacity="0"/></linearGradient></defs>
<text x="22" y="34" fill="#fff" font-weight="800" font-size="14">Customer satisfaction across the journey</text>
<g stroke="rgba(255,255,255,.1)"><path d="M22 80H540M22 130H540M22 180H540M22 230H540"/></g>
<path d="M22 210C90 210 100 140 160 140S230 220 290 205 380 80 430 80 510 60 540 52V250H22Z" fill="url(#fcx)"/>
<path d="M22 210C90 210 100 140 160 140S230 220 290 205 380 80 430 80 510 60 540 52" fill="none" stroke="url(#gcx)" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="800" stroke-dashoffset="800"><animate attributeName="stroke-dashoffset" from="800" to="0" dur="2.6s" fill="freeze"/></path>
<g fill="#fff"><circle cx="160" cy="140" r="6"/><circle cx="290" cy="205" r="6"/><circle cx="430" cy="80" r="6"/></g>
<circle cx="290" cy="205" r="12" fill="none" stroke="#ff6b78" stroke-width="2"><animate attributeName="r" values="8;20;8" dur="2.6s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0;1" dur="2.6s" repeatCount="indefinite"/></circle>
<g font-size="11.5" font-weight="700" fill="#9fb3e0" text-anchor="middle"><text x="50" y="268">Aware</text><text x="160" y="268">Consider</text><text x="290" y="268">Buy</text><text x="410" y="268">Support</text><text x="510" y="268">Advocate</text></g>
<g transform="translate(8 292)">
<rect width="170" height="108" rx="14" {GLASS}/><text x="16" y="28" fill="#9fb3e0" font-size="11" font-weight="700" letter-spacing="1.4">NPS</text>
<circle cx="125" cy="62" r="28" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="8"/><circle cx="125" cy="62" r="28" fill="none" stroke="#6aa3ff" stroke-width="8" stroke-linecap="round" stroke-dasharray="130 176" transform="rotate(-90 125 62)"/>
<text x="16" y="74" fill="#fff" font-size="30" font-weight="800">+42</text><text x="16" y="94" fill="#9fb3e0" font-size="11">Sample trend</text></g>
<g transform="translate(195 292)"><rect width="170" height="108" rx="14" {GLASS}/><text x="16" y="28" fill="#9fb3e0" font-size="11" font-weight="700" letter-spacing="1.4">RESPONSE TIME</text>
<text x="16" y="70" fill="#fff" font-size="30" font-weight="800">-38%</text><path d="M16 90h138" stroke="rgba(255,255,255,.14)" stroke-width="6" stroke-linecap="round"/><path d="M16 90h86" stroke="#4ade80" stroke-width="6" stroke-linecap="round"/></g>
<g transform="translate(382 292)"><rect width="170" height="108" rx="14" {GLASS}/><text x="16" y="28" fill="#9fb3e0" font-size="11" font-weight="700" letter-spacing="1.4">RETENTION</text>
<text x="16" y="70" fill="#fff" font-size="30" font-weight="800">+12%</text><polyline points="16,96 50,88 84,92 118,78 154,70" fill="none" stroke="#ff6b78" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></g>
</svg>'''


# ------------------------------------------------------------------ Home: connected model
def v_model():
    return f'''<svg viewBox="0 0 520 420" {FONT} aria-label="Arron model">
{_defs('m')}
<rect x="10" y="10" width="500" height="80" rx="18" {GLASS}/><text x="34" y="42" fill="#ff8b95" font-size="11" font-weight="800" letter-spacing="2.4">STRATEGY</text><text x="34" y="70" fill="#fff" font-size="20" font-weight="800">Vision, roadmap and business case</text>
<rect x="10" y="118" width="244" height="110" rx="18" {GLASS}/><text x="34" y="152" fill="#ff8b95" font-size="11" font-weight="800" letter-spacing="2.4">PLATFORMS</text><text x="34" y="182" fill="#fff" font-size="19" font-weight="800">ERP and ITSM</text><text x="34" y="206" fill="#9fb3e0" font-size="12.5">Systems of record and service</text>
<rect x="266" y="118" width="244" height="110" rx="18" {GLASS}/><text x="290" y="152" fill="#ff8b95" font-size="11" font-weight="800" letter-spacing="2.4">INTELLIGENCE</text><text x="290" y="182" fill="#fff" font-size="19" font-weight="800">AI, data and agents</text><text x="290" y="206" fill="#9fb3e0" font-size="12.5">Decisions at scale</text>
<rect x="10" y="256" width="500" height="80" rx="18" {GLASS}/><text x="34" y="288" fill="#ff8b95" font-size="11" font-weight="800" letter-spacing="2.4">EXPERIENCE</text><text x="34" y="316" fill="#fff" font-size="20" font-weight="800">Customers, employees and partners</text>
<path d="M260 90v28M260 228v28" stroke="url(#gm)" stroke-width="2.4" class="sv-flow"/>
<rect x="10" y="362" width="500" height="40" rx="20" fill="url(#gm)" opacity=".92"/><text x="260" y="388" text-anchor="middle" fill="#fff" font-size="13" font-weight="800" letter-spacing="3">MEASURABLE BUSINESS OUTCOMES</text></svg>'''


# ------------------------------------------------------------------ Offerings: connected stack
def v_stack():
    layers = [("AI / SI", "Intelligence", "#6aa3ff"), ("ERP", "Operations", "#4a86f0"), ("ITSM", "Service", "#2f6bd8"), ("CX", "Experience", "#ff6b78")]
    out = ''
    for i, (t, s, c) in enumerate(layers):
        y = 40 + i * 78
        out += f'''<g style="animation:float {6+i*.6}s ease-in-out infinite;animation-delay:{i*.3}s">
<path d="M280 {y} L470 {y+36} L280 {y+72} L90 {y+36} Z" fill="{c}" fill-opacity=".28" stroke="{c}" stroke-width="1.6"/>
<path d="M90 {y+36} L280 {y+72} L280 {y+84} L90 {y+48} Z" fill="{c}" fill-opacity=".45"/><path d="M470 {y+36} L280 {y+72} L280 {y+84} L470 {y+48} Z" fill="{c}" fill-opacity=".6"/>
<text x="280" y="{y+40}" text-anchor="middle" fill="#fff" font-size="18" font-weight="800">{t}</text><text x="280" y="{y+58}" text-anchor="middle" fill="#dbe6ff" font-size="11" letter-spacing="2">{s.upper()}</text></g>'''
    return f'''<svg viewBox="0 0 560 420" {FONT} aria-label="Connected stack">
<path d="M280 20V400" stroke="rgba(255,255,255,.18)" stroke-dasharray="3 7"/>{out}
<circle r="5" fill="#fff"><animateMotion dur="5s" repeatCount="indefinite" path="M280 20V400"/></circle></svg>'''


# ------------------------------------------------------------------ Capabilities
def v_consult():
    return f'''<svg viewBox="0 0 560 360" {FONT}><g stroke="rgba(255,255,255,.1)"><path d="M30 300H540M30 240H540M30 180H540M30 120H540M30 60H540"/></g>
<g><rect x="70" y="220" width="62" height="80" rx="8" fill="#6aa3ff" opacity=".35"/><rect x="190" y="170" width="62" height="130" rx="8" fill="#6aa3ff" opacity=".55"/><rect x="310" y="115" width="62" height="185" rx="8" fill="#6aa3ff" opacity=".75"/><rect x="430" y="55" width="62" height="245" rx="8" fill="#6aa3ff"/></g>
<path d="M101 200L221 150L341 95L461 38" fill="none" stroke="#ff6b78" stroke-width="3" stroke-linecap="round" stroke-dasharray="500" stroke-dashoffset="500"><animate attributeName="stroke-dashoffset" to="0" dur="2s" fill="freeze"/></path><circle cx="461" cy="38" r="7" fill="#ff6b78"/>
<g font-size="12" font-weight="700" fill="#9fb3e0" text-anchor="middle"><text x="101" y="328">Assess</text><text x="221" y="328">Plan</text><text x="341" y="328">Build</text><text x="461" y="328">Realize</text></g></svg>'''


def v_services():
    cols = [("DESIGN", ["Requirements", "Architecture", "Prototype"]), ("BUILD", ["Configure", "Integrate", "Test & train"]), ("RUN", ["Monitor", "Support", "Improve"])]
    out = ''
    for i, (t, items) in enumerate(cols):
        x = 12 + i * 182
        out += f'<rect x="{x}" y="30" width="166" height="250" rx="18" {GLASS}/><text x="{x+20}" y="64" fill="#ff8b95" font-size="11" font-weight="800" letter-spacing="2.4">{t}</text>'
        for j, it in enumerate(items):
            out += f'<rect x="{x+16}" y="{84+j*62}" width="134" height="46" rx="10" fill="rgba(255,255,255,.08)"/><text x="{x+32}" y="{112+j*62}" fill="#fff" font-size="13" font-weight="700">{it}</text>'
    return f'''<svg viewBox="0 0 560 330" {FONT}>{out}
<path d="M178 155h16M360 155h16" stroke="#ff6b78" stroke-width="2.4" class="sv-flow"/>
<path d="M30 310H530" stroke="rgba(255,255,255,.25)" stroke-dasharray="3 6"/><circle r="5" fill="#ff6b78"><animateMotion dur="5s" repeatCount="indefinite" path="M30 310H530"/></circle></svg>'''


def v_partners():
    names = ["ServiceNow", "SAP", "Microsoft", "Oracle", "Atlassian", "Salesforce"]
    cx, cy, R = 280, 180, 128
    out = ''
    for i, n in enumerate(names):
        a = -math.pi / 2 + i * 2 * math.pi / 6
        x, y = cx + R * math.cos(a) * 1.55, cy + R * math.sin(a) * 1.1
        out += f'<path d="M{cx},{cy} L{x:.0f},{y:.0f}" stroke="url(#gp)" stroke-width="1.8" class="sv-flow" style="animation-delay:{i*.3}s"/>'
        out += f'<rect x="{x-56:.0f}" y="{y-22:.0f}" width="112" height="44" rx="12" {GLASS}/><text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" fill="#fff" font-size="13" font-weight="800">{n}</text>'
    return f'''<svg viewBox="0 0 560 360" {FONT}><defs><linearGradient id="gp" x1="0" x2="1"><stop offset="0" stop-color="#ff6b78"/><stop offset="1" stop-color="#6aa3ff"/></linearGradient></defs>{out}
<circle cx="{cx}" cy="{cy}" r="44" fill="#fff"/><image href="assets/img/mark.png" x="{cx-30}" y="{cy-22}" width="60" height="42"/></svg>'''


def v_product():
    pts = [("Discover", 280, 58), ("Build", 424, 180), ("Ship", 280, 302), ("Learn", 136, 180)]
    out = ''.join(f'<circle cx="{x}" cy="{y}" r="36" fill="#0a2457" stroke="url(#gpr)" stroke-width="2.4"/><text x="{x}" y="{y+5}" text-anchor="middle" fill="#fff" font-size="13" font-weight="800">{t}</text>' for t, x, y in pts)
    return f'''<svg viewBox="0 0 560 360" {FONT}><defs><linearGradient id="gpr" x1="0" x2="1"><stop offset="0" stop-color="#ff6b78"/><stop offset="1" stop-color="#6aa3ff"/></linearGradient></defs>
<circle cx="280" cy="180" r="122" fill="none" stroke="rgba(255,255,255,.2)" stroke-dasharray="3 7" class="spin"/>
<circle cx="280" cy="180" r="62" fill="rgba(255,255,255,.08)" stroke="rgba(255,255,255,.3)"/><text x="280" y="176" text-anchor="middle" fill="#fff" font-size="15" font-weight="800">Your</text><text x="280" y="196" text-anchor="middle" fill="#fff" font-size="15" font-weight="800">product</text>{out}
<circle r="5" fill="#ff6b78"><animateMotion dur="8s" repeatCount="indefinite" path="M280 58A122 122 0 1 1 279.9 58"/></circle></svg>'''


# ------------------------------------------------------------------ Page-hero visuals
def v_ladder():
    out = ''
    for i, (t, s, r) in enumerate([("ADVISE", "You lead", 150), ("DELIVER", "We co-deliver", 105), ("OPERATE", "We own it", 62)]):
        out += f'<circle cx="280" cy="195" r="{r+30}" fill="rgba(255,255,255,{.04+i*.04})" stroke="rgba(255,255,255,.22)"/>'
    return f'''<svg viewBox="0 0 560 390" {FONT}>{out}
<text x="280" y="55" text-anchor="middle" fill="#9fb3e0" font-size="11" font-weight="800" letter-spacing="2.5">ADVISE · YOU LEAD</text>
<text x="280" y="102" text-anchor="middle" fill="#cfdcff" font-size="11" font-weight="800" letter-spacing="2.5">DELIVER · CO-DELIVER</text>
<text x="280" y="190" text-anchor="middle" fill="#fff" font-size="16" font-weight="800">OPERATE</text><text x="280" y="212" text-anchor="middle" fill="#bcd0f7" font-size="11.5">We own the outcome</text>
<circle r="6" fill="#ff6b78"><animateMotion dur="9s" repeatCount="indefinite" path="M280 45A150 150 0 1 1 279.9 45"/></circle>
<circle r="5" fill="#fff"><animateMotion dur="7s" repeatCount="indefinite" path="M280 90A105 105 0 1 0 280.1 90"/></circle></svg>'''


def v_industries():
    items = ["Banking", "Manufacturing", "Healthcare", "Retail", "Telecom", "Technology", "Energy", "Public sector"]
    out = ''
    for i, t in enumerate(items):
        x, y = 14 + (i % 4) * 136, 40 + (i // 4) * 120
        out += f'<g style="animation:float {5+i*.4}s ease-in-out infinite;animation-delay:{i*.25}s"><rect x="{x}" y="{y}" width="124" height="96" rx="16" {GLASS}/><circle cx="{x+24}" cy="{y+28}" r="6" fill="{"#ff6b78" if i%3==0 else "#6aa3ff"}"/><text x="{x+16}" y="{y+68}" fill="#fff" font-size="13.5" font-weight="800">{t}</text><rect x="{x+16}" y="{y+78}" width="{40+(i*13)%50}" height="4" rx="2" fill="rgba(255,255,255,.25)"/></g>'
    return f'<svg viewBox="0 0 560 290" {FONT}>{out}</svg>'


def _ico(path, x, y, size=26):
    sc = size / 24
    return f'<g transform="translate({x} {y}) scale({sc})" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{path}</g>'


ICON_PATHS = {
    "article": '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 12h6M9 16h6"/>',
    "webinar": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/><path d="M10.5 8.5l4 2-4 2z"/>',
    "career": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V4h6v3M3 13h18"/>',
}


def v_resources():
    rows = [("blog.html", "BLOGS & NEWSLETTER", "Is your enterprise ready for AI?", "#2563d8", "article"),
            ("events.html", "EVENTS & WEBINARS", "ERP selection, step by step", "#d4202f", "webinar"),
            ("careers.html", "CAREERS", "Build the next chapter with us", "#1a9a5b", "career")]
    out = ''
    for i, (href, t, s2, c, ic) in enumerate(rows):
        y = 24 + i * 100
        out += f'''<a href="{href}" class="rrow"><rect class="rowbg" x="20" y="{y}" width="520" height="84" rx="16" {GLASS}/>
<rect x="38" y="{y+14}" width="56" height="56" rx="14" fill="{c}"/>{_ico(ICON_PATHS[ic], 38+15, y+14+15, 26)}
<text x="116" y="{y+37}" fill="#9fb3e0" font-size="11" font-weight="800" letter-spacing="2.2">{t}</text>
<text x="116" y="{y+62}" fill="#fff" font-size="17" font-weight="800">{s2}</text>
<path d="M500 {y+42}h14m-6-6l6 6-6 6" fill="none" stroke="#9fb3e0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></a>'''
    return f'<svg viewBox="0 0 560 330" {FONT}>{out}</svg>'


def v_impact():
    cards = [("Close cycle", "-32%", "#6aa3ff", 16), ("Ticket handling", "-40%", "#ff6b78", 82), ("NPS", "+18", "#4ade80", 148)]
    out = ''
    for t, v, c, _ in cards:
        pass
    for i, (t, v, c, _) in enumerate(cards):
        x = 20 + i * 178
        pts = " ".join(f"{x+16+j*22},{110-(j*5+(i*7)%9)}" for j in range(6))
        out += f'''<g><rect x="{x}" y="24" width="166" height="130" rx="16" {GLASS}/>
<text x="{x+16}" y="52" fill="#9fb3e0" font-size="11" font-weight="800" letter-spacing="1.6">{t.upper()}</text>
<text x="{x+16}" y="94" fill="#fff" font-size="32" font-weight="800">{v}</text>
<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" transform="translate(0 22)"/></g>'''
    bars = ''.join(f'<rect x="{34+i*40}" y="{300-h}" width="26" height="{h}" rx="6" fill="{"#ff6b78" if i==6 else "#6aa3ff"}" opacity="{.35+i*.09:.2f}"/>' for i, h in enumerate([22, 36, 30, 52, 64, 78, 92]))
    return f'''<svg viewBox="0 0 560 330" {FONT}>{out}<rect x="20" y="176" width="520" height="140" rx="16" {GLASS}/>
<text x="38" y="204" fill="#fff" font-size="14" font-weight="800">Program value delivered over time</text>{bars}
<path d="M34 236C140 232 220 210 330 196S470 186 520 180" fill="none" stroke="rgba(255,255,255,.35)" stroke-dasharray="4 6"/></svg>'''


def v_map():
    cities = [("Seattle", 90, 80), ("Los Angeles", 80, 230), ("Chicago", 330, 120), ("New York", 470, 110), ("Atlanta", 400, 230)]
    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="2" fill="rgba(255,255,255,.22)"/>' for x in range(30, 540, 18) for y in range(40, 300, 18) if 24 < x < 520)
    out = ''
    for i, (n, x, y) in enumerate(cities):
        out += f'<path d="M230,215 Q{(230+x)/2},{min(215,y)-60} {x},{y}" fill="none" stroke="url(#gmap)" stroke-width="1.8" class="sv-flow" style="animation-delay:{i*.3}s"/><circle cx="{x}" cy="{y}" r="5" fill="#6aa3ff"/><text x="{x}" y="{y-12}" text-anchor="middle" fill="#bcd0f7" font-size="11" font-weight="700">{n}</text>'
    return f'''<svg viewBox="0 0 560 320" {FONT}><defs><linearGradient id="gmap" x1="0" x2="1"><stop offset="0" stop-color="#ff6b78"/><stop offset="1" stop-color="#6aa3ff"/></linearGradient></defs>{dots}{out}
<circle cx="230" cy="215" r="14" fill="none" stroke="#ff6b78" stroke-width="2"><animate attributeName="r" values="8;30;8" dur="2.8s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0;1" dur="2.8s" repeatCount="indefinite"/></circle>
<circle cx="230" cy="215" r="8" fill="#ff6b78"/><text x="230" y="248" text-anchor="middle" fill="#fff" font-size="15" font-weight="800">Dallas, TX</text><text x="230" y="266" text-anchor="middle" fill="#9fb3e0" font-size="11">Headquarters</text></svg>'''


# ------------------------------------------------------------------ small art
def mini(kind):
    if kind == "ai":
        nodes = [(60, 50), (60, 140), (150, 30), (150, 95), (150, 160), (240, 70), (240, 125)]
        lines = ''.join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="rgba(150,190,255,.35)"/>' for a in nodes[:2] for b in nodes[2:5]) + ''.join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="rgba(150,190,255,.35)"/>' for a in nodes[2:5] for b in nodes[5:])
        dots = ''.join(f'<circle cx="{x}" cy="{y}" r="{8 if i in (3,5) else 6}" fill="{"#ff6b78" if i==5 else "#6aa3ff"}" stroke="#fff" stroke-opacity=".6"/>' for i, (x, y) in enumerate(nodes))
        return f'<svg viewBox="0 0 300 190" preserveAspectRatio="xMidYMid slice">{lines}{dots}<circle r="4" fill="#fff"><animateMotion dur="3s" repeatCount="indefinite" path="M60,50 L150,95 L240,70"/></circle></svg>'
    if kind == "erp":
        out = ''
        for i in range(6):
            x, y = 46 + (i % 3) * 78, 34 + (i // 3) * 68
            out += f'<rect x="{x}" y="{y}" width="64" height="52" rx="10" fill="rgba(255,255,255,.1)" stroke="rgba(255,255,255,.25)"/><rect x="{x+10}" y="{y+34}" width="{20+i*5}" height="5" rx="2.5" fill="{"#ff6b78" if i==4 else "#6aa3ff"}"/>'
        return f'<svg viewBox="0 0 300 190" preserveAspectRatio="xMidYMid slice">{out}<path d="M110 60h14M188 60h14M110 128h14M188 128h14" stroke="#fff" stroke-opacity=".5" stroke-dasharray="3 3"/></svg>'
    if kind == "itsm":
        out = ''
        for i, (t, c) in enumerate([("New", "#ff6b78"), ("Triage", "#6aa3ff"), ("Done", "#4ade80")]):
            x = 30 + i * 92
            out += f'<rect x="{x}" y="50" width="74" height="86" rx="12" fill="rgba(255,255,255,.08)" stroke="rgba(255,255,255,.22)"/><rect x="{x+10}" y="62" width="54" height="22" rx="6" fill="{c}" opacity=".85"/><rect x="{x+10}" y="94" width="40" height="5" rx="2.5" fill="rgba(255,255,255,.5)"/><rect x="{x+10}" y="106" width="28" height="5" rx="2.5" fill="rgba(255,255,255,.3)"/>'
        return f'<svg viewBox="0 0 300 190" preserveAspectRatio="xMidYMid slice">{out}<path d="M106 93h14M198 93h14" stroke="#fff" stroke-dasharray="3 3"/></svg>'
    if kind == "cx":
        return '<svg viewBox="0 0 300 190" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="mcx" x1="0" x2="1"><stop offset="0" stop-color="#6aa3ff"/><stop offset="1" stop-color="#ff6b78"/></linearGradient></defs><path d="M20 140C70 140 80 80 120 80S170 150 205 130 250 50 285 40" fill="none" stroke="url(#mcx)" stroke-width="3.5" stroke-linecap="round"/><g fill="#fff"><circle cx="120" cy="80" r="5"/><circle cx="205" cy="130" r="5"/><circle cx="285" cy="40" r="5"/></g><circle cx="205" cy="130" r="12" fill="none" stroke="#ff6b78"><animate attributeName="r" values="6;16;6" dur="2.6s" repeatCount="indefinite"/></circle></svg>'


def art(kind):
    if kind == "rings":
        return '<svg viewBox="0 0 400 170" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="rgba(255,255,255,.2)"><circle cx="300" cy="85" r="110"/><circle cx="300" cy="85" r="70"/><circle cx="300" cy="85" r="30"/></g><circle cx="300" cy="85" r="7" fill="#ff6b78"/></svg>'
    if kind == "waves":
        return '<svg viewBox="0 0 400 170" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="rgba(255,255,255,.24)"><path d="M0 130Q100 70 200 110T400 40"/><path d="M0 150Q100 90 200 130T400 60"/><path d="M0 110Q100 50 200 90T400 20"/></g><circle cx="200" cy="110" r="6" fill="#ff6b78"/></svg>'
    if kind == "bars":
        return '<svg viewBox="0 0 400 170" preserveAspectRatio="xMidYMid slice"><g fill="rgba(106,163,255,.5)"><rect x="230" y="70" width="34" height="100" rx="6"/><rect x="280" y="40" width="34" height="130" rx="6"/><rect x="330" y="95" width="34" height="75" rx="6"/></g><rect x="280" y="40" width="34" height="130" rx="6" fill="#ff6b78" opacity=".7"/></svg>'
    return '<svg viewBox="0 0 400 170" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="rgba(255,255,255,.22)"><circle cx="200" cy="85" r="60"/><circle cx="260" cy="85" r="60"/><circle cx="320" cy="85" r="60"/></g></svg>'


AVATAR = '<svg viewBox="0 0 200 200"><circle cx="100" cy="78" r="38" fill="rgba(255,255,255,.22)"/><path d="M20 200c0-46 36-74 80-74s80 28 80 74z" fill="rgba(255,255,255,.22)"/></svg>'
