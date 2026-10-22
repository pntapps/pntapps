"""Generate animated SVG assets for the github.com/pntapps profile README.

Usage: python gen_profile.py <site_repo_dir> <out_dir>
GitHub renders SVGs in READMEs as images: CSS @keyframes and SMIL animate, no JS, no external refs.
"""
import base64
import io
import sys

from PIL import Image, ImageDraw

SITE, OUT = sys.argv[1], sys.argv[2]
FONT = "'Segoe UI',Inter,-apple-system,Helvetica,Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"


def b64png(img, size):
    img = img.copy()
    img.thumbnail((size, size), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode()


def write(name, svg):
    with open(f"{OUT}/{name}", "w", encoding="utf8") as f:
        f.write(svg)


logo = b64png(Image.open(f"{SITE}/public/logo.png").convert("RGBA"), 160)

THEMES = {
    "dark": dict(bg1="#060913", bg2="#0d1326", fg="#f2f5ff", muted="#9ba6c9", brand="#22d3ee", brand2="#1d5fd6",
                 line="#222b4a", chip="#0b2a3a", chipfg="#67e8f9", dev="#141b33", dev2="#0a0f1e", orb=0.38),
    "light": dict(bg1="#ffffff", bg2="#eef4ff", fg="#0f172a", muted="#556070", brand="#1d5fd6", brand2="#22d3ee",
                  line="#dbe3f0", chip="#e6efff", chipfg="#174bb0", dev="#ffffff", dev2="#f2f4f7", orb=0.25),
}

# --------------------------------------------------------------------------- banner


def banner(t):
    chips, x = "", 96
    for i, c in enumerate(["iOS", "Android", "macOS", "Windows", "Web", "AI"]):
        w = 24 + len(c) * 10.5
        chips += (f'<g class="chip" style="animation-delay:{0.6 + i * 0.12:.2f}s">'
                  f'<rect x="{x}" y="250" width="{w:.0f}" height="34" rx="17" fill="{t["chip"]}"/>'
                  f'<text x="{x + w / 2:.0f}" y="272" text-anchor="middle" font-size="15" font-weight="600" fill="{t["chipfg"]}">{c}</text></g>')
        x += w + 10
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1280" height="360" viewBox="0 0 1280 360" font-family="{FONT}">
<style>
  .orb1{{animation:drift1 14s ease-in-out infinite}} .orb2{{animation:drift2 18s ease-in-out infinite}}
  @keyframes drift1{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(-70px,40px)}}}}
  @keyframes drift2{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(60px,-30px)}}}}
  .rise{{opacity:0;animation:rise .9s cubic-bezier(.2,.7,.2,1) forwards}}
  @keyframes rise{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
  .chip{{opacity:0;animation:rise .6s ease-out forwards}}
  .float1{{animation:float 6s ease-in-out infinite}} .float2{{animation:float 7s ease-in-out -2s infinite}} .float3{{animation:float 5.5s ease-in-out -4s infinite}}
  @keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-12px)}}}}
  .bar{{transform-box:fill-box;transform-origin:left;animation:grow 3.2s ease-in-out infinite}}
  @keyframes grow{{0%{{transform:scaleX(.15)}}60%,100%{{transform:scaleX(1)}}}}
  .pulse{{transform-box:fill-box;transform-origin:center;animation:pulse 2.4s ease-in-out infinite}}
  @keyframes pulse{{0%,100%{{transform:scale(1);opacity:1}}50%{{transform:scale(1.25);opacity:.6}}}}
  .twinkle{{animation:tw 3s ease-in-out infinite}} @keyframes tw{{0%,100%{{opacity:.2}}50%{{opacity:1}}}}
  @media (prefers-reduced-motion: reduce){{*{{animation:none!important;opacity:1!important}}}}
</style>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["bg1"]}"/><stop offset="1" stop-color="{t["bg2"]}"/></linearGradient>
  <radialGradient id="o1"><stop offset="0" stop-color="{t["brand"]}" stop-opacity="{t["orb"]}"/><stop offset="1" stop-color="{t["brand"]}" stop-opacity="0"/></radialGradient>
  <radialGradient id="o2"><stop offset="0" stop-color="{t["brand2"]}" stop-opacity="{t["orb"]}"/><stop offset="1" stop-color="{t["brand2"]}" stop-opacity="0"/></radialGradient>
  <linearGradient id="txt" x1="0" x2="1"><stop offset="0" stop-color="{t["brand"]}"><animate attributeName="stop-color" values="{t["brand"]};{t["brand2"]};{t["brand"]}" dur="6s" repeatCount="indefinite"/></stop><stop offset="1" stop-color="{t["brand2"]}"><animate attributeName="stop-color" values="{t["brand2"]};{t["brand"]};{t["brand2"]}" dur="6s" repeatCount="indefinite"/></stop></linearGradient>
  <linearGradient id="scr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["brand2"]}"/><stop offset="1" stop-color="{t["brand"]}"/></linearGradient>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.5" fill="{t["line"]}"/></pattern>
  <linearGradient id="fade" x1="0" x2="1"><stop offset="0.3" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>
  <mask id="m"><rect width="1280" height="360" fill="url(#fade)"/></mask>
  <clipPath id="card"><rect width="1280" height="360" rx="24"/></clipPath>
</defs>
<g clip-path="url(#card)">
  <rect width="1280" height="360" fill="url(#bg)"/>
  <rect width="1280" height="360" fill="url(#dots)" mask="url(#m)"/>
  <circle class="orb1" cx="1120" cy="60" r="280" fill="url(#o1)"/>
  <circle class="orb2" cx="820" cy="360" r="240" fill="url(#o2)"/>
  <g fill="{t["brand"]}">
    <circle class="twinkle" cx="760" cy="70" r="2.5"/><circle class="twinkle" style="animation-delay:-1s" cx="1230" cy="300" r="2"/>
    <circle class="twinkle" style="animation-delay:-2s" cx="905" cy="40" r="2"/><circle class="twinkle" style="animation-delay:-1.5s" cx="700" cy="310" r="2.5"/>
  </g>
  <rect x=".5" y=".5" width="1279" height="359" rx="24" fill="none" stroke="{t["line"]}"/>
</g>

<g class="rise">
  <image x="96" y="58" width="60" height="60" href="data:image/png;base64,{logo}" xlink:href="data:image/png;base64,{logo}"/>
  <text x="170" y="99" font-size="28" font-weight="700" fill="{t["fg"]}">PNT Apps</text>
</g>
<g class="rise" style="animation-delay:.15s">
  <text x="96" y="186" font-size="52" font-weight="700" fill="{t["fg"]}" letter-spacing="-1">We build apps people <tspan fill="url(#txt)">love.</tspan></text>
</g>
<g class="rise" style="animation-delay:.3s">
  <text x="96" y="226" font-size="20" fill="{t["muted"]}">Independent app studio from India. Our own apps, open source and client work.</text>
</g>
{chips}

<!-- Laptop -->
<g class="float1">
  <g transform="translate(880 120)">
    <rect width="250" height="158" rx="12" fill="{t["dev"]}" stroke="{t["line"]}" stroke-width="2"/>
    <rect x="12" y="12" width="226" height="134" rx="6" fill="{t["dev2"]}"/>
    <circle cx="26" cy="24" r="4" fill="#ff5f57"/><circle cx="39" cy="24" r="4" fill="#febc2e"/><circle cx="52" cy="24" r="4" fill="#28c840"/>
    <rect x="24" y="42" width="90" height="10" rx="5" fill="url(#scr)"/>
    <rect class="bar" x="24" y="62" width="190" height="8" rx="4" fill="{t["line"]}"/>
    <rect class="bar" style="animation-delay:-.8s" x="38" y="78" width="150" height="8" rx="4" fill="{t["line"]}"/>
    <rect class="bar" style="animation-delay:-1.6s" x="38" y="94" width="110" height="8" rx="4" fill="{t["brand"]}" opacity=".85"/>
    <rect class="bar" style="animation-delay:-2.4s" x="24" y="110" width="170" height="8" rx="4" fill="{t["line"]}"/>
    <path d="M-22 158h294l-16 16H-6z" fill="{t["dev"]}" stroke="{t["line"]}" stroke-width="2" stroke-linejoin="round"/>
  </g>
</g>
<!-- Tablet -->
<g class="float2">
  <g transform="translate(1110 70)">
    <rect width="110" height="150" rx="14" fill="{t["dev"]}" stroke="{t["line"]}" stroke-width="2"/>
    <rect x="9" y="11" width="92" height="128" rx="7" fill="url(#scr)" opacity=".9"/>
    <g fill="#fff" opacity=".9"><rect x="20" y="24" width="32" height="32" rx="8"/><rect x="58" y="24" width="32" height="32" rx="8" opacity=".6"/><rect x="20" y="62" width="32" height="32" rx="8" opacity=".6"/><rect x="58" y="62" width="32" height="32" rx="8"/></g>
    <rect x="20" y="104" width="70" height="8" rx="4" fill="#fff" opacity=".7"/>
    <rect x="20" y="118" width="46" height="8" rx="4" fill="#fff" opacity=".45"/>
  </g>
</g>
<!-- Phone -->
<g class="float3">
  <g transform="translate(820 190)">
    <rect width="78" height="146" rx="16" fill="{t["dev"]}" stroke="{t["line"]}" stroke-width="2"/>
    <rect x="7" y="10" width="64" height="126" rx="10" fill="{t["dev2"]}"/>
    <rect x="27" y="15" width="24" height="5" rx="2.5" fill="{t["line"]}"/>
    <circle class="pulse" cx="39" cy="58" r="16" fill="url(#scr)"/>
    <path d="M34 50l13 8-13 8z" fill="#fff"/>
    <rect x="16" y="88" width="46" height="7" rx="3.5" fill="{t["line"]}"/>
    <rect x="22" y="101" width="34" height="7" rx="3.5" fill="{t["line"]}"/>
    <rect x="16" y="116" width="46" height="12" rx="6" fill="{t["brand"]}"/>
  </g>
</g>
</svg>'''


for name, t in THEMES.items():
    write(f"banner-{name}.svg", banner(t))

# --------------------------------------------------------------------------- typing line

LINES = ["iOS & Android apps", "React Native & Expo", "macOS & Windows software", "Web apps with Next.js",
         "AI features that ship", "ERP & business software"]


def typing(color, caret):
    n, slot = len(LINES), 3.0
    dur = n * slot
    groups = ""
    for i, line in enumerate(LINES):
        w = len(line) * 14.5 + 6
        a, b = i / n, (i + 1) / n
        k = lambda f: f"{a + (b - a) * f:.4f}"
        # type in (0-35%), hold, erase (80-95%)
        width_keys = f"0;{k(0)};{k(.35)};{k(.8)};{k(.95)};1" if i else f"0;{k(.35)};{k(.8)};{k(.95)};1"
        width_vals = f"0;0;{w:.0f};{w:.0f};0;0" if i else f"0;{w:.0f};{w:.0f};0;0"
        groups += f'''<clipPath id="c{i}"><rect x="0" y="0" height="40" width="0"><animate attributeName="width" values="{width_vals}" keyTimes="{width_keys}" dur="{dur}s" repeatCount="indefinite" calcMode="spline" keySplines="{' '.join(['.4 0 .6 1;'] * (width_vals.count(';')))[:-1]}"/></rect></clipPath>
<g clip-path="url(#c{i})"><text x="0" y="29" font-size="26" font-weight="600" fill="{color}">{line.replace("&", "&amp;")}</text></g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="40" viewBox="0 0 640 40" font-family="{MONO}">
<style>.caret{{animation:blink 1s steps(1) infinite}}@keyframes blink{{50%{{opacity:0}}}}</style>
<g transform="translate(18 0)">{groups}</g>
<text x="0" y="29" font-size="26" font-weight="700" fill="{caret}">›</text>
</svg>'''


write("typing-dark.svg", typing("#67e8f9", "#9ba6c9"))
write("typing-light.svg", typing("#1d5fd6", "#556070"))

# --------------------------------------------------------------------------- wave divider


def wave(c1, c2):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="40" viewBox="0 0 1280 40" preserveAspectRatio="none">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{c1}" stop-opacity="0"/><stop offset=".5" stop-color="{c1}"/><stop offset="1" stop-color="{c2}" stop-opacity="0"/></linearGradient></defs>
<path fill="none" stroke="url(#g)" stroke-width="2.5" d="M0 20 Q 80 0 160 20 T 320 20 T 480 20 T 640 20 T 800 20 T 960 20 T 1120 20 T 1280 20 T 1440 20 T 1600 20">
<animateTransform attributeName="transform" type="translate" from="0 0" to="-320 0" dur="6s" repeatCount="indefinite"/></path>
<path fill="none" stroke="url(#g)" stroke-width="1.5" opacity=".45" d="M0 20 Q 80 38 160 20 T 320 20 T 480 20 T 640 20 T 800 20 T 960 20 T 1120 20 T 1280 20 T 1440 20 T 1600 20">
<animateTransform attributeName="transform" type="translate" from="-320 0" to="0 0" dur="9s" repeatCount="indefinite"/></path>
</svg>'''


write("wave-dark.svg", wave("#22d3ee", "#1d5fd6"))
write("wave-light.svg", wave("#1d5fd6", "#22d3ee"))

# --------------------------------------------------------------------------- founder

photo = Image.open(f"{SITE}/public/imran.jpg").convert("RGB").resize((280, 280), Image.LANCZOS)
mask = Image.new("L", photo.size, 0)
ImageDraw.Draw(mask).ellipse((0, 0, 279, 279), fill=255)
round_photo = Image.new("RGBA", photo.size)
round_photo.paste(photo, (0, 0), mask)
buf = io.BytesIO()
round_photo.save(buf, "PNG", optimize=True)
photo64 = base64.b64encode(buf.getvalue()).decode()

write("founder.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200" viewBox="0 0 200 200">
<style>
  .spin{{transform-origin:100px 100px;animation:spin 8s linear infinite}} .spin2{{transform-origin:100px 100px;animation:spin 14s linear infinite reverse}}
  @keyframes spin{{to{{transform:rotate(360deg)}}}}
  .glow{{animation:glow 3s ease-in-out infinite}} @keyframes glow{{0%,100%{{opacity:.35}}50%{{opacity:.75}}}}
</style>
<defs>
  <linearGradient id="r" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22d3ee"/><stop offset=".5" stop-color="#1d5fd6"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></linearGradient>
  <radialGradient id="h"><stop offset=".6" stop-color="#22d3ee" stop-opacity=".5"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
</defs>
<circle class="glow" cx="100" cy="100" r="98" fill="url(#h)"/>
<circle class="spin" cx="100" cy="100" r="88" fill="none" stroke="url(#r)" stroke-width="5" stroke-linecap="round"/>
<circle class="spin2" cx="100" cy="100" r="94" fill="none" stroke="#22d3ee" stroke-width="1.5" stroke-dasharray="2 10" stroke-linecap="round" opacity=".7"/>
<image x="20" y="20" width="160" height="160" href="data:image/png;base64,{photo64}" xlink:href="data:image/png;base64,{photo64}"/>
<g transform="translate(146 146)"><circle r="16" fill="#0d1326" stroke="#22d3ee" stroke-width="2"/><text y="6" text-anchor="middle" font-size="16">🚀</text></g>
</svg>''')

# --------------------------------------------------------------------------- project illustrations

CARD = '''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="220" viewBox="0 0 600 220" font-family="{font}">
<style>{css}
@media (prefers-reduced-motion: reduce){{*{{animation:none!important}}}}</style>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient>
  <radialGradient id="glow"><stop offset="0" stop-color="{accent}" stop-opacity=".45"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
  <pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="1.2" cy="1.2" r="1.2" fill="#ffffff" opacity=".08"/></pattern>
  <clipPath id="cc"><rect width="600" height="220" rx="18"/></clipPath>
  {defs}
</defs>
<g clip-path="url(#cc)">
  <rect width="600" height="220" fill="url(#bg)"/><rect width="600" height="220" fill="url(#dots)"/>
  <circle cx="{gx}" cy="{gy}" r="190" fill="url(#glow)"><animate attributeName="r" values="170;205;170" dur="7s" repeatCount="indefinite"/></circle>
  {body}
  <rect x=".5" y=".5" width="599" height="219" rx="18" fill="none" stroke="#ffffff" stroke-opacity=".08"/>
</g>
<text x="32" y="186" font-size="34" font-weight="700" fill="#fff" letter-spacing="-.5">{title}</text>
<text x="33" y="206" font-size="13" fill="#ffffff" fill-opacity=".65">{tag}</text>
</svg>'''


def card(name, **kw):
    kw.setdefault("defs", "")
    write(f"project-{name}.svg", CARD.format(font=FONT, **kw))


# Veltoret: a cinema screen with posters sliding past and a pulsing play button.
posters = "".join(
    f'<rect x="{i * 86}" y="0" width="74" height="104" rx="8" fill="{c}"/>'
    f'<rect x="{i * 86 + 8}" y="80" width="40" height="6" rx="3" fill="#fff" opacity=".55"/>'
    for i, c in enumerate(["#f59e0b", "#7c3aed", "#ef4444", "#0ea5e9", "#10b981", "#f59e0b", "#7c3aed", "#ef4444",
                           "#0ea5e9", "#10b981"]))
card("veltoret", bg1="#1a1206", bg2="#2a1a05", accent="#f59e0b", gx=470, gy=60, title="Veltoret",
     tag="Your movies and shows, as a private cinema",
     css=".reel{animation:slide 14s linear infinite}@keyframes slide{to{transform:translateX(-430px)}}"
         ".play{transform-origin:438px 92px;animation:beat 2s ease-in-out infinite}@keyframes beat{0%,100%{transform:scale(1)}50%{transform:scale(1.12)}}"
         ".spot{animation:sweep 5s ease-in-out infinite;transform-origin:438px -40px}@keyframes sweep{0%,100%{transform:rotate(-12deg)}50%{transform:rotate(12deg)}}",
     defs='<linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fde68a" stop-opacity=".35"/><stop offset="1" stop-color="#fde68a" stop-opacity="0"/></linearGradient>'
          '<clipPath id="win"><rect x="300" y="26" width="276" height="132" rx="10"/></clipPath>',
     body=f'''<path class="spot" d="M438 -40 L380 170 L496 170 Z" fill="url(#beam)"/>
  <rect x="300" y="26" width="276" height="132" rx="10" fill="#0b0703" stroke="#f59e0b" stroke-opacity=".4" stroke-width="2"/>
  <g clip-path="url(#win)"><g transform="translate(312 40)" opacity=".85"><g class="reel">{posters}</g></g>
  <rect x="300" y="26" width="276" height="132" fill="#000" opacity=".35"/></g>
  <g class="play"><circle cx="438" cy="92" r="28" fill="#f59e0b"/><path d="M429 78l24 14-24 14z" fill="#1a1206"/></g>
  <g fill="#f59e0b" opacity=".9"><rect x="32" y="40" width="120" height="10" rx="5"/><rect x="32" y="60" width="200" height="8" rx="4" opacity=".4"/><rect x="32" y="76" width="170" height="8" rx="4" opacity=".4"/></g>
  <g transform="translate(32 102)"><rect width="210" height="6" rx="3" fill="#fff" opacity=".15"/><rect width="210" height="6" rx="3" fill="#f59e0b"><animate attributeName="width" values="0;210" dur="6s" repeatCount="indefinite"/></rect></g>''')

# PlexiChore: laptop streaming to a tablet over a cable with data dots flowing.
card("plexichore", bg1="#06121f", bg2="#0b2342", accent="#22d3ee", gx=430, gy=110, title="PlexiChore",
     tag="Any Android tablet as a monitor for Windows and Mac",
     css=".cur{animation:move 5s ease-in-out infinite}@keyframes move{0%,15%{transform:translate(0,0)}45%,60%{transform:translate(150px,-6px)}90%,100%{transform:translate(0,0)}}"
         ".tab{animation:bob 4s ease-in-out infinite}@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}",
     defs='<linearGradient id="s" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1d5fd6"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>'
          '<path id="cable" d="M402 140 C 430 175, 470 175, 486 140"/>',
     body='''<g transform="translate(270 40)">
    <rect width="150" height="96" rx="8" fill="#0d1a2e" stroke="#22d3ee" stroke-opacity=".5" stroke-width="2"/>
    <rect x="8" y="8" width="134" height="80" rx="4" fill="url(#s)" opacity=".85"/>
    <rect x="18" y="20" width="60" height="8" rx="4" fill="#fff" opacity=".85"/><rect x="18" y="36" width="100" height="6" rx="3" fill="#fff" opacity=".45"/><rect x="18" y="48" width="80" height="6" rx="3" fill="#fff" opacity=".45"/>
    <path d="M-14 96h178l-10 12H-4z" fill="#0d1a2e" stroke="#22d3ee" stroke-opacity=".5" stroke-width="2" stroke-linejoin="round"/>
  </g>
  <g class="tab"><g transform="translate(446 30)">
    <rect width="120" height="110" rx="12" fill="#0d1a2e" stroke="#22d3ee" stroke-opacity=".6" stroke-width="2"/>
    <rect x="8" y="8" width="104" height="94" rx="6" fill="url(#s)" opacity=".55"/>
    <rect x="18" y="20" width="84" height="8" rx="4" fill="#fff" opacity=".85"><animate attributeName="opacity" values=".2;.85;.85;.2" dur="5s" repeatCount="indefinite"/></rect>
    <rect x="18" y="36" width="60" height="6" rx="3" fill="#fff" opacity=".45"/>
  </g></g>
  <g class="cur"><path d="M300 60 l0 18 l5 -5 l4 9 l4 -2 l-4 -9 l7 0 z" fill="#fff" stroke="#06121f" stroke-width="1.5"/></g>
  <use href="#cable" fill="none" stroke="#22d3ee" stroke-opacity=".35" stroke-width="3" stroke-dasharray="2 6"/>
  <circle r="4" fill="#67e8f9"><animateMotion dur="1.6s" repeatCount="indefinite"><mpath href="#cable"/></animateMotion></circle>
  <circle r="4" fill="#67e8f9"><animateMotion dur="1.6s" begin=".8s" repeatCount="indefinite"><mpath href="#cable"/></animateMotion></circle>
  <g fill="#22d3ee"><rect x="32" y="40" width="130" height="10" rx="5"/><rect x="32" y="60" width="190" height="8" rx="4" opacity=".4"/><rect x="32" y="76" width="150" height="8" rx="4" opacity=".4"/></g>
  <g font-family="Consolas,monospace" font-size="12" fill="#67e8f9"><text x="32" y="114">60 fps · 3 ms<animate attributeName="opacity" values=".4;1;.4" dur="2s" repeatCount="indefinite"/></text></g>''')

# Thrennix: segmented multi-connection progress bars filling at different speeds.
bars = ""
for i, (w, d) in enumerate([(1.6, 0), (2.3, .3), (1.9, .6), (2.8, .2), (2.1, .5)]):
    y = 36 + i * 22
    bars += (f'<rect x="300" y="{y}" width="260" height="12" rx="6" fill="#ffffff" opacity=".08"/>'
             f'<rect x="300" y="{y}" width="0" height="12" rx="6" fill="url(#seg)"><animate attributeName="width" values="0;260;260" keyTimes="0;.8;1" dur="{w}s" begin="{d}s" repeatCount="indefinite"/></rect>')
card("thrennix", bg1="#1a0b06", bg2="#2b1208", accent="#f97316", gx=440, gy=100, title="Thrennix",
     tag="A very fast, simple download manager for Windows",
     css=".arr{animation:drop 1.4s ease-in infinite}@keyframes drop{0%{transform:translateY(-14px);opacity:0}30%{opacity:1}100%{transform:translateY(14px);opacity:0}}"
         ".line{animation:zip 1.2s linear infinite}@keyframes zip{from{transform:translateX(40px);opacity:0}50%{opacity:.8}to{transform:translateX(-60px);opacity:0}}",
     defs='<linearGradient id="seg" x1="0" x2="1"><stop offset="0" stop-color="#f97316"/><stop offset="1" stop-color="#fbbf24"/></linearGradient>',
     body=f'''{bars}
  <g transform="translate(200 60)"><circle cx="36" cy="36" r="34" fill="#f97316" opacity=".15"/><circle cx="36" cy="36" r="34" fill="none" stroke="#f97316" stroke-width="2" opacity=".6"/>
    <g class="arr"><path d="M36 18v30M24 38l12 12 12-12" fill="none" stroke="#fbbf24" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g></g>
  <g stroke="#fbbf24" stroke-width="2" stroke-linecap="round"><line class="line" x1="150" y1="70" x2="185" y2="70"/><line class="line" style="animation-delay:-.4s" x1="140" y1="96" x2="185" y2="96"/><line class="line" style="animation-delay:-.8s" x1="155" y1="122" x2="185" y2="122"/></g>
  <g fill="#f97316"><rect x="32" y="40" width="96" height="10" rx="5"/><rect x="32" y="60" width="110" height="8" rx="4" opacity=".4"/></g>
  <g font-family="Consolas,monospace" font-size="12" fill="#fbbf24"><text x="300" y="160">32 connections · 118 MB/s<animate attributeName="opacity" values=".5;1;.5" dur="1.5s" repeatCount="indefinite"/></text></g>''')

# Ek Chhoan: a phone with big, friendly tiles and a "one touch" ripple.
tiles = "".join(
    f'<rect x="{12 + (i % 2) * 52}" y="{62 + (i // 2) * 44}" width="44" height="36" rx="9" fill="{c}"/>'
    for i, c in enumerate(["#22c55e", "#3b82f6", "#f59e0b", "#ec4899"]))
card("ek-chhoan", bg1="#071a10", bg2="#0c2e1c", accent="#22c55e", gx=470, gy=110, title="Ek Chhoan",
     tag="A calm, elder-friendly Android home screen",
     css=".rip{transform-origin:370px 135px;animation:rip 2.2s ease-out infinite}.rip2{animation-delay:1.1s}"
         "@keyframes rip{from{transform:scale(.3);opacity:.9}to{transform:scale(2.4);opacity:0}}"
         ".heart{transform-origin:480px 70px;animation:beat 1.6s ease-in-out infinite}@keyframes beat{0%,100%{transform:scale(1)}15%{transform:scale(1.2)}30%{transform:scale(1)}}",
     body=f'''<g transform="translate(320 18)">
    <rect width="132" height="190" rx="20" fill="#0d2418" stroke="#22c55e" stroke-opacity=".5" stroke-width="2"/>
    <rect x="8" y="10" width="116" height="170" rx="14" fill="#f8fafc"/>
    <text x="66" y="40" text-anchor="middle" font-size="20" font-weight="700" fill="#0f172a">4:14</text>
    <text x="66" y="54" text-anchor="middle" font-size="8" fill="#556070">Good afternoon</text>
    {tiles}
  </g>
  <circle class="rip" cx="370" cy="135" r="14" fill="none" stroke="#22c55e" stroke-width="3"/>
  <circle class="rip rip2" cx="370" cy="135" r="14" fill="none" stroke="#22c55e" stroke-width="3"/>
  <g class="heart"><path d="M480 82 l-14 -14 a8 8 0 0 1 14 -10 a8 8 0 0 1 14 10 z" fill="#f43f5e"/></g>
  <g font-size="15" font-weight="700" fill="#86efac"><text x="482" y="130">এক ছোঁয়া</text><text x="482" y="152">एक छुअन</text></g>
  <g fill="#22c55e"><rect x="32" y="40" width="110" height="10" rx="5"/><rect x="32" y="60" width="170" height="8" rx="4" opacity=".4"/><rect x="32" y="76" width="140" height="8" rx="4" opacity=".4"/></g>
  <g font-family="Consolas,monospace" font-size="12" fill="#86efac"><text x="32" y="114">no internet · 100% private</text></g>''')

print("ok")
