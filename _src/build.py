#!/usr/bin/env python3
"""Generates the Arron static site into the parent folder. Run: python3 _src/build.py"""
import os
import visuals as V

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHEV = '<svg viewBox="0 0 12 8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M1 1.5l5 5 5-5"/></svg>'
LI = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.1c.6-1 1.9-2 3.9-2 4 0 4.7 2.6 4.7 6V21h-4v-5c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7V21h-4z"/></svg>'

ICONS = {
    "bank": '<path d="M3 21h18M5 21V10M10 21V10M14 21V10M19 21V10M2 10l10-6 10 6"/>',
    "factory": '<path d="M3 21V8l6 4V8l6 4V4h6v17z"/>',
    "heart": '<path d="M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10z"/>',
    "cart": '<path d="M6 6h15l-2 9H8zM6 6L5 3H2"/><circle cx="9" cy="20" r="1.2"/><circle cx="18" cy="20" r="1.2"/>',
    "signal": '<path d="M5 12a10 10 0 0 1 14 0M8 15a6 6 0 0 1 8 0M12 19h.01"/>',
    "code": '<path d="M8 8l-5 4 5 4M16 8l5 4-5 4M14 5l-4 14"/>',
    "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    "gov": '<path d="M3 10l9-6 9 6M5 10v9h14v-9M9 19v-5h6v5"/>',
    "server": '<rect x="3" y="4" width="18" height="6" rx="2"/><rect x="3" y="14" width="18" height="6" rx="2"/><path d="M7 7h.01M7 17h.01"/>',
    "truck": '<path d="M2 6h12v10H2zM14 10h5l3 3v3h-8"/><circle cx="6" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/>',
    "brief": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V4h6v3M3 13h18"/>',
    "plane": '<path d="M2 14l20-8-8 20-3-9z"/>',
}


def icon(k):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[k]}</svg>'


PLATFORMS = ["ServiceNow", "SAP", "Oracle", "Microsoft Azure", "Atlassian", "Salesforce", "AWS", "Google Cloud", "Workday", "NetSuite", "Dynamics 365", "Pega"]

NAV = [("index.html", "Home"), ("offerings.html", "Offerings"), ("capabilities.html", "Capabilities"),
       ("industry.html", "Industry Expertise"), ("resources.html", "Resources"), ("about.html", "About Us")]
OFFERS = [
    ("ai.html", "AI / SI", "Artificial & Super Intelligence", "Strategy, data and agentic AI"),
    ("erp.html", "ERP", "Enterprise Resource Planning", "Select, implement, optimize"),
    ("itsm.html", "ITSM", "IT Service Management", "Faster, smarter service operations"),
    ("cx.html", "CX", "Customer Experience", "Journeys, platforms and insight"),
]


def header(active):
    items = ''
    for href, label in NAV:
        if href == "offerings.html":
            on = ' active' if active in ("offerings.html", "ai.html", "erp.html", "itsm.html", "cx.html") else ''
            menu = '<div class="menu">' + ''.join(f'<a href="{h}"><b>{t}</b><span>{d}</span></a>' for h, _, t, d in OFFERS) + '</div>'
            items += f'<div class="dd"><a class="{on.strip()}" href="offerings.html">{label}{CHEV}</a>{menu}</div>'
        else:
            on = ' class="active"' if href == active else ''
            items += f'<a href="{href}"{on}>{label}</a>'
    return f'''<header class="site-header"><div class="wrap bar">
<a class="logo" href="index.html" aria-label="Arron home"><img src="assets/img/logo.png" alt="Arron — Ahead of now"></a>
<button class="burger" aria-label="Menu"><span></span><span></span></button>
<nav class="nav">{items}<a class="btn btn-red" href="about.html#contact">Talk to us {ARROW}</a></nav></div></header>'''


def footer():
    return f'''<footer class="site-footer"><div class="wrap"><div class="ft">
<div><img src="assets/img/logo-light.png" alt="Arron"><p style="max-width:34ch">Enterprise technology consulting for AI, ERP, ITSM and customer experience. Based in Dallas, Texas.</p></div>
<div><h4>Offerings</h4><ul><li><a href="ai.html">AI / Super Intelligence</a></li><li><a href="erp.html">ERP</a></li><li><a href="itsm.html">ITSM</a></li><li><a href="cx.html">Customer Experience</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="capabilities.html">Capabilities</a></li><li><a href="industry.html">Industry Expertise</a></li><li><a href="resources.html">Resources</a></li><li><a href="about.html">About Us</a></li></ul></div>
<div><h4>Contact</h4><ul><li>Dallas, Texas, USA</li><li><a href="mailto:hello@arron.com">hello@arron.com</a></li><li><a href="about.html#contact">Book a conversation</a></li></ul></div></div>
<div class="fb"><span>© 2026 Arron. All rights reserved.</span><span>Privacy · Terms · Accessibility</span></div></div></footer>'''


def marquee(label="The platforms and ecosystems we work across", names=PLATFORMS):
    items = ''.join(f'<div class="it">{n}</div>' for n in names)
    return f'<div class="marq"><div class="lab">{label}</div><div class="roll"><div class="track">{items}{items}</div></div></div>'


def page(fname, title, desc, active, body):
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="icon" href="assets/img/mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css"></head>
<body>{header(active)}
{body}
{footer()}
<script src="assets/main.js"></script></body></html>'''
    with open(os.path.join(ROOT, fname), "w") as f:
        f.write(html)


def tag(text, sub, pos, red=False):
    return f'<div class="tag{" red" if red else ""}" style="{pos}"><i></i><span>{text}<small>{sub}</small></span></div>'


def hero(crumb, h1, lead, stage, tags='', ctas=True, cls=''):
    cta = f'<div class="hero-cta rv" data-delay=".5"><a class="btn btn-red" href="about.html#contact">Talk to an expert {ARROW}</a><a class="btn btn-ghost" href="#more">Explore below</a></div>' if ctas else ''
    return f'''<section class="hero {cls}"><div class="wrap hero-grid"><div>
<div class="crumbs rv">{crumb}</div><h1 data-split>{h1}</h1><p class="lead rv" data-delay=".35">{lead}</p>{cta}</div>
<div class="stage rv" data-delay=".25">{stage}{tags}</div></div></section>'''


def sh(kicker, h2, p, dark=False):
    return f'<div class="sh"><div><span class="kicker rv">{kicker}</span><h2 data-split>{h2}</h2></div><p class="rv" data-delay=".2">{p}</p></div>'


def rows(items, cls=''):
    return f'<div class="rows {cls}" data-stagger>' + ''.join(
        f'<div class="row"><span class="n">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(items)) + '</div>'


def cta_band(h, p):
    return f'<section style="padding:70px 0 110px"><div class="wrap"><div class="cta rv"><div><h2>{h}</h2><p>{p}</p><a class="btn btn-red" href="about.html#contact">Start a conversation {ARROW}</a></div></div></div></section>'


# =========================================================== OFFERING DETAIL PAGES
OFFER_DATA = {
    "ai": dict(
        file="ai.html", name="Artificial & Super Intelligence", short="AI / SI", visual=V.v_ai, mini="ai",
        h1='Put intelligence to work <span class="r">across the enterprise.</span>',
        lead="From readiness to production-grade agents, we help you apply AI where it changes a number: cost, speed, revenue or risk. And we build toward systems that reason and act across the whole business, responsibly.",
        tags=[("Agent resolved a request", "Handled end to end", "top:-18px;right:-14px", False), ("Model confidence", "Monitored in real time", "bottom:-18px;left:-14px", True)],
        what_p="Four building blocks take you from a promising idea to AI that your people trust and use every day.",
        what=[("AI readiness & strategy", "Find the use cases worth pursuing, size the value and set a sequenced roadmap."),
              ("Data foundations", "Pipelines, quality and architecture that your models can rely on."),
              ("Agents & copilots", "Task-doing AI built into the ERP, service and customer workflows you already run."),
              ("Governance & trust", "Security, compliance and responsible-AI controls designed in from day one.")],
        steps=[("Assess", "Review readiness across data, platforms, skills and risk."), ("Prioritize", "Rank use cases by value and feasibility, then pick the first wins."),
               ("Build", "Prototype, test and take solutions into production."), ("Scale", "Monitor, govern and extend what works across the business.")],
        where=[("server", "Enterprise IT", "AI triage, anomaly detection and self-service."), ("bank", "Banking & Financial", "Fraud signals and compliance monitoring."),
               ("factory", "Manufacturing", "Demand forecasting and predictive maintenance."), ("heart", "Healthcare", "Documentation and operational support."),
               ("cart", "Retail", "Personalization and demand sensing."), ("signal", "Telecom", "Network incident prediction and routing.")],
        platforms=["Azure OpenAI", "AWS Bedrock", "Google Vertex AI", "ServiceNow AI", "SAP Business AI", "Salesforce Einstein", "Atlassian Intelligence", "Databricks", "Snowflake"]),
    "erp": dict(
        file="erp.html", name="Enterprise Resource Planning", short="ERP", visual=V.v_erp, mini="erp",
        h1='The right ERP, <span class="r">chosen and delivered right.</span>',
        lead="Vendor-independent advice and hands-on delivery, so the system that runs your finance and operations fits the way you work and actually gets adopted.",
        tags=[("Finance close", "Automated across entities", "top:-18px;right:-14px", False), ("Supply chain live", "Single source of truth", "bottom:-18px;left:-14px", True)],
        what_p="From the first requirements workshop to life after go-live, we cover the full ERP journey.",
        what=[("Selection", "Requirements, scripted demos and an unbiased comparison of vendors."),
              ("Implementation", "Program leadership and delivery from design through go-live."),
              ("Contract negotiation", "Transparent total cost of ownership and terms that protect you."),
              ("Cloud migration & optimization", "Move to the cloud and keep improving without disrupting operations.")],
        steps=[("Strategy", "Define goals, roadmap and the business case."), ("Select", "Shortlist, demo and negotiate with the right vendor."),
               ("Implement", "Design, configure, integrate, test and train."), ("Optimize", "Stabilize, measure and extend after go-live.")],
        where=[("factory", "Manufacturing", "Planning, shop floor and quality in one system."), ("truck", "Distribution & Supply Chain", "Inventory, logistics and demand visibility."),
               ("gov", "Public Sector", "Modernization for state, local and nonprofit."), ("bank", "Financial Services", "Finance, controls and reporting at scale."),
               ("heart", "Healthcare", "Supply, finance and workforce management."), ("brief", "Professional Services", "Projects, billing and resource planning.")],
        platforms=["SAP S/4HANA", "Oracle Fusion", "Microsoft Dynamics 365", "NetSuite", "Workday", "Infor", "Epicor", "Acumatica", "IFS"]),
    "itsm": dict(
        file="itsm.html", name="IT Service Management", short="ITSM", visual=V.v_itsm, mini="itsm",
        h1='Service operations that <span class="r">resolve faster and cost less.</span>',
        lead="We design and deploy ITIL-aligned service management on leading platforms, with AI handling triage, routing and prediction so your team spends time on what matters.",
        tags=[("Ticket auto-triaged", "Routed in seconds", "top:-18px;right:-14px", False), ("SLA on track", "Predicted before breach", "bottom:-18px;left:-14px", True)],
        what_p="A service desk people want to use, backed by processes that scale as the business grows.",
        what=[("Process optimization", "Standardize and automate incident, change and request workflows."),
              ("Incident & problem management", "Faster resolution, plus root-cause work that cuts repeat tickets."),
              ("Change & release", "Structured approvals, risk scoring and rollback planning."),
              ("Asset management & portal", "A lifecycle-aware CMDB and a self-service portal that gets used.")],
        steps=[("Assess", "Measure maturity across tools, workflows and skills."), ("Roadmap", "Choose the platform, integrations, KPIs and timeline."),
               ("Implement", "Configure portal, SLAs and automation, and migrate from legacy tools."), ("Optimize", "Use analytics to predict breaches and extend to HR and Finance.")],
        where=[("server", "Enterprise IT", "Centralized portals and SLA breach prediction."), ("bank", "BFSI", "Audit-ready change trails and compliance."),
               ("code", "SaaS", "Incident correlation across DevOps pipelines."), ("heart", "Healthcare & Pharma", "SLA-driven support for critical systems."),
               ("cart", "Retail", "Surge detection for peak-season traffic."), ("signal", "Telecom & Media", "Network incident prediction and routing.")],
        platforms=["ServiceNow", "Jira Service Management", "BMC Helix", "Freshservice", "Atlassian Assets", "Microsoft Teams", "Slack", "Zendesk", "PagerDuty"]),
    "cx": dict(
        file="cx.html", name="Customer Experience", short="CX", visual=V.v_cx, mini="cx",
        h1='Turn every interaction <span class="r">into loyalty.</span>',
        lead="We connect the data, platforms and people behind each touchpoint, so customers get one consistent experience wherever they meet you.",
        tags=[("Journey connected", "Every channel, one view", "top:-18px;right:-14px", False), ("Friction removed", "Where customers drop off", "bottom:-18px;left:-14px", True)],
        what_p="Better experiences come from fixing the moments that matter, and the systems underneath them.",
        what=[("Journey design", "Map the customer journey and fix the moments that matter most."),
              ("CX platforms", "CRM, contact center and digital engagement, implemented well."),
              ("Insight & personalization", "Unified data that drives the next best action."),
              ("Service excellence", "AI-assisted agents and self-service that resolve first time.")],
        steps=[("Listen", "Gather feedback, data and journey evidence."), ("Design", "Define target experience and the business case."),
               ("Build", "Implement platforms, integrations and automations."), ("Optimize", "Measure satisfaction and keep improving.")],
        where=[("cart", "Retail & Consumer", "Omnichannel service and personalization."), ("bank", "Banking", "Seamless onboarding and support."),
               ("signal", "Telecom", "Proactive service and churn reduction."), ("heart", "Healthcare", "Patient access and engagement."),
               ("code", "Technology & SaaS", "Product-led onboarding and success."), ("plane", "Travel & Hospitality", "Loyalty and real-time service recovery.")],
        platforms=["Salesforce", "Microsoft Dynamics 365", "Adobe Experience Cloud", "Twilio", "Genesys", "Zendesk", "HubSpot", "Qualtrics", "Five9"]),
}
ORDER = ["ai", "erp", "itsm", "cx"]


def build_offer(key):
    d = OFFER_DATA[key]
    idx = ORDER.index(key)
    others = [OFFER_DATA[k] for k in ORDER if k != key]
    tags = ''.join(tag(t, s, p, r) for t, s, p, r in d["tags"])
    b = hero(f'<a href="index.html">Home</a> / <a href="offerings.html">Offerings</a> / {d["short"]}', d["h1"], d["lead"], d["visual"](), tags)
    b += marquee(f'{d["short"]} platforms and tools we work with', d["platforms"] * 2)
    b += f'<section id="more"><div class="wrap">{sh("What we do", "Everything you need, from first idea to steady state.", d["what_p"])}{rows(d["what"], "c4w")}</div></section>'
    b += '<section class="navy"><div class="wrap">' + sh("How we deliver", "A clear path with no surprises.", "Four stages, each with a defined output, so you always know where the program stands.") + \
         '<div class="proc" data-stagger>' + ''.join(f'<div class="pstep"><span class="n">{i+1}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(d["steps"])) + '</div></div></section>'
    b += '<section><div class="wrap">' + sh("Where it works", "Proven in the industries that run on it.", "The same disciplined approach, tuned to the realities of each sector.") + \
         '<div class="inds c3" data-stagger>' + ''.join(f'<div class="ind">{icon(i)}<h3>{t}</h3><p>{p}</p></div>' for i, t, p in d["where"]) + '</div></div></section>'
    b += '<section class="paper"><div class="wrap">' + sh("Explore further", "Other practices that connect with this one.", "Each practice stands alone, and together they close the gaps between your systems, service and customers.") + \
         '<div class="tiles" style="grid-template-columns:repeat(3,1fr)" data-stagger>' + ''.join(
             f'<a class="tile" href="{o["file"]}"><div class="art">{V.mini(o["mini"])}</div><div class="tb"><span class="k">{o["short"]}</span><h3>{o["name"]}</h3><p>{o_desc(o)}</p><span class="more">Explore {ARROW}</span></div></a>' for o in others) + '</div></div></section>'
    b += cta_band(f"Ready to talk {d['short']}?", "Tell us the outcome you want. We will tell you honestly how to get there.")
    page(d["file"], f'{d["name"]} — Arron', d["lead"][:150], "offerings.html", b)


def o_desc(o):
    return {"ai": "Strategy, data foundations and agentic solutions that move AI from pilot to production.",
            "erp": "Selection, implementation and optimization of the platforms that run finance and operations.",
            "itsm": "Faster resolution and happier users through ITIL-aligned, AI-assisted service operations.",
            "cx": "Journeys, platforms and insight that turn every interaction into loyalty and growth."}[o["mini"]]


def tiles4():
    return '<div class="tiles" data-stagger>' + ''.join(
        f'<a class="tile" href="{OFFER_DATA[k]["file"]}"><div class="art">{V.mini(OFFER_DATA[k]["mini"])}</div><div class="tb"><span class="k">{OFFER_DATA[k]["short"]}</span><h3>{OFFER_DATA[k]["name"]}</h3><p>{o_desc(OFFER_DATA[k])}</p><span class="more">Explore {ARROW}</span></div></a>'
        for k in ORDER) + '</div>'


# =========================================================== HOME
def build_home():
    orbit = f'''<div class="orbit"><svg viewBox="0 0 580 580" aria-hidden="true"><defs><linearGradient id="go" x1="0" x2="1"><stop offset="0" stop-color="#ff6b78"/><stop offset="1" stop-color="#6aa3ff"/></linearGradient></defs>
<circle cx="290" cy="290" r="225" fill="none" stroke="rgba(255,255,255,.16)" stroke-dasharray="3 8"/><circle cx="290" cy="290" r="150" fill="none" stroke="rgba(255,255,255,.16)" stroke-dasharray="3 8"/>
<path d="M290 145V70M435 290h75M290 435v75M145 290H70" stroke="url(#go)" stroke-width="2" class="sv-flow"/>
<g class="spin"><circle cx="290" cy="65" r="5" fill="#ff6b78"/><circle cx="515" cy="290" r="3.5" fill="#9fc0ff"/></g>
<g class="spin rev"><circle cx="290" cy="140" r="4" fill="#9fc0ff"/><circle cx="140" cy="290" r="4" fill="#ff6b78"/><circle cx="290" cy="440" r="3.5" fill="#fff"/></g></svg>
<div class="ocore"><img src="assets/img/mark.png" alt=""></div>
<a class="onode" style="left:50%;top:6%" href="ai.html"><i></i>AI / SI<small>Intelligence</small></a>
<a class="onode" style="left:93%;top:50%" href="erp.html"><i></i>ERP<small>Operations</small></a>
<a class="onode" style="left:50%;top:94%" href="itsm.html"><i></i>ITSM<small>Service</small></a>
<a class="onode" style="left:7%;top:50%" href="cx.html"><i></i>CX<small>Experience</small></a></div>'''
    b = f'''<section class="hero home-hero"><div class="wrap hero-grid"><div>
<div class="crumbs rv">Dallas · Enterprise technology consulting</div>
<h1 data-split>Move <span class="r">ahead of now.</span> Build the enterprise that is ready for what is next.</h1>
<p class="lead rv" data-delay=".4">Arron helps organizations modernize the systems they run on and adopt AI where it counts, across ERP, IT service management and customer experience.</p>
<div class="hero-cta rv" data-delay=".55"><a class="btn btn-red" href="about.html#contact">Start a conversation {ARROW}</a><a class="btn btn-ghost" href="offerings.html">Explore offerings</a></div>
<div class="hero-stats rv" data-delay=".7"><div><b>4</b><span>Core practices</span></div><div><b>18+ yrs</b><span>Leadership experience</span></div><div><b>Certified</b><span>Platform expertise</span></div></div>
</div><div class="rv" data-delay=".25">{orbit}</div></div></section>'''
    b += marquee()
    b += f'''<section id="who"><div class="wrap split2"><div><span class="kicker rv">Who we are</span><h2 data-split>A consultancy built to get enterprises ahead, not just current.</h2>
<p class="lead rv" data-delay=".2">Arron is a Dallas-based technology consulting firm. Our leaders spent decades inside large systems integrators and enterprise software programs. We started Arron to bring that depth to organizations in a more direct, accountable way.</p>
<div class="pill-row rv" data-delay=".3"><span class="pill">Senior-led delivery</span><span class="pill">Technology independent</span><span class="pill">Strategy to run</span></div>
<a class="more rv" style="margin-top:34px" href="about.html">More about Arron {ARROW}</a></div>
<div class="stage rv rv-r" style="background:linear-gradient(145deg,var(--navy-800),var(--navy-950))">{V.v_model()}</div></div></section>'''
    b += f'<section class="paper" id="offer"><div class="wrap">{sh("What we offer", "Four practices. One connected enterprise.", "Each practice stands on its own. Together they close the gaps between your systems, your service teams and your customers.")}{tiles4()}</div></section>'
    why = [("Senior-led delivery", "The people who scope the work are the people who do it."), ("Independent advice", "We recommend what fits your business, not what carries the biggest margin."),
           ("AI with a purpose", "We apply AI where it moves a number, and say so when it will not."), ("Certified depth", "SAP, Azure, ITIL and ServiceNow credentials earned on real programs."),
           ("Outcome-based thinking", "Every engagement starts with the result you need and works back."), ("Built to hand over", "We train your team and document the work so you are never dependent on us.")]
    b += '<section class="navy" id="why"><div class="wrap">' + sh("Why Arron", "Experience you can feel from the first meeting.", "What you get when senior practitioners run the work.") + \
         '<div class="why6" data-stagger>' + ''.join(f'<div><span class="n">{i+1:02d}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(why)) + '</div></div></section>'
    b += '<section id="exp"><div class="wrap">' + sh("Experience", "Proven across industries, platforms and program sizes.", "Decades of delivery across global manufacturers, financial institutions and public bodies.") + \
         '''<div class="stats rv"><div class="stat"><b data-count="18" data-suffix="+">0</b><span>Years of senior leadership experience</span></div><div class="stat"><b data-count="4">0</b><span>Integrated practice areas</span></div><div class="stat"><b data-count="8" data-suffix="+">0</b><span>Industries served</span></div><div class="stat"><b data-count="30" data-suffix="+">0</b><span>Enterprise certifications held</span></div></div>''' + \
         '<div style="margin-top:56px">' + rows([("Large-scale transformation", "Multi-country ERP and cloud programs for global manufacturers and retailers."), ("Regulated environments", "Audit-ready change and service processes for financial services and healthcare."), ("Measurable results", "Programs measured against cost, speed and satisfaction targets set up front.")], "c3") + '</div>' + \
         f'<a class="more" style="margin-top:40px" href="industry.html">See our industry expertise {ARROW}</a></div></section>'
    nxt = [("STEP 01", "Book a discovery call", "Thirty minutes with a senior consultant to frame your challenge. No pitch deck.", "about.html#contact", "Schedule"),
           ("STEP 02", "See how we work", "Understand our consulting, services and partnership models and which fits you.", "capabilities.html", "Capabilities"),
           ("STEP 03", "Read our latest thinking", "Guides, briefings and webinars on AI, ERP, ITSM and customer experience.", "resources.html", "Resources")]
    b += '<section class="paper"><div class="wrap">' + sh("What should you do next", "Pick the starting point that fits you.", "No forms to fill and no sales script. Just a useful conversation.") + \
         '<div class="nexts" data-stagger>' + ''.join(f'<a class="nx" href="{h}"><span class="n">{n}</span><b>{t}</b><p>{p}</p><span class="more">{l} {ARROW}</span></a>' for n, t, p, h, l in nxt) + '</div></div></section>'
    b += cta_band("Ready to get ahead of now?", "Tell us where you are headed. We will tell you honestly how to get there.")
    page("index.html", "Arron — Ahead of now | AI, ERP, ITSM & CX Consulting", "Arron is a Dallas-based technology consultancy helping enterprises modernize with AI, ERP, ITSM and customer experience.", "index.html", b)


# =========================================================== OFFERINGS OVERVIEW
def build_offerings():
    b = hero('<a href="index.html">Home</a> / Offerings', 'Four practices that power <span class="r">the modern enterprise.</span>',
             "Intelligence, operations, service and experience. Start with one, or run them as a single connected program.", V.v_stack())
    b += marquee()
    b += f'<section id="more"><div class="wrap">{sh("Our practices", "Choose your starting point.", "Each practice has its own team, playbook and platform expertise.")}{tiles4()}</div></section>'
    qs = [("ai.html", "Not sure where AI will pay off?", "Artificial & Super Intelligence", "01"), ("erp.html", "Outgrown your ERP, or choosing a new one?", "Enterprise Resource Planning", "02"),
          ("itsm.html", "Drowning in tickets and missed SLAs?", "IT Service Management", "03"), ("cx.html", "Customers leaving between touchpoints?", "Customer Experience", "04")]
    b += '<section class="navy"><div class="wrap">' + sh("Start where it hurts", "Tell us the problem. We will point to the practice.", "A shortcut if you know the pain but not the label.") + \
         '<div style="border-top:1px solid rgba(255,255,255,.14)" data-stagger>' + ''.join(
             f'<a href="{h}" class="qrow"><span class="n">{n}</span><b>{q}</b><span class="a">{a}</span><span class="go">{ARROW}</span></a>' for h, q, a, n in qs) + '</div></div></section>'
    b += cta_band("Not sure where to start?", "Tell us the outcome you want and we will recommend the lightest path to it.")
    page("offerings.html", "Offerings — Arron | AI, ERP, ITSM & CX", "Arron offerings: Artificial & Super Intelligence, ERP, IT Service Management and Customer Experience.", "offerings.html", b)


# =========================================================== CAPABILITIES
def build_cap():
    b = hero('<a href="index.html">Home</a> / Capabilities', 'However you need us, <span class="r">we plug in.</span>',
             "Advise, deliver, partner or build. Four ways to work with Arron, designed around how much of the journey you want us to own.", V.v_ladder())
    b += marquee()
    b += '<section id="more"><div class="wrap">' + sh("Engagement spectrum", "From advice to full ownership.", "Pick the lightest model that gets the job done. You can move along the spectrum as needs change.") + \
         '''<div class="spec rv"><div><span class="lv">You lead</span><h3>Advise</h3><p>Independent guidance and expert oversight while your team drives delivery.</p></div><div><span class="lv">We co-deliver</span><h3>Deliver together</h3><p>Blended teams run programs end to end, with knowledge transfer built in.</p></div><div><span class="lv">We own it</span><h3>Operate & build</h3><p>Managed services and AI-native products delivered against agreed outcomes.</p></div></div></div></section>'''
    caps = [("Consulting", "Strategy you can execute.", "Technology and operating-model advice tied to financial outcomes. We clarify the decision, build the case and map the path.", ["Digital & AI strategy", "Vendor selection", "Process redesign", "Change management"], V.v_consult(), False),
            ("Services", "Delivery and run, handled.", "Implementation, integration and managed support from certified teams, so your platforms stay stable, secure and improving.", ["Implementation", "Integration", "Managed support", "Optimization"], V.v_services(), True),
            ("Partnerships", "An ecosystem on your side.", "We work alongside the leading enterprise platform vendors and specialist firms, and bring the right ones into each engagement.", ["Platform alliances", "Certified experts", "Joint solutions", "Co-selling"], V.v_partners(), False),
            ("Product as a Service", "AI-native development, delivered as a product.", "We design, build and run software with AI at its core, then operate it as a subscription-style service with continuous releases.", ["Product discovery", "AI-native engineering", "Hosted & operated", "Continuous releases"], V.v_product(), True)]
    for i, (k, h, p, pills, vis, flip) in enumerate(caps):
        bg = ' class="paper"' if i % 2 == 0 else ''
        b += f'''<section{bg}><div class="wrap split2{" flip" if flip else ""}"><div><span class="kicker rv">{k}</span><h2 data-split>{h}</h2><p class="lead rv" data-delay=".2">{p}</p>
<div class="pill-row rv" data-delay=".3">{''.join(f'<span class="pill">{x}</span>' for x in pills)}</div></div><div class="stage rv">{vis}</div></div></section>'''
    b += '<section class="navy"><div class="wrap">' + sh("How an engagement runs", "Clear stages. No surprises.", "Whatever the model, the rhythm is the same.") + \
         '<div class="proc" data-stagger>' + ''.join(f'<div class="pstep"><span class="n">{i+1}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate([("Discover", "Listen, assess and define the outcome and success measures."), ("Design", "Agree architecture, plan and business case."), ("Deliver", "Build in short cycles with visible progress every sprint."), ("Sustain", "Hand over, train and keep improving.")])) + '</div></div></section>'
    b += cta_band("Find the model that fits.", "We will recommend the lightest engagement that gets the job done.")
    page("capabilities.html", "Capabilities — Arron | Consulting, Services, Partnerships, Product as a Service", "How Arron works with you: consulting, managed services, technology partnerships and AI-native product development.", "capabilities.html", b)


# =========================================================== INDUSTRY
def build_industry():
    b = hero('<a href="index.html">Home</a> / Industry Expertise', 'Deep experience. <span class="r">Real people.</span>',
             "The industries we serve, the work we have delivered and the consultants behind it.", V.v_industries())
    b += marquee("Technology partners across our client work")
    inds = [("bank", "Banking & Financial", "Audit-ready change trails and compliance monitoring."), ("factory", "Manufacturing", "ERP, supply chain and shop-floor integration."),
            ("heart", "Healthcare & Pharma", "SLA-driven support for critical systems."), ("cart", "Retail & Consumer", "Surge detection and omnichannel experience."),
            ("signal", "Telecom & Media", "Network incident prediction and smart routing."), ("code", "Technology & SaaS", "Incident correlation across DevOps pipelines."),
            ("bolt", "Energy & Utilities", "Asset-heavy operations and field service."), ("gov", "Public Sector", "Modernization for state, local and nonprofit.")]
    b += '<section id="clients"><div class="wrap">' + sh("Clients", "Industries where we have done the work.", "Sector knowledge matters. These are the environments our team knows well.") + \
         '<div class="inds" data-stagger>' + ''.join(f'<div class="ind">{icon(i)}<h3>{t}</h3><p>{p}</p></div>' for i, t, p in inds) + '</div></div></section>'
    cases = [("rings", "ERP · Manufacturing", "One ERP across four plants", "Replaced fragmented legacy systems with a single cloud ERP and unified reporting.", ("-32%", "Close cycle time"), ("4 → 1", "Systems consolidated")),
             ("waves", "ITSM · Financial", "AI-assisted service desk", "Migrated to a modern ITSM platform with auto-triage and a self-service portal.", ("-40%", "Ticket handling time"), ("+25%", "Self-service rate")),
             ("bars", "CX · Retail", "A unified customer view", "Connected CRM, contact center and data to personalize every touchpoint.", ("+18 pt", "NPS improvement"), ("-22%", "Repeat contacts"))]
    b += '<section class="paper"><div class="wrap">' + sh("Case studies", "Representative engagements.", "Examples of the outcomes we design for. Client names withheld.") + \
         '<div class="cases" data-stagger>' + ''.join(f'<div class="case"><div class="art">{V.art(a)}<em>{tg}</em></div><div class="cb"><h3>{t}</h3><p>{p}</p><div class="res"><div><b>{r1[0]}</b><span>{r1[1]}</span></div><div><b>{r2[0]}</b><span>{r2[1]}</span></div></div></div></div>' for a, tg, t, p, r1, r2 in cases) + '</div></div></section>'
    b += '<section><div class="wrap">' + sh("Testimonials", "What clients tell us.", "In their words.") + \
         '''<div class="quotes" data-stagger><div class="quote"><p>They narrowed a crowded vendor field to the one that actually fit us, and the project landed on time. It felt like having an owner on our side of the table.</p><div class="who"><b>VP of Information Technology</b><span>Manufacturing client</span></div></div>
<div class="quote"><p>The team brought real depth in service management and genuinely trained our people. We run the platform ourselves now, with confidence.</p><div class="who"><b>Director of IT Operations</b><span>Financial services client</span></div></div></div></div></section>'''
    people = [("Daniel Reyes", "Principal Architect, SAP & Cloud", "18+ years", "Certified SAP Enterprise and BTP architect bridging business strategy and enterprise platforms, from S/4HANA to AI-enabled solutions.", ["SAP BTP", "S/4HANA", "Business AI"], "Kentucky, USA"),
              ("Priya Nair", "Director, ERP & Enterprise Applications", "15+ years", "Leads ERP selection and implementation across finance and supply chain, focused on adoption and measurable business results.", ["ERP", "Program delivery", "Change"], "Texas, USA"),
              ("Marcus Hale", "Director, Digital & Customer Experience", "12+ years", "Designs customer journeys and the platforms behind them, connecting data, CRM and service channels into one experience.", ["CX", "CRM", "Analytics"], "Texas, USA"),
              ("Elena Brooks", "Managing Partner, ITSM & AI Transformation", "20+ years", "Entrepreneurial executive in IT service management and cloud transformation. ITIL Expert and Azure certified.", ["ServiceNow", "Azure", "ITIL"], "Dallas–Fort Worth, TX")]
    b += '<section class="navy" id="consultants"><div class="wrap">' + sh("Consultants", "The people you will work with.", "Practitioners with decades of enterprise delivery behind them.") + \
         '<div class="people" data-stagger>' + ''.join(f'<article class="person"><div class="ph"><span class="yrs">{y}</span><a class="in" href="#" aria-label="LinkedIn">{LI}</a>{V.AVATAR}</div><div class="pi"><h3>{n}</h3><div class="role">{r}</div><p>{bio}</p><div class="chips">{"".join(f"<span>{c}</span>" for c in ch)}</div><div class="loc">{loc}</div></div></article>' for n, r, y, bio, ch, loc in people) + '</div>' + \
         f'<div style="margin-top:56px;display:flex;gap:14px;flex-wrap:wrap"><a class="btn btn-red" href="resources.html#careers">Join us {ARROW}</a><a class="btn btn-ghost" href="about.html#contact">Meet the team</a></div></div></section>'
    pl = [("ServiceNow", "ITSM · Workflow"), ("SAP", "ERP · BTP"), ("Microsoft", "Azure · Dynamics"), ("Oracle", "ERP · Cloud"), ("Atlassian", "Jira Service Mgmt"), ("Salesforce", "CRM · CX"), ("AWS", "Cloud · AI"), ("Google Cloud", "Data · AI")]
    b += '<section><div class="wrap">' + sh("Our partners", "Strong platforms. Stronger together.", "Certified expertise across the ecosystems our clients already run on.") + \
         '<div class="plogos" data-stagger>' + ''.join(f'<div class="plogo">{n}<small>{s}</small></div>' for n, s in pl) + '</div></div></section>'
    page("industry.html", "Industry Expertise — Arron | Clients, Case Studies & Consultants", "Arron's client work, industry experience and the consultants who deliver it.", "industry.html", b)


# =========================================================== RESOURCES
def build_resources():
    b = hero('<a href="index.html">Home</a> / Resources', 'Ideas worth <span class="r">acting on.</span>',
             "Practical thinking on AI, ERP, ITSM and customer experience, plus the events and roles that keep our community growing.", V.v_resources())
    posts = [("rings", "AI", "Is your enterprise actually ready for AI?", "A practical checklist covering data, governance, skills and use-case selection."), ("waves", "ERP", "Five reasons ERP projects go over budget", "And the early warning signs most steering committees miss."),
             ("bars", "ITSM", "AI triage without losing the human touch", "Where automation helps your service desk and where it should step aside."), ("dots", "CX", "Connecting customer data across channels", "A simple model for one customer view without a rip-and-replace.")]
    b += '<section id="blog"><div class="wrap">' + sh("Blogs & newsletter", "Latest thinking.", "Short, useful reads from the people doing the work.") + '<div class="posts" data-stagger>'
    b += f'<a class="post feat" href="#"><div class="art">{V.art(posts[0][0])}</div><div class="pb"><span class="m">AI · Featured</span><h3>{posts[0][2]}</h3><p>{posts[0][3]} Read it before you invest in a single model.</p><span class="more">Read article {ARROW}</span></div></a>'
    for a, m, t, p in posts[1:]:
        b += f'<a class="post" href="#"><div class="art">{V.art(a)}</div><div class="pb"><span class="m">{m}</span><h3>{t}</h3><p>{p}</p><span class="more">Read article {ARROW}</span></div></a>'
    b += '</div></div></section>'
    b += f'''<section class="navy" style="padding:90px 0"><div class="wrap split2"><div><span class="kicker rv">Newsletter</span><h2 data-split>One useful email, once a month.</h2></div>
<div class="rv" data-delay=".2"><p style="font-size:1.1rem;margin-bottom:26px;max-width:44ch">Short briefings on what is changing in enterprise technology, and what to do about it.</p><form data-demo onsubmit="return false"><div class="news"><input type="email" required placeholder="you@company.com" aria-label="Email"><button class="btn btn-red" type="submit">Subscribe</button></div></form><div class="ok" style="margin-top:16px">Thanks, you are on the list.</div></div></div></section>'''
    ev = [("12", "Feb", "AI readiness for the enterprise", "Live webinar · 45 minutes with Q&A", "Webinar"), ("05", "Mar", "ERP selection roundtable", "Dallas, TX · In person, invite only", "Event"), ("20", "Mar", "ITSM in the age of AI agents", "Live webinar · Hands-on demo", "Webinar")]
    b += '<section id="events"><div class="wrap">' + sh("Events & webinars", "Learn with us, live.", "Upcoming sessions. Register to get the recording if you cannot attend.") + \
         '<div class="events" data-stagger>' + ''.join(f'<div class="event"><div class="d"><b>{d}</b><span>{m}</span></div><div><h3>{t}</h3><p>{p}</p></div><span class="kind">{k}</span></div>' for d, m, t, p, k in ev) + '</div></div></section>'
    jobs = [("Senior ERP Consultant", "Dallas, TX · Hybrid"), ("ServiceNow Architect", "Remote · USA"), ("AI Solutions Engineer", "Dallas, TX · Hybrid"), ("CX Strategy Consultant", "Dallas, TX · Hybrid")]
    b += '<section class="navy" id="careers"><div class="wrap">' + sh("Careers", "Do the best work of your career.", "Join a team where senior practitioners shape the work, learn from each other and stay close to clients.") + \
         '<div class="jobs" data-stagger>' + ''.join(f'<div class="job"><div><b>{t}</b><span>{l}</span></div><a class="more" href="about.html#contact">Apply {ARROW}</a></div>' for t, l in jobs) + '</div></div></section>'
    page("resources.html", "Resources — Arron | Insights, Events & Careers", "Arron insights, newsletter, webinars and career opportunities.", "resources.html", b)


# =========================================================== ABOUT
def build_about():
    b = hero('<a href="index.html">Home</a> / About Us', 'A Dallas company with <span class="r">a national network.</span>',
             "Arron exists to help organizations stay ahead of change with senior expertise, honest advice and work that lasts.", V.v_map())
    b += f'''<section id="more"><div class="wrap split2"><div><span class="kicker rv">Our story</span><h2 data-split>Why “Ahead of now.”</h2>
<p class="lead rv" data-delay=".2">Technology moves faster than most organizations can absorb. Arron was founded on a simple idea: your business should not be catching up to its own systems.</p>
<p class="rv" data-delay=".3" style="margin-top:18px">Headquartered in Dallas, Texas, we are a team of experienced practitioners with a wide network of specialist partners across the country, so we can staff the right people for each engagement.</p></div>
<div class="stats rv" style="grid-template-columns:1fr 1fr"><div class="stat"><b data-count="18" data-suffix="+">0</b><span>Years of leadership experience</span></div><div class="stat"><b data-count="4">0</b><span>Practice areas</span></div><div class="stat" style="border-top:1px solid var(--line);padding-left:0;border-left:0"><b data-count="12" data-suffix="+">0</b><span>Platform partners</span></div><div class="stat" style="border-top:1px solid var(--line)"><b data-count="1">0</b><span>Home base: Dallas</span></div></div></div></section>'''
    vals = [("Integrity", "We say what we think, even when it is not the easy answer."), ("Craft", "We care about the detail, and about work that stands up in production."), ("Partnership", "Your goals are ours. We succeed only when you do."), ("Foresight", "We look past the trend to what will matter in three years.")]
    b += '<section class="navy"><div class="wrap">' + sh("What we stand for", "Our values.", "How we behave when nobody is checking.") + '<div class="values" data-stagger>' + ''.join(f'<div class="val"><span class="n">{i+1:02d}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(vals)) + '</div></div></section>'
    tl = [("FOUNDATION", "Arron is established in Dallas", "A small senior team with one goal: deliver enterprise outcomes without the overhead."), ("EXPANSION", "Four connected practices", "AI, ERP, ITSM and CX come together under one delivery model."),
          ("NETWORK", "Partners and talent nationwide", "An ecosystem of platform vendors and specialists joins the Arron bench."), ("NEXT", "AI-native products", "Product-as-a-service offerings built for the way enterprises will work.")]
    b += '<section><div class="wrap">' + sh("Journey", "Where we are heading.", "A young firm with long experience behind it.") + '<div class="tl" data-stagger>' + ''.join(f'<div class="tli"><b>{k}</b><h3>{t}</h3><p>{p}</p></div>' for k, t, p in tl) + '</div></div></section>'
    b += f'''<section class="paper" id="contact"><div class="wrap cgrid"><div><span class="kicker rv">Contact us</span><h2 data-split>Let's talk about what is next.</h2>
<p class="rv" data-delay=".2" style="margin-top:22px;font-size:1.1rem">Tell us a little about your challenge. A senior member of the team will reply within one business day.</p>
<div class="cinfo rv" data-delay=".3"><div><b>Headquarters</b><span>Dallas, Texas, USA</span></div><div><b>Email</b><span>hello@arron.com</span></div><div><b>Hours</b><span>Mon–Fri, 8am–6pm Central</span></div></div></div>
<div class="rv rv-r"><form class="f" data-demo onsubmit="return false"><div class="two"><label>Name<input required placeholder="Jane Smith"></label><label>Work email<input type="email" required placeholder="jane@company.com"></label></div>
<div class="two"><label>Company<input placeholder="Company name"></label><label>Interested in<select><option>AI / Super Intelligence</option><option>ERP</option><option>ITSM</option><option>Customer Experience</option><option>Careers</option><option>Something else</option></select></label></div>
<label>How can we help?<textarea placeholder="A few lines about your goals or challenge"></textarea></label>
<button class="btn btn-red" type="submit" style="justify-content:center">Send message {ARROW}</button><div class="ok">Thank you. We will be in touch within one business day.</div></form></div></div></section>'''
    page("about.html", "About Us — Arron | Dallas Technology Consulting", "About Arron, a Dallas-based technology consulting company, and how to contact us.", "about.html", b)


if __name__ == "__main__":
    build_home(); build_offerings(); build_cap(); build_industry(); build_resources(); build_about()
    for k in ORDER:
        build_offer(k)
    print("built")
