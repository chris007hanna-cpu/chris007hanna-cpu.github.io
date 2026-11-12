import os
OUT = '/home/hatch/workspace/your_files/link-hub-github'
CSS = """*{margin:0;padding:0;box-sizing:border-box}
::selection{background:#d4af37;color:#111}
body{background:#090b09;color:#ece9e0;font-family:'Barlow',sans-serif;min-height:100vh;
background-image:radial-gradient(ellipse at 50% -10%,rgba(34,197,94,.14),transparent 60%),radial-gradient(ellipse at 85% 110%,rgba(212,175,55,.08),transparent 55%)}
.wrap{max-width:760px;margin:0 auto;padding:26px 20px 52px}
nav{display:flex;gap:7px;flex-wrap:wrap;justify-content:center;align-items:center;margin-bottom:26px}
nav a{color:#a3b5a4;text-decoration:none;font-family:'Oswald',sans-serif;font-size:.84rem;letter-spacing:.1em;padding:7px 13px;border:1px solid #2c352a;border-radius:999px;background:#10130f;text-transform:uppercase}
nav a:hover{border-color:#d4af37;color:#ffd95e}
h1{font-family:'Oswald',sans-serif;font-size:2.1rem;font-weight:600;letter-spacing:.04em;color:#fff;text-align:center}
.sub{text-align:center;color:#a3b5a4;font-size:1rem;margin:8px 0 22px}
.sub b{color:#d4af37}
.sec{display:flex;align-items:center;gap:12px;font-family:'Oswald',sans-serif;color:#8b9c8d;font-size:.8rem;letter-spacing:.28em;text-transform:uppercase;margin:28px 2px 6px}
.sec::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,#3a4536,transparent)}
.card{display:block;text-decoration:none;color:#ece9e0;background:linear-gradient(165deg,#151a13,#0f120e);border:1px solid #2c352a;border-radius:14px;padding:17px 19px;margin:12px 0;transition:transform .15s,border-color .15s}
a.card:hover{transform:translateY(-2px);border-color:#d4af37}
.card .t{font-family:'Oswald',sans-serif;font-size:1.16rem;font-weight:600;letter-spacing:.03em;color:#fff}
.card .s{color:#a3b5a4;font-size:.94rem;margin-top:4px;line-height:1.5}
.hero{border-color:#d4af37;background:linear-gradient(165deg,#1d2718,#12160f)}
.hero .t{color:#ffd95e}
.body{color:#cfd4c9;font-size:1rem;line-height:1.65;margin:10px 2px}
.body li{margin:6px 0 6px 18px}
.price{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.price .amt{font-family:'Oswald',sans-serif;color:#ffd95e;font-size:1.35rem;white-space:nowrap}
.buy{display:inline-block;margin:8px 3px 0;background:#d4af37;color:#111;font-weight:700;font-size:.9rem;padding:10px 16px;border-radius:9px;text-decoration:none}
.buy.ghost{background:transparent;color:#ffd95e;border:1px solid #d4af37}
.guide{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}
.guide div{background:#10130f;border:1px solid #2c352a;border-radius:10px;padding:10px 12px}
.guide b{font-family:'Oswald',sans-serif;color:#ffd95e;font-size:.85rem;letter-spacing:.08em}
.guide p{color:#a3b5a4;font-size:.88rem;line-height:1.45;margin-top:3px}
.foot{text-align:center;color:#7d8a7c;font-size:.85rem;margin-top:34px;line-height:1.6}
.foot a{color:#a3b5a4}"""

def page(fname, title, desc, h1, sub, body):
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://chris007hanna-cpu.github.io/{fname}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;600;700&family=Oswald:wght@500;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="wrap">
<nav><a href="holly-clark.html">Holly Clark</a><a href="holly-guide.html">Surf City Guide</a><a href="holly-pricing.html">Pricing</a><a href="index.html">Home</a></nav>
<h1>{h1}</h1>
<p class="sub">{sub}</p>
{body}
<p class="foot"><a href="holly-clark.html">Back to Holly Clark</a> · Huntington Beach, CA</p>
</div></body></html>"""
    open(os.path.join(OUT, fname), 'w').write(html)
    return fname

BOOK = """<div class="sec">Book Holly</div>
<div class="card hero"><span class="t">MESSAGE HOLLY TO BOOK</span>
<p class="s">Dates, locations, and details are set directly with Holly on Facebook or Instagram.</p></div>
<p style="text-align:center;margin-top:10px">
<a class="buy" href="https://www.facebook.com/profile.php?id=502384225">Holly on Facebook</a>
<a class="buy ghost" href="https://www.instagram.com/orangecounty_girl/">Instagram @orangecounty_girl</a></p>"""

files = []

# ---------- GUIDE ----------
guide_body = """<div class="card hero"><span class="t">HER FAVORITE SPOTS AROUND SURF CITY</span>
<p class="s">Designed and written by Holly Clark. Local spots, good vibes, Surf City USA.</p>
<div class="guide">
<div><b>COFFEE</b><p>602 Coffee House, Blackbird Coffee, Whipped, Starbucks</p></div>
<div><b>BRUNCH</b><p>Jolie, Mama's 39, Bandoleras Café, Pacific Hideaway</p></div>
<div><b>LUNCH</b><p>Focaccia House, Morena's, Prime Cut</p></div>
<div><b>DINNER</b><p>Solita, Sandbar, BLK, Black Trumpet, Degrees</p></div>
<div><b>DAYTIME DRINKS</b><p>The Irishman, Harbour Rackhouse, Driftwood, Johnny's Saloon</p></div>
<div><b>DAYTIME</b><p>Walk through Central Park, the Huntington Beach Pier, people watching on Main Street</p></div>
<div><b>NIGHT</b><p>Movies at Cinemark, concerts, Old World Village, drinks at 2nd Floor, the Lighthouse, Huntington Rooftop Lounge</p></div>
<div><b>STILL ON HER LIST</b><p>Bollini's, Champagne's Kitchen</p></div>
</div></div>
<div class="sec">About the guide</div>
<p class="body">Holly built this guide the way she shoots: by living here. Every spot on it is a place she actually goes, from morning coffee runs to rooftop nights. She designed the original graphic herself in August 2026, and the list keeps growing as she finds new favorites.</p>
<p class="body">Want a guide like this for your business or your town? Holly designs custom local guides too. See the Custom Local Guides service and the guide package on the pricing page.</p>
""" + BOOK
files.append(page('holly-guide.html', "Holly's Guide to Surf City | Holly Clark Photography",
  "Holly Clark's own guide to Huntington Beach: her favorite coffee, brunch, lunch, dinner, drinks, and day and night spots around Surf City USA. Updated often.",
  "HOLLY'S GUIDE TO SURF CITY", "Her favorite spots around <b>Surf City, USA</b>", guide_body))

# ---------- WORK PAGES ----------
def work(fname, name, desc, sub, paragraphs, details):
    lis = ''.join(f"<li>{d}</li>" for d in details)
    body = ''.join(f'<p class="body">{p}</p>' for p in paragraphs)
    body += f'<div class="sec">The details</div><ul class="body">{lis}</ul>' + BOOK
    return page(fname, f"{name} | Holly Clark Photography", desc, name.upper(), sub, body)

files.append(work('holly-work-palm-springs.html', 'Palm Springs Weekend',
  "Holly Clark's Palm Springs weekend photo series from June 2026: desert light, palms, and mid century streets, shot by a Huntington Beach photographer.",
  "Desert light and weekend color, <b>June 2026</b>",
  ["A weekend out of Surf City and into the desert. Holly shot Palm Springs the way she shoots home: honest light, real color, and the small moments between the postcard shots.",
   "Palms against hard blue sky, mid century lines, pool light, and street scenes from a town that runs on sun. It is the same eye she brings to the coast, pointed inland for a weekend."],
  ["Shot on location in Palm Springs, California", "Series date: June 2026", "Style: natural light, travel and lifestyle", "Prints and licensing: message Holly"]))

files.append(work('holly-work-ventura.html', 'Ventura Pier and Beach Series',
  "Holly Clark's Ventura pier and beach photo series from June 2025: a cold, quiet night on the Ventura coast, pier lights and empty sand. Shot after dark.",
  "A cold, quiet night on the <b>Ventura coast</b>, June 2025",
  ["Ventura on a cold night is a different beach than the one in the brochures. Holly stayed out for it: the pier lit up over dark water, empty sand, and that lonely beach mood she says she likes.",
   "This series is her night work at its best. Long looks, low light, and the coast the way it actually feels after the crowds go home."],
  ["Shot on location at the Ventura Pier and beach", "Series date: June 2025", "Style: night, low light, coastal mood", "Prints and licensing: message Holly"]))

files.append(work('holly-work-promenade.html', 'Third Street Promenade: Food and Street',
  "Holly Clark's street and food photography from Barney's Beanery on the Third Street Promenade in Santa Monica, including her Jalapeño Juicy Lucy shot.",
  "Santa Monica street and food, shot at <b>Barney's Beanery</b>",
  ["Street level in Santa Monica. Holly shot the Third Street Promenade around Barney's Beanery, food first: the Jalapeño Juicy Lucy, cheese pull and all, then the street life moving past the table.",
   "Food photography is where her local knowledge pays off twice. She knows the spots, the light at each table, and the exact second a dish looks its best."],
  ["Shot on location, Third Street Promenade, Santa Monica", "Featured dish: Jalapeño Juicy Lucy at Barney's Beanery", "Style: food, street, lifestyle", "Restaurant and brand shoots: see Local Business Content"]))

files.append(work('holly-work-surf-city-people.html', 'Surf City People',
  "Holly Clark's Surf City People series: the faces of Huntington Beach, shot out in the wild by a hometown photographer who knows everybody. More faces coming.",
  "The faces of <b>Huntington Beach</b>",
  ["Holly does not have to go looking for people in Surf City. They find her, at coffee, at the pier, at every local spot in her guide, and her camera is always ready.",
   "Surf City People is her hometown portrait eye at work: friends, regulars, and run ins, shot warm and real, never stiff. This is the series that turns into portrait bookings."],
  ["Shot on location around Huntington Beach", "Style: candid portraits, lifestyle", "Book the same look: see Portraits and Lifestyle", "Prints and licensing: message Holly"]))

# ---------- SERVICE PAGES ----------
def service(fname, name, desc, sub, paragraphs, includes, price_line):
    lis = ''.join(f"<li>{d}</li>" for d in includes)
    body = ''.join(f'<p class="body">{p}</p>' for p in paragraphs)
    body += f'<div class="sec">What is included</div><ul class="body">{lis}</ul>'
    body += f'<div class="sec">Pricing</div><p class="body">{price_line}</p>' + BOOK
    return page(fname, f"{name} | Holly Clark Photography, Huntington Beach", desc, name.upper(), sub, body)

files.append(service('holly-service-portraits.html', 'Portraits and Lifestyle',
  "Portrait and lifestyle photography in Huntington Beach with Holly Clark: natural light sessions on the Orange County coast, mini and full sessions. Book today.",
  "Natural light portraits on the <b>Orange County coast</b>",
  ["Portraits that look like you on your best beach day. Holly shoots natural light portraits and lifestyle sessions at the pier, Central Park, Main Street, and the quiet stretches of sand she knows by heart.",
   "No stiff studio energy. She keeps it moving, keeps it fun, and delivers edited photos you will actually post and print."],
  ["Pre shoot planning on locations, outfits, and timing", "Golden hour scheduling for the best coastal light", "Posed and candid mix, directed the whole way", "Edited, high resolution photos delivered digitally", "Print and sharing rights for personal use"],
  'Mini Session $125 for 30 minutes and 10 edited photos. Full Session $225 for one hour and 25 edited photos. Full details on the <a href="holly-pricing.html" style="color:#ffd95e">pricing page</a>.'))

files.append(service('holly-service-events.html', 'Events and Local Scenes',
  "Event photography in Huntington Beach with Holly Clark: parties, gatherings, and local happenings covered at $150 per hour with fast delivery. Book your date.",
  "Parties and gatherings, covered by a <b>local</b>",
  ["Birthdays, reunions, shop nights, and local happenings. Holly covers events the way a guest with a great camera would, except she never misses the shot and she delivers fast.",
   "She knows the venues, the light, and half the guest list. You get the night back in photos before the buzz wears off."],
  ["Coverage of arrivals, candids, groups, and details", "All the best shots edited, not just a handful", "Fast digital delivery after the event", "Two hour minimum, then hourly", "Travel around Huntington Beach included"],
  'Events run $150 per hour with a two hour minimum. Full details on the <a href="holly-pricing.html" style="color:#ffd95e">pricing page</a>.'))

files.append(service('holly-service-business.html', 'Local Business Content',
  "Content photography for Huntington Beach businesses with Holly Clark: food, storefront, and social content from a photographer who knows every spot in town.",
  "Food, storefront, and social content for <b>local business</b>",
  ["Your customers scroll past stock photos. They stop for the real thing: your food, your storefront, your people, shot by someone who already knows your regulars by name.",
   "Holly builds a half day shoot around your business and delivers edited photos plus ready to post social graphics, so your feeds look alive for weeks from one session."],
  ["Half day shoot at your location", "20 edited photos: food, storefront, team, and details", "5 ready to post social graphics sized for Instagram and Facebook", "Shot list planned with you before the day", "Commercial use rights for your own channels included"],
  'Local Business Content is $299 flat. Full details on the <a href="holly-pricing.html" style="color:#ffd95e">pricing page</a>.'))

files.append(service('holly-service-guides.html', 'Custom Local Guides and Graphics',
  "Custom local guide design by Holly Clark: designed city and business guide graphics in the style of Holly's Guide to Surf City, $149 per guide. Book yours now.",
  "Designed guides in the style of <b>Holly's Guide to Surf City</b>",
  ["Her Surf City guide started as something she made for fun, and local businesses keep asking for one of their own. Now it is a service: a designed guide graphic for your town, your shop, or your event.",
   "You pick the spots and the facts. Holly designs it in her clean, bold style and delivers files ready for social, print, and your window."],
  ["Design in the style of Holly's Guide to Surf City", "Your spots, your categories, your branding colors", "Files for Instagram, Facebook, and print", "One round of text corrections included", "Delivered digitally, ready to post"],
  'Custom Local Guide is $149 per guide. Full details on the <a href="holly-pricing.html" style="color:#ffd95e">pricing page</a>.'))

# ---------- PRICING ----------
PKGS = [
 ('holly-price-mini.html','MINI SESSION','$125','30 minutes, one location, 10 edited photos',
  ["30 minute shoot at one Huntington Beach location","10 edited, high resolution photos","Golden hour or morning light scheduling","Digital delivery, personal print and sharing rights","Best for: fresh profile photos, quick family shots, solo portraits"]),
 ('holly-price-full.html','FULL SESSION','$225','One hour, up to two locations, 25 edited photos',
  ["One hour shoot at up to two locations","25 edited, high resolution photos","Outfit change welcome between locations","Posed and candid mix, fully directed","Digital delivery, personal print and sharing rights","Best for: couples, lifestyle portraits, senior photos"]),
 ('holly-price-groups.html','COUPLES AND GROUPS','$275','One hour, 30 edited photos, beach sessions for groups',
  ["One hour shoot for couples, families, and friend groups","30 edited, high resolution photos","Group and individual shots included","Beach, pier, or Central Park locations","Digital delivery, personal print and sharing rights","Best for: family beach photos and group memories"]),
 ('holly-price-events.html','EVENTS','$150 per hour','Two hour minimum, all the best shots edited',
  ["Event coverage at $150 per hour, two hour minimum","Arrivals, candids, groups, and detail shots","All the best shots edited","Fast digital delivery after the event","Huntington Beach travel included","Best for: birthdays, reunions, shop and venue nights"]),
 ('holly-price-business.html','LOCAL BUSINESS CONTENT','$299','Half day shoot, 20 edited photos, 5 social graphics',
  ["Half day shoot at your business","20 edited photos: food, storefront, team, details","5 ready to post social graphics","Shot list planned with you in advance","Commercial use rights for your own channels","Best for: restaurants, cafes, and local shops"]),
 ('holly-price-guide.html','CUSTOM LOCAL GUIDE','$149','Your own designed guide graphic, print and social files',
  ["Designed guide in the style of Holly's Guide to Surf City","Your spots, categories, and branding colors","Files sized for Instagram, Facebook, and print","One round of text corrections","Digital delivery, ready to post","Best for: businesses, events, and hometown pride"]),
]
price_cards = ''
for fname, name, amt, line, _ in PKGS:
    price_cards += f'<a class="card" href="{fname}"><div class="price"><span class="t">{name}</span><span class="amt">{amt}</span></div><p class="s">{line}. Tap for the full breakdown.</p></a>'
pricing_body = price_cards + '<p class="body">Every package can be adjusted. Message Holly for dates, details, and custom quotes.</p>' + BOOK
files.append(page('holly-pricing.html', 'Pricing | Holly Clark Photography, Huntington Beach',
  "Holly Clark photography pricing for Huntington Beach: mini $125, full $225, groups $275, events $150 per hour, business $299, guides $149. Packages below.",
  'PRICING', 'Real numbers, <b>no guessing</b>. Tap any package for the full breakdown.', pricing_body))

def _price_desc(name, line):
    n = name.lower()
    mid = f"Holly Clark {n} in Huntington Beach: {line}. What is included, how booking works, and how to reserve your date."
    short = f"Holly Clark {n} package: {line}. What is included, how booking works, and how to reserve your date."
    for d in (mid, short, mid.replace("reserve your date", "reserve a date"), short.replace("reserve your date", "reserve a date")):
        if 150 <= len(d) <= 160:
            return d
    return mid

for fname, name, amt, line, includes in PKGS:
    lis = ''.join(f"<li>{d}</li>" for d in includes)
    body = f'<div class="card hero"><div class="price"><span class="t">{name}</span><span class="amt">{amt}</span></div><p class="s">{line}.</p></div>'
    body += f'<div class="sec">What you get</div><ul class="body">{lis}</ul>'
    body += '<div class="sec">How it works</div><p class="body">Message Holly on Facebook or Instagram with your date and what you are dreaming up. She confirms the plan and the price in writing before anything is booked. A small deposit holds your date, and the balance is due on the day of the shoot. Edited photos are delivered digitally.</p>' + BOOK
    files.append(page(fname, f"{name} {amt} | Holly Clark Photography",
      _price_desc(name, line),
      name, f'<b>{amt}</b> · {line}', body))

print('built', len(files), 'pages')
for f in files: print(' ', f)
