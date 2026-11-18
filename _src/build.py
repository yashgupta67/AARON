#!/usr/bin/env python3
"""Generates the Arron static site into the parent folder. Run: python3 _src/build.py"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import visuals as V

VER = str(int(__import__('time').time()))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHEV = '<svg width="10" height="7" viewBox="0 0 12 8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M1 1.5l5 5 5-5"/></svg>'
LI = '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.1c.6-1 1.9-2 3.9-2 4 0 4.7 2.6 4.7 6V21h-4v-5c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7V21h-4z"/></svg>'

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
    "map": '<path d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2z"/><path d="M9 4v14M15 6v14"/>',
    "doc": '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
    "chart": '<path d="M4 20V4M4 20h16M8 16v-5M13 16V8M18 16v-8"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.6 2.7-6 6-6s6 2.4 6 6M16 5.2a3.2 3.2 0 0 1 0 5.6M18 14.4c2 .8 3 2.6 3 5.6"/>',
    "shield": '<path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/>',
    "cog": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
}


def icon(k):
    return f'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[k]}</svg>'


def photo(name, alt=""):
    return f'<img src="assets/img/photos/{name}.jpg" alt="{alt}" loading="lazy">'


def part(name, cls="art ph", extra=""):
    return f'<div class="{cls}">{photo(name)}{extra}</div>'


PLATFORMS = ["ServiceNow", "SAP", "Oracle", "Microsoft Azure", "Atlassian", "Salesforce", "AWS", "Google Cloud", "Workday", "NetSuite", "Dynamics 365", "Pega"]

# ------------------------------------------------------------------ NAV
MENUS = {
    "offerings.html": dict(groups=[(None, [
        ("ai.html", "AI / Super Intelligence", "Strategy, data foundations and agentic AI"),
        ("erp.html", "ERP", "Selection, implementation and optimization"),
        ("itsm.html", "ITSM", "Faster, smarter IT service operations"),
        ("cx.html", "Customer Experience", "Journeys, platforms and insight")])],
        foot=("offerings.html", "View all offerings"), wide=False),
    "capabilities.html": dict(groups=[(None, [
        ("consulting.html", "Consulting", "Strategy and advice you can execute"),
        ("services.html", "Services", "Implementation, integration and managed support"),
        ("partnerships.html", "Partnerships", "A certified ecosystem on your side"),
        ("product.html", "Product as a Service", "AI-native development, delivered as a product")])],
        foot=("capabilities.html", "How we work with you"), wide=False),
    "industry.html": dict(groups=[
        ("Clients", [("case-studies.html", "Case Studies", "Representative engagements and outcomes"), ("testimonials.html", "Testimonials", "What clients say about working with us")]),
        ("Consultants", [("consultants.html", "Our Consultants & Partners", "Profiles of our team and partner network"), ("careers.html", "Join Us", "Open roles and how we hire")])],
        foot=("industry.html", "Industries we serve"), wide=True),
    "resources.html": dict(groups=[(None, [
        ("blog.html", "Blogs & Newsletter", "Insights on AI, ERP, ITSM and CX"),
        ("events.html", "Events & Webinars", "Live sessions and on-demand recordings"),
        ("careers.html", "Careers", "Build your career with Arron")])],
        foot=("resources.html", "All resources"), wide=False),
}
NAV = [("index.html", "Home"), ("offerings.html", "Offerings"), ("capabilities.html", "Capabilities"),
       ("industry.html", "Industry Expertise"), ("resources.html", "Resources"), ("about.html", "About Us")]
SECTION = {}
for sec, m in MENUS.items():
    SECTION[sec] = sec
    for g, items in m["groups"]:
        for h, *_ in items:
            SECTION.setdefault(h, sec)
for _a in ["ai-readiness","erp-over-budget","ai-triage-human-touch","connecting-customer-data","erp-demo-truth","itsm-migration","pilot-to-production","cx-beyond-nps"]:
    SECTION[_a + ".html"] = "resources.html"
SECTION["careers.html"] = "resources.html"  # careers lives under Resources; also reachable from Industry > Consultants > Join Us


def header(fname):
    active = SECTION.get(fname, fname)
    items = ''
    for href, label in NAV:
        if href in MENUS:
            m = MENUS[href]
            body = ''
            for g, its in m["groups"]:
                col = ''
                if g:
                    col += f'<h5>{g}</h5>'
                col += ''.join(f'<a href="{h}"><b>{t}</b><span>{d}</span></a>' for h, t, d in its)
                body += f'<div class="mcol">{col}</div>'
            foot = f'<a class="foot" href="{m["foot"][0]}">{m["foot"][1]} →</a>'
            cls = "menu wide" if m["wide"] else "menu"
            on = "active" if active == href else ""
            items += f'<div class="dd"><a class="{on}" href="{href}">{label}{CHEV}</a><div class="{cls}">{body}{foot}</div></div>'
        else:
            on = ' class="active"' if href == active else ''
            items += f'<a href="{href}"{on}>{label}</a>'
    return f'''<header class="site-header"><div class="wrap bar">
<a class="logo" href="index.html" aria-label="Arron home"><img src="assets/img/logo.png" alt="Arron — Ahead of now"></a>
<button class="burger" aria-label="Menu"><span></span><span></span></button>
<nav class="nav">{items}<a class="btn btn-red" href="about.html#contact">Talk to us {ARROW}</a></nav></div></header>'''


def footer():
    def col(title, links):
        return f'<div><h4>{title}</h4><ul>' + ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in links) + '</ul></div>'
    return f'''<footer class="site-footer"><div class="wrap"><div class="ft" style="grid-template-columns:1.5fr repeat(4,1fr)">
<div><img src="assets/img/logo-light.png" alt="Arron"><p style="max-width:34ch">Enterprise technology consulting for AI, ERP, ITSM and customer experience. Based in Dallas, Texas.</p></div>
{col("Offerings", [("ai.html", "AI / Super Intelligence"), ("erp.html", "ERP"), ("itsm.html", "ITSM"), ("cx.html", "Customer Experience")])}
{col("Capabilities", [("consulting.html", "Consulting"), ("services.html", "Services"), ("partnerships.html", "Partnerships"), ("product.html", "Product as a Service")])}
{col("Explore", [("case-studies.html", "Case Studies"), ("testimonials.html", "Testimonials"), ("consultants.html", "Consultants"), ("blog.html", "Blog"), ("events.html", "Events"), ("careers.html", "Careers")])}
{col("Company", [("about.html", "About Us"), ("about.html#contact", "Contact"), ("mailto:hello@arron.com", "hello@arron.com")])}</div>
<div class="fb"><span>© 2026 Arron. All rights reserved.</span><span>Dallas, Texas · Privacy · Terms</span></div></div></footer>'''


def marquee(label="The platforms and ecosystems we work across", names=PLATFORMS):
    items = ''.join(f'<div class="it">{n}</div>' for n in names)
    return f'<div class="marq"><div class="lab">{label}</div><div class="roll"><div class="track">{items}{items}</div></div></div>'


def page(fname, title, desc, body):
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="icon" href="assets/img/mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css?v={VER}"></head>
<body>{header(fname)}
{body}
{footer()}
<script src="assets/main.js?v={VER}"></script></body></html>'''
    with open(os.path.join(ROOT, fname), "w") as f:
        f.write(html)


def hero(crumb, h1, lead, stage, stage_cls="", cta=True, cta_html=None):
    c = cta_html if cta_html else f'<div class="hero-cta rv" data-delay=".5"><a class="btn btn-red" href="about.html#contact">Talk to an expert {ARROW}</a><a class="btn btn-ghost" href="#more">Explore below</a></div>' if cta else ''
    return f'''<section class="hero"><div class="wrap hero-grid"><div>
<div class="crumbs rv">{crumb}</div><h1 data-split>{h1}</h1><p class="lead rv" data-delay=".35">{lead}</p>{c}</div>
<div class="stage {stage_cls} rv" data-delay=".25">{stage}</div></div></section>'''


def photo_stage(name, title, sub):
    return f'{photo(name)}<div class="cap"><b>{title}</b><span>{sub}</span></div>'


def sh(kicker, h2, p):
    return f'<div class="sh"><div><span class="kicker rv">{kicker}</span><h2 data-split>{h2}</h2></div><p class="rv" data-delay=".2">{p}</p></div>'


def rows(items, cls=''):
    return f'<div class="rows {cls}" data-stagger>' + ''.join(
        f'<div class="row"><span class="n">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(items)) + '</div>'


def proc(steps):
    return '<div class="proc" data-stagger>' + ''.join(f'<div class="pstep"><span class="n">{i+1}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(steps)) + '</div>'


def cta_band(h, p, label="Start a conversation", href="about.html#contact"):
    return f'<section style="padding:70px 0 110px"><div class="wrap"><div class="cta rv"><div><h2>{h}</h2><p>{p}</p><a class="btn btn-red" href="{href}">{label} {ARROW}</a></div></div></div></section>'


def tile(href, k, title, desc, art_html):
    return f'<a class="tile" href="{href}"><div class="art">{art_html}</div><div class="tb"><span class="k">{k}</span><h3>{title}</h3><p>{desc}</p><span class="more">Explore {ARROW}</span></div></a>'



def resources_stage(active=None):
    if active == "blog.html":
        items = [("#more", "article", "#2563d8", "Blog articles", "Latest thinking on AI, ERP, ITSM and CX", "8 articles"),
                 ("#newsletter", "mail", "#7a4bd8", "Monthly newsletter", "One useful email, once a month", "Free"),
                 ("events.html", "webinar", "#d4202f", "Events & Webinars", "Live sessions and on-demand recordings", "6 sessions"),
                 ("careers.html", "career", "#1a9a5b", "Careers", "Open roles and how we hire", "6 open roles")]
    else:
        items = [("blog.html", "article", "#2563d8", "Blogs & Newsletter", "Insights on AI, ERP, ITSM and CX, plus a monthly briefing", "8 articles"),
                 ("events.html", "webinar", "#d4202f", "Events & Webinars", "Live sessions, roundtables and on-demand recordings", "6 sessions"),
                 ("careers.html", "career", "#1a9a5b", "Careers", "Open roles and how we hire", "6 open roles")]
    out = ''
    for href, ic, c, t, d, n in items:
        out += f'''<a class="rlink" href="{href}"><span class="ri" style="background:{c}"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{V.ICON_PATHS[ic]}</svg></span>
<span class="rt"><b>{t}</b><span>{d}</span></span><span class="rn">{n}</span><span class="rg">{ARROW}</span></a>'''
    return f'<div class="rstack">{out}</div>'


# =========================================================== DETAIL PAGES (offerings + capabilities)
D = {}
D["ai"] = dict(
    file="ai.html", parent=("offerings.html", "Offerings"), name="Artificial & Super Intelligence", short="AI / SI", visual=V.v_ai, mini="ai",
    tile_desc="Strategy, data foundations and agentic solutions that move AI from pilot to production.",
    h1='Put intelligence to work <span class="r">across the enterprise.</span>',
    lead="From readiness to production-grade agents, we help you apply AI where it changes a number: cost, speed, revenue or risk. And we build toward systems that reason and act across the whole business, responsibly.",
    what_p="Four building blocks take you from a promising idea to AI that your people trust and use every day.",
    what=[("AI readiness & strategy", "Find the use cases worth pursuing, size the value and set a sequenced roadmap."),
          ("Data foundations", "Pipelines, quality and architecture that your models can rely on."),
          ("Agents & copilots", "Task-doing AI built into the ERP, service and customer workflows you already run."),
          ("Governance & trust", "Security, compliance and responsible-AI controls designed in from day one.")],
    steps=[("Assess", "Review readiness across data, platforms, skills and risk."), ("Prioritize", "Rank use cases by value and feasibility, then pick the first wins."),
           ("Build", "Prototype, test and take solutions into production."), ("Scale", "Monitor, govern and extend what works across the business.")],
    third=("Where it works", "Proven in the industries that run on it.", "The same disciplined approach, tuned to the realities of each sector.",
           [("server", "Enterprise IT", "AI triage, anomaly detection and self-service."), ("bank", "Banking & Financial", "Fraud signals and compliance monitoring."),
            ("factory", "Manufacturing", "Demand forecasting and predictive maintenance."), ("heart", "Healthcare", "Documentation and operational support."),
            ("cart", "Retail", "Personalization and demand sensing."), ("signal", "Telecom", "Network incident prediction and routing.")]),
    plat_label="AI platforms and tools we work with",
    platforms=["Azure OpenAI", "AWS Bedrock", "Google Vertex AI", "ServiceNow AI", "SAP Business AI", "Salesforce Einstein", "Atlassian Intelligence", "Databricks", "Snowflake"])
D["erp"] = dict(
    file="erp.html", parent=("offerings.html", "Offerings"), name="Enterprise Resource Planning", short="ERP", visual=V.v_erp, mini="erp",
    tile_desc="Selection, implementation and optimization of the platforms that run finance and operations.",
    h1='The right ERP, <span class="r">chosen and delivered right.</span>',
    lead="Vendor-independent advice and hands-on delivery, so the system that runs your finance and operations fits the way you work and actually gets adopted.",
    what_p="From the first requirements workshop to life after go-live, we cover the full ERP journey.",
    what=[("Selection", "Requirements, scripted demos and an unbiased comparison of vendors."),
          ("Implementation", "Program leadership and delivery from design through go-live."),
          ("Contract negotiation", "Transparent total cost of ownership and terms that protect you."),
          ("Cloud migration & optimization", "Move to the cloud and keep improving without disrupting operations.")],
    steps=[("Strategy", "Define goals, roadmap and the business case."), ("Select", "Shortlist, demo and negotiate with the right vendor."),
           ("Implement", "Design, configure, integrate, test and train."), ("Optimize", "Stabilize, measure and extend after go-live.")],
    third=("Where it works", "Proven in the industries that run on it.", "The same disciplined approach, tuned to the realities of each sector.",
           [("factory", "Manufacturing", "Planning, shop floor and quality in one system."), ("truck", "Distribution & Supply Chain", "Inventory, logistics and demand visibility."),
            ("gov", "Public Sector", "Modernization for state, local and nonprofit."), ("bank", "Financial Services", "Finance, controls and reporting at scale."),
            ("heart", "Healthcare", "Supply, finance and workforce management."), ("brief", "Professional Services", "Projects, billing and resource planning.")]),
    plat_label="ERP platforms we work with",
    platforms=["SAP S/4HANA", "Oracle Fusion", "Microsoft Dynamics 365", "NetSuite", "Workday", "Infor", "Epicor", "Acumatica", "IFS"])
D["itsm"] = dict(
    file="itsm.html", parent=("offerings.html", "Offerings"), name="IT Service Management", short="ITSM", visual=V.v_itsm, mini="itsm",
    tile_desc="Faster resolution and happier users through ITIL-aligned, AI-assisted service operations.",
    h1='Service operations that <span class="r">resolve faster and cost less.</span>',
    lead="We design and deploy ITIL-aligned service management on leading platforms, with AI handling triage, routing and prediction so your team spends time on what matters.",
    what_p="A service desk people want to use, backed by processes that scale as the business grows.",
    what=[("Process optimization", "Standardize and automate incident, change and request workflows."),
          ("Incident & problem management", "Faster resolution, plus root-cause work that cuts repeat tickets."),
          ("Change & release", "Structured approvals, risk scoring and rollback planning."),
          ("Asset management & portal", "A lifecycle-aware CMDB and a self-service portal that gets used.")],
    steps=[("Assess", "Measure maturity across tools, workflows and skills."), ("Roadmap", "Choose the platform, integrations, KPIs and timeline."),
           ("Implement", "Configure portal, SLAs and automation, and migrate from legacy tools."), ("Optimize", "Use analytics to predict breaches and extend to HR and Finance.")],
    third=("Where it works", "Proven in the industries that run on it.", "The same disciplined approach, tuned to the realities of each sector.",
           [("server", "Enterprise IT", "Centralized portals and SLA breach prediction."), ("bank", "BFSI", "Audit-ready change trails and compliance."),
            ("code", "SaaS", "Incident correlation across DevOps pipelines."), ("heart", "Healthcare & Pharma", "SLA-driven support for critical systems."),
            ("cart", "Retail", "Surge detection for peak-season traffic."), ("signal", "Telecom & Media", "Network incident prediction and routing.")]),
    plat_label="ITSM platforms and tools we work with",
    platforms=["ServiceNow", "Jira Service Management", "BMC Helix", "Freshservice", "Atlassian Assets", "Microsoft Teams", "Slack", "Zendesk", "PagerDuty"])
D["cx"] = dict(
    file="cx.html", parent=("offerings.html", "Offerings"), name="Customer Experience", short="CX", visual=V.v_cx, mini="cx",
    tile_desc="Journeys, platforms and insight that turn every interaction into loyalty and growth.",
    h1='Turn every interaction <span class="r">into loyalty.</span>',
    lead="We connect the data, platforms and people behind each touchpoint, so customers get one consistent experience wherever they meet you.",
    what_p="Better experiences come from fixing the moments that matter, and the systems underneath them.",
    what=[("Journey design", "Map the customer journey and fix the moments that matter most."),
          ("CX platforms", "CRM, contact center and digital engagement, implemented well."),
          ("Insight & personalization", "Unified data that drives the next best action."),
          ("Service excellence", "AI-assisted agents and self-service that resolve first time.")],
    steps=[("Listen", "Gather feedback, data and journey evidence."), ("Design", "Define target experience and the business case."),
           ("Build", "Implement platforms, integrations and automations."), ("Optimize", "Measure satisfaction and keep improving.")],
    third=("Where it works", "Proven in the industries that run on it.", "The same disciplined approach, tuned to the realities of each sector.",
           [("cart", "Retail & Consumer", "Omnichannel service and personalization."), ("bank", "Banking", "Seamless onboarding and support."),
            ("signal", "Telecom", "Proactive service and churn reduction."), ("heart", "Healthcare", "Patient access and engagement."),
            ("code", "Technology & SaaS", "Product-led onboarding and success."), ("plane", "Travel & Hospitality", "Loyalty and real-time service recovery.")]),
    plat_label="CX platforms and tools we work with",
    platforms=["Salesforce", "Microsoft Dynamics 365", "Adobe Experience Cloud", "Twilio", "Genesys", "Zendesk", "HubSpot", "Qualtrics", "Five9"])

D["consulting"] = dict(
    file="consulting.html", parent=("capabilities.html", "Capabilities"), name="Consulting", short="Consulting", visual=V.v_consult, photo="sticky-notes",
    tile_desc="Technology and operating-model advice tied to financial outcomes.",
    h1='Strategy you can <span class="r">actually execute.</span>',
    lead="Technology and operating-model advice tied to financial outcomes. We clarify the decision, build the case and map the path, then stay close while it gets done.",
    what_p="Independent advice across the decisions that shape how your enterprise runs.",
    what=[("Digital & AI strategy", "A prioritized roadmap linking technology bets to business results."),
          ("Vendor selection", "Unbiased evaluation and negotiation across platforms and partners."),
          ("Process & operating model", "Redesign how work flows across finance, supply chain and service."),
          ("Change & adoption", "People-first planning so new systems and ways of working stick.")],
    steps=[("Listen", "Interview stakeholders and review the current state."), ("Frame", "Define the problem, options and success measures."),
           ("Recommend", "Present a costed, sequenced plan with clear trade-offs."), ("Enable", "Support leaders through decisions and the first delivery wave.")],
    third=("What you get", "Deliverables you can act on Monday.", "Every consulting engagement ends with tangible work product, not slideware.",
           [("map", "Roadmap", "A sequenced plan with owners and milestones."), ("chart", "Business case", "Costs, benefits and risk in plain numbers."),
            ("doc", "Vendor scorecards", "Transparent comparison against your requirements."), ("cog", "Target operating model", "Roles, processes and governance defined."),
            ("users", "Change plan", "Communication, training and adoption tactics."), ("shield", "Risk register", "Known risks with mitigations and triggers.")]),
    plat_label="Frameworks and methods we use",
    platforms=["ITIL 4", "TOGAF", "Prince2", "Agile / SAFe", "COBIT", "Lean Six Sigma", "ADKAR", "Value stream mapping", "OKRs"])
D["services"] = dict(
    file="services.html", parent=("capabilities.html", "Capabilities"), name="Services", short="Services", visual=V.v_services, photo="dev-team",
    tile_desc="Implementation, integration and managed support from certified teams.",
    h1='Delivery and run, <span class="r">handled.</span>',
    lead="Implementation, integration and managed support from certified teams, so your platforms stay stable, secure and continuously improving.",
    what_p="Hands-on delivery from first configuration to steady-state operations.",
    what=[("Implementation", "Design, configure and launch your platforms on a proven delivery method."),
          ("Integration", "Connect ERP, service and customer systems through reliable interfaces."),
          ("Managed support", "Tiered support and monitoring against agreed service levels."),
          ("Optimization", "Regular releases, tuning and enhancements that keep value growing.")],
    steps=[("Mobilize", "Set up the team, governance and plan."), ("Build", "Configure, integrate and test in short cycles."),
           ("Transition", "Train users, cut over and stabilize."), ("Run", "Operate, support and improve against service levels.")],
    third=("What you get", "Service you can measure.", "Clear commitments, transparent reporting and a team that knows your landscape.",
           [("check", "Defined SLAs", "Response and resolution targets in writing."), ("chart", "Monthly reporting", "Performance, risks and improvement ideas."),
            ("users", "Named team", "Consistent people who know your business."), ("shield", "Security first", "Access, audit and data-protection controls."),
            ("cog", "Continuous improvement", "A standing backlog of enhancements."), ("doc", "Full documentation", "Runbooks and knowledge you own.")]),
    plat_label="Delivery tools and platforms",
    platforms=["Jira", "Azure DevOps", "ServiceNow", "GitHub", "Jenkins", "Terraform", "Datadog", "Splunk", "Confluence"])
D["partnerships"] = dict(
    file="partnerships.html", parent=("capabilities.html", "Capabilities"), name="Partnerships", short="Partnerships", visual=V.v_partners, photo="handshake",
    tile_desc="A certified ecosystem of platform vendors and specialist firms.",
    h1='An ecosystem <span class="r">on your side.</span>',
    lead="We work alongside leading enterprise platform vendors and specialist firms, and bring the right ones into each engagement so you get depth without the sprawl.",
    what_p="Partnerships are only useful when they make your project better. Ours are built around that.",
    what=[("Platform alliances", "Working relationships with the vendors behind your core systems."),
          ("Certified expertise", "Consultants certified on the platforms we recommend and deliver."),
          ("Joint solutions", "Pre-built accelerators and reference architectures with partners."),
          ("Co-innovation", "Pilots and early access to new platform capabilities.")],
    steps=[("Align", "Match your goals to the right partner capabilities."), ("Certify", "Ensure the team holds current platform credentials."),
           ("Co-build", "Deliver together under one accountable lead."), ("Grow", "Share learning and extend into new use cases.")],
    third=("What you get", "The benefit of a network, with one point of accountability.", "We stay your single lead, whichever partners join the work.",
           [("shield", "Vendor-neutral advice", "We recommend what fits, not what we resell."), ("users", "Right-sized teams", "Specialists on demand, not permanent overhead."),
            ("bolt", "Faster starts", "Accelerators and templates from partner ecosystems."), ("check", "Aligned delivery", "One plan, one governance, one lead."),
            ("chart", "Better commercial terms", "Partner programs that benefit you."), ("map", "Roadmap access", "Early insight into platform direction.")]),
    plat_label="Technology partner ecosystem",
    platforms=["ServiceNow", "SAP", "Microsoft", "Oracle", "Atlassian", "Salesforce", "AWS", "Google Cloud", "Workday"])
D["product"] = dict(
    file="product.html", parent=("capabilities.html", "Capabilities"), name="Product as a Service", short="Product as a Service", visual=V.v_product, photo="laptop-dark",
    tile_desc="AI-native software designed, built and run for you as a subscription-style service.",
    h1='AI-native development, <span class="r">delivered as a product.</span>',
    lead="We design, build and run software with AI at its core, then operate it as a subscription-style service with continuous releases, so you get outcomes without carrying the engineering burden.",
    what_p="From first idea to a live product, with the team that built it staying to run it.",
    what=[("Product discovery & design", "Validate the problem, the users and the value before building."),
          ("AI-native engineering", "Software designed around models and agents from the first line."),
          ("Hosted & operated", "We run the platform, security and uptime on your behalf."),
          ("Continuous releases", "Regular improvements shaped by real usage and your feedback.")],
    steps=[("Discover", "Define the problem, users and measurable outcome."), ("Prototype", "Build and test a working version with real users."),
           ("Launch", "Release, onboard and operate the live product."), ("Evolve", "Learn from usage and ship improvements continuously.")],
    third=("What you get", "A product, not a project.", "Subscription-style delivery that keeps improving after launch.",
           [("bolt", "Fast time to value", "Working software in weeks, not quarters."), ("cog", "No platform burden", "We handle hosting, scaling and security."),
            ("chart", "Usage-led roadmap", "Features driven by data, not guesswork."), ("shield", "Enterprise-grade controls", "Governance for AI and data from day one."),
            ("users", "Embedded team", "Product, design and engineering in one squad."), ("check", "Predictable cost", "A simple recurring fee against agreed outcomes.")]),
    plat_label="Technology we build with",
    platforms=["Python", "TypeScript", "Kubernetes", "Azure", "AWS", "PostgreSQL", "Snowflake", "OpenAI & Anthropic models", "Terraform"])
OFFER_KEYS = ["ai", "erp", "itsm", "cx"]
CAP_KEYS = ["consulting", "services", "partnerships", "product"]


def art_for(d):
    if "mini" in d:
        return V.mini(d["mini"])
    return f'{photo(d["photo"])}'


def tile_for(d, photo_art=False):
    art_html = f'{photo(d["photo"])}' if "photo" in d else V.mini(d["mini"])
    cls = " ph" if "photo" in d else ""
    return f'<a class="tile" href="{d["file"]}"><div class="art{cls}">{art_html}</div><div class="tb"><span class="k">{d["short"]}</span><h3>{d["name"]}</h3><p>{d["tile_desc"]}</p><span class="more">Explore {ARROW}</span></div></a>'


def build_detail(key):
    d = D[key]
    keys = OFFER_KEYS if key in OFFER_KEYS else CAP_KEYS
    others = [D[k] for k in keys if k != key]
    par = d["parent"]
    b = hero(f'<a href="index.html">Home</a> / <a href="{par[0]}">{par[1]}</a> / {d["short"]}', d["h1"], d["lead"], d["visual"]())
    b += marquee(d["plat_label"], d["platforms"] * 2)
    b += f'<section id="more"><div class="wrap">{sh("What we do", "Everything you need, from first idea to steady state.", d["what_p"])}{rows(d["what"], "c4w")}</div></section>'
    b += '<section class="navy"><div class="wrap">' + sh("How we deliver", "A clear path with no surprises.", "Four stages, each with a defined output, so you always know where the program stands.") + proc(d["steps"]) + '</div></section>'
    k, h2, p, items = d["third"]
    b += '<section><div class="wrap">' + sh(k, h2, p) + '<div class="inds c3" data-stagger>' + ''.join(f'<div class="ind">{icon(i)}<h3>{t}</h3><p>{x}</p></div>' for i, t, x in items) + '</div></div></section>'
    b += '<section class="paper"><div class="wrap">' + sh("Explore further", f'Other {par[1].lower()} to explore.', "Each one stands alone, and together they close the gaps between your systems, service and customers.") + \
         '<div class="tiles" style="grid-template-columns:repeat(3,1fr)" data-stagger>' + ''.join(tile_for(o) for o in others) + '</div></div></section>'
    b += cta_band(f"Ready to talk {d['short']}?", "Tell us the outcome you want. We will tell you honestly how to get there.")
    page(d["file"], f'{d["name"]} — Arron', d["lead"][:150], b)


def tiles_for(keys):
    return '<div class="tiles" data-stagger>' + ''.join(tile_for(D[k]) for k in keys) + '</div>'


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
<div class="collage rv rv-r"><div class="c1">{photo("team-room", "Consultants working with a client team")}</div><div class="c2">{photo("dashboard", "Analytics dashboard")}</div>
<div class="badge"><b>18+ years</b><span>of senior leadership across global enterprise programs</span></div></div></div></section>'''
    b += f'<section class="paper" id="offer"><div class="wrap">{sh("What we offer", "Four practices. One connected enterprise.", "Each practice stands on its own. Together they close the gaps between your systems, your service teams and your customers.")}{tiles_for(OFFER_KEYS)}</div></section>'
    why = [("Senior-led delivery", "The people who scope the work are the people who do it."), ("Independent advice", "We recommend what fits your business, not what carries the biggest margin."),
           ("AI with a purpose", "We apply AI where it moves a number, and say so when it will not."), ("Certified depth", "SAP, Azure, ITIL and ServiceNow credentials earned on real programs."),
           ("Outcome-based thinking", "Every engagement starts with the result you need and works back."), ("Built to hand over", "We train your team and document the work so you are never dependent on us.")]
    b += '<section class="navy" id="why"><div class="wrap">' + sh("Why Arron", "Experience you can feel from the first meeting.", "What you get when senior practitioners run the work.") + \
         '<div class="why6" data-stagger>' + ''.join(f'<div><span class="n">{i+1:02d}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(why)) + '</div></div></section>'
    b += '<section id="exp"><div class="wrap">' + sh("Experience", "Proven across industries, platforms and program sizes.", "Decades of delivery across global manufacturers, financial institutions and public bodies.") + \
         '''<div class="stats rv"><div class="stat"><b data-count="18" data-suffix="+">0</b><span>Years of senior leadership experience</span></div><div class="stat"><b data-count="4">0</b><span>Integrated practice areas</span></div><div class="stat"><b data-count="8" data-suffix="+">0</b><span>Industries served</span></div><div class="stat"><b data-count="30" data-suffix="+">0</b><span>Enterprise certifications held</span></div></div>''' + \
         '<div style="margin-top:56px">' + rows([("Large-scale transformation", "Multi-country ERP and cloud programs for global manufacturers and retailers."), ("Regulated environments", "Audit-ready change and service processes for financial services and healthcare."), ("Measurable results", "Programs measured against cost, speed and satisfaction targets set up front.")], "c3") + '</div>' + \
         f'<div style="display:flex;gap:26px;flex-wrap:wrap;margin-top:40px"><a class="more" href="case-studies.html">Read our case studies {ARROW}</a><a class="more" href="industry.html">Industries we serve {ARROW}</a></div></div></section>'
    nxt = [("STEP 01", "Book a discovery call", "Thirty minutes with a senior consultant to frame your challenge. No pitch deck.", "about.html#contact", "Schedule"),
           ("STEP 02", "See how we work", "Understand our consulting, services and partnership models and which fits you.", "capabilities.html", "Capabilities"),
           ("STEP 03", "Read our latest thinking", "Guides, briefings and webinars on AI, ERP, ITSM and customer experience.", "resources.html", "Resources")]
    b += '<section class="paper"><div class="wrap">' + sh("What should you do next", "Pick the starting point that fits you.", "No forms to fill and no sales script. Just a useful conversation.") + \
         '<div class="nexts" data-stagger>' + ''.join(f'<a class="nx" href="{h}"><span class="n">{n}</span><b>{t}</b><p>{p}</p><span class="more">{l} {ARROW}</span></a>' for n, t, p, h, l in nxt) + '</div></div></section>'
    b += cta_band("Ready to get ahead of now?", "Tell us where you are headed. We will tell you honestly how to get there.")
    page("index.html", "Arron — Ahead of now | AI, ERP, ITSM & CX Consulting", "Arron is a Dallas-based technology consultancy helping enterprises modernize with AI, ERP, ITSM and customer experience.", b)


# =========================================================== HUBS
def build_offerings():
    b = hero('<a href="index.html">Home</a> / Offerings', 'Four practices that power <span class="r">the modern enterprise.</span>',
             "Intelligence, operations, service and experience. Start with one, or run them as a single connected program.", V.v_stack())
    b += marquee()
    b += f'<section id="more"><div class="wrap">{sh("Our practices", "Choose your starting point.", "Each practice has its own team, playbook and platform expertise.")}{tiles_for(OFFER_KEYS)}</div></section>'
    qs = [("ai.html", "Not sure where AI will pay off?", "Artificial & Super Intelligence", "01"), ("erp.html", "Outgrown your ERP, or choosing a new one?", "Enterprise Resource Planning", "02"),
          ("itsm.html", "Drowning in tickets and missed SLAs?", "IT Service Management", "03"), ("cx.html", "Customers leaving between touchpoints?", "Customer Experience", "04")]
    b += '<section class="navy"><div class="wrap">' + sh("Start where it hurts", "Tell us the problem. We will point to the practice.", "A shortcut if you know the pain but not the label.") + \
         '<div style="border-top:1px solid rgba(255,255,255,.14)" data-stagger>' + ''.join(
             f'<a href="{h}" class="qrow"><span class="n">{n}</span><b>{q}</b><span class="a">{a}</span><span class="go">{ARROW}</span></a>' for h, q, a, n in qs) + '</div></div></section>'
    b += cta_band("Not sure where to start?", "Tell us the outcome you want and we will recommend the lightest path to it.")
    page("offerings.html", "Offerings — Arron | AI, ERP, ITSM & CX", "Arron offerings: Artificial & Super Intelligence, ERP, IT Service Management and Customer Experience.", b)


def build_cap():
    b = hero('<a href="index.html">Home</a> / Capabilities', 'However you need us, <span class="r">we plug in.</span>',
             "Advise, deliver, partner or build. Four ways to work with Arron, designed around how much of the journey you want us to own.", V.v_ladder())
    b += marquee()
    b += '<section id="more"><div class="wrap">' + sh("Engagement spectrum", "From advice to full ownership.", "Pick the lightest model that gets the job done. You can move along the spectrum as needs change.") + \
         '''<div class="spec rv"><div><span class="lv">You lead</span><h3>Advise</h3><p>Independent guidance and expert oversight while your team drives delivery.</p></div><div><span class="lv">We co-deliver</span><h3>Deliver together</h3><p>Blended teams run programs end to end, with knowledge transfer built in.</p></div><div><span class="lv">We own it</span><h3>Operate & build</h3><p>Managed services and AI-native products delivered against agreed outcomes.</p></div></div></div></section>'''
    b += f'<section class="paper"><div class="wrap">{sh("Our capabilities", "Four ways to work with us.", "Each capability has its own page with the detail.")}{tiles_for(CAP_KEYS)}</div></section>'
    b += '<section class="navy"><div class="wrap">' + sh("How an engagement runs", "Clear stages. No surprises.", "Whatever the model, the rhythm is the same.") + \
         proc([("Discover", "Listen, assess and define the outcome and success measures."), ("Design", "Agree architecture, plan and business case."), ("Deliver", "Build in short cycles with visible progress every sprint."), ("Sustain", "Hand over, train and keep improving.")]) + '</div></section>'
    b += cta_band("Find the model that fits.", "We will recommend the lightest engagement that gets the job done.")
    page("capabilities.html", "Capabilities — Arron | Consulting, Services, Partnerships, Product as a Service", "How Arron works with you: consulting, managed services, technology partnerships and AI-native product development.", b)


# ---------- industry data
INDS = [("bank", "Banking & Financial", "Audit-ready change trails and compliance monitoring."), ("factory", "Manufacturing", "ERP, supply chain and shop-floor integration."),
        ("heart", "Healthcare & Pharma", "SLA-driven support for critical systems."), ("cart", "Retail & Consumer", "Surge detection and omnichannel experience."),
        ("signal", "Telecom & Media", "Network incident prediction and smart routing."), ("code", "Technology & SaaS", "Incident correlation across DevOps pipelines."),
        ("bolt", "Energy & Utilities", "Asset-heavy operations and field service."), ("gov", "Public Sector", "Modernization for state, local and nonprofit.")]

CASES = [
    dict(cat="erp", photo="meeting-table", tag="ERP · Manufacturing", title="One ERP across four plants", ind="Manufacturing", svc="ERP",
         ch="Four plants ran separate legacy systems, so month-end close took weeks and inventory was invisible.", sol="Vendor-neutral selection, then a phased cloud ERP rollout with unified reporting.", r=(("-32%", "Close cycle time"), ("4 → 1", "Systems consolidated"))),
    dict(cat="itsm", photo="dashboard", tag="ITSM · Financial services", title="An AI-assisted service desk", ind="Financial services", svc="ITSM",
         ch="Ticket volumes and manual routing were driving missed SLAs and audit findings.", sol="Migrated to a modern ITSM platform with auto-triage, a self-service portal and audit-ready change flows.", r=(("-40%", "Ticket handling time"), ("+25%", "Self-service rate"))),
    dict(cat="cx", photo="sticky-notes", tag="CX · Retail", title="A unified customer view", ind="Retail", svc="CX",
         ch="Customer data sat in four tools, so service teams could not see the full history.", sol="Connected CRM, contact center and data to personalize every touchpoint.", r=(("+18 pt", "NPS improvement"), ("-22%", "Repeat contacts"))),
    dict(cat="ai", photo="laptop-dark", tag="AI · Healthcare", title="Intelligent documentation support", ind="Healthcare", svc="AI",
         ch="Clinical teams spent hours on documentation that slowed patient throughput.", sol="Governed AI assistant embedded in existing workflows, with human review built in.", r=(("-30%", "Documentation time"), ("100%", "Human-reviewed output"))),
    dict(cat="erp", photo="office", tag="ERP · Public sector", title="Modernizing a county back office", ind="Public sector", svc="ERP",
         ch="Aging finance and HR systems were costly to maintain and hard to audit.", sol="Requirements-led selection and implementation with strong change management.", r=(("-28%", "Run cost"), ("1", "Platform for finance and HR"))),
    dict(cat="itsm", photo="servers", tag="ITSM · Telecom", title="Predicting incidents before they land", ind="Telecom", svc="ITSM",
         ch="Network incidents surfaced only after customers called in.", sol="Event correlation and AI-driven routing feeding a single service platform.", r=(("-35%", "Major incidents"), ("+20%", "First-time resolution"))),
    dict(cat="cx", photo="highfive", tag="CX · Banking", title="Faster, simpler customer onboarding", ind="Banking", svc="CX",
         ch="New customers abandoned onboarding because it spanned too many steps and systems.", sol="Redesigned the journey and connected CRM, identity and servicing into one flow.", r=(("-45%", "Onboarding time"), ("+15%", "Completion rate"))),
]
QUOTES = [
    ("They narrowed a crowded vendor field to the one that actually fit us, and the project landed on time. It felt like having an owner on our side of the table.", "VP of Information Technology", "Manufacturing client", "VP"),
    ("The team brought real depth in service management and genuinely trained our people. We run the platform ourselves now, with confidence.", "Director of IT Operations", "Financial services client", "DO"),
    ("They told us where AI would not pay off, which is exactly why we trusted them on where it would.", "Chief Digital Officer", "Healthcare client", "CD"),
    ("Clear plan, honest estimates and senior people who stayed involved the whole way. That is rare.", "Program Director", "Public sector client", "PD"),
    ("Our customer teams finally see one view of the customer. The difference in service quality was visible within a quarter.", "Head of Customer Operations", "Retail client", "HC"),
    ("They negotiated terms we would not have achieved alone and then helped us deliver on the contract.", "CFO", "Distribution client", "CF"),
]
PEOPLE = [("Daniel Reyes", "Principal Architect, SAP & Cloud", "18+ years", "Certified SAP Enterprise and BTP architect bridging business strategy and enterprise platforms, from S/4HANA to AI-enabled solutions.", ["SAP BTP", "S/4HANA", "Business AI"], "Kentucky, USA"),
          ("Priya Nair", "Director, ERP & Enterprise Applications", "15+ years", "Leads ERP selection and implementation across finance and supply chain, focused on adoption and measurable business results.", ["ERP", "Program delivery", "Change"], "Texas, USA"),
          ("Marcus Hale", "Director, Digital & Customer Experience", "12+ years", "Designs customer journeys and the platforms behind them, connecting data, CRM and service channels into one experience.", ["CX", "CRM", "Analytics"], "Texas, USA"),
          ("Elena Brooks", "Managing Partner, ITSM & AI Transformation", "20+ years", "Entrepreneurial executive in IT service management and cloud transformation. ITIL Expert and Azure certified.", ["ServiceNow", "Azure", "ITIL"], "Dallas–Fort Worth, TX")]


def case_card(c):
    return f'''<div class="case" data-cat="{c["cat"]}"><div class="art ph">{photo(c["photo"], c["title"])}<em>{c["tag"]}</em></div><div class="cb"><h3>{c["title"]}</h3>
<div class="cs-sec"><b>Challenge</b><p>{c["ch"]}</p></div><div class="cs-sec"><b>Approach</b><p>{c["sol"]}</p></div>
<div class="res"><div><b>{c["r"][0][0]}</b><span>{c["r"][0][1]}</span></div><div><b>{c["r"][1][0]}</b><span>{c["r"][1][1]}</span></div></div></div></div>'''


def build_industry():
    b = hero('<a href="index.html">Home</a> / Industry Expertise', 'Deep experience. <span class="r">Real people.</span>',
             "The industries we serve, the work we have delivered and the consultants behind it.", V.v_industries())
    b += marquee("Technology partners across our client work")
    b += '<section id="more"><div class="wrap">' + sh("Industries", "Sector knowledge that shortens the learning curve.", "These are the environments our team knows well.") + \
         '<div class="inds" data-stagger>' + ''.join(f'<div class="ind">{icon(i)}<h3>{t}</h3><p>{p}</p></div>' for i, t, p in INDS) + '</div></div></section>'
    tl = [("case-studies.html", "Clients", "Case Studies", "Representative engagements, with the challenge, approach and results.", "boardroom"),
          ("testimonials.html", "Clients", "Testimonials", "What clients say about working with Arron.", "highfive"),
          ("consultants.html", "Consultants", "Consultants & Partners", "Profiles of our team and the partner network we bring in.", "team-room")]
    b += '<section class="paper"><div class="wrap">' + sh("Explore", "See the work and the people.", "Everything you need to judge whether we are the right fit.") + \
         '<div class="tiles" style="grid-template-columns:repeat(3,1fr)" data-stagger>' + ''.join(
             f'<a class="tile" href="{h}"><div class="art ph">{photo(ph)}</div><div class="tb"><span class="k">{k}</span><h3>{t}</h3><p>{d}</p><span class="more">Explore {ARROW}</span></div></a>' for h, k, t, d, ph in tl) + '</div></div></section>'
    b += cta_band("Working in one of these sectors?", "We will bring people who have done it before.")
    page("industry.html", "Industry Expertise — Arron | Clients, Case Studies & Consultants", "Arron's client work, industry experience and the consultants who deliver it.", b)


def build_cases():
    b = hero('<a href="index.html">Home</a> / <a href="industry.html">Industry Expertise</a> / Case Studies', 'Results you can <span class="r">point to.</span>',
             "Representative engagements across ERP, ITSM, AI and customer experience, with the challenge, the approach and the outcome.", V.v_impact())
    b += marquee("Technology partners across our client work")
    f = CASES[0]
    feat = f'''<div class="feature rv"><div class="art ph">{photo("boardroom", f["title"])}</div><div class="fb2"><span class="kicker">Featured · {f["tag"]}</span><h3>{f["title"]}</h3><p>{f["ch"]} {f["sol"]}</p>
<div class="res"><div><b>{f["r"][0][0]}</b><span>{f["r"][0][1]}</span></div><div><b>{f["r"][1][0]}</b><span>{f["r"][1][1]}</span></div></div></div></div>'''
    b += f'''<section id="more"><div class="wrap">{sh("Case studies", "Representative engagements.", "Examples of the outcomes we design for. Client names withheld.")}{feat}
<div id="caselist"><div class="chipbar" data-filter="#caselist"><button class="fbtn on" data-f="all">All</button><button class="fbtn" data-f="erp">ERP</button><button class="fbtn" data-f="itsm">ITSM</button><button class="fbtn" data-f="ai">AI</button><button class="fbtn" data-f="cx">CX</button></div>
<div class="cases" data-stagger>{''.join(case_card(c) for c in CASES[1:])}</div></div></div></section>'''
    b += cta_band("Want results like these?", "Tell us your goal and we will share the most relevant experience.")
    page("case-studies.html", "Case Studies — Arron", "Representative Arron engagements across ERP, ITSM, AI and CX.", b)


def build_testimonials():
    stage = photo_stage("highfive", "“A partner, not a vendor.”", "Feedback from the clients we have worked with")
    b = hero('<a href="index.html">Home</a> / <a href="industry.html">Industry Expertise</a> / Testimonials', 'What clients <span class="r">say about us.</span>',
             "Straight feedback from the leaders we have worked alongside, in their own words.", stage, "photo")
    q = QUOTES[0]
    b += f'''<section id="more"><div class="wrap">{sh("Testimonials", "Trust is earned on delivery.", "Names are withheld at clients' request; roles and sectors are as given.")}
<div class="bigq rv"><div class="art ph">{photo("meeting-table", "Client workshop")}</div><div class="qb"><div class="mark">“</div><p>{q[0]}</p><b>{q[1]}</b><span>{q[2]}</span></div></div>
<div class="qgrid" data-stagger>{''.join(f'<div class="qcard"><div class="mark">“</div><p>{t}</p><div class="who"><div class="av">{i}</div><div><b>{r}</b><span>{s}</span></div></div></div>' for t, r, s, i in QUOTES[1:])}</div></div></section>'''
    b += cta_band("Be our next success story.", "Start with a conversation about what you want to achieve.")
    page("testimonials.html", "Testimonials — Arron", "What Arron clients say about working with us.", b)


def build_consultants():
    stage = photo_stage("team-room", "Senior practitioners on every engagement", "Our consultants and partner network")
    b = hero('<a href="index.html">Home</a> / <a href="industry.html">Industry Expertise</a> / Consultants', 'The people you <span class="r">will work with.</span>',
             "Practitioners with decades of enterprise delivery behind them, supported by a network of specialist partners.", stage, "photo")
    b += '<section id="more" class="paper"><div class="wrap">' + sh("Our consultants", "Meet the team.", "Profiles of the practitioners who lead our engagements.") + \
         '<div class="people" data-stagger>' + ''.join(f'<article class="person"><div class="ph"><span class="yrs">{y}</span>{V.AVATAR}</div><div class="pi"><h3>{n}</h3><div class="role">{r}</div><p>{bio}</p><div class="chips">{"".join(f"<span>{c}</span>" for c in ch)}</div><div class="loc">{loc}</div></div></article>' for n, r, y, bio, ch, loc in PEOPLE) + '</div></div></section>'
    pl = [("ServiceNow", "ITSM · Workflow"), ("SAP", "ERP · BTP"), ("Microsoft", "Azure · Dynamics"), ("Oracle", "ERP · Cloud"), ("Atlassian", "Jira Service Mgmt"), ("Salesforce", "CRM · CX"), ("AWS", "Cloud · AI"), ("Google Cloud", "Data · AI")]
    b += '<section><div class="wrap">' + sh("Our partners", "Strong platforms. Stronger together.", "Certified expertise across the ecosystems our clients already run on.") + \
         '<div class="plogos" data-stagger>' + ''.join(f'<div class="plogo">{n}<small>{s}</small></div>' for n, s in pl) + '</div></div></section>'
    b += f'''<section class="band">{photo("team-laptop", "Team collaborating")}<div class="wrap"><span class="kicker">Join us</span><h2>Do the best work of your career.</h2><p style="margin:20px 0 32px;max-width:48ch;font-size:1.1rem;color:#cfdcff">We hire experienced consultants and architects who want to stay close to clients and to the work.</p><a class="btn btn-red" href="careers.html">See open roles {ARROW}</a></div></section>'''
    page("consultants.html", "Consultants & Partners — Arron", "Meet the Arron consultants and our partner network.", b)


POSTS = [
    ("ai", "AI", "Is your enterprise actually ready for AI?", "A practical checklist covering data, governance, skills and use-case selection.", "laptop-dark", "8 min read"),
    ("erp", "ERP", "Five reasons ERP projects go over budget", "And the early warning signs most steering committees miss.", "meeting-table", "6 min read"),
    ("itsm", "ITSM", "AI triage without losing the human touch", "Where automation helps your service desk and where it should step aside.", "dashboard", "5 min read"),
    ("cx", "CX", "Connecting customer data across channels", "A simple model for one customer view without a rip-and-replace.", "sticky-notes", "7 min read"),
    ("erp", "ERP", "How to run an ERP demo that tells you the truth", "Scripts, scoring and the questions vendors hope you will not ask.", "boardroom", "6 min read"),
    ("itsm", "ITSM", "Migrating off a legacy ITSM tool", "A step-by-step approach that protects data, SLAs and morale.", "servers", "9 min read"),
    ("ai", "AI", "From pilot to production: where AI projects stall", "The four gaps between a good demo and a dependable system.", "dev-team", "7 min read"),
    ("cx", "CX", "Measuring experience beyond NPS", "Signals that actually predict loyalty and what to do with them.", "highfive", "5 min read"),
]

ARTICLES = [
    ("ai-readiness", "Most AI programs stall not on the model but on everything around it. Before you fund a pilot, test your readiness across four areas.",
     [("Data access", "Can the right people reach clean, governed data for your top use cases? If not, fix that first."),
      ("Use-case selection", "Rank ideas by value and feasibility, and start with one whose outcome you can measure within a quarter."),
      ("Skills and ownership", "Name a business owner for every use case, not just a technical lead."),
      ("Governance", "Decide up front how you will handle security, privacy, bias and human review.")]),
    ("erp-over-budget", "ERP overruns are rarely a surprise in hindsight. These five causes show up again and again, usually early enough to act on.",
     [("Unclear requirements", "Teams discover what they need halfway through configuration, when change is most expensive."),
      ("Underestimated data migration", "Cleaning and mapping legacy data takes longer than any plan assumes."),
      ("Customization creep", "Every bespoke change adds cost now and upgrade pain later."),
      ("Weak change management", "A system nobody adopts delivers none of the promised value."),
      ("No independent oversight", "Vendor timelines tend to be optimistic. Someone on your side needs to challenge them.")]),
    ("ai-triage-human-touch", "AI can route and categorize tickets faster than any team. The question is where it should stop and a person should start.",
     [("Start with categorization and routing", "These are low-risk, high-volume tasks where AI helps most."),
      ("Keep people on high-impact incidents", "Major outages and sensitive requests deserve human judgment."),
      ("Measure resolution quality", "Speed alone can hide wrong answers. Track reopen rates and satisfaction too."),
      ("Let agents correct the model", "Make feedback easy so the system improves from real corrections.")]),
    ("connecting-customer-data", "One customer view does not require replacing every system. It requires a clear plan for identity, integration and use.",
     [("Start from the questions", "Pick the three things your teams most need to know about a customer."),
      ("Unify identity first", "Match records reliably before you try to analyze anything."),
      ("Integrate in layers", "Connect systems gradually instead of attempting a big-bang rebuild."),
      ("Put insight where people work", "A dashboard nobody opens helps no one. Surface it inside the agent's screen."),
      ("Govern consent", "Respect preferences and regulations from the start.")]),
    ("erp-demo-truth", "A polished vendor demo shows what the product does best. A scripted demo shows whether it fits you.",
     [("Script from your real processes", "Give every vendor the same scenarios drawn from your daily work."),
      ("Score on one sheet", "Use identical criteria so comparisons are fair and defensible."),
      ("Involve end users", "The people who will use the system spot gaps that executives miss."),
      ("Ask to see the edge cases", "Exceptions and failures reveal more than the happy path."),
      ("Insist on hands-on time", "A sandbox session beats any slide.")]),
    ("itsm-migration", "Moving off a legacy service management tool is a chance to simplify. It is also easy to disrupt service if you rush.",
     [("Inventory what you really use", "Retire unused workflows rather than copying them across."),
      ("Clean data before moving it", "Migrating bad records only moves the problem."),
      ("Migrate in waves", "Start with low-risk queues and learn before the critical ones."),
      ("Run in parallel where it matters", "Keep a safety net for urgent services during cutover."),
      ("Retrain with real tickets", "People learn fastest on the work they actually do.")]),
    ("pilot-to-production", "Plenty of AI demos work. Far fewer become dependable systems. The gap usually comes down to four things.",
     [("Data access", "Production needs reliable, permissioned data, not a one-off extract."),
      ("Integration", "Value appears only when AI is wired into the workflow people use."),
      ("Ownership", "Someone must be accountable for the outcome after launch."),
      ("Monitoring", "Models drift. You need to watch quality and cost continuously.")]),
    ("cx-beyond-nps", "Net Promoter Score is useful but incomplete. Better signals show where loyalty is won or lost.",
     [("Customer effort", "How hard was it to get help? Effort predicts loyalty well."),
      ("Resolution and repeat contact", "Did the issue stay fixed, or did the customer have to come back?"),
      ("Behavioral signals", "Usage patterns and drop-offs often speak louder than surveys."),
      ("Closing the loop", "Follow up on feedback so customers see that it matters."),
      ("Link to revenue", "Tie experience measures to retention and growth so they get funded.")]),
]


def build_blog():
    stage = photo_stage("meeting-table", "Insights from the field", "Practical writing on AI, ERP, ITSM and CX")
    signup = f'''<div class="hero-signup rv" data-delay=".5"><span class="hs-label">Get the monthly newsletter</span>
<form data-demo onsubmit="return false"><div class="news"><input type="email" required placeholder="you@company.com" aria-label="Email address"><button class="btn btn-red" type="submit">Subscribe {ARROW}</button></div></form>
<div class="ok">Thanks, you are on the list.</div><p class="hs-note">One useful email a month. Free, and you can unsubscribe any time. <a href="#more">Or browse the articles below ↓</a></p></div>'''
    b = hero('<a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Blogs & Newsletter', 'Latest <span class="r">thinking.</span>',
             "Practical writing on AI, ERP, ITSM and customer experience from the people doing the work.", stage, "photo", cta_html=signup)
    f = POSTS[0]
    feat = f'<a class="feature rv" href="{ARTICLES[0][0]}.html"><div class="art ph">{photo(f[4])}</div><div class="fb2"><span class="kicker">{f[1]} · Featured</span><h3>{f[2]}</h3><p>{f[3]} Read it before you invest in a single model.</p><span class="more" style="margin-top:24px">Read article {ARROW}</span></div></a>'
    cards = ''.join(f'<a class="post" href="{ARTICLES[i+1][0]}.html" data-cat="{c}"><div class="art ph">{photo(ph)}</div><div class="pb"><span class="m">{t} · {rt}</span><h3>{ti}</h3><p>{de}</p><span class="more">Read article {ARROW}</span></div></a>' for i, (c, t, ti, de, ph, rt) in enumerate(POSTS[1:]))
    b += f'''<section id="more"><div class="wrap">{sh("Blogs", "Insights from the field.", "Filter by topic to find what is useful to you.")}{feat}
<div id="postlist"><div class="chipbar" data-filter="#postlist"><button class="fbtn on" data-f="all">All</button><button class="fbtn" data-f="ai">AI</button><button class="fbtn" data-f="erp">ERP</button><button class="fbtn" data-f="itsm">ITSM</button><button class="fbtn" data-f="cx">CX</button></div>
<div class="posts" data-stagger>{cards}</div></div></div></section>'''
    b += f'''<section class="navy" style="padding:90px 0" id="newsletter"><div class="wrap split2"><div><span class="kicker rv">Newsletter</span><h2 data-split>One useful email, once a month.</h2></div>
<div class="rv" data-delay=".2"><p style="font-size:1.1rem;margin-bottom:26px;max-width:44ch">Short briefings on what is changing in enterprise technology, and what to do about it.</p><form data-demo onsubmit="return false"><div class="news"><input type="email" required placeholder="you@company.com" aria-label="Email"><button class="btn btn-red" type="submit">Subscribe</button></div></form><div class="ok" style="margin-top:16px">Thanks, you are on the list.</div></div></div></section>'''
    page("blog.html", "Blogs & Newsletter — Arron", "Arron insights on AI, ERP, ITSM and customer experience, plus our monthly newsletter.", b)


def build_articles():
    for i, (slug, intro, pts) in enumerate(ARTICLES):
        c, tag, title, desc, ph, rt = POSTS[i]
        stage = photo_stage(ph, title, f"{tag} · {rt}")
        b = hero(f'<a href="index.html">Home</a> / <a href="resources.html">Resources</a> / <a href="blog.html">Blogs</a> / {tag}', title, desc, stage, "photo", cta=False)
        b += f'''<section id="more"><div class="wrap" style="max-width:920px"><span class="kicker">{tag} · {rt}</span><p class="lead" style="font-size:1.3rem;color:var(--ink);font-weight:500;margin-bottom:46px">{intro}</p>
<h2 style="font-size:1.8rem;margin-bottom:8px">Key takeaways</h2>{rows([(a, b2) for a, b2 in pts], "c2")}
<div style="margin-top:56px;padding:34px 38px;border-radius:20px;background:var(--paper);display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap"><div><b style="font:800 1.2rem var(--fd);color:var(--ink);display:block">Want to talk this through?</b><span style="color:var(--muted)">A senior consultant can help you apply this to your situation.</span></div><a class="btn btn-red" href="about.html#contact">Talk to an expert {ARROW}</a></div></div></section>'''
        others = [j for j in range(len(POSTS)) if j != i][:3]
        b += '<section class="paper"><div class="wrap">' + sh("Keep reading", "More from the blog.", "Related articles on AI, ERP, ITSM and CX.") + '<div class="posts" data-stagger>' + ''.join(
            f'<a class="post" href="{ARTICLES[j][0]}.html"><div class="art ph">{photo(POSTS[j][4])}</div><div class="pb"><span class="m">{POSTS[j][1]} · {POSTS[j][5]}</span><h3>{POSTS[j][2]}</h3><p>{POSTS[j][3]}</p><span class="more">Read article {ARROW}</span></div></a>' for j in others) + '</div></div></section>'
        page(f"{slug}.html", f"{title} — Arron", desc, b)


def build_events():
    stage = photo_stage("workshop", "Learn with us, live", "Webinars, roundtables and workshops")
    b = hero('<a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Events & Webinars', 'Learn with us, <span class="r">live.</span>',
             "Webinars, roundtables and workshops on the topics our clients ask about most.", stage, "photo")
    up = [("12", "Feb", "AI readiness for the enterprise", "Live webinar · 45 minutes with Q&A", "Webinar", "laptop-dark"), ("05", "Mar", "ERP selection roundtable", "Dallas, TX · In person, invite only", "Event", "workshop"), ("20", "Mar", "ITSM in the age of AI agents", "Live webinar · Hands-on demo", "Webinar", "dashboard")]
    b += '<section id="more"><div class="wrap">' + sh("Upcoming", "On the calendar.", "Register to join live, or to receive the recording if you cannot attend.") + \
         '<div class="evcards" data-stagger>' + ''.join(f'<div class="evc"><div class="art ph">{photo(ph)}<div class="pill-d"><b>{d}</b><span>{m}</span></div></div><div class="eb"><span class="k">{k}</span><h3>{t}</h3><p>{p}</p><a class="more" href="about.html#contact">Register {ARROW}</a></div></div>' for d, m, t, p, k, ph in up) + '</div></div></section>'
    od = [("Choosing an ERP without regret", "On demand · 38 min", "meeting-table"), ("Building a business case for ITSM", "On demand · 42 min", "boardroom"), ("Customer journeys that convert", "On demand · 35 min", "sticky-notes")]
    b += '<section class="paper"><div class="wrap">' + sh("On demand", "Watch when it suits you.", "Recordings of past webinars, free to watch.") + \
         '<div class="evcards" data-stagger>' + ''.join(f'<div class="evc"><div class="art ph">{photo(ph)}</div><div class="eb"><span class="k">Webinar recording</span><h3>{t}</h3><p>{d}</p><a class="more" href="about.html#contact">Request recording {ARROW}</a></div></div>' for t, d, ph in od) + '</div></div></section>'
    b += cta_band("Want us at your event?", "Our consultants speak on AI, ERP, ITSM and customer experience.", "Invite a speaker")
    page("events.html", "Events & Webinars — Arron", "Upcoming and on-demand Arron webinars and events.", b)


def build_careers():
    stage = photo_stage("team-laptop", "Build your career with Arron", "Senior practitioners, real clients, room to grow")
    b = hero('<a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Careers', 'Do the best work <span class="r">of your career.</span>',
             "Join a team where senior practitioners shape the work, learn from each other and stay close to clients.", stage, "photo")
    b += f'<section id="more"><div class="wrap">{sh("Why Arron", "What it is like to work here.", "A small, senior team with the ambition of a much larger firm.")}' + rows([
        ("Meaningful work", "Modern ERP, service and AI programs for organizations that depend on them."),
        ("Senior colleagues", "Learn directly from people with decades of delivery experience."),
        ("Funded learning", "Certification budgets and protected time to build new skills."),
        ("Flexibility", "Dallas-anchored and remote-friendly, with clear expectations.")], "c4w") + '</div></section>'
    jobs = [("Senior ERP Consultant", "ERP", "Dallas, TX", "Hybrid"), ("ServiceNow Architect", "ITSM", "Remote · USA", "Full-time"), ("AI Solutions Engineer", "AI", "Dallas, TX", "Hybrid"),
            ("CX Strategy Consultant", "CX", "Dallas, TX", "Hybrid"), ("SAP BTP Developer", "ERP", "Remote · USA", "Full-time"), ("Delivery Manager", "ITSM", "Dallas, TX", "Hybrid")]
    b += f'''<section class="paper"><div class="wrap">{sh("Open roles", "Find your role.", "Do not see a fit? Send us a note anyway.")}
<div id="joblist"><div class="chipbar" data-filter="#joblist"><button class="fbtn on" data-f="all">All</button><button class="fbtn" data-f="erp">ERP</button><button class="fbtn" data-f="itsm">ITSM</button><button class="fbtn" data-f="ai">AI</button><button class="fbtn" data-f="cx">CX</button></div>
<div class="roles">{''.join(f'<a class="rolerow" href="about.html#contact" data-cat="{c.lower()}"><b>{t}</b><span class="d tagd">{c}</span><span class="l">{l}</span><span class="more">{k} {ARROW}</span></a>' for t, c, l, k in jobs)}</div></div></div></section>'''
    b += '<section class="navy"><div class="wrap">' + sh("How we hire", "A process that respects your time.", "Four steps, usually completed within three weeks.") + \
         proc([("Apply", "Send your profile or a short note."), ("Conversation", "Meet a senior consultant to discuss your experience."), ("Case discussion", "Talk through a real engagement scenario."), ("Offer", "Meet the leadership team and receive your offer.")]) + '</div></section>'
    b += cta_band("Ready to join us?", "Send us your profile and tell us what you want to work on.", "Get in touch")
    page("careers.html", "Careers — Arron", "Careers at Arron: open roles and how we hire.", b)


def build_resources():
    b = hero('<a href="index.html">Home</a> / Resources', 'Ideas worth <span class="r">acting on.</span>',
             "Practical thinking on AI, ERP, ITSM and customer experience, plus the events and roles that keep our community growing.", resources_stage())
    tl = [("blog.html", "Blogs & Newsletter", "Insights from the field", "Practical writing on AI, ERP, ITSM and CX, plus a monthly newsletter.", "laptop-dark"),
          ("events.html", "Events & Webinars", "Learn with us, live", "Upcoming sessions and on-demand recordings.", "workshop"),
          ("careers.html", "Careers", "Build your career with Arron", "Open roles and how we hire.", "team-laptop")]
    b += '<section id="more"><div class="wrap">' + sh("Explore", "Three ways to engage.", "Read, learn or join us.") + '<div class="tiles" style="grid-template-columns:repeat(3,1fr)" data-stagger>' + ''.join(
        f'<a class="tile" href="{h}"><div class="art ph">{photo(ph)}</div><div class="tb"><span class="k">{k}</span><h3>{t}</h3><p>{d}</p><span class="more">Explore {ARROW}</span></div></a>' for h, k, t, d, ph in tl) + '</div></div></section>'
    b += '<section class="paper"><div class="wrap">' + sh("Latest", "Fresh from the blog.", "Three recent reads.") + '<div class="posts" data-stagger>' + ''.join(
        f'<a class="post" href="{ARTICLES[i+1][0]}.html"><div class="art ph">{photo(ph)}</div><div class="pb"><span class="m">{t} · {rt}</span><h3>{ti}</h3><p>{de}</p><span class="more">Read article {ARROW}</span></div></a>' for i, (c, t, ti, de, ph, rt) in enumerate(POSTS[1:4])) + '</div></div></section>'
    b += cta_band("Get the monthly briefing.", "One useful email, once a month.", "Subscribe", "blog.html#newsletter")
    page("resources.html", "Resources — Arron | Insights, Events & Careers", "Arron insights, newsletter, webinars and career opportunities.", b)


def build_about():
    b = hero('<a href="index.html">Home</a> / About Us', 'A Dallas company with <span class="r">a national network.</span>',
             "Arron exists to help organizations stay ahead of change with senior expertise, honest advice and work that lasts.", V.v_map())
    b += f'''<section id="more"><div class="wrap split2"><div class="collage rv" ><div class="c1">{photo("office", "Arron office")}</div><div class="c2">{photo("team-laptop", "Team at work")}</div><div class="badge"><b>Dallas, TX</b><span>Headquarters, with a network of specialists nationwide</span></div></div>
<div><span class="kicker rv">Our story</span><h2 data-split>Why “Ahead of now.”</h2>
<p class="lead rv" data-delay=".2">Technology moves faster than most organizations can absorb. Arron was founded on a simple idea: your business should not be catching up to its own systems.</p>
<p class="rv" data-delay=".3" style="margin-top:18px">Headquartered in Dallas, Texas, we are a team of experienced practitioners with a wide network of specialist partners across the country, so we can staff the right people for each engagement.</p>
<div class="stats rv" style="grid-template-columns:1fr 1fr 1fr;margin-top:40px"><div class="stat"><b data-count="18" data-suffix="+">0</b><span>Years of leadership</span></div><div class="stat"><b data-count="4">0</b><span>Practice areas</span></div><div class="stat"><b data-count="12" data-suffix="+">0</b><span>Platform partners</span></div></div></div></div></section>'''
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
    page("about.html", "About Us — Arron | Dallas Technology Consulting", "About Arron, a Dallas-based technology consulting company, and how to contact us.", b)


if __name__ == "__main__":
    build_home(); build_offerings(); build_cap(); build_industry(); build_cases(); build_testimonials(); build_consultants()
    build_resources(); build_blog(); build_articles(); build_events(); build_careers(); build_about()
    for k in OFFER_KEYS + CAP_KEYS:
        build_detail(k)
    print("built", len([f for f in os.listdir(ROOT) if f.endswith('.html')]), "pages")
