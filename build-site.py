from PIL import Image
import base64, io, os, re

def b64img(path, w, q=80):
    im = Image.open(path).convert('RGB')
    im.thumbnail((w, w*3))
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=q)
    return base64.b64encode(buf.getvalue()).decode()

def fileimg(path, w, out, q=80):
    # M22: same resize/quality as b64img, but written to a file under assets/
    # instead of embedded as base64. Returns the site-relative path.
    im = Image.open(path).convert('RGB')
    im.thumbnail((w, w*3))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out, 'JPEG', quality=q)
    return out

def clean_title(t):
    # Demote emojis out of card/program titles: strip a leading run of emoji
    # entities / pictographs (keeps leading digits, e.g. numbered steps).
    return re.sub(r'^(\s|&#[0-9]+;|[\U0001F000-\U0001FAFF\U0001D400-\U0001D7FF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u20E3])+', '', t).strip()

B = '/home/hatch/workspace/your_files/empire/books/'
books = [
 ("phone-flip-playbook/cover/cover-front-2000x3000.jpg","The Phone Flip Playbook","live",
  [("Kindle $2.99","https://www.amazon.com/dp/B0HMK8F68P/?tag=hannaenterpri-20"),("Paperback $9.99","https://www.amazon.com/dp/B0HMPK373Y/?tag=hannaenterpri-20"),("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=The%20Phone%20Flip%20Playbook%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("ai-coding-agents-2026/cover/cover-front-2000x3000.jpg","AI Coding Agents 2026","live",
  [("Kindle $3.99","https://www.amazon.com/dp/B0HMMDHNJD/?tag=hannaenterpri-20"),("Paperback $9.99","https://www.amazon.com/dp/B0HMN3GPNW/?tag=hannaenterpri-20"),("Buy direct $3.99","shop.html#direct"),("Google Play $3.99","https://play.google.com/store/search?q=AI%20Coding%20Agents%202026%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("embracing-the-unknown/cover-front-2000x3000.jpg","Embracing the Unknown","live",
  [("Kindle $2.99","https://www.amazon.com/dp/B0HMMNQ3ZF/?tag=hannaenterpri-20"),("Paperback $9.99","https://www.amazon.com/dp/B0HMMHLKGV/?tag=hannaenterpri-20"),("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Embracing%20the%20Unknown%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("dad-jokes/cover-front-2000x3000.jpg","Dad Jokes","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Dad%20Jokes%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("digital-product-empire/cover-front-2000x3000.jpg","Digital Product Empire","direct",
  [("Buy direct $4.99","shop.html#direct"),("Google Play $4.99","https://play.google.com/store/search?q=Digital%20Product%20Empire%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("faceless-fortune/cover-front-2000x3000.jpg","Faceless Fortune","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Faceless%20Fortune%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("fiverr-fast-start/cover-front-2000x3000.jpg","Fiverr Fast Start","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Fiverr%20Fast%20Start%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("free-money-handbook/cover-front-2000x3000.jpg","Free Money Handbook","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Free%20Money%20Handbook%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("instant-ramen-chef/cover-front-2000x3000.jpg","Instant Ramen Chef","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Instant%20Ramen%20Chef%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("laugh-attack/cover-front-2000x3000.jpg","Laugh Attack","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Laugh%20Attack%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("marketplace-millions/cover-front-2000x3000.jpg","Marketplace Millions","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Marketplace%20Millions%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("mojo-programming/cover/cover-front-2000x3000.jpg","Mojo 1.0","direct",
  [("Buy direct $3.99","shop.html#direct"),("Google Play $3.99","https://play.google.com/store/search?q=Mojo%201.0%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("phone-repair-mastery/cover-front-2000x3000.jpg","Phone Repair Mastery","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Phone%20Repair%20Mastery%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("side-hustle-stack/cover-front-2000x3000.jpg","Side Hustle Stack","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Side%20Hustle%20Stack%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("solid-state-ev-guide/cover/cover-front-2000x3000.jpg","Solid-State EV Buyer's Guide","direct",
  [("Buy direct $3.99","shop.html#direct"),("Google Play $3.99","https://play.google.com/store/search?q=Solid-State%20EV%20Buyer%27s%20Guide%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("street-survival-guide/cover-2000x3000.jpg","Surviving on the Street","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=Surviving%20on%20the%20Street%20Christopher%20J.%20Hanna&amp;c=books")]),
 ("zero-dollar-startup/cover-front-2000x3000.jpg","The $0 Startup","direct",
  [("Buy direct $2.99","shop.html#direct"),("Google Play $2.99","https://play.google.com/store/search?q=The%20%240%20Startup%20Christopher%20J.%20Hanna&amp;c=books")]),
]

CSS = '''*{margin:0;padding:0;box-sizing:border-box}
::selection{background:#d4af37;color:#111}
body{background:#090b09;color:#ece9e0;font-family:'Barlow',sans-serif;min-height:100vh;
background-image:radial-gradient(ellipse at 50% -10%,rgba(34,197,94,.14),transparent 60%),radial-gradient(ellipse at 85% 110%,rgba(212,175,55,.08),transparent 55%);}
.wrap{max-width:760px;margin:0 auto;padding:26px 20px 52px}
nav{display:flex;gap:7px;flex-wrap:wrap;justify-content:center;align-items:center;margin-bottom:26px}
nav a{color:#a3b5a4;text-decoration:none;font-family:'Oswald',sans-serif;font-size:.84rem;letter-spacing:.1em;
padding:7px 13px;border:1px solid #2c352a;border-radius:999px;background:#10130f;text-transform:uppercase;white-space:nowrap}
nav a:hover{border-color:#d4af37;color:#ffd95e}
nav a.on{color:#ffd95e;border-color:#d4af37;background:#171c12}
a:focus-visible{outline:2px solid #ffd95e;outline-offset:2px}
.ngrp{position:relative;display:inline-flex}
.ngrp>a::after{content:"▾";margin-left:6px;color:#d4af37;font-size:.7rem}
.drop{position:absolute;top:calc(100% + 7px);left:50%;transform:translate(-50%,5px);min-width:218px;background:#0f120e;border:1px solid #37402f;border-radius:13px;padding:6px;opacity:0;visibility:hidden;transition:opacity .15s,transform .15s,visibility .15s;z-index:60;box-shadow:0 20px 44px rgba(0,0,0,.6)}
.ngrp:hover .drop,.ngrp:focus-within .drop{opacity:1;visibility:visible;transform:translate(-50%,0)}
.drop a{display:block;border:0;border-radius:8px;background:transparent;padding:8px 11px;font-size:.8rem;white-space:normal}
.drop a:hover,.drop a.on{background:#171c12}
header{text-align:center;margin-bottom:26px;padding-bottom:22px;border-bottom:1px solid #232a20}
header img{width:108px;height:108px;border-radius:50%;border:3px solid #d4af37;box-shadow:0 0 34px rgba(212,175,55,.32);object-fit:cover}
h1{font-family:'Oswald',sans-serif;font-size:2.35rem;font-weight:600;letter-spacing:.05em;margin-top:14px;color:#fff}
.tag{color:#a3b5a4;font-size:1.02rem;margin-top:5px}
.tag b{color:#d4af37}
.card{display:block;text-decoration:none;color:#ece9e0;background:linear-gradient(165deg,#151a13,#0f120e);
border:1px solid #2c352a;border-radius:14px;padding:17px 19px;margin:12px 0;transition:transform .15s,border-color .15s,box-shadow .15s}
.card:hover{transform:translateY(-2px);border-color:#d4af37;box-shadow:0 10px 30px rgba(0,0,0,.55)}
.card .t{font-family:'Oswald',sans-serif;font-size:1.16rem;font-weight:600;letter-spacing:.03em;color:#fff}
.card .s{color:#a3b5a4;font-size:.94rem;margin-top:4px;line-height:1.5}
.hero{border-color:#d4af37;background:linear-gradient(165deg,#1d2718,#12160f)}
.hero .t{color:#ffd95e}
.topbtns{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 8px}
.topcol{flex:1 1 240px;display:flex;flex-direction:column}
.topbtn{display:block;text-align:center;text-decoration:none;font-family:'Oswald',sans-serif;font-weight:700;font-size:1.02rem;letter-spacing:.05em;text-transform:uppercase;padding:15px 12px;border-radius:12px;border:1px solid #d4af37;color:#ffd95e;background:linear-gradient(165deg,#1d2718,#12160f);transition:transform .15s,box-shadow .15s}
.topbtn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(0,0,0,.55)}
.topbtn.gold{background:#d4af37;color:#111}
.topbtn.gold:hover{background:#ffd95e}
.affdisc{color:#8b9c8d;font-size:.8rem;text-align:center;margin-top:6px;line-height:1.4}
.appcard{display:flex;gap:14px;align-items:center}
.appcard img{width:56px;height:56px;border-radius:14px;flex:none;box-shadow:0 4px 14px rgba(0,0,0,.5)}
.freetag{display:inline-block;background:#d4af37;color:#111;font-family:'Oswald',sans-serif;font-size:.66rem;font-weight:700;letter-spacing:.1em;padding:2px 8px;border-radius:999px;margin-left:9px;vertical-align:middle;text-transform:uppercase}
.vidfac{position:relative;display:block;width:100%;aspect-ratio:16/9;border-radius:10px;overflow:hidden;border:1px solid #37402f;background:#000;cursor:pointer;margin-top:10px}
.vidfac img{width:100%;height:100%;object-fit:cover;display:block}
.vidfac .vplay{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:64px;height:64px;border-radius:50%;background:rgba(212,175,55,.92);color:#111;font-size:1.55rem;line-height:64px;text-align:center;box-shadow:0 8px 24px rgba(0,0,0,.6)}
.vidfac:hover .vplay{background:#ffd95e}
.vidfac iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.vidnote{color:#8b9c8d;font-size:.8rem;margin-top:6px}
.vidfac.nothumb{background:linear-gradient(165deg,#1a2115,#0b0f0b)}
.vidfac .vlabel{position:absolute;left:0;right:0;bottom:12px;text-align:center;color:#a3b5a4;font-family:'Oswald',sans-serif;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase}
.sec{display:flex;align-items:center;gap:12px;font-family:'Oswald',sans-serif;color:#8b9c8d;font-size:.8rem;letter-spacing:.28em;text-transform:uppercase;margin:28px 2px 6px}
.sec::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,#3a4536,transparent)}
.row{display:flex;gap:10px;flex-wrap:wrap}
.row .card{flex:1 1 30%;text-align:center;padding:13px 6px;margin:6px 0}
.row .card .t{font-size:.97rem}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px}
.book{background:linear-gradient(165deg,#151a13,#0f120e);border:1px solid #2c352a;border-radius:14px;padding:12px;text-align:center}
.book img{width:100%;max-width:170px;height:auto;border-radius:8px;box-shadow:0 6px 18px rgba(0,0,0,.55)}
.book .bt{font-family:'Oswald',sans-serif;color:#fff;font-size:1rem;margin-top:10px;line-height:1.25}
.badge{display:inline-block;margin-top:8px;font-size:.8rem;color:#a3b5a4;border:1px solid #2c352a;padding:4px 10px;border-radius:999px}
.buy{display:inline-block;margin:8px 3px 0;background:#d4af37;color:#111;font-weight:700;font-size:.86rem;letter-spacing:.02em;
padding:8px 13px;border-radius:9px;text-decoration:none}
.buy:hover{background:#ffd95e}
.tiers{display:flex;gap:10px;margin-top:14px}
.tier{flex:1;background:#0b0f0b;border:1px solid #2c352a;border-radius:10px;text-align:center;padding:9px 4px}
.tn{font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:#8b9c8d}
.tp{font-family:'Oswald',sans-serif;font-size:1.15rem;color:#ffd95e;margin-top:2px}
.cta{margin-top:13px;font-weight:700;color:#d4af37;font-size:.95rem}
.note{color:#a3b5a4;font-size:.95rem;margin:20px 6px;line-height:1.55}
.proof{display:flex;gap:10px;flex-wrap:wrap;margin:16px 0 4px}
.pf{flex:1 1 21%;min-width:128px;background:linear-gradient(165deg,#151a13,#0f120e);border:1px solid #2c352a;border-top:2px solid #d4af37;border-radius:12px;padding:13px 8px 11px;text-align:center}
.pf .n{font-family:'Oswald',sans-serif;font-size:1.35rem;font-weight:600;color:#ffd95e;line-height:1.1}
.pf .l{font-size:.72rem;letter-spacing:.07em;text-transform:uppercase;color:#a3b5a4;margin-top:4px;line-height:1.45}
footer{text-align:center;color:#5f7263;font-size:.85rem;margin-top:36px;line-height:1.5}
footer a{color:#d4af37;text-decoration:none}
.fmap{font-size:.8rem;line-height:2.05;margin-bottom:18px}
.fmap a{color:#8fa392}
.fmap a:hover{color:#ffd95e}
details.pv{margin-top:10px;text-align:left}
details.pv summary{cursor:pointer;list-style:none;font-family:'Oswald',sans-serif;font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:#ffd95e;border:1px solid #37402f;border-radius:8px;padding:7px 10px;background:#0b0f0b;text-align:center}
details.pv summary::-webkit-details-marker{display:none}
details.pv summary:hover{border-color:#d4af37}
.flip{margin-top:9px}
.fp{display:none;width:100%;height:auto;border-radius:6px;box-shadow:0 4px 14px rgba(0,0,0,.5)}
.fp.on{display:block}
.ftext{display:none;background:linear-gradient(165deg,#1a2115,#10130e);border:1px solid #37402f;padding:14px 13px;color:#dfe4d8;font-size:.88rem;line-height:1.6;text-align:left}
.ftext.on{display:block}
.ftext .fb-t{font-family:'Oswald',sans-serif;color:#ffd95e;font-size:1rem;letter-spacing:.03em;margin-bottom:7px}
.fctl{display:flex;align-items:center;justify-content:space-between;margin-top:8px}
.fbtn{background:#0b0f0b;border:1px solid #37402f;color:#ffd95e;font-family:'Oswald',sans-serif;font-size:.78rem;letter-spacing:.08em;padding:6px 12px;border-radius:8px;cursor:pointer}
.fbtn:hover{border-color:#d4af37}
.fcount{color:#8b9c8d;font-size:.8rem;font-family:'Oswald',sans-serif;letter-spacing:.1em}
.lookbtn{display:block;margin-top:10px;font-family:'Oswald',sans-serif;font-size:.82rem;letter-spacing:.08em;text-transform:uppercase;color:#ffd95e;border:1px solid #37402f;border-radius:8px;padding:9px 10px;background:#0b0f0b;text-align:center;text-decoration:none}
.lookbtn:hover{border-color:#d4af37}
a.pvlink{text-decoration:none;color:inherit}
.bt a.pvlink{color:inherit}
@media(min-width:720px){.grid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:560px){h1{font-size:1.85rem}.pf{flex:1 1 42%}.drop{min-width:188px}}
.card>a.clink{display:block;text-decoration:none;color:inherit}
details.wyg{margin-top:12px;border-top:1px solid #2c352a;padding-top:11px}
details.wyg summary{cursor:pointer;list-style:none;display:inline-block;font-family:'Oswald',sans-serif;font-size:.82rem;letter-spacing:.1em;text-transform:uppercase;color:#ffd95e;border:1px solid #37402f;border-radius:8px;padding:8px 14px;background:#0b0f0b}
details.wyg summary::-webkit-details-marker{display:none}
details.wyg summary:hover{border-color:#d4af37}
details.wyg summary:focus-visible{outline:2px solid #ffd95e;outline-offset:2px}
.wygb{margin-top:12px;background:#0b0f0b;border:1px solid #2c352a;border-radius:10px;padding:14px 16px;color:#cfe0cd;font-size:.92rem;line-height:1.55}
.wygb h4{font-family:'Oswald',sans-serif;color:#ffd95e;font-size:.86rem;letter-spacing:.12em;text-transform:uppercase;margin:13px 0 5px}
.wygb h4:first-child{margin-top:2px}
.wygb .wp{font-family:'Oswald',sans-serif;color:#ffd95e;font-size:1.02rem;letter-spacing:.02em}
.wygb ul,.wygb ol{margin:0 0 4px 19px}
.wygb li{margin-bottom:3px}
.wygb p{margin-bottom:4px}
.card .t{position:relative;z-index:2}
.card .t a{color:#ffd95e;text-decoration:underline;text-underline-offset:3px;text-decoration-color:rgba(212,175,55,.55);position:relative;z-index:2}
.card .t a:hover{color:#ffe98a;text-decoration-color:#ffd95e}
a.lk{color:#ffd95e;text-decoration:underline;text-underline-offset:2px;text-decoration-color:rgba(212,175,55,.5)}
a.lk:hover{color:#ffe98a;text-decoration-color:#ffd95e}
.visitbtn{display:block;margin-top:11px;text-align:center;font-family:'Oswald',sans-serif;font-size:.86rem;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:#ffd95e;text-decoration:none;border:1px solid #d4af37;border-radius:9px;padding:10px 12px;background:linear-gradient(165deg,#1d2718,#12160f)}
.visitbtn:hover{background:#d4af37;color:#111}
.bkcard{display:block;text-decoration:none;color:#ece9e0;background:linear-gradient(165deg,#151a13,#0f120e);border:1px solid #2c352a;border-radius:14px;padding:14px 12px 13px;text-align:center;transition:transform .15s,border-color .15s,box-shadow .15s}
.bkcard:hover{transform:translateY(-2px);border-color:#d4af37;box-shadow:0 10px 30px rgba(0,0,0,.55)}
.bkcard img{width:100%;max-width:170px;height:auto;border-radius:8px;box-shadow:0 6px 18px rgba(0,0,0,.55)}
.bkcard .bt{font-family:'Oswald',sans-serif;color:#fff;font-size:1rem;margin-top:10px;line-height:1.25}
.bkline{color:#a3b5a4;font-size:.86rem;margin-top:5px;line-height:1.5}
.bkline b{color:#ffd95e;font-weight:600}
.bkview{display:inline-block;margin-top:11px;font-family:'Oswald',sans-serif;font-size:.8rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#ffd95e;border:1px solid #37402f;border-radius:8px;padding:7px 14px;background:#0b0f0b}
.bkcard:hover .bkview{border-color:#d4af37;background:#d4af37;color:#111}
.bkhero{display:flex;gap:20px;flex-wrap:wrap;align-items:flex-start;margin-top:4px}
.bkhero .cov{flex:0 0 216px;max-width:62vw}
.bkhero .cov img{width:100%;height:auto;border-radius:10px;box-shadow:0 10px 30px rgba(0,0,0,.6);border:1px solid #2c352a;display:block}
.bkhero .cov a.pvlink{display:block}
.bkinfo{flex:1 1 280px;min-width:250px}
.bkinfo .bkline{font-size:.95rem}
.bksec{display:flex;align-items:center;gap:12px;font-family:'Oswald',sans-serif;color:#8b9c8d;font-size:.8rem;letter-spacing:.28em;text-transform:uppercase;margin:28px 2px 10px}
.bksec::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,#3a4536,transparent)}
.bkabout p{color:#dfe4d8;font-size:.97rem;line-height:1.62;margin-bottom:9px}
.bookstack{background:linear-gradient(165deg,#151a13,#0f120e);border:1px solid #2c352a;border-radius:14px;padding:16px;text-align:left}
.bookstack .bt{font-family:'Oswald',sans-serif;color:#fff;font-size:1.05rem;line-height:1.3}
.buystack{display:flex;flex-direction:column;gap:9px;margin-top:12px}
.buystack .buy{margin:0;display:flex;justify-content:space-between;align-items:center;gap:10px;padding:12px 15px;font-size:.95rem;border-radius:10px}
.buy.alt{background:transparent;color:#ffd95e;border:1px solid #d4af37}
.buy.alt:hover{background:#1d2718}
.buy .bprice{font-family:'Oswald',sans-serif;letter-spacing:.03em;white-space:nowrap}
.bknote{color:#8b9c8d;font-size:.84rem;line-height:1.5;margin-top:12px}
.fgrow{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:12px 15px;font-size:.95rem;border:1px solid #2c352a;border-radius:10px;color:#a3b5a4;background:#0b0f0b}
.bkabout ul{margin:2px 0 10px 20px;line-height:1.65;color:#dfe4d8;font-size:.97rem}
.bkabout li{margin-bottom:3px}'''

VID_JS = '''<script>
document.addEventListener('click',function(e){
if(e.target.closest('a'))return;
var f=e.target.closest('.vidfac');
if(!f||f.dataset.on)return;
f.dataset.on='1';
var src=f.dataset.list?('https://www.youtube-nocookie.com/embed/videoseries?list='+f.dataset.list+'&autoplay=1'):('https://www.youtube-nocookie.com/embed/'+f.dataset.vid+'?autoplay=1&rel=0');
var i=document.createElement('iframe');
i.src=src;i.allow='autoplay; encrypted-media; picture-in-picture';i.allowFullscreen=true;i.title='YouTube video player';
f.innerHTML='';f.appendChild(i);
});
</script>'''

def vidfac(vid):
    return ('<span class="vidfac" data-vid="%s" role="button" aria-label="Play video here">'
            '<img src="https://i.ytimg.com/vi/%s/hqdefault.jpg" alt="Video thumbnail" loading="lazy">'
            '<span class="vplay">&#9654;</span></span>') % (vid, vid)

def appcard():
    return ('<a class="card appcard" href="https://chris007hanna-cpu.github.io/sleep-app/">'
            '<img src="sleep-app/icons/icon-192.png" alt="Sleep Sounds App icon">'
            '<span><span class="t" style="display:block">&#127769; SLEEP SOUNDS APP<span class="freetag">Free</span></span>'
            '<span class="s" style="display:block">The free What We Do In Darkness app: every sleep video in one place. Open it, then save it to your home screen.</span></span></a>\n')

def chanfac(ucid):
    th = CHANTHUMB.get(ucid)
    if th:
        return ('<span class="vidfac" data-list="UU%s" role="button" aria-label="Play this channel here">'
                '<img src="https://i.ytimg.com/vi/%s/hqdefault.jpg" alt="This channel\'s newest video" loading="lazy">'
                '<span class="vplay">&#9654;</span><span class="vlabel">Tap to play this channel here</span></span>') % (ucid[2:], th)
    return ('<span class="vidfac nothumb" data-list="UU%s" role="button" aria-label="Play this channel here">'
            '<span class="vplay">&#9654;</span><span class="vlabel">Tap to play this channel here</span></span>') % ucid[2:]

def chancard(url, t, s, ucid):
    return ('<div class="card"><div class="t"><a href="%s" target="_blank" rel="noopener">%s</a></div><div class="s">%s</div>%s'
            '<a class="visitbtn" href="%s" target="_blank" rel="noopener">Visit channel on YouTube</a>'
            '<noscript><div class="s"><a href="%s">Watch on YouTube</a></div></noscript></div>\n') % (url, clean_title(t), s, chanfac(ucid), url, url)

# ---------- PARITY DATA (live catalogs pulled 2026-11-07, site parity lane) ----------
# CHANTHUMB: channel id -> its newest public video id, so every channel facade
# shows that channel's own current thumbnail instead of one identical blank tile.
CHANTHUMB = {
 'UC6M4P62to1D6jMt0smdqiNQ': 'Q-dSW_UTPeY',
 'UC5nNRc2NdXLV1FXln9TZh9g': '-KqhdlxgoYI',
 'UCeLSNAQUPYVs9vF6rG4Edcg': 'auGfy2J_RaI',
 'UCzPkgcxxy2-ZQxwtOHypjeQ': 'AG4tIlBSkFM',
 'UCmOTdy0tWfsEOePjpIA1P3w': 'D5kpwPBMvi4',
 'UCvnip76il00fnmbQtcuxiFA': '4cBzVEDv_oI',
 'UCU2K7DdBvh3EgdulrttEXqA': '6xFM1QceEYg',
 'UCttOpXwbrJTwIOuoAf0GXsw': '_l6kcIfJhz8',
 'UCOa38iZ_dzxk98hBiQRsl6Q': 'mvMHqBE_ddg',
 'UCXD_Tww1wi5pn2n3JxGhLtw': '4oFs5BywKYo',
 'UCjEckDqnLQTCBIT4JaMP0VA': 'a_2dQ2d3yw4',
 'UCEUUYLKRajxVicLbFP2Kflg': '-tlJ2j-JkuQ',
 'UC1os6Wse_GZEkUw10Y0WxBQ': 'jvm0VHAyEyc',
 'UCr4Chp7whht_UR9syZJ-1Ww': 'fPUXTVfl7uA',
}

# SLEEP_VIDS: every public What We Do In Darkness video, newest first: (id, title, is_short)
SLEEP_VIDS = [
 ('Q-dSW_UTPeY', "Santa's Workshop 🎅 3 Hours of Howling Wind | Cozy Christmas Sleep Scene", False),
 ('a_Ka7LmhRSk', 'Fireplace Sounds for Sleeping | Christmas Fireplace, Crackling Fire, Stockings & Garland | 3 Hours', False),
 ('7pgOsNkVLVQ', 'Which Dream Bed Would You Sleep In Tonight? 🛏️ 12 Dream Beds, Pick Your Number | 3 Hours ASMR Sleep', False),
 ('6_JdiYCVvmo', 'Reindeer Barn 🦌 3 Hours of Howling Wind | Cozy Winter Sleep Scene', False),
 ('SQwIKRQGX5g', 'Howling Wind Sounds 10 Hours 🌬️ Black Screen | Strong Winter Wind for Deep Sleep', False),
 ('6cKCyK_5e8U', 'Howling Wind Sounds for Sleeping 🌬️ the Strongest Gusts #shorts', True),
 ('M3YGIj1PFRY', 'Long Day? Close the Laptop. Press Play. Sleep. 🌙 #shorts', True),
 ('VlAT5vIhjG4', 'Sleigh Ride Through the Snow | Sleigh Bells, Hooves in Snow & Cold Wind | 3 Hours Sleep Sounds', False),
 ('2yH1pUbBSz0', 'Rotisserie Turkey over an Open Fire 🦃🔥 Crackling Hearth & Spit Creaks | 3 Hours Fall Ambience', False),
 ('PMegbg-ME6U', 'Hayloft at Night 🍂🌙 Moonlight, Hay Rustle & a Sleeping Cat | 3 Hours Fall Sleep Ambience', False),
 ('5l3Q0S1W5SA', 'Locked In Safe 🔒 Zombie Outbreak Sleep Ambience | Rain on a Van Roof, 8 Hours', False),
 ('roWv_8W6fZ8', 'The Quiet Bend: Autumn Stream at Dusk for Sleep #shorts', True),
 ('f0fZr1Ivl4g', 'Sleigh Ride Through the Snow | Preview of Our 3 Hour Sleep Film', False),
 ('jUwk08NJa74', 'Autumn Forest Stream 🍂 3 Hours of Gothic Sleep Music | Fall Sleep Scene', False),
 ('--zDuIVBqBU', 'Harvest Moon Over the Fields 🌕🌾 Fireflies Under a Giant Moon #shorts', True),
 ('rfxZ4V82pm0', 'Harvest Moon Over the Fields 🌕🌾 3 Hours of Gothic Sleep Music | Fall Sleep Scene', False),
 ('9_lE3PS0zbo', 'Falling Autumn Leaves 🍂🍁 3 Hours of Gothic Sleep Music | Fall Sleep Scene', False),
 ('rSD_kU9UerM', 'Autumn Forest Stream 🍂 Babbling Water, Falling Leaves and Fireflies #shorts', True),
 ('HeJgruMRWyw', 'Falling Autumn Leaves 🍂🍁 Gothic Sleep Music', True),
 ('J2tuoBx-VEI', 'Changing-Color Forest 🍂🌲 The Canopy Turning, Marimba & a Far Stream #shorts', True),
 ('6VHzeHu52EE', 'Harvest Farm at Dusk 🌾🌆 Windmill, Crickets and Hay Bales #shorts', True),
 ('5_9NmvQfMu8', 'Scarecrow Field at Dusk 🌾🌙 The Crow, the Pumpkins and the Harvest Moon #shorts', True),
 ('H5XdS7pwoDY', 'Wood Stove Cabin in Fall Rain 🔥🌧️ Fire Glow, Tin-Roof Rain and a Puppy #shorts', True),
 ('wgWNWns0xgw', 'Changing-Color Forest 🍂🌲 3 Hours of Gothic Sleep Music | Fall Sleep Scene', False),
 ('jj9MBjltsdA', 'Blue Noise 10 Hours 💤 Black Screen | Focus, Study & Deep Sleep Sounds', False),
 ('PJRC667XEzc', 'Harvest Farm at Dusk 🌾🌆 3 Hours of Gothic Sleep Music | Fall Sleep Scene', False),
 ('IRhJA7Nm-JI', 'Scarecrow Field at Dusk 🌾🌙 3 Hours of Gothic Sleep Music | Fall Sleep Scene', False),
 ('BJynhWjblg4', 'Wood Stove Cabin in Fall Rain 🔥🌧️ 3 Hours of Gothic Sleep Music | Fall Sleep Scene', False),
 ('gayMinQ0kMs', 'Black Cat on a Moonlit Fence 🐈\u200d⬛🌙 The Night Watch #shorts', True),
 ('4HL391uzPkE', 'Apple Orchard at Night 🍎🌙 Moonlight, Fireflies and Falling Apples #shorts', True),
 ('d72VeZ3inD8', 'Haunted Lighthouse in Fog 🗼🌫️ The Beam Turns Through the Mist #shorts', True),
 ('4VhEeg4KKXA', 'Violet Noise 10 Hours 💤 Black Screen | Focus, Study & Deep Sleep Sounds', False),
 ('DOWhS9cJWZs', 'Sleepy Hollow 🎃 The Horseman Waits at the Bridge #shorts', True),
 ('S9E8rtl_URc', 'Owl Hollow 🦉 Two Owls Under a Full Moon #shorts', True),
 ('5oa-yCSUaIY', 'Apple Orchard at Night 🍎🌙 3 Hours of Gothic Sleep Music | Fall Sleep Scene', False),
 ('FCb5dK9Shns', 'Mad Scientist Castle 3 Hours | Arcing Voltage & Sparks | Sleepy Halloween Ambience', False),
 ('Xp4vO3mHGlQ', 'Haunted Lighthouse in Fog 3 Hours | A Slow Beam Turning Through Mist | Sleepy Halloween Ambience', False),
 ('HS7mOy9yAIc', 'Sleepy Hollow Halloween 3 Hours | Spooky Silhouettes & Soft Ghosts | Sleepy Halloween Ambience', False),
 ('pzdsjT_q91A', 'Owl Hollow 3 Hours | Owls Calling Softly in the Autumn Woods | Night Sleep Ambience', False),
 ('KQ5F3YjCZdk', 'For Those Who Served: Send Us Your Photos', True),
 ('xE10uLPSgz8', 'Trick-or-Treat Porch 🎃 3 Hours of Gothic Sleep Music | Halloween Sleep Scene', False),
 ('5VGtzteolow', "Witch's Forest Cottage 🌙 3 Hours of Gothic Sleep Music | Halloween Sleep Scene", False),
 ('4QdBqMdy1Yw', 'Corn Maze Night Wind 🌽🌙 The Maze Is Quiet Tonight #shorts', True),
 ('K758R8VBbJQ', 'Corn Maze Night Wind 🌽🌙 3 Hours of Gothic Sleep Music | Halloween Sleep Scene', False),
 ('KdMHD3Nk-e0', "POV: It's 2AM and You STILL Can't Sleep 😴 Pink Noise | Part 2 #shorts", True),
 ('B5GfEIjV7tw', 'Zombie Band Sleep Session 🧟 The Band That Never Sleeps #shorts', True),
 ('ii4CKzvslk8', 'Haunted Hayride 🎃 Torchlight, Monsters & the Pumpkin Rider | 10 Hours of Gothic Sleep Music', False),
 ('ImS3WP8zaUE', 'Zombie Band Sleep Session 🧟 10 Hours of Gothic Sleep Music | Halloween Sleep Scene', False),
 ('9EiGOmnRACY', 'Thunderstorm Sounds 10 Hours, Rain and Thunder for Sleep and Relaxation', False),
 ('CCECosWc1RU', 'Fan Noise 10 Hours, Sleep Sound for Deep Sleep All Night', False),
 ('KjLARyPTOnM', 'Haunted Pumpkin Patch 🎃 Halloween Sleep Scene | 10 Hours of Spooky Sleep Music', False),
 ('4QUDk3ZukCw', 'Ghost Train in the Fog 🌫️🚂 10 Hours of Haunting Sleep Music | Halloween Sleep Scene', False),
 ('1recnaZYhgM', 'Black Cat on a Moonlit Fence 🐈\u200d⬛🌙 3 Hours of Gothic Sleep Music | Halloween Sleep Scene', False),
 ('ls2wFZJ3J7M', 'Friendly Graveyard Ghosts 👻 10 Hours of Gothic Sleep Music | Halloween Sleep Scene', False),
 ('0cs-DcOAHw0', 'Haunted Hayride, Coming Soon | Halloween Sleep Scene', True),
 ('iJxGnGFBjuY', 'Haunted Pumpkin Patch | Halloween Sleep Scene', True),
 ('MacMbhtRKf4', 'Ghost Train in the Fog | Halloween Sleep Scene', True),
 ('QMBF3_w-t9M', '5 Sounds. 10 Hours Each. Zero Interruptions. 🌙 The Sleep Channel Trailer #shorts', True),
 ('fexkrTjJJJk', "POV: It's 2AM and You Can't Sleep 😴 Brown Noise Deep Sleep Fix #shorts", True),
 ('8vwBtFRYBlc', 'Ringing Ears? Try THIS Tonight 👂 Violet Noise Tinnitus Hack #shorts', True),
 ('yCBWECt_6Ok', "You've Been Sleeping to the WRONG Noise 😴 Brown vs White #shorts", True),
 ('Qi6ntiiiQBQ', 'Which Noise Knocks YOU Out? 😴 White vs Brown vs Pink #shorts', True),
 ('Vn3_OgkEmiU', 'Pink Noise 10 Hours for Sleeping 💤 Black Screen | Deeper Sleep & Relaxation', False),
 ('b0UVAYISW1k', 'Brown Noise 10 Hours 💤 Black Screen | Deep Sleep, ADHD Focus & Tinnitus Relief', False),
 ('yAnDkOkFK_Q', 'White Noise 10 Hours for Deep Sleep 💤 Black Screen | No Interruptions | Baby Sleep & Focus', False),
]

# WATCH_SHORTS: every public Short on the fleet, grouped by channel: (channel, [(id, title)])
WATCH_SHORTS = [
 ('AI BLACK BELT', [
   ('V-4trRgDOqU', 'How to Use ChatGPT for Work Emails: The Prompt Fix That Saved My Afternoon #shorts'),
   ('LY8cE2N2vjw', 'The Free AI Told Me to Buy Saffron #shorts'),
   ('nk39n_WnVQ8', "Same AI. One Company Wins. Here's Why. #shorts"),
   ('J1e1ojQzYDg', 'The Voice Sample: Emails That Sound Like You #shorts'),
   ('j6yVDEkhThw', 'The Voice Match Drill | AI Black Belt Lesson 2 #shorts'),
   ('jarqLBdKHKI', 'The 60-Second Prompt Drill | AI Black Belt Lesson 1 #shorts'),
 ]),
 ('DARK TALES RETOLD', [
   ('CFnUaxMV4GE', 'Scary Stories to Listen to at Night Got Her Like This #shorts'),
   ('Ugq1ABS2Guk', 'He Chatted With Police Above the Body, Then Heard It Beating #shorts'),
   ('Oy5nKsea7dM', 'The Tell-Tale Heart — He Could Hear It Beating… 🕯️'),
 ]),
 ('ONE-POT BROKE KITCHEN', [
   ('AG4tIlBSkFM', 'The Marsala Pour: Where the Slow Cooker Sauce Actually Comes From #shorts'),
   ('aPgGW4VWxMk', 'Hot Sauce Is Not Optional: The Loaded Finish on 94 Cent Rice and Beans #shorts'),
   ('za4sS_HqpVI', '$1.87 Dinner That ACTUALLY Fills You Up 🍚'),
   ('AVM6kzR5LbI', 'The Flavor Trick That Makes $1.87 Rice and Beans Taste Like $10 #shorts'),
   ('88M3aDceBSg', 'Empty Fridge? Watch This. | One-Pot Broke Kitchen'),
 ]),
 ('PAPER FIRST TRADING', [
   ('uM3nexDu9YI', 'Paper Trading for Beginners, With Coffee Gone Cold and Zero Real Money #shorts'),
   ('Cf0bYKuVik0', 'Real Money Stays Off the Table Until Paper Proves It'),
 ]),
 ('PAWS WHILE YOU WORK', [
   ('mvMHqBE_ddg', 'DOG TV | Golden Retriever Running Through Autumn Leaves #shorts'),
   ('pFRpxX0lHTw', 'DOG TV | Chipmunk on Lookout Duty for Dogs to Watch #shorts'),
   ('x6YZAlQV_pE', 'Dog TV for Dogs Home Alone: He Watched Until He Fell Asleep | Paws While You Work'),
   ('idlXZ-ceW6c', 'DOG TV | Squirrel in the Snow Hunting for His Nut #shorts'),
   ('RIj3No1F79k', 'DOG TV | Leave This On For Your Dog While You Work #shorts'),
 ]),
 ('PHONE FLIP ACADEMY', [
   ('D5kpwPBMvi4', 'Buying a Used Phone? What to Check Before the Cash Moves | Phone Flip Academy'),
   ('vwL3nMq3wWA', 'Battery + Face ID: Check Three Before You Buy Any Phone #shorts'),
   ('nC3hoEOwSFc', 'iCloud + Carrier Lock: The Check That Kills More Flips Than Anything #shorts'),
   ('cEODdNH-Q5k', 'Test Everything Before You Seal a Repaired Phone #shorts'),
   ('y3jSh2iSfXI', 'Check the IMEI Before You Buy Any Phone #shorts'),
   ('RgmfGPDpQnU', 'Check Any Used Phone in 5 Minutes, The 5 Checks #shorts'),
   ('xdZXG6a9KNE', 'Flipping $20 Phones: The Whole Process in 40 Seconds #shorts'),
   ('LrwpnmLWueA', 'The $199 Trap: Never Pay a Shop to Fix a Flip Phone #Shorts'),
   ('h6RVb5Ub7CQ', "$20 Phone → $60 Flip 💰 Here's How"),
 ]),
 ('ROBOT BRAIN WORKSHOP', [
   ('c7NX5Ohdci8', 'How to Train a Robot Brain With Teachable Machine, Starting From Your Old Phone'),
   ('rxsvyWZ0dK8', 'We Taught a Robot Brain to See in Under a Minute'),
   ('wwQdodGmIrE', 'Your Drawer Phone Is Already a Robot Brain'),
 ]),
 ('SIMPLE SURVIVAL', [
   ('g8Ib4A7WGwg', 'He Copied This Creek Water Filter Straight Off His Phone'),
   ('GMzdigeuJL8', 'Ferro Rod Fire: Catch the Spark in a Tinder Bundle #shorts'),
   ('vo0j5vnJ2Cs', "The Space Blanket Lie: Why Mylar Alone Won't Keep You Warm #shorts"),
   ('GjsCcVEn5Xo', 'The Cheapest Blackout Light Starts Fires: The 3 Candle Rules #shorts'),
   ('wsWoRHGBPGw', 'Turn Soda Can Pull Tabs Into a Tough Bracelet'),
   ('SMpcN2dAMWs', 'You Are Lighting Your Fire in the Wrong Order'),
   ('rFwhCt5PrsY', 'Clear Water Can Still Make You Sick | The Bottle Filter Verdict'),
   ('DlOhsDYSNfk', 'Creek Water Filter in a Bottle #shorts'),
   ('pkAIaNN2ZYA', '5 Fires From One Match Kit'),
   ('uOp9Iujk7Ug', 'The Rice and Oil Lamp Lie: What Actually Happens'),
 ]),
 ('THE CLAIM VS. THE RECORD', [
   ('jZXBoI8ioEE', 'Can You Drive Without a License? He Said Everybody Knows You Can #shorts'),
   ('1LXCpWevATA', 'The NATO Driving Permit Is a Translation Booklet.'),
 ]),
 ('THE INSTANT RAMEN CHEF!', [
   ('-KqhdlxgoYI', 'Cook Along With Us | The Instant Ramen Chef! #shorts'),
   ('3UuSczbDSkU', 'Midnight Ramen in 60 Seconds: Black Garlic Oil + Pumpkin Miso #shorts'),
   ('pjySsV-Ccnk', 'Butter Garlic Ramen, Fixed Forever in 68 Seconds #shorts'),
   ('3XPOsQX-YbU', 'Mayo Garlic Ramen in 60 Seconds'),
 ]),
 ('WHAT IF MACHINE', [
   ('4cBzVEDv_oI', 'What If the Ocean Drained Overnight? The Couch Went Silent #shorts'),
   ('lX6tlEjEJo0', 'Could Anyone Survive If the Sun Went Out? #shorts'),
   ('zR-K4ztRGzs', 'The Ocean Is the Engine Room of the Planet #shorts'),
   ('-r78nFtsjvA', 'What If the Sun Went Out? The First 8 Minutes ☀️❌ #Shorts'),
   ('dLGy7qMkHbU', 'What If the Ocean Drained Overnight? 🌊'),
 ]),
 ('WHAT WE DO IN DARKNESS', [
   ('6cKCyK_5e8U', 'Howling Wind Sounds for Sleeping 🌬️ the Strongest Gusts #shorts'),
   ('M3YGIj1PFRY', 'Long Day? Close the Laptop. Press Play. Sleep. 🌙 #shorts'),
   ('roWv_8W6fZ8', 'The Quiet Bend: Autumn Stream at Dusk for Sleep #shorts'),
   ('--zDuIVBqBU', 'Harvest Moon Over the Fields 🌕🌾 Fireflies Under a Giant Moon #shorts'),
   ('rSD_kU9UerM', 'Autumn Forest Stream 🍂 Babbling Water, Falling Leaves and Fireflies #shorts'),
   ('HeJgruMRWyw', 'Falling Autumn Leaves 🍂🍁 Gothic Sleep Music'),
   ('J2tuoBx-VEI', 'Changing-Color Forest 🍂🌲 The Canopy Turning, Marimba & a Far Stream #shorts'),
   ('6VHzeHu52EE', 'Harvest Farm at Dusk 🌾🌆 Windmill, Crickets and Hay Bales #shorts'),
   ('5_9NmvQfMu8', 'Scarecrow Field at Dusk 🌾🌙 The Crow, the Pumpkins and the Harvest Moon #shorts'),
   ('H5XdS7pwoDY', 'Wood Stove Cabin in Fall Rain 🔥🌧️ Fire Glow, Tin-Roof Rain and a Puppy #shorts'),
   ('gayMinQ0kMs', 'Black Cat on a Moonlit Fence 🐈\u200d⬛🌙 The Night Watch #shorts'),
   ('4HL391uzPkE', 'Apple Orchard at Night 🍎🌙 Moonlight, Fireflies and Falling Apples #shorts'),
   ('d72VeZ3inD8', 'Haunted Lighthouse in Fog 🗼🌫️ The Beam Turns Through the Mist #shorts'),
   ('DOWhS9cJWZs', 'Sleepy Hollow 🎃 The Horseman Waits at the Bridge #shorts'),
   ('S9E8rtl_URc', 'Owl Hollow 🦉 Two Owls Under a Full Moon #shorts'),
   ('KQ5F3YjCZdk', 'For Those Who Served: Send Us Your Photos'),
   ('4QdBqMdy1Yw', 'Corn Maze Night Wind 🌽🌙 The Maze Is Quiet Tonight #shorts'),
   ('KdMHD3Nk-e0', "POV: It's 2AM and You STILL Can't Sleep 😴 Pink Noise | Part 2 #shorts"),
   ('B5GfEIjV7tw', 'Zombie Band Sleep Session 🧟 The Band That Never Sleeps #shorts'),
   ('0cs-DcOAHw0', 'Haunted Hayride, Coming Soon | Halloween Sleep Scene'),
   ('iJxGnGFBjuY', 'Haunted Pumpkin Patch | Halloween Sleep Scene'),
   ('MacMbhtRKf4', 'Ghost Train in the Fog | Halloween Sleep Scene'),
   ('QMBF3_w-t9M', '5 Sounds. 10 Hours Each. Zero Interruptions. 🌙 The Sleep Channel Trailer #shorts'),
   ('fexkrTjJJJk', "POV: It's 2AM and You Can't Sleep 😴 Brown Noise Deep Sleep Fix #shorts"),
   ('8vwBtFRYBlc', 'Ringing Ears? Try THIS Tonight 👂 Violet Noise Tinnitus Hack #shorts'),
   ('yCBWECt_6Ok', "You've Been Sleeping to the WRONG Noise 😴 Brown vs White #shorts"),
   ('Qi6ntiiiQBQ', 'Which Noise Knocks YOU Out? 😴 White vs Brown vs Pink #shorts'),
 ]),
 ('WRITTEN IN THE STARS DAILY', [
   ('6xFM1QceEYg', 'Aquarius Daily Reading, November 7, 2026 #Shorts'),
   ('0J4V1CLKSWs', 'Capricorn Daily Reading, November 6, 2026 #Shorts'),
   ('u-kPwrMl8yk', 'Sagittarius Daily Reading, November 5, 2026 #Shorts'),
   ('FUXXbjEaVHA', 'Scorpio Daily Reading, November 4, 2026 #Shorts'),
   ('YicqBRsYkCQ', 'Virgo Horoscope Today, She Checked Her Daily Horoscope With Her Coffee and It Knew #Shorts'),
   ('4kiRw05xY3k', 'Libra Daily Reading, November 3, 2026 #Shorts'),
   ('HPzdZ-hWZp0', 'Virgo Daily Reading, November 2, 2026 #Shorts'),
   ('DY_36UTCMQE', 'Leo Daily Reading, November 1, 2026 #Shorts'),
   ('xX7ddbhs6xg', 'Scorpio Daily Reading, October 31, 2026 #shorts'),
   ('zxEvZwNovTA', 'Cancer Daily Reading, October 31, 2026 #Shorts'),
   ('bDp0s2YPXSg', 'Gemini Daily Reading, October 30, 2026 #Shorts'),
   ('4rO8xlFNvKI', 'Taurus Daily Reading, October 29, 2026 #Shorts'),
   ('bZo8bXohmBg', 'Aries Daily Reading, October 28, 2026 #Shorts'),
   ('9CuODtCS8u4', 'Pisces Daily Reading, October 27, 2026 #Shorts'),
   ('E3_6lGlesec', 'Aquarius Daily Reading, October 26, 2026 #Shorts'),
   ('wOwXT2QOikQ', 'Capricorn Daily Reading, October 25, 2026 #Shorts'),
   ('I8qMC_vAB18', 'Sagittarius Daily Reading, October 24, 2026 #Shorts'),
   ('dBNOgbQY_cs', 'Scorpio Daily Reading, October 23, 2026 #Shorts'),
   ('Rfqwda42WGs', 'Taurus Daily Reading, October 22, 2026 #Shorts'),
   ('2i3Kmy-ApRs', 'Aries Daily Reading, October 21, 2026 #Shorts'),
   ('r-ketoid1WY', 'Pisces Daily Reading, October 20, 2026 #Shorts'),
   ('fTaHCUcreUE', 'Aquarius Daily Reading, October 19, 2026 #Shorts'),
   ('iVPBEqHRxo8', 'Libra Daily Reading, October 18, 2026 #Shorts'),
 ]),
]

# ---------- LINKIFY (Irish's hyperlink rule, 2026-11-03): names are the links ----------
# Every channel name, product name, and roster name that appears as visible
# text carries its link. Runs inside page() and the preview writer over text
# nodes only: tags, attributes, existing anchors, scripts, styles, titles and
# form controls are never touched, so markup and prices cannot be disturbed.
_LK_YT = ' target="_blank" rel="noopener"'
_LK_MAP = [
 ("WHAT WE DO IN DARKNESS", "https://www.youtube.com/@WhatWeDoInDarkness", 1),
 ("What We Do In Darkness", "https://www.youtube.com/@WhatWeDoInDarkness", 1),
 ("THE INSTANT RAMEN CHEF!", "https://www.youtube.com/@TheInstantRamenChef", 1),
 ("THE INSTANT RAMEN CHEF", "https://www.youtube.com/@TheInstantRamenChef", 1),
 ("The Instant Ramen Chef!", "https://www.youtube.com/@TheInstantRamenChef", 1),
 ("The Instant Ramen Chef", "https://www.youtube.com/@TheInstantRamenChef", 1),
 ("DARK TALES RETOLD", "https://www.youtube.com/@DarkTalesRetoldTV", 1),
 ("Dark Tales Retold", "https://www.youtube.com/@DarkTalesRetoldTV", 1),
 ("GILDED HEARTS DRAMA", "https://www.youtube.com/@GildedHeartsDramaOfficial", 1),
 ("Gilded Hearts Drama", "https://www.youtube.com/@GildedHeartsDramaOfficial", 1),
 ("ONE-POT BROKE KITCHEN", "https://www.youtube.com/@OnePotBrokeKitchen", 1),
 ("ONE POT BROKE KITCHEN", "https://www.youtube.com/@OnePotBrokeKitchen", 1),
 ("One-Pot Broke Kitchen", "https://www.youtube.com/@OnePotBrokeKitchen", 1),
 ("One Pot Broke Kitchen", "https://www.youtube.com/@OnePotBrokeKitchen", 1),
 ("PHONE FLIP ACADEMY", "https://www.youtube.com/@PhoneFlipAcademy", 1),
 ("Phone Flip Academy", "https://www.youtube.com/@PhoneFlipAcademy", 1),
 ("WHAT IF MACHINE", "https://www.youtube.com/@WhatIfMachineTV", 1),
 ("What If Machine", "https://www.youtube.com/@WhatIfMachineTV", 1),
 ("AI BLACK BELT", "https://www.youtube.com/@AIBlackBeltHQ", 1),
 ("AI Black Belt", "https://www.youtube.com/@AIBlackBeltHQ", 1),
 ("WRITTEN IN THE STARS DAILY", "https://www.youtube.com/@WrittenInTheStarsDaily", 1),
 ("Written in the Stars Daily", "https://www.youtube.com/@WrittenInTheStarsDaily", 1),
 ("Written in the Stars", "https://www.youtube.com/@WrittenInTheStarsDaily", 1),
 ("SIMPLE SURVIVAL", "https://www.youtube.com/@SimpleSurvivalHQ", 1),
 ("Simple Survival", "https://www.youtube.com/@SimpleSurvivalHQ", 1),
 ("PAWS WHILE YOU WORK", "https://www.youtube.com/@PawsWhileYouWork", 1),
 ("Paws While You Work", "https://www.youtube.com/@PawsWhileYouWork", 1),
 ("ROBOT BRAIN WORKSHOP", "https://www.youtube.com/channel/UCXD_Tww1wi5pn2n3JxGhLtw", 1),
 ("Robot Brain Workshop", "https://www.youtube.com/channel/UCXD_Tww1wi5pn2n3JxGhLtw", 1),
 ("PAPER FIRST TRADING", "https://www.youtube.com/@PaperFirstTrading", 1),
 ("Paper First Trading", "https://www.youtube.com/@PaperFirstTrading", 1),
 ("THE CLAIM VS. THE RECORD", "https://www.youtube.com/@ClaimVsRecord", 1),
 ("The Claim vs. The Record", "https://www.youtube.com/@ClaimVsRecord", 1),
 ("Claim vs. The Record", "https://www.youtube.com/@ClaimVsRecord", 1),
 ("Claim vs The Record", "https://www.youtube.com/@ClaimVsRecord", 1),
 ("Simple Survival 72 Hour Ready Binder", "preview-survival-72-hour-binder.html", 0),
 ("72 Hour Ready Binder", "preview-survival-72-hour-binder.html", 0),
 ("AI Memory Sync Kit", "preview-ai-memory-sync-kit.html", 0),
 ("AI Like a Pro", "preview-ai-like-a-pro.html", 0),
 ("Broke to Budget", "preview-broke-to-budget-planner.html", 0),
 ("Colors of Noise", "sleep.html", 0),
 ("Sleep Sounds App", "https://chris007hanna-cpu.github.io/sleep-app/", 0),
 ("The Phone Flip Playbook", "preview-phone-flip-playbook.html", 0),
 ("AI Coding Agents 2026", "preview-ai-coding-agents-2026.html", 0),
 ("Embracing the Unknown", "preview-embracing-the-unknown.html", 0),
 ("Digital Product Empire", "preview-digital-product-empire.html", 0),
 ("Faceless Fortune", "preview-faceless-fortune.html", 0),
 ("Fiverr Fast Start", "preview-fiverr-fast-start.html", 0),
 ("Free Money Handbook", "preview-free-money-handbook.html", 0),
 ("Instant Ramen Chef", "preview-instant-ramen-chef.html", 0),
 ("Laugh Attack", "preview-laugh-attack.html", 0),
 ("Marketplace Millions", "preview-marketplace-millions.html", 0),
 ("Phone Repair Mastery", "preview-phone-repair-mastery.html", 0),
 ("Side Hustle Stack", "preview-side-hustle-stack.html", 0),
 ("Solid-State EV Buyer's Guide", "preview-solid-state-ev-guide.html", 0),
 ("Solid-State EV Buyer&#x27;s Guide", "preview-solid-state-ev-guide.html", 0),
 ("Solid-State EV Buyer&#39;s Guide", "preview-solid-state-ev-guide.html", 0),
 ("Surviving on the Street", "preview-street-survival-guide.html", 0),
 ("The $0 Startup", "preview-zero-dollar-startup.html", 0),
 ("Mojo Programming", "preview-mojo-programming.html", 0),
 ("Mojo 1.0", "preview-mojo-programming.html", 0),
 ("Dad Jokes", "preview-dad-jokes.html", 0),
 ("Angelica Bradeen", "models.html", 0),
 ("Angelica Danielle", "models.html", 0),
 ("Leah Hamilton", "models.html", 0),
 ("Heather Lou", "models.html", 0),
 ("Holly Clark", "holly-clark.html", 0),
 ("Tito", "tito.html", 0),
]
_LK_MAP.sort(key=lambda x: -len(x[0]))
_LK_RE = re.compile(r'(?<![A-Za-z0-9&])(%s)(?![A-Za-z0-9])' % "|".join(re.escape(p) for p, _, _ in _LK_MAP))
_LK_BY_PHRASE = {p: (u, ext) for p, u, ext in _LK_MAP}
_LK_SKIP = {'a', 'script', 'style', 'title', 'textarea', 'select', 'option', 'noscript', 'button'}
_LK_STATS = {}
def linkify(html, self_href=None):
    parts = re.split(r'(<[^>]+>)', html)
    depth = {}
    out = []
    for part in parts:
        if part.startswith('<'):
            m = re.match(r'</?\s*([A-Za-z0-9]+)', part)
            if m:
                tag = m.group(1).lower()
                if part.startswith('</'):
                    depth[tag] = max(0, depth.get(tag, 0) - 1)
                elif not part.rstrip().endswith('/>') and tag not in ('img', 'br', 'hr', 'input', 'meta', 'link', 'source'):
                    depth[tag] = depth.get(tag, 0) + 1
            out.append(part)
            continue
        if not part or any(depth.get(t, 0) > 0 for t in _LK_SKIP):
            out.append(part)
            continue
        def _sub(mo):
            phrase = mo.group(1)
            url, ext = _LK_BY_PHRASE[phrase]
            if self_href and url == self_href:
                return phrase
            _LK_STATS[phrase] = _LK_STATS.get(phrase, 0) + 1
            return '<a class="lk" href="%s"%s>%s</a>' % (url, _LK_YT if ext else '', phrase)
        out.append(_LK_RE.sub(_sub, part))
    return "".join(out)

def page(title, desc, active, h1, tag, body, script=""):
    primary = [("index.html","HOME"),("books.html","BOOKS"),("shop.html","SHOP")]
    groups = [
        ("services.html","SERVICES",[("services.html","Services Overview"),("realestate.html","Real Estate"),("localbusiness.html","Local Business"),("cardealers.html","Car Dealers"),("propertymanagement.html","Property Management"),("rentalhosts.html","Airbnb &amp; VRBO Hosts"),("insurance.html","Insurance Agents"),("hotels.html","Hotels &amp; Motels"),("taxi.html","Taxi &amp; Limo Services"),("restaurants.html","Restaurants &amp; Hospitality"),("virtual.html","Virtual Services"),("sell.html","Sell With Us")]),
        ("talent.html","TALENT",[("talent.html","Talent Hub"),("artists.html","Artists"),("models.html","Models"),("glamour.html","Glamour"),("djs.html","DJs"),("actors.html","Actors &amp; Voice"),("singers.html","Singers"),("creators.html","Creators"),("athletes.html","Athletes"),("comedians.html","Comedians"),("podcasters.html","Podcasters")]),
    ]
    tail = [("watch.html","WATCH"),("sleep.html","SLEEP")]
    nav = "".join('<a href="%s"%s>%s</a>' % (u, ' class="on"' if u == active else '', n) for u, n in primary)
    for hub, label, kids in groups:
        on = ' class="on"' if any(u == active for u, _ in kids) else ''
        drop = "".join('<a href="%s"%s>%s</a>' % (u, ' class="on"' if u == active else '', n) for u, n in kids)
        nav += '<span class="ngrp"><a href="%s"%s>%s</a><span class="drop">%s</span></span>' % (hub, on, label, drop)
    nav += "".join('<a href="%s"%s>%s</a>' % (u, ' class="on"' if u == active else '', n) for u, n in tail)
    fmap_items = [("index.html","Home"),("books.html","Books"),("shop.html","Shop"),("sell.html","Sell"),("sleep.html","Sleep"),("watch.html","Watch"),("services.html","Services"),("realestate.html","Real Estate"),("localbusiness.html","Local Business"),("cardealers.html","Car Dealers"),("propertymanagement.html","Property Management"),("rentalhosts.html","Airbnb &amp; VRBO"),("insurance.html","Insurance"),("hotels.html","Hotels &amp; Motels"),("taxi.html","Taxi &amp; Limo"),("restaurants.html","Restaurants"),("virtual.html","Virtual Services"),("talent.html","Talent"),("artists.html","Artists"),("models.html","Models"),("glamour.html","Glamour"),("djs.html","DJs"),("actors.html","Actors"),("singers.html","Singers"),("creators.html","Creators"),("athletes.html","Athletes"),("comedians.html","Comedians"),("podcasters.html","Podcasters"),("legal.html","Legal")]
    fmap = " &middot; ".join('<a href="%s">%s</a>' % (u, n) for u, n in fmap_items)
    _pg = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="wrap">
<nav>{nav}</nav>
<header><img src="assets/logo.jpg" alt="Irish shamrock coin logo">
<h1>{h1}</h1><p class="tag">{tag}</p></header>
{body}
<footer><div class="fmap">{fmap}</div><a href="index.html">&larr; All our links</a><br><br>Site run by <b style="color:#d4af37">Nova &#128176;</b> &mdash; Irish's AI partner.</footer>
</div>{script}''' + VID_JS + '''</body></html>'''
    return linkify(_pg, active)

def card(url, t, s, hero=False):
    return '<a class="card%s" href="%s"><div class="t">%s</div><div class="s">%s</div></a>\n' % (" hero" if hero else "", url, clean_title(t), s)

# ---------- PACKAGE DETAIL PANELS ("What you get") ----------
_PAGECTX = 'services'
_MISSING = []
_GUAR_CTX = {'localbusiness', 'cardealers', 'propertymanagement', 'rentalhosts', 'insurance', 'hotels', 'taxi', 'restaurants'}
_GUAR_HTML = '<h4>Our guarantee</h4><p><b>More business than you can handle &mdash; or we work for free.</b> Your Google profile built and live within 14 days, or your setup fee comes back. If your Google calls, direction requests, and bookings don&rsquo;t climb within 60 days, your monthly pauses &mdash; we work free until it moves.</p>'
_HOW_FIVERR = ["Pick your tier and order on Fiverr — payment stays secure with Fiverr the whole way.", "We confirm the details with you inside the Fiverr order.", "We do the work and deliver through Fiverr.", "You review the delivery right in the order thread."]
_HOW_MSG = ["Message us with the job — what you need and what it is for.", "We confirm the scope and the flat price in writing before anything starts.", "We build it and send it over for your review.", "You approve it, or tell us what to adjust."]
_HOW_MONTHLY = ["Message us and we map the plan to your goals first.", "We set up your pages, calendar, and first work.", "We run it daily — you watch the work land on your pages.", "Billing is monthly while the plan is active."]
_HOW_SETUP = ["Message us about your business — trade, town, and what you need.", "We confirm your setup and price in writing before anything starts.", "We build your setup and put it live.", "Your Google profile is built and live within 14 days — guaranteed."]
_TL_FIVERR = "Set on the Fiverr gig page for the tier you pick — you see the exact delivery days before you pay."
_TL_GUAR = "Setups are built and live within 14 days — guaranteed (see Our guarantee below). Monthly services run month to month while active."
_TL_MONTHLY = "Month to month while the plan is active — the first cycle starts at setup."
_TL_MSG = "We agree the delivery date with you in writing before work starts — no surprises."
DETAILS = {}
def _slug(t):
    t = clean_title(t)
    t = t.replace('&amp;', ' and ')
    t = re.sub(r'&[A-Za-z#0-9]+;', '-', t)
    t = t.replace('&', ' and ')
    t = re.sub(r'[^A-Za-z0-9]+', '-', t).strip('-').upper()
    return t
def _priceline(tiers):
    parts = ["%s %s" % (n, p) for n, p in tiers if p]
    if not parts:
        return "Custom quote &mdash; message us for scope &amp; price"
    return " &middot; ".join(parts)
def _panel(title, tiers, url):
    slug = _slug(title)
    e = DETAILS.get((_PAGECTX, slug)) or DETAILS.get(('*', slug))
    if e is None:
        _MISSING.append((_PAGECTX, slug))
        return ''
    price = e.get('price') or _priceline(tiers)
    monthly = bool(tiers) and any(p for _, p in tiers) and all(('/mo' in (p or '')) for _, p in tiers if p)
    if e.get('how'):
        how = e['how']
    elif 'fiverr' in url:
        how = _HOW_FIVERR
    elif _PAGECTX in _GUAR_CTX:
        how = _HOW_SETUP
    elif monthly:
        how = _HOW_MONTHLY
    else:
        how = _HOW_MSG
    if e.get('timeline'):
        tl = e['timeline']
    elif 'fiverr' in url:
        tl = _TL_FIVERR
    elif _PAGECTX in _GUAR_CTX:
        tl = _TL_GUAR
    elif monthly:
        tl = _TL_MONTHLY
    else:
        tl = _TL_MSG
    h = '<details class="wyg"><summary>What you get</summary><div class="wygb">'
    h += '<p class="wp">%s</p>' % price
    h += '<h4>What you get</h4><ul>' + "".join('<li>%s</li>' % x for x in e['get']) + '</ul>'
    h += '<h4>How it works</h4><ol>' + "".join('<li>%s</li>' % x for x in how) + '</ol>'
    h += '<h4>Timeline</h4><p>%s</p>' % tl
    h += '<h4>Who it fits</h4><p>%s</p>' % e['fits']
    h += '<h4>Not included</h4><ul>' + "".join('<li>%s</li>' % x for x in e['notincl']) + '</ul>'
    if _PAGECTX in _GUAR_CTX and not e.get('noguar'):
        h += _GUAR_HTML
    h += '</div></details>'
    return h
def _pkg(url, title, desc, th, tiers, cta):
    return '<div class="card"><a class="clink" href="%s"><div class="t">%s</div><div class="s">%s</div><div class="tiers">%s</div><div class="cta">%s &rarr;</div></a>%s</div>' % (url, clean_title(title), desc, th, cta, _panel(title, tiers, url))


# ---------- LOOK-INSIDE PREVIEWS (page-flip panels; images flat in assets/previews/<slug>-page-N.jpg) ----------
import json as _json, html as _html
try:
    _pvman = _json.load(open('assets/previews/manifest.json'))
except Exception:
    _pvman = {}
FLIP_JS = """<script>
document.addEventListener('click',function(e){
var b=e.target.closest('[data-fnav]');if(!b)return;
var f=b.closest('.flip');if(!f)return;
var pages=f.querySelectorAll('.fp');var cur=0;
pages.forEach(function(p,i){if(p.classList.contains('on'))cur=i;});
var n=cur+(b.getAttribute('data-fnav')==='next'?1:-1);
if(n<0)n=pages.length-1;if(n>=pages.length)n=0;
pages[cur].classList.remove('on');pages[n].classList.add('on');
f.querySelector('.fcount').textContent=(n+1)+' / '+pages.length;
});
</script>"""
def back_page(title, paras, foot):
    body = "".join('<p style="margin-bottom:8px">%s</p>' % _html.escape(p) for p in paras if p.strip())
    return '<div class="fb-t">%s</div>%s<div style="color:#ffd95e;font-family:Oswald,sans-serif;font-size:.85rem;letter-spacing:.04em;margin-top:4px">%s</div>' % (title, body, foot)
def flipper(slug, back_html, label):
    pages = _pvman.get(slug, {}).get('pages', [])
    fps = "".join('<img class="fp%s" src="assets/previews/%s-%s" alt="Preview page" loading="lazy">' % (" on" if i == 0 else "", slug, fn) for i, fn in enumerate(pages))
    fps += '<div class="fp ftext%s">%s</div>' % ("" if pages else " on", back_html)
    total = len(pages) + 1
    ctl = '<div class="fctl"><button type="button" class="fbtn" data-fnav="prev">&larr; Prev</button><span class="fcount">1 / %d</span><button type="button" class="fbtn" data-fnav="next">Next &rarr;</button></div>' % total
    return '<details class="pv"><summary>%s</summary><div class="flip">%s%s</div></details>' % (label, fps, ctl)

# ---------- PER-ITEM PREVIEW PAGES (click cover/title -> preview-<slug>.html with a BIG flipper) ----------
# An item gets a preview page only when it has real interior pages (cover + pages + back cover);
# cover-only items (1 manifest page) get no page and no link.
PV_BOOK_META = {}  # slug -> (title, format line) for the 17 books; filled in by the books loop below
def pv_pages(slug):
    return _pvman.get(slug, {}).get('pages', [])
def pv_has(slug):
    return len(pv_pages(slug)) > 1
def pv_link(slug):
    if not pv_has(slug):
        return ''
    return '<a class="lookbtn" href="preview-%s.html">&#128214; Look Inside &mdash; flip through it</a>' % slug
def pv_href(slug):
    return ('preview-%s.html' % slug) if pv_has(slug) else None
def big_flipper(slug, back_html):
    pages = pv_pages(slug)
    fps = "".join('<img class="fp%s" src="assets/previews/%s-%s" alt="Preview page" loading="lazy">' % (" on" if i == 0 else "", slug, fn) for i, fn in enumerate(pages))
    fps += '<div class="fp ftext">%s</div>' % back_html
    total = len(pages) + 1
    ctl = '<div class="fctl"><button type="button" class="fbtn" data-fnav="prev">&larr; Prev</button><span class="fcount">1 / %d</span><button type="button" class="fbtn" data-fnav="next">Next &rarr;</button></div>' % total
    return '<div class="flip bigflip">%s%s</div>' % (fps, ctl)
def book_desc(slug, limit=1300):
    try:
        raw = open('/home/hatch/workspace/your_files/empire/books/kdp-upload-kit/%s/description-kdp-source.txt' % slug).read()
    except Exception:
        return []
    raw = re.sub(r'</?p>', '\n\n', raw)
    raw = _html.unescape(re.sub(r'<[^>]+>', '', raw))
    paras = [p.strip() for p in raw.split('\n\n') if p.strip()]
    out, total = [], 0
    for p in paras:
        if out and total + len(p) > limit:
            out.append('\u2026')
            break
        out.append(p); total += len(p)
    return out

def _proof(items):
    return '<div class="proof">' + "".join('<div class="pf"><div class="n">%s</div><div class="l">%s</div></div>' % (n, l) for n, l in items) + '</div>'
PROOF_TALENT = _proof([("11th","Heather Lou \u2014 Maxim Centerfold"),("Led her group in the final round","Heather Lou \u2014 Maxim Elegance"),("19th","Angelica Danielle \u2014 Maxim Centerfold"),("17","Books published \u2014 Hanna Press"),("100%","Talent keeps ownership of their work")])
PROOF_SVC = _proof([("17","Books published \u2014 Hanna Press"),("16","YouTube channels run"),("4","Online stores live"),("100%","You keep your accounts &amp; your work")])

# ---------- BOOKS ----------
# Grid cards are clean (cover + title + price line as text + View Book) and link
# to a per-book detail page (book-<slug>.html) that carries the full breakdown,
# every buying route with its exact original href, and the cart Add buttons —
# the cart snippet wires .book/.bt/a.buy on the detail pages exactly as it used
# to on the grid, so cart item titles, prices, and codes are unchanged.
BOOK_DETAIL_FILES = []
_BOOK_HOOKS = {
 "phone-flip-playbook": "turn cheap prepaid phones into real side income, starting with $0 to $40 and a phone",
 "ai-coding-agents-2026": "build software by directing AI coding agents, in plain English for complete beginners",
 "embracing-the-unknown": "face job loss and a life that stops following the plan, and learn to move again",
 "dad-jokes": "300 so bad they are good, family friendly dad jokes in twelve laugh loaded chapters",
 "digital-product-empire": "build real digital products once and sell them a thousand times, in plain language",
 "faceless-fortune": "build a faceless media business with a phone, free AI tools, and ninety days of showing up",
 "fiverr-fast-start": "land your first paying freelance clients with nothing but a phone and an internet connection",
 "free-money-handbook": "find the unclaimed money, settlements, and benefits with your name on them, with no hype",
 "instant-ramen-chef": "turn a fifty cent pack of instant ramen into a real noodle shop bowl, fifty ways",
 "laugh-attack": "500 brand new, original one liners in fifteen chapters on everything life throws at you",
 "marketplace-millions": "sell on Facebook Marketplace for same day cash, the complete plain language playbook",
 "mojo-programming": "learn Mojo, the first programming language built from the ground up for the AI hardware era",
 "phone-repair-mastery": "fix your own phone for the cost of the part, and turn that skill into real income",
 "side-hustle-stack": "thirty honest ways to turn just a phone into income, a field guide for starting from zero",
 "solid-state-ev-guide": "understand solid state EV batteries before you buy your next electric car",
 "street-survival-guide": "practical instruction, not inspiration, for surviving on the street when life collapses",
 "zero-dollar-startup": "launch a real business with literally zero dollars, no savings, no credit, no investors",
}
def _fit_desc(title, hook):
    # Branded meta description fitted to 150-160 chars as written in the file.
    import itertools as _itb
    core = "%s by Christopher J. Hanna — %s" % (title, hook)
    clauses = [" — a Hanna Press book from Irish + Nova",
               ". Buy direct from our shop and we keep 100%",
               ", live on Google Play Books",
               ", from Irish + Nova and Hanna Press",
               ". Real lessons, plain language, no fluff"]
    combos = []
    for r in range(len(clauses), 0, -1):
        for combo in _itb.combinations(range(len(clauses)), r):
            d = core + "".join(clauses[i] for i in combo)
            if not d.endswith((".", "%")):
                d += "."
            combos.append(d)
    for d in combos:
        if 150 <= len(d) <= 160:
            return d
    suffix = " — a Hanna Press book from Irish + Nova."
    words = hook.split()
    while words:
        d = "%s by Christopher J. Hanna — %s%s" % (title, " ".join(words), suffix)
        if len(d) <= 160:
            return d
        words.pop()
    return core[:160]

def _book_meta_desc(title, slug):
    return _fit_desc(title, _BOOK_HOOKS.get(slug, "a Hanna Press book"))
# ----- DETAIL RULE breakdown for book detail pages (added 2026-11-10) -----
# Every priced item carries the full breakdown: what you get, how it works,
# timeline, who it fits, not included. Built only from the book's own format
# data above, so prices and routes in the panel can never drift from the stack.
_BOOK_FIT = {
 "phone-flip-playbook": "Beginners starting with $0 to $40 and a phone, who want a legal side hustle they can start this week.",
 "ai-coding-agents-2026": "Complete beginners who want to build real software by directing AI coding agents, in plain English, with no coding background.",
 "embracing-the-unknown": "Anyone facing job loss or a life that stopped following the plan, who needs an honest way to move again.",
 "dad-jokes": "Dads, families, teachers, and anyone who needs clean jokes that land with every age in the room.",
 "digital-product-empire": "Creators who want to build a real digital product once and sell it on repeat, explained in plain language.",
 "faceless-fortune": "Anyone who wants to build a media business without showing their face, using a phone and free AI tools.",
 "fiverr-fast-start": "New freelancers who want their first paying clients with nothing but a phone and an internet connection.",
 "free-money-handbook": "Anyone who suspects money is sitting out there with their name on it — unclaimed funds, settlements, and benefits — and wants to find it without hype.",
 "instant-ramen-chef": "Home cooks who want a fifty cent pack of instant ramen to eat like a real noodle shop bowl.",
 "laugh-attack": "Anyone who needs a deep bench of brand new one liners — for speeches, posts, classrooms, or the dinner table.",
 "marketplace-millions": "Resellers and declutterers who want same day cash from Facebook Marketplace, without getting scammed.",
 "mojo-programming": "Programmers and curious beginners who want Mojo, the first language built from the ground up for the AI hardware era.",
 "phone-repair-mastery": "Anyone who wants to fix their own phone for the cost of the part — and turn that skill into real income.",
 "side-hustle-stack": "Anyone starting from zero with just a phone, who wants honest ways to earn, laid out plainly.",
 "solid-state-ev-guide": "Anyone planning to buy an electric car who wants solid state batteries understood before they spend.",
 "street-survival-guide": "Anyone sleeping rough, couch surfing, or close to the street — and the people who help them.",
 "zero-dollar-startup": "Anyone with no savings, no credit, and no investors who still wants to launch a real business.",
}
_INCOME_NOTE = "No income, sales, or results are promised. The book teaches the method; what it earns depends on your market and your work."
_BOOK_NOTINCL_EXTRA = {
 "phone-flip-playbook": [_INCOME_NOTE, "No phones, parts, tools, or carrier accounts are included — you supply the phones; the book supplies the method."],
 "ai-coding-agents-2026": ["No job, income, or client work is promised. The book teaches the skill; what it earns depends on your work.", "No software, subscriptions, or AI tool accounts are included."],
 "digital-product-empire": [_INCOME_NOTE],
 "faceless-fortune": [_INCOME_NOTE],
 "fiverr-fast-start": [_INCOME_NOTE],
 "free-money-handbook": ["Not every search finds money, and no recovery is promised.", "You file your own claims and keep everything you recover. This book finds and explains; it cannot claim money for you."],
 "marketplace-millions": [_INCOME_NOTE],
 "phone-repair-mastery": [_INCOME_NOTE, "No parts or tools are included — you supply the phone and the part."],
 "side-hustle-stack": [_INCOME_NOTE],
 "zero-dollar-startup": [_INCOME_NOTE],
 "embracing-the-unknown": ["This is a personal story and a framework for moving again — not therapy, counseling, or medical advice."],
 "solid-state-ev-guide": ["Battery dates come from manufacturer announcements and can slip. The book teaches you how to judge the claims; it does not guarantee any launch date."],
 "street-survival-guide": ["General information from lived experience. It is not medical, legal, or official agency advice, and it does not replace local shelters, services, or emergency help."],
 "mojo-programming": ["No software, accounts, or hardware are included."],
 "instant-ramen-chef": ["No ingredients or cookware are included — this is the book only."],
}
def _book_panel(title, slug, extra, has_pv, price_line):
    gets, routes, times = [], [], []
    for _label, _u in extra:
        _nm, _, _pr = _label.rpartition(' $')
        if 'amazon.com' in _u:
            _rt = 'on Amazon'
        elif 'play.google.com' in _u:
            _rt = 'on Google Play Books'
        else:
            _rt = 'EPUB from our shop'
        gets.append('%s edition — $%s (%s)' % (_nm, _pr, _rt))
    gets.append('Every edition is the same complete book.')
    if has_pv:
        gets.append('Real pages from the book are in Look inside on this page, before you buy.')
    if any('amazon.com' in _u for _l, _u in extra):
        routes.append('Kindle and paperback buttons check out securely on Amazon')
    if any('play.google.com' in _u for _l, _u in extra):
        routes.append('the Google Play button checks out on Google Play Books')
    if any(_u == 'shop.html#direct' for _l, _u in extra):
        routes.append("buy direct takes you to the shop's Direct section, where this book sells as an EPUB, yours forever")
    _rj = '; '.join(routes)
    _rj = _rj[:1].upper() + _rj[1:]
    how = ['Choose your format in Get your copy below — every button is labeled with its price.',
           _rj + '.',
           'Or collect first: the Add buttons under the stack put books in the cart, so you can check out once. Discount codes apply in the cart; bundles are excluded, since they are already priced down.']
    if any(('amazon.com' in _u or 'play.google.com' in _u) for _l, _u in extra):
        times.append('Kindle and Google Play editions are delivered by those stores as soon as your purchase completes.')
    if any(_u == 'shop.html#direct' for _l, _u in extra):
        times.append('Direct EPUB orders are emailed by us — usually within a few hours, always the same day.')
    if any(_l.startswith('Paperback') for _l, _u in extra):
        times.append('Paperbacks are printed on demand and shipped by Amazon.')
    _has_pb = any(_l.startswith('Paperback') for _l, _u in extra)
    notincl = ['Every edition except the Amazon paperback is a digital ebook — nothing else ships, and no physical extras are included.' if _has_pb else 'This book is a digital ebook in every edition — nothing physical ships.']
    notincl += _BOOK_NOTINCL_EXTRA.get(slug, [])
    h = '<details class="wyg"><summary>What you get</summary><div class="wygb">'
    h += '<p class="wp">%s</p>' % price_line
    h += '<h4>What you get</h4><ul>' + "".join('<li>%s</li>' % _html.escape(x) for x in gets) + '</ul>'
    h += '<h4>How it works</h4><ol>' + "".join('<li>%s</li>' % _html.escape(x) for x in how) + '</ol>'
    h += '<h4>Timeline</h4><p>%s</p>' % _html.escape(' '.join(times))
    h += '<h4>Who it fits</h4><p>%s</p>' % _html.escape(_BOOK_FIT.get(slug, 'Readers who want this subject taught plainly, start to finish.'))
    h += '<h4>Not included</h4><ul>' + "".join('<li>%s</li>' % _html.escape(x) for x in notincl) + '</ul>'
    h += '</div></details>'
    return h

cards = ""
for cover, title, status, extra in books:
    _bslug = cover.split('/')[0]
    _bfmt = "Kindle &amp; paperback &mdash; live on Amazon now" if status == "live" else ("EPUB ebook &mdash; buy direct or on Google Play Books" if status == "direct" else ("%s &mdash; Kindle &amp; paperback" % extra))
    PV_BOOK_META[_bslug] = (title, _bfmt)
    _dfile = 'book-%s.html' % _bslug
    BOOK_DETAIL_FILES.append(_dfile)
    img = '<img src="%s" alt="%s cover">' % (fileimg(B + cover, 240, 'assets/covers/%s-240.jpg' % _bslug, 76), title)
    _fmt_txt = " &middot; ".join('%s <b>$%s</b>' % (_l.rpartition(' $')[0], _l.rpartition(' $')[2]) for _l, _u in extra)
    cards += '<a class="bkcard" href="%s">%s<div class="bt">%s</div><div class="bkline">%s</div><span class="bkview">View Book</span></a>\n' % (_dfile, img, title, _fmt_txt)
    # ----- per-book detail page -----
    _hook = _BOOK_HOOKS.get(_bslug, "a Hanna Press book")
    _ptitle = "%s — %s | Hanna Press, Irish + Nova" % (title, _hook[:1].upper() + _hook[1:])
    _pdesc = _book_meta_desc(title, _bslug)
    _covimg = '<img src="%s" alt="%s cover">' % (fileimg(B + cover, 300, 'assets/covers/%s-300.jpg' % _bslug, 78), title)
    if pv_has(_bslug):
        _covimg = '<a class="pvlink" href="preview-%s.html" title="Look inside">%s</a>' % (_bslug, _covimg)
    _hero = ('<div class="bkhero"><div class="cov">%s</div><div class="bkinfo">'
             '<div class="bkline">%s</div>'
             '<div class="bkline" style="margin-top:7px">%s</div>'
             '<p class="note" style="margin:12px 0 0">By <b style="color:#ffd95e">Christopher J. Hanna</b> &mdash; Hanna Press, from Irish + Nova.</p>'
             '<p style="margin-top:12px"><a class="lk" href="#get">Get your copy &darr;</a></p>'
             '</div></div>') % (_covimg, _bfmt, _fmt_txt)
    _about = "".join('<p>%s</p>' % _html.escape(p) for p in book_desc(_bslug, limit=100000))
    _dbody = _hero
    _dbody += '<div class="bksec">About this book</div><div class="bkabout">%s</div>' % _about
    if pv_has(_bslug):
        _dbody += '<div class="bksec">Look inside</div>' + big_flipper(_bslug, back_page(title, book_desc(_bslug), _bfmt))
    _rows = ""
    for _label, _u in extra:
        _nm, _, _pr = _label.rpartition(' $')
        _cls = 'buy' if _label.startswith('Buy direct') else 'buy alt'
        _rows += '<a class="%s" href="%s"><span>%s</span><span class="bprice">$%s</span></a>' % (_cls, _u, _nm, _pr)
    _amz = '<p class="bknote">As an Amazon Associate, we earn from qualifying purchases.</p>' if any('amazon.com' in _u for _l, _u in extra) else ''
    _stack = ('<div class="book bookstack" id="get"><div class="bt">%s</div>'
              '<div class="buystack">%s</div>'
              '<p class="bknote">Every route above is the same book in a different format &mdash; pick yours. Buy direct and 100%% of the price stays with us. Collecting several books? Use the Add buttons under the stack and check out once from the cart.</p>%s</div>') % (title, _rows, _amz)
    _dbody += '<div class="bksec">The full breakdown</div>' + _book_panel(title, _bslug, extra, pv_has(_bslug), _fmt_txt)
    _dbody += '<div class="bksec">Get your copy</div>' + _stack
    _dbody += '<p class="note"><a class="lk" href="books.html">&larr; Back to all 19 books</a></p>'
    open(_dfile, 'w').write(page(_ptitle, _pdesc, "books.html", title, _bfmt, _dbody, FLIP_JS if pv_has(_bslug) else ""))
    print('book detail page', _dfile, 'desc', len(_pdesc))
# ----- AI Black Belt Field Guides -----
# Irish's order 2026-11-09: the Field Guides were missing from the catalog
# entirely. Both books are IN PRODUCTION (manuscripts complete; no store route
# is live yet), so per the claims gate their detail pages carry the full
# breakdown and the set series prices as TEXT only, with NO buy buttons. The
# buttons switch on here the day a route actually goes live.
_FG_DIR = '/home/hatch/workspace/your_files/empire/courses/ai-tool-howto-series/'
def _fg_desc(path):
    try:
        raw = open(path).read()
    except Exception:
        return []
    raw = re.sub(r'</?p>', '\n\n', raw)
    raw = _html.unescape(re.sub(r'<[^>]+>', '', raw))
    return [p.strip() for p in raw.split('\n\n') if p.strip()]
_FG_CHAPTERS_11 = ["What ElevenLabs Is, What It Costs, and What It Is Honestly Not For", "Your Account, Set Up Right on the Free Plan", "A Tour of the Interface, Only What You Will Actually Touch", "Your First Generation, From Text on a Page to a Voice You Can Use", "Directing the Voice, Settings, Staging, and Getting the Take You Want", "Voices, The Library, Your Shelf, and Designing a Voice of Your Own", "The Project, A Narrated Story Episode, Built Start to Finish", "Power Moves, Voice Cloning, Dubbing, and the Habits of a Daily User", "The Mistakes Chapter, What Goes Wrong, What It Sounds Like, and the Fix", "Plugging ElevenLabs Into the Rest of Your Work", "Where ElevenLabs Sits in the AI Bible, Book 08, Tools", "Next Steps, The Academy Labs and What to Build Next"]
_FG_CHAPTERS_LOVABLE = ["What Lovable Is, What It Costs, and What It Is Honestly Not For", "Your Account, Set Up Right on the Free Plan", "A Tour of the Interface, Only What You Will Actually Touch", "Your First Prompt, From an Idea to a Working Page", "Talking to the Builder, Edits, Fixes, and Getting Unstuck", "Pages, Sections, and Style, Making It Look Like Your Business", "The Project, A Booking Page for a Local Service, Built Start to Finish", "Power Moves, Databases, Settings, and the Habits of a Daily User", "The Mistakes Chapter, What Breaks, What It Looks Like, and the Fix", "Plugging Lovable Into the Rest of Your Work", "Where Lovable Sits in the AI Bible, Book 08, Tools", "Next Steps, The Academy Labs and What to Build Next"]
FG_BOOKS = [
 dict(dfile='book-how-to-use-lovable.html', title='How to Use Lovable',
      subtitle='Build Real Apps Without Code',
      series='AI Black Belt Field Guides, Book One', animal='The beaver, the builder',
      cover=_FG_DIR + 'book-01-lovable/kdp-kit/cover-front-2000x3000.jpg',
      prices=[("Kindle", "$9.99"), ("Paperback", "$14.99"), ("Buy direct", "$9.99")],
      hook='build real apps without code with Lovable, the step by step field guide for beginners',
      facts='Twelve chapters. The print interior runs 106 pages. Book One of the series.',
      desc=_fg_desc(_FG_DIR + 'book-01-lovable/kdp-kit/description-kdp-source.txt'), chapters=_FG_CHAPTERS_LOVABLE),
 dict(dfile='book-how-to-use-elevenlabs.html', title='How to Use ElevenLabs',
      subtitle='Give Your Work a Voice That Sounds Human',
      series='AI Black Belt Field Guides, Book Two', animal='The nightingale, the voice',
      cover=_FG_DIR + 'book-02-elevenlabs/kdp-kit/cover-front-2000x3000.jpg',
      prices=[("Kindle", "$9.99"), ("Paperback", "$14.99"), ("Buy direct", "$9.99")],
      hook='give your work a voice that sounds human with ElevenLabs, the step by step field guide',
      facts='Twelve chapters, 26,712 words. Book Two of the series.',
      desc=["How to Use ElevenLabs teaches the ElevenLabs AI voice platform the way the Field Guides teach every tool: one book, one tool, start to finish, with a real project you build yourself. By the end you will have written, directed, generated, checked, and exported a complete narrated audio episode that sounds like a person made it on purpose, and you will have proven every part of that with your own ears.",
            "Read it with ElevenLabs open in front of you and a pair of headphones within reach. You do not need recording equipment, a trained voice, or a paid plan. The free plan is enough for every chapter in this book, including the full project in Chapter Seven, as long as you work the way Chapter Two teaches: short drafts, careful settings, and no wasted generations.",
            "The project at the heart of the book is a narrated story episode, built start to finish in Chapter Seven. Around it, the book covers your account on the free plan, the interface controls your hands will actually touch, directing a voice with settings and staging, the Voice Library and designing a voice of your own, voice cloning and dubbing, and the mistakes chapter: what goes wrong, what it sounds like, and the fix.",
            "One rule runs through every chapter that touches cloning: you clone only your own voice, or a voice whose owner has clearly agreed. And one honesty note, printed in the book itself: it makes no promise about money. A voice is a tool. What it earns depends on the work you point it at.",
            "This is Book Two of the AI Black Belt Field Guides from Hanna Press, the series that teaches one AI tool per book, each with one original animal on the cover. ElevenLabs gets the nightingale, the voice."],
      chapters=_FG_CHAPTERS_11),
]
_FG_FIT = {
 'book-how-to-use-lovable.html': "Small business owners, trades, studios, and one person services who keep saying they need a website that actually does something — and anyone with an app idea and no programmer.",
 'book-how-to-use-elevenlabs.html': "Creators, narrators, and small teams who want human sounding voice work without recording equipment, a trained voice, or a paid plan.",
}
def _fg_panel(fg):
    gets = ['%s edition — %s, at launch' % (_n, _p) for _n, _p in fg['prices']]
    gets.append(fg['facts'])
    if fg.get('chapters'):
        gets.append('All twelve chapter titles are listed in What is inside on this page.')
    how = ['This book is in production, so there is nothing to buy on this page yet.',
           'The day distribution opens, this page gains a live button for every edition: Kindle and paperback on Amazon, and the ebook direct from our shop and on our stores.',
           'Until then, the prices shown are the set series prices, so you know exactly what launch will cost.']
    tl = 'The manuscript is complete and the book is in production at Hanna Press. Buying opens the day distribution goes live; no date is promised until a route is verified live.'
    notincl = ['No orders or preorders are taken today.',
               "The tool itself is not included. You use your own account, and every chapter in this book works on the tool's free plan."]
    _wp = ' &middot; '.join('%s %s' % (_n, _p) for _n, _p in fg['prices']) + ' &mdash; at launch'
    h = '<details class="wyg"><summary>What you get</summary><div class="wygb">'
    h += '<p class="wp">%s</p>' % _wp
    h += '<h4>What you get</h4><ul>' + "".join('<li>%s</li>' % _html.escape(x) for x in gets) + '</ul>'
    h += '<h4>How it works</h4><ol>' + "".join('<li>%s</li>' % _html.escape(x) for x in how) + '</ol>'
    h += '<h4>Timeline</h4><p>%s</p>' % _html.escape(tl)
    h += '<h4>Who it fits</h4><p>%s</p>' % _html.escape(_FG_FIT.get(fg['dfile'], 'Readers who want one AI tool taught start to finish.'))
    h += '<h4>Not included</h4><ul>' + "".join('<li>%s</li>' % _html.escape(x) for x in notincl) + '</ul>'
    h += '</div></details>'
    return h

fg_cards = ""
for _fg in FG_BOOKS:
    BOOK_DETAIL_FILES.append(_fg['dfile'])
    _fimg = '<img src="%s" alt="%s cover">' % (fileimg(_fg['cover'], 240, 'assets/covers/%s-240.jpg' % _fg['dfile'][5:-5], 76), _fg['title'])
    _fprice = " &middot; ".join('%s <b>%s</b>' % (_n, _p) for _n, _p in _fg['prices'])
    fg_cards += '<a class="bkcard" href="%s">%s<div class="bt">%s</div><div class="bkline">%s</div><span class="badge">In production</span><br><span class="bkview">View Book</span></a>\n' % (_fg['dfile'], _fimg, _fg['title'], _fprice)
    _ftitle = "%s — %s | Hanna Press, Irish + Nova" % (_fg['title'], _fg['hook'][:1].upper() + _fg['hook'][1:])
    _fdesc = _fit_desc(_fg['title'], _fg['hook'])
    _fcov = '<img src="%s" alt="%s cover">' % (fileimg(_fg['cover'], 300, 'assets/covers/%s-300.jpg' % _fg['dfile'][5:-5], 78), _fg['title'])
    _fhero = ('<div class="bkhero"><div class="cov">%s</div><div class="bkinfo">'
              '<div class="bkline">%s &mdash; Hanna Press</div>'
              '<div class="bkline" style="margin-top:7px">%s, on the cover</div>'
              '<div class="bkline" style="margin-top:7px">%s</div>'
              '<p class="note" style="margin:12px 0 0">By <b style="color:#ffd95e">Irish and Nova</b>. %s</p>'
              '<p style="margin-top:12px"><a class="lk" href="#get">Release details &darr;</a></p>'
              '</div></div>') % (_fcov, _fg['series'], _fg['animal'][:1].upper() + _fg['animal'][1:], _fprice, _fg['facts'])
    _fbody = _fhero
    _fbody += '<div class="bksec">About this book</div><div class="bkabout">%s</div>' % "".join('<p>%s</p>' % _html.escape(p) for p in _fg['desc'])
    if _fg.get('chapters'):
        _fbody += '<div class="bksec">What is inside</div><div class="bkabout"><ul>%s</ul></div>' % "".join('<li>%s</li>' % _html.escape(c) for c in _fg['chapters'])
    _frows = "".join('<div class="fgrow"><span>%s</span><span class="bprice">%s</span></div>' % (_n, _p) for _n, _p in _fg['prices'])
    _fstack = ('<div class="book bookstack" id="get"><div class="bt">%s</div>'
               '<div class="buystack">%s</div>'
               '<p class="bknote">In production at Hanna Press. This book is not on sale yet, so there are no buy buttons here. The prices above are the set series prices, and the day distribution opens, this page gains a live button for every edition: Kindle and paperback on Amazon, and the ebook direct from our shop and on our stores.</p></div>') % (_fg['title'], _frows)
    _fbody += '<div class="bksec">The full breakdown</div>' + _fg_panel(_fg)
    _fbody += '<div class="bksec">Release pricing</div>' + _fstack
    _fbody += '<p class="note"><a class="lk" href="books.html">&larr; Back to all 19 books</a></p>'
    open(_fg['dfile'], 'w').write(page(_ftitle, _fdesc, "books.html", _fg['title'], _fg['series'] + ' &mdash; <b>in production</b>', _fbody))
    print('field guide page', _fg['dfile'], 'desc', len(_fdesc))
_fg_section = ('<div class="sec">AI Black Belt Field Guides</div><div class="grid">%s</div>\n'
               '<p class="note">The Field Guides teach one AI tool per book, start to finish, each with one original animal on the cover. Book One and Book Two are in production at Hanna Press. Their pages carry the full breakdown now, and buying opens on each page the day that book goes live.</p>') % fg_cards

books_body = '''<div class="grid">%s</div>
<p class="note">19 titles from Hanna Press &mdash; money, hustle, tech, humor, and hard-won lessons.<br>Seventeen are live on Google Play Books and buyable direct from our shop; three are also live on Amazon Kindle and paperback. The two Field Guides below are in production and open for sale at launch.</p>
%s
<p class="note">Prefer to listen? All 16 of our Google Play books are also live as audiobooks on Google Play.</p>
<p class="note" style="font-size:.8rem">As an Amazon Associate, we earn from qualifying purchases.</p>''' % (cards, _fg_section)
open('books.html','w').write(page("The Books — Hanna Press by Irish + Nova","All 19 books from Hanna Press by Irish + Nova: money, hustle, tech, humor, hard-won lessons, and the AI Black Belt Field Guides. Live in our shop today.","books.html","THE BOOKS","19 titles. <b>One library.</b>", books_body))

# ---------- SHOP ----------
shop_body = card("https://irish007.gumroad.com","&#128717;&#65039; GUMROAD","Wallpaper mega packs, prompt packs, coloring books.")
shop_body += card("https://whop.com/irish007/products","&#127978; WHOP STORE","Every digital product, one storefront.")
shop_body += '<div class="sec">Featured right now</div>'
for url, t, s in [
 ("https://irish007.gumroad.com/l/dvmqmu","&#9878;&#65039; 52 AI PROMPTS FOR LAWYERS — $19","Intake, explainers, marketing, practice management. Ethics-safe, plug-and-play."),
 ("https://irish007.gumroad.com/l/agdpv","&#127968; 52 AI PROMPTS FOR MORTGAGE BROKERS — $19","Borrower emails, realtor scripts, market updates."),
 ("https://irish007.gumroad.com/l/jrplkj","&#129463; 52 AI PROMPTS FOR DENTISTS — $19","Reminders, recalls, review requests, front-desk scripts."),
 ("https://irish007.gumroad.com/l/uubasi","&#127875; HALLOWEEN WALLPAPER MEGA BUNDLE — $8","Two spooky phone theme packs in one bundle."),
 ("https://irish007.gumroad.com/l/vrqjpd","&#10013;&#65039; BIBLE VERSE COLORING BOOK — $10","25 faith pages with KJV scripture. Print at home, color forever."),
 ("https://irish007.gumroad.com/l/jkcrs","&#127876; COZY CHRISTMAS COLORING BOOK — $8","25 cozy scenes &amp; scripture, 300 DPI print-ready."),
 ("https://irish007.gumroad.com/l/bifcdk","&#127919; VISION BOARD RESOLUTION 2027 — $10","Set the goals, map the year, track it monthly."),
]:
    shop_body += card(url, t, s)
open('shop.html','w').write(page("Shop — Irish's Digital Products","Digital products by Irish: AI prompt packs, coloring books, wallpaper bundles, planners. Ko-fi, Gumroad, Whop.","shop.html","THE SHOP","Digital products that <b>earn their keep.</b>", shop_body))

# ---------- SLEEP ----------
sleep_body = card("https://whatwedoindarkness.bandcamp.com/album/colors-of-noise-sleep-focus-vol-1","&#127911; COLORS OF NOISE — THE ALBUM","Sleep &amp; Focus, Vol. 1. Five noise colors &times; 12 minutes. $7 or more on Bandcamp.", True)
def _sleeptile(vid, t, blurb):
    return '<div class="card"><div class="t"><a href="https://youtu.be/%s" target="_blank" rel="noopener">%s</a></div><div class="s">%s</div>%s<noscript><div class="s"><a href="https://youtu.be/%s">Watch on YouTube</a></div></noscript></div>\n' % (vid, clean_title(t.replace('&', '&amp;')), blurb, vidfac(vid), vid)
sleep_body += '<div class="sec">Sleep films &amp; noise — every public video</div>'
for vid, t, _sh in [x for x in SLEEP_VIDS if not x[2]]:
    sleep_body += _sleeptile(vid, t, "From What We Do In Darkness. Plays right here on this page.")
sleep_body += '<div class="sec">Sleep Shorts</div>'
for vid, t, _sh in [x for x in SLEEP_VIDS if x[2]]:
    sleep_body += _sleeptile(vid, t, "A short one from What We Do In Darkness. Plays right here on this page.")
sleep_body += chancard("https://www.youtube.com/@WhatWeDoInDarkness","&#127769; THE CHANNEL — WHAT WE DO IN DARKNESS","New colors and scenes dropping. Subscribe and sleep better.","UC6M4P62to1D6jMt0smdqiNQ")
open('sleep.html','w').write(page("Sleep Sounds &amp; Noise Videos — What We Do In Darkness","Sleep sounds by Irish + Nova: 10-hour white, brown, pink, and blue noise videos plus the Colors of Noise album — deep sleep, focus, and tinnitus relief nightly.","sleep.html","SLEEP SOUNDS","Ten hours a night, <b>every night.</b>", sleep_body))

# ---------- FOR THOSE WHO SERVED (photo submissions, 2026-10-19) ----------
_served_hero = fileimg('media-generation-served-hero-0-629b9bab-4f09-438f-b1ca-3c1d0dc8601b.jpg', 880, 'assets/served-hero.jpg', 68)
served_body = '<style>'
served_body += '.svform{background:linear-gradient(165deg,#151a13,#0f120e);border:1px solid #d4af37;border-radius:14px;padding:20px;margin:12px 0}'
served_body += '.svform label{display:block;font-family:Oswald,sans-serif;font-size:.86rem;letter-spacing:.08em;text-transform:uppercase;color:#ffd95e;margin:16px 0 6px}'
served_body += '.svform label:first-of-type{margin-top:0}'
served_body += '.svform .hint{color:#a3b5a4;font-size:.88rem;margin:5px 0 0;line-height:1.5}'
served_body += '.svform input[type=file],.svform input[type=email],.svform textarea{width:100%;background:#0b0f0b;border:1px solid #37402f;border-radius:9px;color:#ece9e0;padding:11px 12px;font-family:Barlow,sans-serif;font-size:.98rem}'
served_body += '.svform label.consent{display:flex;gap:10px;align-items:flex-start;font-family:Barlow,sans-serif;text-transform:none;letter-spacing:0;color:#dfe4d8;font-size:.95rem;line-height:1.5;margin-top:18px;cursor:pointer}'
served_body += '.svform label.consent input{margin-top:3px;width:18px;height:18px;flex:none}'
served_body += '.upbtn{display:block;width:100%;margin-top:18px;background:#d4af37;color:#111;font-family:Oswald,sans-serif;font-weight:700;font-size:1.05rem;letter-spacing:.06em;padding:14px;border:0;border-radius:10px;cursor:pointer;text-transform:uppercase}'
served_body += '.upbtn:hover{background:#ffd95e}'
served_body += '</style>'
served_body += '<img src="' + _served_hero + '" alt="American flag flying at dawn over rows of white headstones" style="width:100%;height:auto;border-radius:14px;border:1px solid #d4af37;box-shadow:0 12px 34px rgba(0,0,0,.55);margin:0 0 6px">'
served_body += '<div class="card hero"><div class="t">A FILM BUILT FROM YOUR PHOTOS</div><div class="s">We are making a Veterans Day sleep film for our channel, What We Do In Darkness. It is called Rain on Tent Canvas, For Those Who Served: one calm night of rain on canvas, built to honor the men and women who served. We want it filled with real faces, including yours. Send us a photo of someone who served, and we will weave it into the film.</div></div>'
served_body += '<div class="sec">What to send</div>'
served_body += '<div class="card"><div class="t">THE PHOTO</div><div class="s">One clear photo of the person who served, or of their grave or headstone. In uniform, on duty, or a favorite portrait. Any era, any branch. Veterans and the fallen are both welcome here.</div></div>'
served_body += card("submit.html","&#9998; WORDS AND MORE","A favorite quote, a letter, a poem, or their story in your words: anything you want honored alongside them is welcome. Send words on their own through our Send It To Nova page and pick Quotes, letters, and words.")
served_body += '<div class="card"><div class="t">NO NAMES, JUST HONORED</div><div class="s">Photos appear in the film with no names attached and nothing announced. They are simply there, honored, the way a photograph on the mantel is.</div></div>'
served_body += '<div class="card"><div class="t">THE DATES</div><div class="s">Please send photos by Sunday, November 1, 2026, so we can finish the film in time. It premieres on Veterans Day, Wednesday, November 11, 2026, on What We Do In Darkness.</div></div>'
served_body += '<div class="sec">Send their photo</div>'
served_body += '<form class="svform" action="https://formsubmit.co/593f14d5528cf6abad38eef7b60d8b16" method="POST" enctype="multipart/form-data">'
served_body += '<input type="hidden" name="_subject" value="For Those Who Served: new photo submission">'
served_body += '<input type="hidden" name="_template" value="table">'
served_body += '<input type="hidden" name="_next" value="https://chris007hanna-cpu.github.io/for-those-who-served.html?sent=1">'
served_body += '<label for="sv-photo">Upload their photo</label>'
served_body += '<input id="sv-photo" type="file" name="photo" accept="image/*" required>'
served_body += '<p class="hint">One clear photo, any era, any branch. A JPG or PNG works best.</p>'
served_body += '<label for="sv-about">Anything you want us to know about them</label>'
served_body += '<textarea id="sv-about" name="about_them" rows="4"></textarea>'
served_body += '<p class="hint">Kept private. This is never shown in the film.</p>'
served_body += '<label for="sv-email">Your contact email (optional)</label>'
served_body += '<input id="sv-email" type="email" name="contact_email" placeholder="you@example.com">'
served_body += '<p class="hint">Only if you want us to be able to reach you about your submission.</p>'
served_body += '<label class="consent"><input type="checkbox" name="consent" value="Yes: I have the right to share this photo and I give permission for it to appear in the film" required><span>I have the right to share this photo and I give permission for it to appear in the film.</span></label>'
served_body += '<button class="upbtn" type="submit">Upload Your Photo</button>'
served_body += '</form>'
served_body += '<p class="note">You keep every right to your photo. Sending it gives us permission to include it in the film and in promotion for the film, nothing more. Questions about a submission: whatwedoindarkness@gmail.com</p>'
served_body += chancard("https://www.youtube.com/@WhatWeDoInDarkness","&#127769; WATCH THE FILM ON WHAT WE DO IN DARKNESS","Rain on Tent Canvas, For Those Who Served premieres on Veterans Day, November 11, 2026. Subscribe now so you do not miss it.","UC6M4P62to1D6jMt0smdqiNQ")
served_body += card("index.html","ALL OUR LINKS","Books, products, services, and every channel, in one place.")
open('for-those-who-served.html','w').write(page("For Those Who Served: Veterans Photo Submissions | Irish + Nova","Send a photo of someone who served for our Veterans Day film on What We Do In Darkness. Photos are honored with no names attached. Send yours by Nov 1, 2026.","sleep.html","FOR THOSE WHO SERVED","Their photo in the film. <b>No names, just honored.</b>", served_body))
print('for-those-who-served.html', os.path.getsize('for-those-who-served.html'))

# ---------- SEND IT TO NOVA (submissions hub, 2026-10-19) ----------
submit_body = '<style>'
submit_body += '.svform{background:linear-gradient(165deg,#151a13,#0f120e);border:1px solid #d4af37;border-radius:14px;padding:20px;margin:12px 0}'
submit_body += '.svform label{display:block;font-family:Oswald,sans-serif;font-size:.86rem;letter-spacing:.08em;text-transform:uppercase;color:#ffd95e;margin:16px 0 6px}'
submit_body += '.svform label:first-of-type{margin-top:0}'
submit_body += '.svform .hint{color:#a3b5a4;font-size:.88rem;margin:5px 0 0;line-height:1.5}'
submit_body += '.svform input[type=file],.svform input[type=email],.svform input[type=text],.svform select,.svform textarea{width:100%;background:#0b0f0b;border:1px solid #37402f;border-radius:9px;color:#ece9e0;padding:11px 12px;font-family:Barlow,sans-serif;font-size:.98rem}'
submit_body += '.svform label.consent{display:flex;gap:10px;align-items:flex-start;font-family:Barlow,sans-serif;text-transform:none;letter-spacing:0;color:#dfe4d8;font-size:.95rem;line-height:1.5;margin-top:18px;cursor:pointer}'
submit_body += '.svform label.consent input{margin-top:3px;width:18px;height:18px;flex:none}'
submit_body += '.upbtn{display:block;width:100%;margin-top:18px;background:#d4af37;color:#111;font-family:Oswald,sans-serif;font-weight:700;font-size:1.05rem;letter-spacing:.06em;padding:14px;border:0;border-radius:10px;cursor:pointer;text-transform:uppercase}'
submit_body += '.upbtn:hover{background:#ffd95e}'
submit_body += '</style>'
submit_body += '<div class="card hero"><div class="t">ONE FRONT DOOR FOR EVERYTHING YOU SEND US</div><div class="s">A photo for the veterans film. A picture of a grave or a headstone. Words you want carried with someone who served: a favorite quote, a letter, a poem, their story. An audition clip. A newspaper clipping. Anything you want included is welcome here. Pick what you are sending, attach a file or paste a link, and hit send. Nova reviews everything that lands here.</div></div>'
submit_body += card("for-those-who-served.html","&#127482;&#127480; SENDING A PHOTO FOR THE VETERANS FILM?","For Those Who Served has its own page with the full story. Send photos by November 1, 2026. They appear in the film with no names attached, just honored. The form below works too, just pick the veterans category.", True)
submit_body += '<div class="sec">What each one means</div>'
submit_body += '<div class="card"><div class="t">VETERANS FILM: PHOTO FOR FOR THOSE WHO SERVED</div><div class="s">A photo of someone who served, for our Veterans Day film. Any era, any branch. No names in the film, just honored.</div></div>'
submit_body += '<div class="card"><div class="t">GRAVES AND HEADSTONES</div><div class="s">A photo of their grave or headstone, the place where they rest.</div></div>'
submit_body += '<div class="card"><div class="t">QUOTES, LETTERS, AND WORDS</div><div class="s">A favorite quote, a letter, a poem, or their story in your words, carried with their beat in the film.</div></div>'
submit_body += '<div class="card"><div class="t">AUDITION: SINGERS</div><div class="s">Send a clip or a link of you singing. Nova listens to every single one.</div></div>'
submit_body += '<div class="card"><div class="t">AUDITION: MODELS AND ACTORS</div><div class="s">Photos, reels, clips, whatever you have. New faces are welcome here.</div></div>'
submit_body += '<div class="card"><div class="t">AUDITION: BANDS (SLEEP SESSIONS)</div><div class="s">A track or a live clip from your band, for our Band Sleep Sessions.</div></div>'
submit_body += '<div class="card"><div class="t">PHOTOS FOR OUR CHANNELS</div><div class="s">Pictures you shot that fit our channels and pages.</div></div>'
submit_body += '<div class="card"><div class="t">NEWSPAPER ARTICLE OR STORY</div><div class="s">A clipping, a scan, or a link to a story you want us to see.</div></div>'
submit_body += '<div class="card"><div class="t">VIDEO CLIP OR LINK</div><div class="s">Any clip worth our eyes. Paste the link or upload the file.</div></div>'
submit_body += '<div class="card"><div class="t">OTHER</div><div class="s">If it does not fit a box above, it goes here.</div></div>'
submit_body += '<div class="card"><div class="t">NO FORM NEEDED</div><div class="s">You can also simply reply to Nova on any platform with your pics, links, video clips, and articles: Instagram, Facebook, TikTok, YouTube, wherever you already talk to us. This page just keeps everything in one pile so nothing gets lost.</div></div>'
submit_body += '<div class="sec">Send it</div>'
submit_body += '<form class="svform" id="sb-form" action="https://formsubmit.co/593f14d5528cf6abad38eef7b60d8b16" method="POST" enctype="multipart/form-data">'
submit_body += '<input type="hidden" id="sb-subject" name="_subject" value="New submission from the Send It To Nova page">'
submit_body += '<input type="hidden" name="_template" value="table">'
submit_body += '<input type="hidden" name="_next" value="https://chris007hanna-cpu.github.io/submit.html?sent=1">'
submit_body += '<label for="sb-cat">What are you sending?</label>'
submit_body += '<select id="sb-cat" name="category" required><option value="" disabled selected>Choose one...</option><option value="Veterans Film: photo for For Those Who Served">Veterans Film: photo for For Those Who Served</option><option value="Graves and headstones">Graves and headstones</option><option value="Quotes, letters, and words">Quotes, letters, and words</option><option value="Audition: Singers">Audition: Singers</option><option value="Audition: Models and Actors">Audition: Models and Actors</option><option value="Audition: Bands (Sleep Sessions)">Audition: Bands (Sleep Sessions)</option><option value="Photos for our channels">Photos for our channels</option><option value="Newspaper article or story">Newspaper article or story</option><option value="Video clip or link">Video clip or link</option><option value="Other">Other</option></select>'
submit_body += '<label for="sb-name">Your name (optional)</label>'
submit_body += '<input id="sb-name" type="text" name="sender_name" placeholder="Your name">'
submit_body += '<label for="sb-email">Your contact email</label>'
submit_body += '<input id="sb-email" type="email" name="contact_email" placeholder="you@example.com">'
submit_body += '<p class="hint">Optional, but add it if you want Nova to be able to reply to you about your submission.</p>'
submit_body += '<label for="sb-link">A link (optional)</label>'
submit_body += '<input id="sb-link" type="text" name="link" placeholder="https://...">'
submit_body += '<p class="hint">For audition videos, clips, and articles that already live online.</p>'
submit_body += '<label for="sb-file">Upload a file (optional)</label>'
submit_body += '<input id="sb-file" type="file" name="attachment" accept="image/*,.pdf" multiple>'
submit_body += '<p class="hint">Photos, pics, and scans of newspaper articles. JPG or PNG works best.</p>'
submit_body += '<label for="sb-notes">Tell us about it</label>'
submit_body += '<textarea id="sb-notes" name="notes" rows="4"></textarea>'
submit_body += '<p class="hint">Who is in it, where it came from, or the words you want carried with them.</p>'
submit_body += '<label class="consent"><input type="checkbox" name="consent" value="Yes: I have the right to share this and I give permission for Irish + Nova to review it and, where relevant, feature it" required><span>I have the right to share this and I give permission for Irish + Nova to review it and, where relevant, feature it.</span></label>'
submit_body += '<button class="upbtn" type="submit">Send It To Nova</button>'
submit_body += '</form>'
submit_body += '<p class="note">You keep every right to what you send. Sending it gives us permission to review it and, where it fits the category you picked, to feature it. Nothing gets sold and nothing goes anywhere else. Questions about a submission: whatwedoindarkness@gmail.com</p>'
submit_body += card("watch.html","&#128250; WATCH OUR CHANNELS","Seventeen YouTube channels and our TikToks: sleep sounds, ramen, dark tales, broke cooking, phone flipping, horoscopes, survival skills, and more.")
submit_body += card("talent.html","&#127908; THE TALENT HUB","Singers, models, actors, and bands: see the roster and where you could land.")
submit_body += card("index.html","ALL OUR LINKS","Books, products, services, and every channel, in one place.")
submit_script = '<script>(function(){var c=document.getElementById("sb-cat"),s=document.getElementById("sb-subject"),f=document.getElementById("sb-form");function upd(){if(c&&s&&c.value){s.value="Send It To Nova: "+c.value;}}if(c){c.addEventListener("change",upd);}if(f){f.addEventListener("submit",upd);}})();</script>'
open('submit.html','w').write(page("Send It To Nova: Submissions and Auditions | Irish + Nova","Send it to Nova: one page for veterans film photos, singer, model, actor and band auditions, channel photos, articles and video clips. We review it all.","submit.html","SEND IT TO NOVA","Photos, auditions, articles, clips. <b>One page, Nova reviews it all.</b>", submit_body, submit_script))
print('submit.html', os.path.getsize('submit.html'))

# ---------- WATCH ----------
watch_body = '<div class="sec">YouTube channels</div>'
watch_body += appcard()
for url, t, s, ucid in [
 ("https://www.youtube.com/@AIBlackBeltHQ","&#129355; AI BLACK BELT","Earn your black belt in AI \u2014 free lessons, pro systems.","UC1os6Wse_GZEkUw10Y0WxBQ"),
 ("https://www.youtube.com/@BrokeSurvivalGuide","&#9978; BROKE SURVIVAL GUIDE","Real survival skills for when the money runs out, free resources, street skills, and getting back on your feet starting from zero.","UCLIZHhTq6Pr3CZqYZgCqVbg"),
 ("https://www.youtube.com/@DarkTalesRetoldTV","&#128214; DARK TALES RETOLD","Stories after dark.","UCeLSNAQUPYVs9vF6rG4Edcg"),
 ("https://www.youtube.com/@GildedHeartsDramaOfficial","&#127917; GILDED HEARTS DRAMA","Original romance dramas, clean and sweeping.","UCodnwgPUqXfIMeLUTIZFmAw"),
 ("https://www.youtube.com/@MicroFarmerOfficial","&#127793; MICRO FARMER","Small livestock, aquaponics, microgreens, mushrooms, quail and homestead gigs, small scale. The Shrimp Farmer is the flagship series.","UCr4Chp7whht_UR9syZJ-1Ww"),
 ("https://www.youtube.com/@OnePotBrokeKitchen","&#127858; ONE-POT BROKE KITCHEN","Real food, no money.","UCzPkgcxxy2-ZQxwtOHypjeQ"),
 ("https://www.youtube.com/@PaperFirstTrading","&#128200; PAPER FIRST TRADING","The journal proves itself on paper first.","UCjEckDqnLQTCBIT4JaMP0VA"),
 ("https://www.youtube.com/@PawsWhileYouWork","&#128062; PAWS WHILE YOU WORK","Dog TV for the workday: nature worth watching, all day long.","UCOa38iZ_dzxk98hBiQRsl6Q"),
 ("https://www.youtube.com/@PhoneFlipAcademy","&#128241; PHONE FLIP ACADEMY","Buy low, sell high — phones.","UCmOTdy0tWfsEOePjpIA1P3w"),
 ("https://www.youtube.com/channel/UCXD_Tww1wi5pn2n3JxGhLtw","&#129302; ROBOT BRAIN WORKSHOP","Old drawer phones become robot brains.","UCXD_Tww1wi5pn2n3JxGhLtw"),
 ("https://www.youtube.com/@SimpleSurvivalHQ","&#127794; SIMPLE SURVIVAL","Simple survival that actually works. Real skills, no hype.","UCttOpXwbrJTwIOuoAf0GXsw"),
 ("https://www.youtube.com/@ClaimVsRecord","&#9878;&#65039; THE CLAIM VS. THE RECORD","The claim, checked against the real record.","UCEUUYLKRajxVicLbFP2Kflg"),
 ("https://www.youtube.com/@TheCrowDecoded","&#128038; THE CROW DECODED","How smart crows and ravens really are, proven study by study.","UCJ1YbFbuwBjJebnQb9ebboA"),
 ("https://www.youtube.com/@TheInstantRamenChef","&#127836; THE INSTANT RAMEN CHEF!","Making instant ramen awesome — bold upgrades from a normal home kitchen.","UC5nNRc2NdXLV1FXln9TZh9g"),
 ("https://www.youtube.com/@WhatIfMachineTV","&#127744; WHAT IF MACHINE","One change rewrites everything.","UCvnip76il00fnmbQtcuxiFA"),
 ("https://www.youtube.com/@WhatWeDoInDarkness","&#127769; WHAT WE DO IN DARKNESS","Sleep &amp; focus noise.","UC6M4P62to1D6jMt0smdqiNQ"),
 ("https://www.youtube.com/@WrittenInTheStarsDaily","&#10024; WRITTEN IN THE STARS DAILY","Your horoscope, every morning.","UCU2K7DdBvh3EgdulrttEXqA"),
]: watch_body += chancard(url, t, s, ucid)
watch_body += '<div class="sec">TikTok</div>'
for url, t, s in [
 ("https://www.tiktok.com/@irish00769","&#127925; @irish00769","The main feed — empire building daily."),
 ("https://www.tiktok.com/@theinstantramenchef","&#127836; @theinstantramenchef","Ramen, short and loud."),
 ("https://www.tiktok.com/@whatwedoindarknes1","&#127769; @whatwedoindarknes1","Sleep sounds, short form."),
]: watch_body += card(url, t, s)
watch_body += '<div class="sec">Channel apps</div>'
watch_body += '<div class="card"><div class="s">Free Android apps, one per channel. Each app carries its channel videos and sends you straight back to watch them. Tap a card to download the APK, open it on your phone, and allow the install when Android asks.</div></div>'
for url, t, s in [
 ("assets/downloads/ai-black-belt-v1.apk","&#129355; AI BLACK BELT APP","Earn your black belt in AI: the AI Black Belt lessons app."),
 ("assets/downloads/claim-vs-record-v1.apk","&#9878;&#65039; CLAIM VS. THE RECORD APP","The claim, checked against the real record: every episode in one place."),
 ("assets/downloads/dark-tales-v1.apk","&#128214; DARK TALES APP","Stories after dark: the Dark Tales Retold companion."),
 ("assets/downloads/flip-scanner-v1.apk","&#128241; FLIP SCANNER APP","Phone Flip Academy in your pocket: the flip checks from the lessons."),
 ("assets/downloads/one-pot-v1.apk","&#127858; ONE POT RECIPES APP","The One-Pot Broke Kitchen recipes, searchable, with favorites."),
 ("assets/downloads/paper-trading-journal-v1.apk","&#128200; PAPER TRADING JOURNAL APP","The Paper First Trading logbook for paper sessions."),
 ("assets/downloads/paws-while-you-work-v1.apk","&#128062; PAWS WHILE YOU WORK APP","Dog TV episodes for Paws While You Work, plus the leaving home checklist."),
 ("assets/downloads/ramen-chef-v1.apk","&#127836; RAMEN CHEF RECIPES APP","All 71 ramen recipes from the book and The Instant Ramen Chef! channel."),
 ("assets/downloads/robot-brain-v1.apk","&#129302; ROBOT BRAIN APP","Old drawer phones become robot brains: the Robot Brain Workshop companion."),
 ("assets/downloads/simple-survival-v1.1.apk","&#127794; SIMPLE SURVIVAL APP","Offline survival skills plus the Simple Survival episode list."),
 ("assets/downloads/sleep-scenes-v1.apk","&#127769; SLEEP SCENES APP","The What We Do In Darkness companion: scenes and sleep films in one place."),
 ("assets/downloads/sleep-sounds-v1.apk","&#127911; SLEEP SOUNDS APP","The sound library from the sleep channel, ready on your phone."),
 ("assets/downloads/what-if-machine-v1.apk","&#127744; WHAT IF MACHINE APP","One change rewrites everything: every What If Machine video in one place."),
 ("assets/downloads/written-in-the-stars-v1.apk","&#10024; WRITTEN IN THE STARS APP","Every daily reading and sign Short from Written in the Stars Daily."),
]: watch_body += card(url, t, s)
open('watch.html','w').write(page("Watch — Irish + Nova: Seventeen YouTube Channels &amp; Videos","Watch Irish + Nova: seventeen YouTube channels and three TikToks. Sleep sounds, ramen, dark tales, survival skills, dog TV, robot builds, and paper trading.","watch.html","WATCH","Seventeen channels. <b>Zero boring.</b>", watch_body))

def _D(get, fits, notincl, **kw):
    d = {'get': get, 'fits': fits, 'notincl': notincl}
    d.update(kw)
    return d

_HYBRID = "Prefer a manager-style deal? This page also offers the hybrid — $295/mo + 10% of the revenue we generate for you. Ask us and we will map both options."
_OWN = "You keep 100% ownership of your work, pages, and accounts — we work for you"
_NOGUARANTEE = "Results are worked for, never guaranteed — the other side always decides"

DETAILS.update({
# ================= SERVICES (Fiverr gigs + build & design + summaries) =================
('*','NONFICTION-EBOOK-GHOSTWRITING'): _D(
 ["A nonfiction manuscript built from your idea", "Structured like a book that sells", "Written in your voice", "Finished manuscript delivered through Fiverr"],
 "Founders, experts, and professionals with a book in them and no time to write it.",
 ["Publishing and marketing the book (see Become an Author on the Virtual Services page)", "Fiction manuscripts"]),
('*','KINDLE-PAPERBACK-FORMATTING'): _D(
 ["Clean, professional KDP formatting for Kindle", "Clean, professional KDP formatting for paperback", "Upload-ready files — no errors, no headaches"],
 "Authors with a finished manuscript that needs to go up on Amazon cleanly.",
 ["Cover design (see Book Cover Design)", "Editing the manuscript text itself"]),
('*','10-TIKTOK-SCRIPTS'): _D(
 ["10 short-form scripts", "Hooks built into every script", "Written for your niche", "Ready to film"],
 "Creators and businesses who post short-form video and run dry on ideas.",
 ["Filming or editing the videos", "Posting them for you (see Social Media Management)"]),
('*','YOUTUBE-SEO-TITLES-DESCRIPTIONS-TAGS'): _D(
 ["Clickable titles written for your videos", "Keyword-loaded descriptions", "Tags that rank"],
 "YouTubers whose videos deserve more search traffic than they get.",
 ["Video editing or uploads", "Full channel management (see YouTube Channel Management)"]),
('*','SOCIAL-MEDIA-MANAGEMENT'): _D(
 ["Instagram, TikTok, and Facebook run end-to-end", "Posting handled for you", "Captions written for you", "Engagement handled for you"],
 "Owners and creators who need their socials run daily without living on their phone.",
 ["Paid advertising campaigns", "Long-form video production (see our channel and video services)"]),
('*','WEBSITE-DESIGN-AND-BUILD'): _D(
 ["A fast, real website you own — like this one", "Business sites, link hubs, shops, and landing pages built for you"],
 "Businesses that need a real website without agency pricing games.",
 ["A custom domain name — yours to register; we point it at your site", "Ongoing management after launch (see Website Building &amp; Management)"]),
('*','APP-CREATION'): _D(
 ["Your app designed and built", "Prototype through launch-ready", "Built around what you want the app to do"],
 "Founders with an app idea and no dev team.",
 ["App store fees charged by Apple or Google", "Ongoing maintenance after launch (scoped separately if you want it)"],
 price="Custom quote — message us with the idea and we scope it"),
('*','FULL-STORE-SETUP'): _D(
 ["Your Ko-fi, Gumroad, or Whop store built for you", "Products loaded", "Payments wired", "Ready to sell"],
 "Sellers who want a working store without the setup headache.",
 ["The products themselves (we build those too — see the Shop)", "Fees charged by the store platform"],
 price="Custom quote — message us about your store"),
('*','BOOK-COVER-DESIGN'): _D(
 ["Covers that sell the click", "Kindle cover", "Paperback wrap", "Audiobook square"],
 "Authors who need a cover that looks like it belongs on the shelf.",
 ["Interior formatting (see KDP Formatting)", "Publishing the book itself"]),
('*','YOUTUBE-THUMBNAILS'): _D(
 ["Thumbnails that punch — bold, clickable, on-brand", "Designed per video"],
 "YouTubers who want clicks, not just views sitting in search.",
 ["Titles and descriptions (see YouTube SEO)", "Channel management"]),
('*','AI-SETUP-FOR-YOUR-BUSINESS'): _D(
 ["Your own AI workhorse, set up for your business", "Content workflows set up", "Customer reply workflows set up", "Bookkeeping prompts set up", "Trained on your business"],
 "Owners who want AI doing real work, not another app to learn.",
 ["AI platform subscriptions charged by the AI providers", "Replacing your staff — this makes your team faster"],
 price="Custom quote — message us about your business"),
('*','AI-MEMORY-SYNC-SETUP-DONE-FOR-YOU'): _D(
 ["Standard Setup ($149): your AI Memory Sync vault structure created in your own cloud storage, in plain text files you own",
  "Your primary AI connected and loaded with the starter capsule",
  "The basics configured: your key facts, your projects, and your preferences in place",
  "A plain language walkthrough on the call, so you can run and update the vault yourself afterward",
  "Plus Setup ($295): everything in Standard Setup",
  "A second AI connected and synced to the same vault",
  "A month of weekly check-ins to tune the vault to how you actually use it"],
 "Owners of the AI Memory Sync Kit who would rather have their vault built with them on a call than set it up alone, and anyone who wants a second AI sharing the same memory.",
 ["The AI Memory Sync Kit itself, if you do not own it yet (it is in the Shop)",
  "Your AI provider accounts and any subscriptions those providers charge",
  "New writing for your vault beyond the starter capsule and your basics",
  "Ongoing management after the Plus month of check-ins ends"],
 how=["Message us to book your setup and tell us which AI you use most.",
  "We confirm your tier and schedule your guided call in writing before anything starts.",
  "On the call, we build your vault with you: the structure created, your AI connected, the starter capsule loaded, and the basics configured.",
  "You finish the call running the vault yourself, with the walkthrough fresh in hand."],
 timeline="Setup calls are scheduled within a few business days of your message, and the setup itself happens on that one call. Plus Setup check-ins run weekly for one month from your setup call."),
('*','STORE-LISTING-COPY'): _D(
 ["Product descriptions that convert browsers into buyers", "Written for any marketplace"],
 "Sellers whose listings get views but not sales.",
 ["Store setup (see Full Store Setup)", "Product photography"]),
('*','ARTIST-REPRESENTATION'): _D(
 ["Full-stack representation for musicians — socials, YouTube, distribution, fan club, merch, and press", "Monthly tiers at $195, $495, and $995", "One-time packages on the Artists page too: press kits, launch campaigns, channel rebuilds"],
 "Musicians ready for a machine behind the music.",
 ["Nothing is ordered from this card — the Artists page carries the full breakdown"],
 how=["Open the Artists page for the full breakdown of every tier and package.", "Message us about your music and your goals.", "We map the right tier or package with you before anything starts."]),
('*','REAL-ESTATE-MARKETING-FOR-AGENTS-AND-BROKERAGES'): _D(
 ["Social media management", "A video for every listing", "Monthly content calendars", "Market report videos", "AI training for your office", "Full breakdown on the Real Estate page"],
 "Agents and brokerages whose marketing should look like their listings.",
 ["Nothing is ordered from this card — programs are by consultation on the Real Estate page"],
 how=["Open the Real Estate page for the full breakdown.", "Message us with your market and your volume.", "We reply with the right program for you."]),
('*','VIRTUAL-SERVICES-DONE-FOR-YOU-FROM-ANYWHERE'): _D(
 ["Audiobook Production — from $149 per finished hour", "Become an Author — from $1,495", "Podcast Production — from $79 per episode", "YouTube Channel Management — from $395/mo", "Virtual Front Office — from $295/mo", "Resume &amp; LinkedIn Makeover — from $59"],
 "Anyone who wants the work done for them, from anywhere — every service here is delivered 100% online.",
 ["Nothing is ordered from this card — each service is scoped on the Virtual Services page first"],
 how=["Open the Virtual Services page for the full breakdown of each service.", "Message us with the job.", "We confirm the package and price with you, then we do the work."]),
# ================= VIRTUAL =================
('*','AUDIOBOOK-PRODUCTION'): _D(
 ["Your book professionally narrated", "Mastered, ACX-ready files", "Handled end to end", "Produced with the exact pipeline behind our 16 audiobooks"],
 "Authors with a finished book that needs an audio edition.",
 ["Writing or editing the book (see Become an Author)", "Your own ACX or Audible account setup"],
 price="From $149 per finished hour",
 timeline="Priced per finished hour of audio — we confirm your total from your word count before we start."),
('*','BECOME-AN-AUTHOR'): _D(
 ["A book with your name on it", "We write it with you", "Formatted for Amazon", "Cover designed", "Walked onto Amazon through Hanna Press"],
 "Founders and professionals who want the authority of a book without writing it themselves.",
 ["Guaranteed sales or bestseller status — nobody honest can promise that", "Your Amazon KDP account itself (we walk you through it)"],
 price="From $1,495 — full package"),
('*','PODCAST-PRODUCTION'): _D(
 ["You record — we do the rest", "Episodes cut and edited", "Show notes written", "Clips pulled", "Posted everywhere"],
 "Podcasters who would rather record than edit.",
 ["Recording your parts — that is the one thing only you can do", "Podcast hosting platform fees"]),
('*','YOUTUBE-CHANNEL-MANAGEMENT'): _D(
 ["Uploads handled", "Titles written", "Thumbnails handled", "Shorts handled", "Run by the team behind seventeen channels of our own"],
 "Channel owners who want the channel run without running it themselves.",
 ["Filming your videos", "Paid advertising"],
 price="From $395/mo"),
('*','VIRTUAL-FRONT-OFFICE'): _D(
 ["Inbox triage", "Scheduling handled", "Follow-ups handled"],
 "Owners drowning in their own messages.",
 ["Bookkeeping and accounting", "Legal or medical advice of any kind"],
 price="From $295/mo"),
('*','RESUME-AND-LINKEDIN-MAKEOVER'): _D(
 ["Your resume rebuilt — fast-turn and sharp", "Your LinkedIn profile rebuilt", "Or both together at the bundle price"],
 "Job hunters who need to look like the hire, on paper and online.",
 ["Submitting applications for you", "Interview coaching"]),
# ================= LOCAL BUSINESS =================
('localbusiness','LOCAL-BUSINESS-GROWTH-GET-FOUND-GET-BOOKED'): _D(
 ["A Google Business Profile that gets you found", "An assistant that answers questions and books appointments 24/7", "Online ordering without the delivery-app cut", "A website we build and manage for you", "Every piece stacks onto a website package — or stands on its own", "Full breakdown on the Local Business page"],
 "Shops, trades, clinics, and food trucks that Google can't see yet.",
 ["Nothing is ordered from this card — the Local Business page carries the full menu"],
 how=["Open the Local Business page for the full breakdown.", "Message us with your trade and your town.", "We reply with the right stack for your business."]),
('*','WEBSITE-BUILDING-AND-MANAGEMENT'): _D(
 ["A fast, real website you own", "Services, prices, photos, menus, and booking on the site", "Designed and built by us", "Managed by us — new photos, seasonal specials, menu changes, holiday hours", "Never stale, never a do-it-yourself headache"],
 "Local businesses that need a home base online that stays current.",
 ["Your domain name registration (the name stays yours; we guide you)", "The stackable add-ons below, unless your package includes them"],
 price="By consultation",
 timeline="Updates you send us go live the same day."),
('*','GOOGLE-BUSINESS-PROFILE-SETUP'): _D(
 ["Your Google Business Profile built properly", "Categories set up", "Services listed", "Photos added", "Hours and attributes set", "The listing that shows up in Google Maps and &ldquo;near me&rdquo; searches"],
 "Businesses with no Google profile — or a dead one.",
 ["The booking assistant (a separate monthly add-on)", "The review funnel (a separate add-on, or included in the Full Stack)"]),
('*','GOOGLE-BUSINESS-PROFILE-RESCUE-AUDIT'): _D(
 ["A human written audit of your public Google listing, read exactly the way customers see it",
  "A PDF scorecard covering your categories, services, photos, hours, and reviews",
  "A plain English fix list you can work through yourself",
  "The three highest impact fixes first, in the order we would do them",
  "A clear note on what is missing, what is wrong, and what is already working"],
 "Local businesses that already have a Google listing and want to know what is holding it back before they pay to rebuild it. It fits shops, trades, clinics, salons, and food businesses in and around Hot Springs.",
 ["Fixing the listing for you. The fixes themselves are our Google Business Profile Setup service, and the audit fee does not include that build",
  "A website, a booking assistant, or a review funnel. Each is a separate service",
  "Managing your profile month to month",
  "No ranking guarantees. Google decides rankings, and nobody honest can promise a position, a number of calls, or a number of bookings"],
 price="$49 one time",
 how=["Message us with your business name and your town.",
  "We read your public Google listing exactly as customers see it. No login is needed, and we never ask for your password.",
  "We write your scorecard and your fix list by hand and send them to you as a PDF.",
  "You work the fix list yourself, or you book our Google Business Profile Setup and we fix it for you."],
 timeline="Delivered within 3 business days of your order. One time audit. No monthly charge, and no subscription.",
 noguar=True),
('*','THE-BOOKING-AND-FAQ-ASSISTANT'): _D(
 ["Attached to your Google profile and your website", "Answers the basics — hours, prices, services, directions", "Books appointments straight into your calendar", "Answers 24/7 — including the 9 PM customer who would have called the next name on the list"],
 "Businesses losing after-hours customers to the next name on the list.",
 ["Medical details — the assistant never takes them; it just books", "Legal advice — legal intake never gives it", "Complex quotes that need your eye — the assistant books the conversation"],
 timeline="Answers 24/7 once live."),
('*','ONLINE-ORDERING-YOUR-OWN-PAGE'): _D(
 ["Ordering on your own page — menu, order, payment through your own payment apps", "A QR code for the truck or counter", "No roughly 30% delivery-app cut on your own orders", "For trucks: daily location posts — &ldquo;today we're here&rdquo;"],
 "Food trucks and restaurants paying a cut of every order to delivery apps.",
 ["Delivery drivers — this is ordering and pickup, not a delivery fleet", "Your payment-app accounts themselves (we wire ordering to them)"]),
('*','REVIEW-FUNNEL'): _D(
 ["A QR code for the counter, the receipt, or the truck window", "Walks happy customers straight to leaving you a Google review", "Reviews that rank your profile, made automatic"],
 "Any local business whose happy customers never quite leave the review.",
 ["Fake or incentivized reviews — never; this funnel asks real customers", "Monthly review management (part of the monthly programs)"],
 price="Add-on $49/mo · Included in the Full Stack"),
('*','GET-FOUND'): _D(
 ["Your Google Business Profile set up and optimized", "The review funnel running every day"],
 "Businesses Google can't see yet, starting with being found.",
 ["The booking assistant (Get Booked and up)", "A website (see Website Building &amp; Management)"]),
('*','GET-BOOKED'): _D(
 ["Everything in Get Found", "The Booking &amp; FAQ Assistant on your profile and your site", "Questions answered and appointments booked around the clock while you do the actual work"],
 "Businesses that get found but lose the after-hours booking.",
 ["Online ordering (a stackable add-on)", "The website build itself (see Website Building &amp; Management)"]),
('*','THE-FULL-STACK'): _D(
 ["Your website built and managed by us", "Your Google profile set up and optimized", "The booking assistant answering and booking 24/7", "Online ordering where it fits", "The review funnel included", "One team running your entire online presence"],
 "Owners who want the whole front desk handled by one team.",
 ["A posted flat price — the stack is scoped to your business first"],
 price="By consultation"),
('*','LAWYERS-INTAKE-THAT-BOOKS-CONSULTS'): _D(
 ["The intake assistant answers FAQs", "Captures case-type basics", "Books consultations", "Your Google profile running underneath", "The review funnel collecting reviews automatically"],
 "Solo attorneys and small firms — our pilot vertical, the one we're proving first.",
 ["Legal advice — the assistant never gives it", "Case evaluation — consultations are yours"]),
# ================= CAR DEALERS =================
('cardealers','SETUP-PROFILE-ASSISTANT-AND-FUNNEL-LIVE'): _D(
 ["Your Google Business Profile built properly for sales and service", "The lead assistant connected", "The review funnel in place", "One-time setup — we handle the whole build"],
 "Dealerships that need the machine built before it can answer.",
 ["The monthly Lead Assistant itself (a separate monthly)", "Your inventory feed or DMS — the assistant works on your profile and website"]),
('cardealers','LEAD-ASSISTANT'): _D(
 ["An assistant on your profile and your website", "Answers inventory questions 24/7 — price, availability, trade-ins, financing basics", "Books the test drive while your team sleeps"],
 "Lots losing the 9 P.M. buyer to whoever answers first.",
 ["Negotiating deals — the assistant books the appointment; your team closes", "Your CRM or DMS subscription"],
 timeline="Answers 24/7 once live — including the buyer who messages at 9 P.M."),
('cardealers','FULL-LOT'): _D(
 ["Everything in Lead Assistant", "Service-drive retention — oil-change and tire reminders that book the bay", "Sold-customer follow-up sequences that bring buyers back", "The review funnel run for you every day"],
 "Dealerships that want sales and service both fed by one machine.",
 ["Third-party listing sites and their fees", "Your DMS or CRM subscription"]),
('cardealers','CAR-DEALERS-LEADS-ANSWERED-IN-60-SECONDS'): _D(
 ["Your Google profile built properly", "A 24/7 lead assistant that books test drives", "Service-drive retention", "A review funnel", "Full breakdown on the Car Dealers page"],
 "Dealers who know the lot that answers first wins the sale.",
 ["Nothing is ordered from this card — the Car Dealers page carries the full menu"],
 how=["Open the Car Dealers page for the full breakdown.", "Message us about your lot — sales, service, or both.", "We map your setup and confirm pricing with you first."]),
# ================= PROPERTY MANAGEMENT =================
('propertymanagement','SETUP-PROFILE-ASSISTANT-AND-FUNNEL-LIVE'): _D(
 ["Your Google Business Profile built properly", "The tenant assistant connected", "The review funnel in place", "One-time setup — we handle the whole build"],
 "Property managers who need the front office built before it can run.",
 ["The monthly Tenant Assistant itself (a separate monthly)", "Your property management software subscription"]),
('propertymanagement','TENANT-ASSISTANT'): _D(
 ["Answers tenant FAQs 24/7", "Takes maintenance requests with photos — the 2 A.M. leak gets logged and routed, not lost", "Vacancy showings scheduled automatically", "An application checklist that collects everything before you ever pick up the phone"],
 "Managers whose nights and weekends get eaten by tenant messages.",
 ["Emergency dispatch decisions — requests are logged and routed to you", "Rent collection and accounting"],
 timeline="On duty 24/7 once live — tenants and prospects answered around the clock."),
('propertymanagement','FULL-PORTFOLIO'): _D(
 ["Everything in Tenant Assistant for up to 50 doors", "Lease-renewal reminder sequences", "A monthly one-page owner report produced for you — the summary your owners actually read"],
 "Managers who also answer to owners.",
 ["More than 50 doors — per-door pricing by consultation, tell us the count"],
 timeline="Includes a monthly one-page owner report, every month the plan runs."),
('propertymanagement','PROPERTY-MANAGEMENT-THE-FRONT-OFFICE-THAT-NEVER-CLOSES'): _D(
 ["A tenant assistant on duty 24/7", "Maintenance logged with photos", "Showings scheduled", "Renewals chased", "A monthly owner report produced for you", "Full breakdown on the Property Management page"],
 "Property managers running buildings instead of inboxes.",
 ["Nothing is ordered from this card — the Property Management page carries the full menu"],
 how=["Open the Property Management page for the full breakdown.", "Message us with how many doors you run.", "We map the setup and quote it straight."]),
# ================= RENTAL HOSTS =================
('rentalhosts','LISTING-MAKEOVER'): _D(
 ["Your listing rewritten to sell the stay", "Copy that answers guest questions before they're asked", "Your photos reordered so the best shots land first", "Titles worked the way a marketer works them"],
 "Hosts whose place is better than their listing makes it look.",
 ["New photography — the makeover works with your photos", "Platform listing fees"]),
('rentalhosts','GUEST-ASSISTANT'): _D(
 ["Booking confirmations sent", "Check-in instructions sent", "House rules shared", "Local recommendations shared", "A mid-stay check-in", "The checkout nudge", "Timed review requests that turn happy stays into five-star reviews", "Turnover coordination with cleaner checklists", "An auto-message on every booking"],
 "Hosts who want hotel-speed guest care without living in the inbox.",
 ["Cleaning itself — we coordinate your cleaners; we don't clean", "Fees charged by Airbnb or VRBO"],
 timeline="Runs on every booking, automatically, per property."),
('rentalhosts','DIRECT-BOOKING-WEBSITE'): _D(
 ["Your own booking page", "Guests book direct — you keep the 15%+ the platforms take from every stay", "One flat monthly instead of a cut of every booking, forever"],
 "Hosts with repeat guests who keep paying the platform cut.",
 ["Payment processing fees from your own payment accounts", "Your domain name"]),
('rentalhosts','MULTI-PROPERTY-HOSTS'): _D(
 ["The guest assistant across your whole portfolio", "The review engine across the portfolio", "Direct booking across the portfolio", "Scoped to your doors"],
 "Hosts running several properties.",
 ["A flat posted price — the portfolio is scoped first"],
 price="By consultation"),
('rentalhosts','RENTAL-HOSTS-FIVE-STAR-CARE-BOOKINGS-THE-PLATFORMS-DON-T-TAX'): _D(
 ["Listing makeovers", "A guest assistant that runs the whole stay", "Your own direct-booking page", "Full breakdown on the Rental Hosts page"],
 "Airbnb and VRBO hosts done paying the platform cut on repeat guests.",
 ["Nothing is ordered from this card — the Rental Hosts page carries the full menu"],
 how=["Open the Rental Hosts page for the full breakdown.", "Message us about your place — one cabin or a whole portfolio.", "We map what we'd build first."]),
# ================= INSURANCE =================
('insurance','SETUP-PROFILE-ASSISTANT-AND-FUNNEL-LIVE'): _D(
 ["Your Google Business Profile built properly", "The quote-intake assistant connected", "The review funnel in place", "One-time setup — we handle the whole build"],
 "Agencies that need the follow-up machine built first.",
 ["The monthly Assistant + Renewals itself (a separate monthly)", "Your agency management system subscription"]),
('insurance','ASSISTANT-RENEWALS'): _D(
 ["A quote-intake assistant that captures the basics", "Books the conversation with you", "Renewal-reminder sequences that reach every client before a policy lapses"],
 "Agencies losing clients to silence, not price.",
 ["Binding coverage or final premium quotes — the assistant captures basics and books you", "Regulated advice to your clients"],
 timeline="Renewal sequences run ahead of every lapse date, automatically."),
('insurance','FULL-AGENCY'): _D(
 ["Everything in Assistant + Renewals", "Seasonal campaigns run for you — Medicare AEP, ACA open enrollment, storm season", "A referral engine — insurance is a referral business, and we make asking automatic"],
 "Agencies that want renewals, seasons, and referrals all run for them.",
 ["Your carrier appointments and licensing — the machine runs on your existing book"]),
('insurance','INSURANCE-THE-MONEY-IS-IN-RENEWALS'): _D(
 ["A quote-intake assistant", "Renewal-reminder sequences", "Seasonal campaigns", "A referral engine", "Full breakdown on the Insurance page"],
 "Agents who know the money is in renewals.",
 ["Nothing is ordered from this card — the Insurance page carries the full menu"],
 how=["Open the Insurance page for the full breakdown.", "Message us about your book — lines you write, size of the agency.", "We map your setup with straight answers."]),
# ================= HOTELS =================
('hotels','SETUP-PROFILE-ASSISTANT-AND-REVIEW-ENGINE-LIVE'): _D(
 ["Your Google profile built properly — the listing travelers actually find", "The guest messaging assistant connected", "The review engine in place — timed requests that turn happy stays into the five-star reviews that rank you", "One-time setup; we handle the whole build"],
 "Hotels and motels that need the guest machine built first.",
 ["The monthly Guest Messaging Assistant itself (a separate monthly)", "OTA listing fees"]),
('hotels','GUEST-MESSAGING-ASSISTANT'): _D(
 ["Pre-arrival messages with check-in details and parking", "Amenity and Wi-Fi answers", "Late-checkout offers", "Local tips your guests actually use", "A warm mid-stay check-in", "Every message in your voice, answered in seconds — at 2 P.M. or 2 A.M."],
 "Properties whose front desk can't answer at 2 A.M. — but guests still ask.",
 ["Front-desk staffing — the assistant covers messaging, not your desk", "OTA listing fees"],
 timeline="Answers in seconds, around the clock, per property."),
('hotels','DIRECT-BOOKING-WEBSITE'): _D(
 ["Your own booking page", "Live rates and real availability", "Payment through your own accounts", "Skip the 15&ndash;25% OTA commission on every direct stay"],
 "Properties tired of handing 15&ndash;25% of every room to a platform.",
 ["Payment processing fees from your own accounts", "Your PMS or channel manager subscription"]),
('hotels','FULL-PROPERTY'): _D(
 ["Your Google profile run for you", "The guest messaging assistant", "Your direct-booking website", "The review engine worked daily", "Seasonal and event content that fills the slow weeks before your competitors notice them"],
 "Owners who want the whole front office run for them.",
 ["OTA commissions on bookings that still come through the platforms — direct bookings are the ones that skip the cut"]),
('hotels','HOTELS-AND-MOTELS-DIRECT-BOOKINGS-FIVE-STAR-CARE'): _D(
 ["A guest messaging assistant that answers in seconds around the clock", "A review engine that fills your profile with five stars", "Your own direct-booking website", "Full breakdown on the Hotels page"],
 "Hotels and motels paying 15&ndash;25% of every room to platforms.",
 ["Nothing is ordered from this card — the Hotels page carries the full menu"],
 how=["Open the Hotels page for the full breakdown.", "Message us about your property — rooms, market, platforms.", "We map what we'd build first."]),
# ================= TAXI =================
('taxi','SETUP-PROFILE-BOOKING-ASSISTANT-AND-REVIEW-FUNNEL-LIVE'): _D(
 ["Your Google profile built properly for &ldquo;taxi near me&rdquo; and airport searches", "The booking assistant connected to your site", "The review funnel in place", "One-time setup; we handle the whole build"],
 "Taxi and limo companies that need the booking machine built first.",
 ["The monthly Booking Assistant itself (a separate monthly)", "Your dispatch software subscription"]),
('taxi','BOOKING-ASSISTANT'): _D(
 ["Booking and dispatch intake on web and text", "Takes the ride details", "Instant quotes for airport runs and events", "Confirms the booking", "Reminders that kill no-shows", "24/7 — including the 4 A.M. airport run nobody wants to answer for"],
 "Companies losing riders who can't get an answer.",
 ["Driving the rides — the assistant books; your fleet rolls", "Your dispatch software subscription"],
 timeline="Answers 24/7 once live — quotes in seconds."),
('taxi','FULL-FLEET'): _D(
 ["Everything in Booking Assistant", "Corporate-account content built for you", "Outreach that lands the hotels, offices, and event venues", "The review funnel run daily, so your rating climbs while the fleet rolls"],
 "Fleets that want the account business, not just the street hail.",
 ["Guaranteed corporate accounts — we court them; they decide"]),
('taxi','TAXI-AND-LIMO-THE-PHONE-THAT-NEVER-SLEEPS'): _D(
 ["A booking and dispatch assistant on web and text", "Instant quotes for airport runs and events", "Corporate-account content", "A review funnel that climbs while the fleet rolls", "Full breakdown on the Taxi &amp; Limo page"],
 "Taxi and limo services losing riders to whoever answers first.",
 ["Nothing is ordered from this card — the Taxi &amp; Limo page carries the full menu"],
 how=["Open the Taxi &amp; Limo page for the full breakdown.", "Message us about your fleet — cars, coverage, airport work or events.", "We map your setup with a straight answer on what we'd build first."]),
# ================= RESTAURANTS =================
('restaurants','SETUP-PROFILE-ASSISTANT-AND-REVIEW-FUNNEL-LIVE'): _D(
 ["Your Google profile built properly — hours, menus, photos, the listing hungry people actually find", "The reservations assistant connected", "The review funnel in place", "One-time setup; we handle the whole build"],
 "Restaurants that need the booking machine built first.",
 ["The monthly Reservations Assistant itself (a separate monthly)", "Your point-of-sale system"]),
('restaurants','RESERVATIONS-ASSISTANT'): _D(
 ["Reservations taken on your website and your Google profile", "The waitlist handled", "Confirmations sent", "Day-of reminders that cut no-shows", "The waitlist worked in real time", "One flat monthly — never a per-cover fee, never a charge for your own regulars"],
 "Restaurants paying per-cover fees to seat their own regulars.",
 ["Per-cover fees — never; that is the whole point", "Your point-of-sale system"],
 timeline="Books and confirms around the clock once live."),
('restaurants','FULL-HOUSE'): _D(
 ["Everything in Reservations Assistant", "Catering intake that answers in seconds and books the consult", "Private-events intake, the same", "Menu and seasonal content posted for you", "The review funnel run daily"],
 "Restaurants whose high-ticket inquiries slip away unanswered.",
 ["Kitchen or floor staffing — we fill the book; your team runs the room"]),
('restaurants','RESTAURANTS-RESERVATIONS-WITHOUT-PER-COVER-FEES'): _D(
 ["Reservations and the waitlist handled on your own page", "One flat monthly — never a per-cover charge", "Catering and private-events intake", "A review funnel", "Full breakdown on the Restaurants page"],
 "Restaurants done paying for every seat twice.",
 ["Nothing is ordered from this card — the Restaurants page carries the full menu"],
 how=["Open the Restaurants page for the full breakdown.", "Message us about your room — seats, service style, catering or events.", "We map what we'd build first."]),
})

DETAILS.update({
# ================= ARTISTS =================
('artists','ARTIST-STARTER'): _D(
 ["Social media run daily — Facebook, Instagram, X, TikTok", "Content calendar planned for you", "Posts published for you", "Captions written for you", "Comments handled", _HYBRID],
 "Artists who need a consistent, professional presence without living on their phone.",
 ["YouTube channel management (Full Machine and up)", "Distribution cleanup (Full Machine and up)", "Fan club build and running (Full Machine and up)", "Merch designs (Full Machine, or the one-time Merch Design Pack)", _OWN]),
('artists','THE-FULL-MACHINE'): _D(
 ["Everything in Artist Starter", "YouTube channels rebuilt and managed", "Distribution cleanup — Spotify, Apple Music, and everywhere else, one name, every release", "Your website managed", "A fan club built and run", "Merch designs from our factory", _HYBRID],
 "Artists with a catalog and an audience who need the whole machine run for them.",
 ["The A-list press and label push (Legacy)", "Podcast and interview bookings (Legacy)", "Tour and booking support (Legacy)", _OWN]),
('artists','LEGACY'): _D(
 ["Everything in the Full Machine", "Press kits pitched to major music press and labels", "Podcast and interview bookings", "Tour and booking support"],
 "Artists with a story the world should hear, ready for a serious run.",
 [_NOGUARANTEE, _OWN]),
('artists','PRESS-KIT-AND-EPK-BUILD'): _D(
 ["A press kit bio written for media, labels, and venues", "Your photos presented in the kit", "Your best quotes and numbers pulled up front", "One clean link you can send anywhere"],
 "Artists who need a professional kit ready to send.",
 ["Pitching the kit (see Press &amp; Podcast Pitch Wave)", "New photography — the kit is built from your existing photos"]),
('artists','ALBUM-LAUNCH-CAMPAIGN'): _D(
 ["Countdown content built for your release", "A video-drop strike on release day", "Pre-order setup so fans can buy on day one", "Release-day press and playlist push"],
 "Artists with a release date set.",
 ["Distribution itself — your distributor still delivers the release (see Distribution Cleanup)", "Ongoing monthly management after launch day"],
 timeline="Built around your release date — countdown, day-one strike, and the release-day push."),
('artists','YOUTUBE-CHANNEL-REBUILD'): _D(
 ["Channel branding rebuilt", "SEO across the channel", "Back catalog organized and searchable", "A Shorts program built from your best moments"],
 "Artists whose channel no longer represents them.",
 ["Ongoing channel management (monthly plans)", "New filming — the rebuild works from your existing catalog"]),
('artists','DISTRIBUTION-CLEANUP'): _D(
 ["Fragmented artist pages unified", "Missing releases delivered to Spotify, Apple Music, and everywhere else", "One name, whole catalog, everywhere"],
 "Artists whose catalog is scattered across names and pages.",
 ["Future releases after the cleanup (monthly plans)", "Royalties owed by third parties — we fix the catalog; your distributor pays you"]),
('artists','FAN-CLUB-SETUP'): _D(
 ["Your fan club built", "Early listens for members", "Exclusive drops set up", "Direct fan access set up", "A free tier to build the core, and a paid tier ready when it rolls"],
 "Artists with fans who want more than the public feed.",
 ["Running the club month to month (monthly plans)", "Merch fulfillment"]),
('artists','MERCH-DESIGN-PACK'): _D(
 ["Five original merch designs, print-ready", "Album bundles planned for your store", "Limited-edition drops planned"],
 "Artists who want merch without hiring a designer.",
 ["Printing and fulfillment — designs are print-ready files for your printer or print-on-demand service", "Store setup (see Full Store Setup)"]),
('artists','PRESS-AND-PODCAST-PITCH-WAVE'): _D(
 ["One focused wave of pitches to music podcasts, blogs, and press", "Your story and your new release, professionally packaged for the pitch"],
 "Artists with a release or a story worth pitching right now.",
 ["Guaranteed placements — outlets decide; we make the pitch professional", "An ongoing PR retainer"]),
('artists','WHITE-LABEL-YOUR-ROSTER-OUR-MACHINE'): _D(
 ["Your artists' socials run by us, under your name", "Launches run by us, under your name", "YouTube run by us, under your name", "Fan clubs run by us, under your name", "Your clients see your brand; we do the work"],
 "Managers and indie labels who want a full machine without hiring one.",
 ["Your client relationships — you stay the face; we stay invisible", "Anything under our name — white-label means your brand only"],
 price="Custom quote — per-artist pricing, monthly; message us for rates"),
('artists','AGENT-NETWORK-BRING-US-ARTISTS-EARN-25'): _D(
 ["Bring us an artist who signs, and you earn 25% of their first package", "Or 25% of their first three months of representation", "You hunt; we service; you get paid"],
 "Scouts, promoters, and connectors who know artists ready for a machine behind them.",
 ["Payment before the artist signs and pays — the 25% is on signed business", "Servicing the artist — that part is ours"],
 price="You earn 25%"),
# ================= MODELS =================
('models','MODEL-STARTER'): _D(
 ["Your showcase portfolio page on our site", "A weekly promo post across our channels during your competition"],
 "Models in a competition who need a professional home base and steady promo.",
 ["Daily vote-push content (Contender and up)", "Social media management (Contender and up)", "You keep 100% rights to your photos; we post only what you approve"]),
('models','CONTENDER'): _D(
 ["Everything in Model Starter", "Daily vote-push content during your competition", "Your socials managed end-to-end while you compete"],
 "Models in the thick of a competition who need daily push behind them.",
 ["Promo videos and network cross-promotion (Cover Run)", "Campaign management past your competition run", "You keep 100% rights to your photos; we post only what you approve"]),
('models','COVER-RUN'): _D(
 ["Everything in Contender", "Daily content", "Promo videos", "Cross-promotion across our whole model and artist network", "Full campaign management to the final round"],
 "Models making a serious run at the final rounds.",
 ["The votes themselves — we run the campaign; your audience casts the votes", "You keep 100% rights to your photos; we post only what you approve"]),
('models','PET-STARTER'): _D(
 ["A showcase portfolio page for your pet on our site", "A weekly feature post across our channels"],
 "Pet owners who want their animal presented like a star.",
 ["Scheduled posting and fan engagement (Social Animal and up)", "Brand-deal outreach (Celebrity Pet)"]),
('models','SOCIAL-ANIMAL'): _D(
 ["Everything in Pet Starter", "Scheduled posts for your pet's pages", "Growth pushes", "Fan engagement handled"],
 "Pets building a following of their own.",
 ["Videos and brand-deal outreach (Celebrity Pet)"]),
('models','CELEBRITY-PET'): _D(
 ["Everything in Social Animal", "Videos built for your pet", "Cross-promotion across our network", "Brand-deal outreach"],
 "Pets with star potential and an owner ready to run with it.",
 ["Guaranteed brand deals — we do the outreach; brands decide"]),
# ================= GLAMOUR =================
('glamour','GLAMOUR-STARTER'): _D(
 ["Your showcase portfolio page on our site", "A weekly promo post across our channels during your competition or feature run"],
 "Glamour models who need a polished home base and steady promo.",
 ["Daily vote-push content (Glamour Contender and up)", "Social media management (Glamour Contender and up)", "You keep 100% rights to your photos; we post only what you approve"]),
('glamour','GLAMOUR-CONTENDER'): _D(
 ["Everything in Glamour Starter", "Daily vote-push content", "Your socials managed end-to-end while you compete"],
 "Glamour models in a competition who need daily push behind them.",
 ["Promo videos and network cross-promotion (Glamour Cover Run)", "You keep 100% rights to your photos; we post only what you approve"]),
('glamour','GLAMOUR-COVER-RUN'): _D(
 ["Everything in Glamour Contender", "Daily content", "Promo videos", "Cross-promotion across our whole model and artist network", "Full campaign management to the final round"],
 "Glamour models making a serious run at the final rounds.",
 ["The votes themselves — we run the campaign; your audience casts the votes", "You keep 100% rights to your photos; we post only what you approve"]),
('glamour','GLAMOUR-PORTFOLIO-PAGE'): _D(
 ["Your own showcase page on our site", "Your best shots presented like a feature", "Your story on the page", "Booking contact on the page"],
 "Glamour models who need one polished link to send.",
 ["New photography — the page is built from your existing shots", "Ongoing promo (monthly plans)"]),
('glamour','GLAMOUR-PROMO-REEL'): _D(
 ["A short, elegant promo video cut from your photos and footage", "Styled and scored by our team", "Ready to post everywhere"],
 "Glamour models who want motion, not just stills.",
 ["A photo shoot — the reel is cut from your existing photos and footage", "Paid ad spend"]),
('glamour','GLAMOUR-PRESS-KIT'): _D(
 ["Your bio written for the kit", "Your best shots presented", "Your features listed", "Contact details in one professional kit"],
 "Glamour models pitching features and bookings.",
 ["Pitching the kit (monthly plans)", "New photography"]),
# ================= ACTORS =================
('actors','STARTER'): _D(
 ["Headshot portfolio page on our site", "Your socials run daily", "Your casting profiles kept current", _HYBRID],
 "Actors who need a professional presence that stays current.",
 ["Demo reel build (Full Machine, or the one-time Demo Reel Build)", "Casting submission waves and press kit (Full Machine and up)", _OWN]),
('actors','THE-FULL-MACHINE'): _D(
 ["Everything in Starter", "A professional demo reel built and refreshed by our video factory", "Casting submission waves", "A full press kit", "Interview pitching", _HYBRID],
 "Actors actively auditioning who need submissions and materials handled.",
 ["Dedicated placement campaigns and direct producer outreach (Legacy)", "Press handling (Legacy)", _OWN]),
('actors','LEGACY'): _D(
 ["Everything in the Full Machine", "Dedicated placement campaigns", "Direct producer and director outreach", "Press handling"],
 "Actors making a serious run.",
 ["Guaranteed roles or placements — casting decides", _OWN]),
('actors','DEMO-REEL-BUILD'): _D(
 ["A casting-grade demo reel cut from your footage by our video factory", "Paced and titled for casting", "Ready to submit"],
 "Actors with footage that needs a professional cut.",
 ["Filming new scenes — the reel is cut from your existing footage", "Headshots"]),
('actors','ACTOR-PRESS-KIT-AND-EPK'): _D(
 ["Your bio", "Your headshots presented", "Your credits listed", "Reel links included", "A contact sheet"],
 "Actors who need one professional kit to send.",
 ["A demo reel (see Demo Reel Build)", "Pitching the kit (monthly plans)"]),
('actors','HEADSHOT-PORTFOLIO-PAGE'): _D(
 ["Your own showcase page on our site", "Your headshots on the page", "Your reel embedded", "Your credits listed", "Booking contact on the page"],
 "Actors who need one clean link for casting.",
 ["New headshots — the page is built from your existing shots", "Ongoing page management (monthly plans)"]),
('actors','CASTING-PITCH-WAVE'): _D(
 ["You packaged professionally for casting", "Pitched to casting calls, indie productions, and commercial work in one coordinated wave"],
 "Actors ready to be put in front of casting right now.",
 ["Guaranteed auditions or roles — casting decides", "Ongoing submissions (monthly plans)"]),
('actors','IMDB-AND-PROFILE-CLEANUP'): _D(
 ["Your IMDb profile fixed and unified", "Your casting profiles fixed and unified", "One consistent professional presence everywhere"],
 "Actors whose profiles are scattered or out of date.",
 ["Credits you have not earned — we present your real record, polished", "Ongoing profile management (monthly plans)"]),
('actors','VOICE-STARTER'): _D(
 ["A voice portfolio page with your demos hosted", "Your socials run daily", "Your casting profiles kept current", _HYBRID],
 "Voice actors who need demos hosted and a presence that stays current.",
 ["Demo production (Voice Full Machine, or the one-time Voice Demo Reel)", "Weekly submission waves (Voice Full Machine and up)", _OWN]),
('actors','VOICE-FULL-MACHINE'): _D(
 ["Everything in Voice Starter", "Commercial and character demos produced by our studio", "Your Voices and Voice123 profiles managed", "Weekly submission waves", _HYBRID],
 "Voice actors auditioning weekly who want production and submissions handled.",
 ["Agent pitching (Voice Legacy)", "Direct casting outreach (Voice Legacy)", _OWN]),
('actors','VOICE-LEGACY'): _D(
 ["Everything in Voice Full Machine", "Agent pitching", "Direct outreach to animation, game, and audiobook casting"],
 "Voice actors making a serious career run.",
 ["Guaranteed bookings — casting decides", _OWN]),
('actors','VOICE-DEMO-REEL'): _D(
 ["A produced commercial or character demo", "Scripted by our team", "Directed by our team", "Mixed and ready for casting platforms"],
 "Voice actors who need a demo that sounds like the work they want.",
 ["Additional demos beyond the one produced", "Ongoing submissions (monthly plans)"]),
('actors','VOICE-PORTFOLIO-PAGE'): _D(
 ["Your own page on our site", "Playable demos on the page", "Your range presented", "Booking contact on the page"],
 "Voice actors who need one link that plays their range.",
 ["Demo production (see Voice Demo Reel)", "Ongoing management (monthly plans)"]),
('actors','CASTING-PLATFORM-SETUP'): _D(
 ["Voices profile built properly", "Voice123 profile built properly", "ACX profile built properly", "Bios, demos, tags, and rates set to get you found"],
 "Voice actors whose platform profiles are empty or unfinished.",
 ["Producing the demos themselves (see Voice Demo Reel)", "Ongoing profile management (monthly plans)"]),
('actors','STUNT-REEL-BUILD'): _D(
 ["A stunt reel cut from your footage by our video factory", "Falls, fights, driving, and wire work paced the way coordinators actually watch them"],
 "Stunt performers with footage that needs a coordinator-grade cut.",
 ["Filming new stunts — the reel is cut from your existing footage", "Coordinator outreach (see Coordinator &amp; Production Outreach)"],
 price="Custom quote — per project"),
('actors','COORDINATOR-AND-PRODUCTION-OUTREACH'): _D(
 ["Your credits, certifications, and reel packaged", "Put in front of stunt coordinators and productions in one coordinated wave", "Follow-up handled by us"],
 "Stunt performers ready to be put in front of coordinators.",
 ["Guaranteed bookings — coordinators decide", "Ongoing representation — talk to us about the stunt division"],
 price="Custom quote — per wave"),
('actors','WHITE-LABEL-REPRESENTATION'): _D(
 ["Your roster's pages run by us under your brand", "Reels run by us under your brand", "Socials run by us under your brand", "Your talent, our machine, your name on it"],
 "Acting coaches and agencies.",
 ["Your client relationships — you stay the face", "Anything under our name"],
 price="Custom quote — per-actor monthly"),
('actors','AGENT-NETWORK-EARN-25'): _D(
 ["Bring us a signing actor or voice actor", "Earn 25% of their first package, or of their first 3 months"],
 "Connectors who know talent ready for representation.",
 ["Payment before the talent signs and pays", "Servicing the talent — that part is ours"],
 price="You earn 25%"),
})

DETAILS.update({
# ================= SINGERS =================
('singers','STARTER'): _D(
 ["Your singer showcase page on our site, with your best recordings up front", "Your socials run daily", _HYBRID],
 "Singers who need a showcase and a presence that stays alive.",
 ["Performance videos (Full Machine and up)", "YouTube channel management (Full Machine and up)", "Audition and competition submission waves (Full Machine and up)", _OWN]),
('singers','THE-FULL-MACHINE'): _D(
 ["Everything in Starter", "Performance videos cut from your recordings", "Your YouTube channel managed", "Audition and competition submission waves", "Collaboration outreach", _HYBRID],
 "Singers pushing for competitions, collaborations, and a bigger audience.",
 ["A&amp;R and label pitching (Legacy)", "Press and booking support (Legacy)", _OWN]),
('singers','LEGACY'): _D(
 ["Everything in the Full Machine", "A&amp;R and label pitching", "Press", "Booking support"],
 "Singers making a serious run.",
 ["Guaranteed deals or bookings — labels and venues decide", _OWN]),
('singers','SINGER-PRESS-KIT-AND-EPK'): _D(
 ["Your bio", "Your photos presented", "Your best recordings in the kit", "Booking contact", "One professional kit that opens doors"],
 "Singers who need one kit to send.",
 ["Pitching the kit (monthly plans)", "New recordings"]),
('singers','VOCAL-DEMO-VIDEO'): _D(
 ["A performance video cut from your best recording", "Styled for reach", "Captioned for reach", "Ready to pitch"],
 "Singers whose best recording deserves a video face.",
 ["Recording the performance — the video is cut from your existing recording", "Ongoing channel management"]),
('singers','YOUTUBE-CHANNEL-BUILD'): _D(
 ["A proper artist channel — branding", "Your catalog uploaded and organized", "Descriptions that get found"],
 "Singers whose channel is a pile of uploads, not a presence.",
 ["Ongoing channel management (monthly plans)", "New filming"]),
('singers','AUDITION-WAVE'): _D(
 ["You packaged professionally", "Submitted to singing competitions, shows, and open calls in one coordinated wave"],
 "Singers ready to be submitted right now.",
 ["Guaranteed selection — shows decide", "Ongoing submissions (monthly plans)"]),
('singers','FAN-CLUB-SETUP'): _D(
 ["A private fan club space", "Launch content", "A welcome sequence that turns listeners into loyalists"],
 "Singers with listeners who want closer access.",
 ["Running the club month to month (monthly plans)"]),
('singers','MERCH-DESIGN-PACK'): _D(
 ["Five original merch designs built around your name and image"],
 "Singers who want merch without hiring a designer.",
 ["Printing and fulfillment — designs are print-ready files for your printer or print-on-demand service"]),
('singers','WHITE-LABEL-REPRESENTATION'): _D(
 ["Your singers' socials run by us under your brand", "Videos run by us under your brand", "Fan clubs run by us under your brand"],
 "Managers and labels.",
 ["Your client relationships — you stay the face", "Anything under our name"],
 price="Custom quote — per-artist monthly"),
('singers','AGENT-NETWORK-EARN-25'): _D(
 ["Bring us a signing singer", "Earn 25% of their first package, or of their first 3 months"],
 "Connectors who know singers ready for a machine behind them.",
 ["Payment before the singer signs and pays", "Servicing the singer — that part is ours"],
 price="You earn 25%"),
# ================= CREATORS =================
('creators','STARTER'): _D(
 ["A content calendar that never runs dry", "Your posting run daily by us", "Profiles cleaned up", "Every platform pointed at your growth", _HYBRID],
 "Creators who post inconsistently and know it costs them.",
 ["Clip factory cuts (Full Machine and up)", "Brand-deal outreach (Full Machine and up)", "Link hub management (Full Machine and up)", _OWN]),
('creators','THE-FULL-MACHINE'): _D(
 ["Everything in Starter", "Our clip factory cutting shorts and reels from your streams and videos daily", "Brand-deal outreach", "Your link hub managed", _HYBRID],
 "Creators with more content than time.",
 ["Sponsorship negotiation (Legacy)", "Merch line and PR (Legacy)", _OWN]),
('creators','LEGACY'): _D(
 ["Everything in the Full Machine", "Sponsorship negotiation", "A merch line", "PR", "Full channel management across every platform you touch"],
 "Creators making a serious run at this being the job.",
 ["Guaranteed sponsorships — brands decide", _OWN]),
('creators','CLIP-PACK-10-SHORTS'): _D(
 ["Ten scroll-stopping clips cut from your existing content", "Captioned for reach", "Ready to post everywhere"],
 "Creators sitting on long content nobody clips.",
 ["Filming new content — clips are cut from what you already have", "Posting them (monthly plans)"]),
('creators','BRAND-DEAL-PITCH-WAVE'): _D(
 ["Your media kit numbers built", "Pitched to brands in one coordinated wave"],
 "Creators ready for brand money.",
 ["Guaranteed deals — brands decide", "Negotiation (Legacy)"]),
('creators','CREATOR-MEDIA-KIT'): _D(
 ["Your rates in the kit", "Your stats in the kit", "Your audience presented", "Your best content featured"],
 "Creators who get asked for a media kit and don't have one.",
 ["Pitching the kit (see Brand Deal Pitch Wave)"]),
('creators','CHANNEL-REBUILD'): _D(
 ["Channel branding rebuilt", "Banners rebuilt", "Descriptions rebuilt", "Playlists rebuilt", "Links rebuilt — your channel looking like a business"],
 "Creators whose channel looks smaller than they are.",
 ["Ongoing channel management (monthly plans)"]),
('creators','MERCH-DESIGN-PACK'): _D(
 ["Five original merch designs built around your brand"],
 "Creators who want merch without hiring a designer.",
 ["Printing and fulfillment — designs are print-ready files for your printer or print-on-demand service"]),
# ================= ATHLETES =================
('athletes','STARTER'): _D(
 ["Your athlete profile page on our site", "Your socials run daily", "Your record and story presented like a pro's", _HYBRID],
 "Athletes who need to look like pros before sponsors will treat them like pros.",
 ["Highlight reels (Full Machine, or the one-time Highlight Reel)", "Sponsor pitch waves and press kit (Full Machine and up)", _OWN]),
('athletes','THE-FULL-MACHINE'): _D(
 ["Everything in Starter", "Highlight reels cut from your footage", "Sponsor pitch waves", "Event and fight promotion", "A full press kit", _HYBRID],
 "Athletes actively competing and chasing sponsors.",
 ["Sponsor negotiation (Legacy)", "Camp and season content coverage (Legacy)", "Press handling (Legacy)", _OWN]),
('athletes','LEGACY'): _D(
 ["Everything in the Full Machine", "Sponsor negotiation", "Camp and season content coverage", "Press handling"],
 "Athletes making a serious run.",
 ["Guaranteed sponsors — sponsors decide", _OWN]),
('athletes','HIGHLIGHT-REEL'): _D(
 ["A sponsor-grade highlight reel cut from your footage", "Your best moments, paced to hit hard"],
 "Athletes with footage sponsors need to see.",
 ["Filming new footage — the reel is cut from what you have", "Sponsor pitching (see Sponsor Pitch Wave)"]),
('athletes','SPONSOR-PITCH-WAVE'): _D(
 ["Your story and stats packaged", "Pitched to local and national sponsors in one coordinated wave"],
 "Athletes ready to ask for sponsor money properly.",
 ["Guaranteed sponsors — sponsors decide", "Negotiation (Legacy)"]),
('athletes','ATHLETE-PRESS-KIT'): _D(
 ["Your bio", "Your record", "Your photos", "Your highlights — one professional kit that opens sponsor doors"],
 "Athletes who need the kit sponsors ask for.",
 ["Pitching the kit (see Sponsor Pitch Wave)"]),
('athletes','ATHLETE-PROFILE-PAGE'): _D(
 ["Your own page on our site", "Your story on the page", "Your record on the page", "Your highlights on the page", "Sponsor contact on the page"],
 "Athletes who need one pro link to send.",
 ["Ongoing page management (monthly plans)"]),
('athletes','MERCH-DESIGN-PACK'): _D(
 ["Five original merch designs built around your name and nickname"],
 "Athletes who want merch without hiring a designer.",
 ["Printing and fulfillment — designs are print-ready files for your printer or print-on-demand service"]),
# ================= COMEDIANS =================
('comedians','STARTER'): _D(
 ["Your comedian showcase page", "Your socials run daily", "Your best clips posted on a schedule that builds a following", _HYBRID],
 "Stand-ups who need clips working for them between shows.",
 ["Weekly set clip editing (Full Machine, or the one-time Set Clip Pack)", "Booking pitch waves and podcast guesting outreach (Full Machine and up)", _OWN]),
('comedians','THE-FULL-MACHINE'): _D(
 ["Everything in Starter", "Set clips edited weekly", "Booking pitch waves to clubs and shows", "Podcast guesting outreach", _HYBRID],
 "Comics ready to fill bigger rooms.",
 ["Special and taping promotion campaigns (Legacy)", "Tour support and press (Legacy)", _OWN]),
('comedians','LEGACY'): _D(
 ["Everything in the Full Machine", "Special and taping promotion campaigns", "Tour support", "Press"],
 "Comics making a serious run.",
 ["Guaranteed bookings — clubs decide", _OWN]),
('comedians','SET-CLIP-PACK'): _D(
 ["Your best bits cut into shareable clips", "Captioned for reach", "Ready to post everywhere"],
 "Comics sitting on set footage nobody has clipped.",
 ["Filming new sets — clips are cut from your existing footage", "Posting them (monthly plans)"]),
('comedians','COMEDY-EPK'): _D(
 ["Your bio", "Your clips", "Your credits", "Booking contact — the kit clubs and bookers ask for"],
 "Comics who need the kit bookers ask for.",
 ["Pitching the kit (see Booking Pitch Wave)"]),
('comedians','BOOKING-PITCH-WAVE'): _D(
 ["You packaged professionally", "Pitched to clubs, shows, and private events in one coordinated wave"],
 "Comics ready to be pitched right now.",
 ["Guaranteed bookings — clubs decide", "Ongoing pitching (monthly plans)"]),
('comedians','YOUTUBE-CHANNEL-BUILD'): _D(
 ["A proper comedy channel — branding", "Your sets uploaded and organized", "Descriptions that get found"],
 "Comics whose channel doesn't match their act.",
 ["Ongoing channel management (monthly plans)"]),
('comedians','FAN-CLUB-SETUP'): _D(
 ["A private fan space", "Launch content", "A welcome sequence that turns laughs into loyalists"],
 "Comics with fans who want closer access.",
 ["Running the club month to month (monthly plans)"]),
# ================= PODCASTERS =================
('podcasters','STARTER'): _D(
 ["Your show page on our site", "Episode clips cut and posted", "Your socials run daily", _HYBRID],
 "Podcasters who record consistently but promote sporadically.",
 ["Full production support (Full Machine and up)", "Guest booking outreach (Full Machine and up)", _OWN]),
('podcasters','THE-FULL-MACHINE'): _D(
 ["Everything in Starter", "Full production support — editing", "Show notes written", "Daily clips", "Guest booking outreach that lands names", _HYBRID],
 "Shows ready to sound and look like a production, not a hobby.",
 ["Sponsor and ad pitching (Legacy)", "Network outreach and live event promotion (Legacy)", _OWN]),
('podcasters','LEGACY'): _D(
 ["Everything in the Full Machine", "Sponsor and ad pitching", "Network outreach", "Live event promotion"],
 "Shows making a serious run.",
 ["Guaranteed sponsors — sponsors decide", _OWN]),
('podcasters','PODCAST-LAUNCH-PACKAGE'): _D(
 ["Show artwork", "A trailer produced", "Platform setup everywhere", "Launch episodes packaged", "A release campaign"],
 "New shows launching properly, or existing shows relaunching.",
 ["Recording the episodes — episode production support is on monthly plans", "Ongoing management after launch"]),
('podcasters','EPISODE-CLIP-PACK'): _D(
 ["Ten clips and audiograms cut from your episodes", "Captioned for reach", "Ready to post"],
 "Podcasters whose episodes never become clips.",
 ["Editing the episodes themselves (monthly plans)", "Posting the clips (monthly plans)"]),
('podcasters','GUEST-BOOKING-WAVE'): _D(
 ["Your show pitched to the guests you actually want, in one coordinated wave"],
 "Shows that need bigger guests than their inbox lands.",
 ["Guaranteed guests — guests decide", "Interview preparation"]),
('podcasters','SHOW-MEDIA-KIT'): _D(
 ["Your stats in the kit", "Your audience presented", "Your rates in the kit — the kit sponsors ask for, done right"],
 "Shows sponsors ask for numbers from.",
 ["Pitching the kit (see Sponsor Pitch Wave)"]),
('podcasters','SPONSOR-PITCH-WAVE'): _D(
 ["Your numbers packaged", "Pitched to sponsors and ad buyers in one coordinated wave"],
 "Shows with an audience worth selling.",
 ["Guaranteed sponsors — sponsors decide", "Ongoing ad sales (Legacy)"]),
# ================= DJS =================
('djs','DJ-STARTER'): _D(
 ["Your DJ profile page on our site", "Your socials run daily", "Every gig, mix, and release posted on schedule", _HYBRID],
 "DJs who need a presence that never misses a gig post.",
 ["Set and mix videos (Full Machine and up)", "YouTube and SoundCloud management (Full Machine and up)", "Booking pitch waves and press kit (Full Machine and up)", _OWN]),
('djs','THE-FULL-MACHINE'): _D(
 ["Everything in DJ Starter", "Set and mix videos cut and posted by our factory", "Your YouTube and SoundCloud managed", "Booking pitch waves to venues and promoters", "A full press kit", _HYBRID],
 "DJs chasing bigger rooms.",
 ["Tour and residency support (Legacy)", "Promoter and label outreach (Legacy)", "Press handling (Legacy)", _OWN]),
('djs','DJ-LEGACY'): _D(
 ["Everything in the Full Machine", "Tour and residency support", "Promoter and label outreach", "Press handling"],
 "DJs making a serious run.",
 ["Guaranteed bookings — venues and promoters decide", _OWN]),
('djs','DJ-PRESS-KIT-AND-EPK'): _D(
 ["Your bio", "Your photos", "Your mixes", "Booking contact — one kit promoters actually answer"],
 "DJs who need the kit promoters ask for.",
 ["Pitching the kit (see Booking Pitch Wave)"]),
('djs','LIVE-SET-VIDEO'): _D(
 ["Your set cut into a punchy, booking-grade video", "The moments that get you booked again, up front"],
 "DJs with set footage that should be working for them.",
 ["Filming the set — the video is cut from your existing footage", "Ongoing video work (monthly plans)"]),
('djs','BOOKING-PITCH-WAVE'): _D(
 ["You packaged professionally", "Pitched to venues, promoters, and events in one coordinated wave"],
 "DJs ready to be pitched right now.",
 ["Guaranteed bookings — venues decide", "Ongoing pitching (monthly plans)"]),
('djs','MIX-SHOWCASE-PAGE'): _D(
 ["Your own page on our site", "Your best mixes up front", "Booking contact on the page"],
 "DJs who need one link that plays their best work.",
 ["Ongoing page management (monthly plans)"]),
# ================= REAL ESTATE =================
('realestate','CONTENT-STARTER'): _D(
 ["Your monthly content calendar, built for you", "30 days of posts planned and written", "New listings, just solds, open houses, and market stats covered", "Testimonial posts that turn happy clients into your best advertising"],
 "Agents who post their own content but want the whole month built for them.",
 ["Posting it for you (Monthly Management and up)", "Listing videos (Monthly Management and up)"],
 timeline="A full month of content, planned and written — you post it on your schedule."),
('realestate','MONTHLY-MANAGEMENT'): _D(
 ["Everything in Content Starter", "We run it all — your social media managed daily", "A listing video for every new listing", "A monthly market report video that makes you the expert your market watches"],
 "Agents who want the marketing department handled, not helped.",
 ["Listing copy at a luxury standard (Luxury Partner)", "Open house campaigns (Luxury Partner)"],
 timeline="Includes a monthly market report video, every month the plan runs."),
('realestate','LUXURY-PARTNER'): _D(
 ["Everything in Monthly Management", "Listing copy written to a luxury standard", "Open house campaigns", "A personal brand run like a business"],
 "Luxury agents and top teams.",
 ["A fixed package price — the program is scoped to your volume first"],
 price="By consultation — scoped to your volume"),
('realestate','LISTING-VIDEO'): _D(
 ["A vertical promo video for your listing, cut from your photos", "Ready for Reels, TikTok, and Shorts"],
 "Agents who want every listing moving, not just listed.",
 ["Photography — the video is cut from your listing photos", "Posting it (monthly programs)"],
 timeline="Ready the day your listing hits the market — send the photos when it lists."),
('realestate','LISTING-COPY'): _D(
 ["Your MLS description written", "A luxury listing narrative that sells the life, not just the square footage"],
 "Agents whose listings read like everyone else's.",
 ["MLS entry and syndication — you paste the copy into your systems", "Photography"]),
('realestate','OPEN-HOUSE-KIT'): _D(
 ["Promo graphics for the open house", "Story posts", "A recap reel after the event — an open house that markets itself"],
 "Agents who want the open house to work before and after the day.",
 ["Hosting the event — we market it; you host it", "Paid ad spend"]),
('realestate','PROFILE-MAKEOVER'): _D(
 ["Your bio rebuilt across every platform", "Your link page rebuilt", "Your branding rebuilt — one polished presence that matches your price point"],
 "Agents whose online presence undersells their listings.",
 ["Ongoing management (monthly programs)", "New headshots"]),
('realestate','AI-TRAINING-FOR-YOUR-OFFICE'): _D(
 ["A hands-on workshop for your brokerage", "Your agents using AI for listings, follow-ups, and marketing"],
 "Brokerages that want the whole office levelled up at once.",
 ["One-on-one coaching after the workshop (ask us)", "Ongoing content management (monthly programs)"],
 price="By consultation — priced per office",
 timeline="Your agents leave using AI the same day — that is the point of the workshop."),
('realestate','AI-LIKE-A-PRO-LIVE-WORKSHOP-FOR-REALTORS'): _D(
 ["One live 90 minute virtual workshop for one realtor office, up to 8 agents, taught live by Irish + Nova online",
  "Built from our AI for Realtors course, Rung 3 of the AI Like a Pro ladder, already live as a course",
  "The five AI tools that save a listing agent the most time, picked for real estate work",
  "Prompt sets for listings, ready to copy and use the same day",
  "Prompt sets for follow up with buyers, sellers, and past clients",
  "Prompt sets for open houses, from invites to recap posts",
  "Live practice on real office work during the session",
  "The safety rules, what never goes into an AI tool, so client details stay protected",
  "A 7 day starter plan so your office keeps using the tools after the session ends"],
 "Realtor offices and brokerages with up to 8 agents in the session who want the whole office using AI for listings, follow up, and open houses. It fits listing teams and small brokerages best. No tech background is needed.",
 ["Listings sold, commissions, leads, or income results. This is education and time saving training only, and nobody honest can promise sales outcomes",
  "Done for you marketing or content management. Our Real Estate monthly programs cover that work separately",
  "One to one coaching after the session. Follow up training can be booked separately",
  "AI platform subscriptions charged by the AI providers. The session runs on free tools first",
  "The self paced AI Like a Pro course itself. That course is sold separately in our Shop and on Udemy"],
 price="$195 flat per session",
 how=["Message us with your office name, your town, and how many agents will join.",
  "We confirm the session time and the flat $195 price in writing before anything starts.",
  "Pay by PayPal or Cash App to hold your slot.",
  "We meet live online for 90 minutes. Your agents follow along, practice on real work, and leave with the prompt sets and the 7 day starter plan."],
 timeline="Sessions are booked and scheduled in advance, at a time we agree in writing. One booking is one 90 minute session for one office of up to 8 agents.",
 noguar=True),
})

# ---------- SERVICES ----------
gigs = [
 ("&#128218; NONFICTION eBOOK GHOSTWRITING","Your idea, written like a book that sells. Nonfiction manuscripts, structured, voiced, and finished.",[("Starter","$40"),("Standard","$50"),("Premium","$95")],"http://www.fiverr.com/s/aeeo4Rg"),
 ("&#128214; KINDLE + PAPERBACK FORMATTING","Clean, professional KDP formatting for Kindle and paperback — upload-ready files, no errors, no headaches.",[("Basic","$40"),("Standard","$45"),("Premium","$55")],"http://www.fiverr.com/s/GPPLQ03"),
 ("&#127916; 10 TIKTOK SCRIPTS","Scroll-stopping short-form scripts with hooks built in — written for your niche, ready to film.",[("Basic","$15"),("Standard","$35"),("Premium","$70")],"http://www.fiverr.com/s/NeepqyQ"),
 ("&#128269; YOUTUBE SEO — TITLES, DESCRIPTIONS, TAGS","Get found. Clickable titles, keyword-loaded descriptions, and tags that rank.",[("Basic","$10"),("Standard","$25"),("Premium","$45")],"http://www.fiverr.com/s/X00BVKk"),
 ("&#128241; SOCIAL MEDIA MANAGEMENT","Instagram, TikTok, and Facebook — run end-to-end: posting, captions, and engagement handled for you.",[("Starter","$95/mo"),("Growth","$195/mo"),("Empire","$395/mo")],"https://www.fiverr.com/irish00007"),
]
scards = ""
for title, desc, tiers, url in gigs:
    th = "".join('<div class="tier"><div class="tn">%s</div><div class="tp">%s</div></div>' % (n, p) for n, p in tiers)
    scards += _pkg(url, title, desc, th, tiers, "Order on Fiverr") + '\n'
services_body = scards + '<p class="note">Every order runs through Fiverr — secure payment, clear packages, no funny business.<br>Questions first? <a href="https://www.fiverr.com/irish00007" style="color:#ffd95e">Message us on Fiverr</a>.</p>'
def _gigcard(title, desc, tiers, url, cta):
    th = "".join('<div class="tier"><div class="tn">%s</div><div class="tp">%s</div></div>' % (n, p) for n, p in tiers if p)
    if not th:
        th = '<div class="tier"><div class="tn">Custom quote</div><div class="tp">Message for scope &amp; price</div></div>'
    return _pkg(url, title, desc, th, tiers, cta)
FIVP = "https://www.fiverr.com/irish00007"
FBP = "https://www.facebook.com/Irish00007"
_idx = services_body.rfind('<p class="note">')
_head, _note_part = services_body[:_idx], services_body[_idx:]
_extra = '<div class="sec">Build &amp; design</div>'
_extra += _gigcard("&#128187; WEBSITE DESIGN &amp; BUILD", "A fast, real website you own — like this one. Business sites, link hubs, shops, landing pages.", [("Basic","$40"),("Standard","$90"),("Empire","$180")], FIVP, "Order on Fiverr")
_extra += _gigcard("&#128241; APP CREATION", "Got an app idea? We design and build it — prototype to launch-ready. Tell us what you want it to do.", [], FBP, "Message us")
_extra += _gigcard("&#127978; FULL STORE SETUP", "Ko-fi, Gumroad, or Whop store built for you — products loaded, payments wired, ready to sell.", [], FBP, "Message us")
_extra += _gigcard("&#128218; BOOK COVER DESIGN", "Covers that sell the click — Kindle, paperback wraps, and audiobook squares.", [("Basic","$20"),("Standard","$45"),("Premium","$80")], FIVP, "Order on Fiverr")
_extra += _gigcard("&#128444;&#65039; YOUTUBE THUMBNAILS", "Thumbnails that punch. Bold, clickable, on-brand.", [("Basic","$10"),("Standard","$25"),("Premium","$50")], FIVP, "Order on Fiverr")
_extra += _gigcard("&#129302; AI SETUP FOR YOUR BUSINESS", "Your own AI workhorse — content, customer replies, bookkeeping prompts, set up and trained on your business.", [], FBP, "Message us")
_extra += _gigcard("&#9997;&#65039; STORE LISTING COPY", "Product descriptions that convert browsers into buyers, for any marketplace.", [("Basic","$10"),("Standard","$30"),("Premium","$60")], FIVP, "Order on Fiverr")
_extra += '<div class="sec">AI, done for you</div>'
_extra += _gigcard("&#129513; AI MEMORY SYNC SETUP, DONE FOR YOU", "Own the AI Memory Sync Kit and want it running today? We build your vault with you on a short guided call: connected, loaded, configured, and walked through in plain language.", [("Standard Setup","$149"),("Plus Setup","$295")], FBP, "Message us to book")
_extra += '<div class="sec">For musicians</div>'
_extra += _gigcard("&#127908; ARTIST REPRESENTATION", "Full-stack representation for musicians — socials, YouTube, distribution, fan club, merch, press. Monthly tiers from $195 and one-time packages (press kits, launch campaigns, channel rebuilds).", [("Starter","$195/mo"),("Full Machine","$495/mo"),("Legacy","$995/mo")], "artists.html", "See the artist packages")
services_body = _head + _extra + _note_part
services_body = PROOF_SVC + services_body
open('services.html','w').write(page("Services — Hire Irish + Nova","Hire Irish + Nova: eBook ghostwriting, KDP formatting, TikTok scripts, YouTube SEO, social media management, and local business services that get you booked.","services.html","SERVICES","Done fast. Done right. <b>Powered by Irish + Nova.</b>", services_body))

# ---------- ARTISTS ----------
def _acard(title, desc, tiers, url, cta):
    th = "".join('<div class="tier"><div class="tn">%s</div><div class="tp">%s</div></div>' % (n, p) for n, p in tiers if p)
    return _pkg(url, title, desc, th, tiers, cta)
_PAGECTX = 'artists'
artists_body = card("https://www.facebook.com/Irish00007", "&#11088; FOUNDING ARTIST SLOT — ONE AVAILABLE", "We are selecting ONE legacy artist to represent free — our showcase. Full machine, no charge, in exchange for the credit. Think that's you? Message us and make your case.", True)
artists_body += '<div class="sec">Monthly representation</div>'
artists_body += _acard("&#127908; ARTIST STARTER", "Social media run daily — Facebook, Instagram, X, TikTok. Content calendar, posts, captions, comments handled. You play music; we run the machine.", [("Starter","$195/mo")], FBP, "Message us")
artists_body += _acard("&#127911; THE FULL MACHINE", "Everything in Starter, plus: YouTube channels rebuilt and managed, distribution cleanup (Spotify, Apple Music — one name, every release), your website managed, a fan club built and run, merch designs from our factory.", [("Full Machine","$495/mo")], FBP, "Message us")
artists_body += _acard("LEGACY", "The Full Machine plus the A-list push: press kits pitched to major music press and labels, podcast and interview bookings, tour and booking support. For artists with a story the world should hear.", [("Legacy","$995/mo")], FBP, "Message us")
artists_body += '<p class="note">Prefer a manager-style deal? <b style="color:#ffd95e">$295/mo + 10%</b> of the revenue we generate for you — merch, fan club, bookings. We eat when you eat.</p>'
artists_body += '<div class="sec">&Agrave; la carte — one-time packages</div>'
for t, d, p in [
 ("&#128220; PRESS KIT &amp; EPK BUILD","A press kit that gets answered: bio, photos, your best quotes and numbers, one clean link. Built for media, labels, and venues.","$99"),
 ("&#128640; ALBUM LAUNCH CAMPAIGN","A full launch war for your release: countdown content, video-drop strike, pre-order setup so fans can BUY on day one, release-day press and playlist push.","$499"),
 ("&#127916; YOUTUBE CHANNEL REBUILD","Your channel made yours again — branding, SEO, back-catalog organized and searchable, a Shorts program built from your best moments.","$249"),
 ("&#127925; DISTRIBUTION CLEANUP","Fragmented artist pages unified, missing releases delivered to Spotify, Apple Music, and everywhere else. One name, whole catalog.","$199"),
 ("&#11088; FAN CLUB SETUP","Your fan club, built: early listens, exclusive drops, direct fan access. Free tier to build the core, paid tier when it rolls.","$199"),
 ("&#128085; MERCH DESIGN PACK","Five original merch designs, print-ready — plus album bundles and limited-edition drops planned for your store.","$79"),
 ("&#127897;&#65039; PRESS &amp; PODCAST PITCH WAVE","One focused wave of pitches to music podcasts, blogs, and press — your story, your new release, professionally packaged.","$149"),
]:
    artists_body += _acard(t, d, [("One-time", p)], FBP, "Message us")
artists_body += '<div class="sec">For managers &amp; labels</div>'
artists_body += _acard("&#127978; WHITE-LABEL — YOUR ROSTER, OUR MACHINE", "Managers and indie labels: we run your artists' socials, launches, YouTube, and fan clubs under YOUR name. Your clients see your brand; we do the work. Per-artist pricing, monthly.", [], FBP, "Message us for rates")
artists_body += _acard("&#129309; AGENT NETWORK — BRING US ARTISTS, EARN 25%", "Scouts, promoters, connectors: bring us an artist who signs, and you earn 25% of their first package or first three months of representation. You hunt; we service; you get paid.", [], FBP, "Join the network")
artists_body += '<p class="note">Every package is built and run by <b style="color:#ffd95e">Irish + Nova</b> — the same team behind 17 books, seventeen YouTube channels, and four online stores. Artists keep 100% ownership of their music, pages, and stores. Always.</p>'
open('artists.html','w').write(page("Artist Representation — Irish + Nova","Artist representation by Irish + Nova: social media run daily, YouTube, distribution, fan clubs, merch, and press — for musicians building their next chapter.","artists.html","ARTIST REPRESENTATION","You make the music. <b>We make it loud.</b>", artists_body))

# ---------- MODELS ----------
MODEL_FORM_URL = "https://forms.gle/nY93JRXZvZu2Wyf27"
AP = '/home/hatch/workspace/your_files/empire/social/angelica-promo/'
ahero = fileimg(AP + 'browser-download-20261011T175221.731498281Z-0-01a064c1-b5a5-8c66-9c27-45100f687e66_2217ab_cropped.webp', 800, 'assets/models/angelica-hero-800.jpg')
aphotos = ""
for _i, f in enumerate(["browser-download-20261011T175233.844251653Z-1-01a0639a-1249-2585-b886-fac31c052dd6_2217ab_cropped.webp","browser-download-20261011T175311.491413075Z-2-01a063a7-7255-3ed7-da05-aea21ede059f_2217ab_cropped.webp"], 1):
    aphotos += '<div class="book"><img src="%s" alt="Angelica Danielle portfolio photo" loading="lazy"></div>\n' % fileimg(AP + f, 500, 'assets/models/angelica-gallery-%02d-500.jpg' % _i)
HP = '/home/hatch/workspace/your_files/empire/models/heather-lou/'
hhero = fileimg(HP + 'maxim-1.webp', 800, 'assets/models/heather-hero-800.jpg')
hphotos = ""
for _i, f in enumerate(['maxim-2.webp','maxim-3.webp','fb-last-night.jpg','fb-moon.jpg','fb-bonus-vote.jpg'], 1):
    hphotos += '<div class="book"><img src="%s" alt="Heather Lou portfolio photo" loading="lazy"></div>\n' % fileimg(HP + f, 500, 'assets/models/heather-gallery-%02d-500.jpg' % _i)
LP = '/home/hatch/workspace/your_files/empire/talent-agency/leah-video-bank/'
lhero = fileimg(LP + 'leah-portrait-red.jpg', 800, 'assets/models/leah-hero-800.jpg')
lphotos = ""
for _i, f in enumerate(['leah-waterfall.jpg','leah-lake-fence.jpg','leah-denim.jpg','leah-red-lips.jpg','leah-bw-woods.jpg','leah-close-selfie.jpg','leah-red-top.jpg','leah-bw-sparkle-1.jpg','leah-bw-sparkle-2.jpg','leah-lake-smile.jpg','leah-bw-water.jpg','leah-umbrella-creek.jpg','leah-bw-tree.jpg','leah-selfie-soft.jpg','leah-bw-mirror.jpg','leah-photolab-collage.jpg','leah-lake-rock.jpg','leah-mirror-triptych.jpg','leah-bandana-profile.jpg','leah-bandana-front.jpg','leah-street-mask.jpg','leah-silver-gown.jpg','leah-green-hair.jpg','leah-green-hair-chin.jpg','leah-cap-sparkle.jpg','leah-red-streak.jpg','leah-blonde-curls.jpg','leah-love-sand.jpg','leah-red-dress-mirror.jpg','leah-red-hair-mirror.jpg','leah-red-hair-chin.jpg','leah-white-shirt.jpg','leah-orange-tee-mirror.jpg','leah-overalls-mirror.jpg','leah-mask-jersey-hip.jpg','leah-mask-jersey-crossed.jpg','leah-mask-jersey-raised.jpg','leah-mask-jersey-profile.jpg','leah-mask-jersey-peace.jpg','leah-jersey-smile.jpg','leah-jersey-step.jpg','leah-jersey-back.jpg','leah-jersey-back-turn.jpg','leah-jersey-peace.jpg','leah-street-walk-flow.jpg','leah-street-sign-suv.jpg','leah-street-truck.jpg','leah-street-crossing.jpg','leah-street-post.jpg','leah-street-motorcycle.jpg','leah-street-redwall.jpg','leah-jersey-lookback.jpg'], 1):
    lphotos += '<div class="book"><img src="%s" alt="Leah Hamilton portfolio photo" loading="lazy"></div>\n' % fileimg(LP + f, 500, 'assets/models/leah-portfolio-%02d-500.jpg' % _i)
lmotion = ""
for _i, f in enumerate(['spa-city-scoop-dancing-queen-leah-full-res-2025-05-31.jpg','frame-30.jpg','frame-45.jpg','leah-confirmed-1911866939658374-frame.jpg'], 1):
    lmotion += '<div class="book"><img src="%s" alt="Leah Hamilton dancing in Hot Springs" loading="lazy"></div>\n' % fileimg(LP + f, 500, 'assets/models/leah-motion-%02d-500.jpg' % _i)
lstand = '<div style="background:rgba(255,217,94,.07);border-left:3px solid #ffd95e;padding:10px 14px;margin:12px 0;line-height:1.9"><b style="color:#ffd95e">THE DANCING QUEEN FILE</b><br>Spa City Scoop named her the Dancing Queen of Hot Springs (May 31, 2025): <b>177 likes, 217 comments, 66 shares</b>, and the comments are still going.<br>Street clips of her dancing pass <b>4,600 views</b> on a single TikTok.<br>Her bridge dance under the blue and pink lights is the clip the town shares.</div>'
hstand = '<div style="background:rgba(255,217,94,.07);border-left:3px solid #ffd95e;padding:10px 14px;margin:12px 0;line-height:1.9"><b style="color:#ffd95e">MAXIM STANDINGS</b><br>Centerfold Quarterfinals: <b>11th</b> of 14<br>Salty Mermaid (closed Oct 14): <b>final result still posting</b> — Semi-Final Wild Card: <b>23rd</b> of 26<br>Natural Beauty: <b>9th</b> of 10<br>Next Maxim Model Search Quarterfinals: <b>9th</b> of 11<br>IVY Swimwear: <b>5th</b> of 12 in the round closed Oct 16 — new round live: <b>23rd</b> of 45 in Quarterfinals Wild Card<br>Elegance (closed Oct 13): led her group in the final round — Maxim never published a final result.<br>Miss USA Guest of Honor: <b>closed</b>, advanced from Round 2 (number 2 in her group, Top 6 advanced), reached the Quarterfinals at Rank 5, then eliminated. The site published no exact final place.</div>'
_PAGECTX = 'models'
models_body = '<div class="sec">Founding models — exclusively represented by Irish + Nova</div>'
models_body += ('<div class="book" style="padding:0;overflow:hidden"><img src="%s" alt="Heather Lou" style="width:100%%;display:block"><div style="text-align:left;padding:16px"><div class="bt" style="font-size:1.5rem">HEATHER LOU</div><div class="s" style="color:#ffd95e;margin-top:2px"><b>Founding Model — Exclusively represented by Irish + Nova Talent Management</b></div><div class="s" style="color:#9fb3a1;margin-top:4px;line-height:1.6">Five Maxim competitions, one queen. We vote daily, run her promo, and build her reach.</div>' + hstand + '<a class="buy" href="https://models.maxim.com/t/5BPPJMZ7">VOTE FOR HEATHER — FREE, DAILY</a></div></div>') % hhero
models_body += '<div class="sec">Heather Lou — the full gallery</div>'
models_body += '<div class="grid">%s</div>' % hphotos
models_body += '<div style="border-top:1px solid rgba(255,217,94,.4);max-width:520px;margin:72px auto 0"></div>'
models_body += ('<div class="book" style="padding:0;overflow:hidden;margin-top:40px"><img src="%s" alt="Angelica Danielle" style="width:100%%;display:block"><div style="text-align:left;padding:16px"><div class="bt" style="font-size:1.5rem">ANGELICA DANIELLE</div><div class="s" style="color:#ffd95e;margin-top:2px"><b>Founding Model — Exclusively represented by Irish + Nova Talent Management</b></div><div class="s" style="color:#9fb3a1;margin-top:4px;line-height:1.5">Maxim competitor — <b style="color:#ffd95e">Quarterfinals Wild Card: 19th of 45</b> &middot; Salty Mermaid (closed Oct 14): final result still posting. We vote daily, run her promo, and build her reach.</div><a class="buy" href="https://models.maxim.com/t/LAZKZURF">VOTE FOR ANGELICA — FREE, DAILY</a></div></div>') % ahero
models_body += '<div class="grid">%s</div>' % aphotos
models_body += '<div style="border-top:1px solid rgba(255,217,94,.4);max-width:520px;margin:72px auto 0"></div>'
models_body += ('<div class="book" style="padding:0;overflow:hidden;margin-top:40px"><img src="%s" alt="Leah Hamilton" style="width:100%%;display:block"><div style="text-align:left;padding:16px"><div class="bt" style="font-size:1.5rem">LEAH HAMILTON</div><div class="s" style="color:#ffd95e;margin-top:2px"><b>Founding Model, exclusively represented by Irish + Nova Talent Management</b></div><div class="s" style="color:#9fb3a1;margin-top:4px;line-height:1.6">Hot Springs knows her as the Dancing Queen. One woman, her silver gloves, and every corner in town turned into a stage. We run her socials, build her pages, and take the act to the contests and screens it deserves.</div>' + lstand + '<a class="buy" href="https://www.facebook.com/profile.php?id=61594023933396">FOLLOW LEAH ON FACEBOOK</a></div></div>') % lhero
models_body += '<div class="sec">Leah Hamilton, the portfolio</div>'
models_body += '<div class="grid">%s</div>' % lphotos
models_body += '<div class="sec">The Dancing Queen in motion</div>'
models_body += '<div class="grid">%s</div>' % lmotion
models_body += card(MODEL_FORM_URL, "&#128247; MODELS — UPLOAD YOUR PHOTOS", "Managed models: send us your portfolio photos here. We build your showcase page from what you send — you approve everything before it posts.", True)
models_body += '<div class="sec">Model management — sign up</div>'
models_body += '<p class="note">Angelica, Heather, and Leah are our <b style="color:#ffd95e">founding models</b> — represented at the full Cover Run level as the faces of this roster; they are the proof. New models sign up below. You keep 100% rights to your photos; we post only what you approve.</p>'
def _mpack(title, desc, tiers):
    th = "".join('<div class="tier"><div class="tn">%s</div><div class="tp">%s</div></div>' % (n, p) for n, p in tiers)
    return _pkg(FBP, title, desc, th, tiers, "Message us to sign up")
models_body += _mpack("&#128248; MODEL STARTER", "Your showcase portfolio page on our site + a weekly promo post across our channels during your competition.", [("Starter","$95/mo")])
models_body += _mpack("&#128293; CONTENDER", "Everything in Starter, plus daily vote-push content and your socials managed end-to-end while you compete.", [("Contender","$195/mo")])
models_body += _mpack("COVER RUN", "The full machine: daily content, promo videos, cross-promotion across our whole model and artist network, and full campaign management to the final round.", [("Cover Run","$395/mo")])
models_body += '<div class="sec">For the animals</div>'
models_body += card(FBP, "&#128008; FOUNDING PETS", "Our first pet clients are already signed: Tito, Peyton Collier's cat, Cheese, Scotty's cat, and Peyton's dog, Tito's best friend and partner in crime. Star treatment. The rest of the animal kingdom can sign up below.", True)
models_body += '<div class="book" style="text-align:left;padding:16px;margin-top:14px"><div class="bt" style="font-size:1.3rem">&#128008; TITO</div><div class="s" style="color:#ffd95e;margin-top:2px"><b>Founding Pet — Irish + Nova Talent Management</b></div><div class="s" style="color:#9fb3a1;margin-top:4px;line-height:1.6">Tito is Peyton Collier\'s cat: a brown tabby born March 27, 2018. He is loving, clingy, talkative, and proudly bossy, and he loves the outdoors and car rides. Tito is an abuse survivor who lost a leg and most of his tail, and it has slowed him down not one bit. His own page and photo gallery are live, and Nova runs his posts.</div></div>'
models_body += '<p class="note" style="text-align:left"><a href="tito.html" style="color:#ffd95e"><b>Visit Tito\'s own page</b></a></p>'
models_body += '<div class="book" style="text-align:left;padding:16px;margin-top:14px"><div class="bt" style="font-size:1.3rem">&#128021; THE PARTNER IN CRIME</div><div class="s" style="color:#ffd95e;margin-top:2px"><b>Founding Pet — Irish + Nova Talent Management</b></div><div class="s" style="color:#9fb3a1;margin-top:4px;line-height:1.6">Peyton\'s dog is Tito\'s best friend: a black and tan scruffy terrier mix who loves lake days and car rides every bit as much as Tito does. Her name and full bio land here the moment Peyton sends them, and Nova runs her posts too.</div></div>'
def _ppet(title, desc, tiers):
    th = "".join('<div class="tier"><div class="tn">%s</div><div class="tp">%s</div></div>' % (n, p) for n, p in tiers)
    return _pkg(FBP, title, desc, th, tiers, "Message us to sign up")
models_body += _ppet("&#128049; PET STARTER", "A showcase portfolio page for your pet on our site + a weekly feature post across our channels.", [("Pet Starter","$25/mo")])
models_body += _ppet("&#128054; SOCIAL ANIMAL", "Everything in Pet Starter, plus scheduled posts, growth pushes, and fan engagement handled for your pet's pages.", [("Social Animal","$49/mo")])
models_body += _ppet("&#127916; CELEBRITY PET", "The full machine for animals: videos, cross-promotion across our network, and brand-deal outreach. Some pets were born for this.", [("Celebrity Pet","$99/mo")])
models_script = '<style>.book img{cursor:zoom-in}</style><script>(function(){var ov=document.createElement("div");ov.style.cssText="position:fixed;inset:0;background:rgba(0,0,0,.93);display:none;align-items:center;justify-content:center;z-index:999;padding:18px";var im=document.createElement("img");im.alt="";im.style.cssText="max-width:94vw;max-height:92vh;border-radius:10px;box-shadow:0 12px 44px rgba(0,0,0,.7)";var x=document.createElement("button");x.textContent="\u00d7";x.setAttribute("aria-label","Close");x.style.cssText="position:absolute;top:14px;right:18px;background:#0b0f0b;color:#ffd95e;border:1px solid #d4af37;border-radius:999px;width:42px;height:42px;font-size:1.5rem;line-height:1;cursor:pointer";ov.appendChild(im);ov.appendChild(x);document.body.appendChild(ov);function close(){ov.style.display="none";im.removeAttribute("src");document.body.style.overflow="";}ov.addEventListener("click",close);document.addEventListener("keydown",function(e){if(e.key==="Escape"){close();}});var imgs=document.querySelectorAll(".book img");for(var i=0;i<imgs.length;i++){imgs[i].addEventListener("click",function(){im.src=this.src;ov.style.display="flex";document.body.style.overflow="hidden";});}})();</script>'
open('models.html','w').write(page("Models — Managed by Irish + Nova","Models managed by Irish + Nova: founding models Angelica Danielle, Heather Lou, and Leah Hamilton, the Hot Springs Dancing Queen. Portfolios, vote campaigns.","models.html","THE MODELS","Managed loud. <b>Judged on results.</b>", models_body, models_script))

# ---------- TITO ----------
tito_body = card(FBP, "&#128008; TITO THE TABBY", "Founding Pet of Irish + Nova Talent Management, and already the boss of it.", True)
tito_body += '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin-top:14px"><img src="assets/tito-bed.jpg" alt="Tito the brown tabby sitting on his bed among the pillows" style="width:100%;border-radius:12px"><img src="assets/tito-belly.jpg" alt="Tito the brown tabby lounging on his back on the bed" style="width:100%;border-radius:12px"><img src="assets/tito-face.jpg" alt="Close up of Tito the tabby getting his face petted" style="width:100%;border-radius:12px"></div>'
tito_body += card(FBP, "&#128220; HIS STORY", "Tito is Peyton Collier's cat: a brown tabby with a mackerel pattern, born March 27, 2018. He is loving, clingy, talkative, and proudly bossy, and he loves the outdoors and car rides. Tito is an abuse survivor who lost a leg and most of his tail, and it has slowed him down not one bit. These days he supervises the house, demands his treats, and rides like he owns the car. Nova runs his page and his posts.", False)
tito_body += card(FBP, "&#128021; THE PARTNER IN CRIME", "Tito's best friend is Peyton's dog, a black and tan scruffy terrier mix who loves lake days and car rides every bit as much as Tito does. Her founding pet profile joins this page the moment Peyton sends her name and bio.", False)
tito_body += '<p class="note">Tito is part of the founding roster at <a href="models.html" style="color:#ffd95e"><b>Irish + Nova Talent Management</b></a>. Want your pet on the roster? <a href="models.html" style="color:#ffd95e"><b>See the pet packages</b></a>.</p>'
open('tito.html','w').write(page("Tito the Tabby — Founding Pet | Irish + Nova","Meet Tito: Peyton Collier's brown tabby, a three legged abuse survivor and founding pet of Irish + Nova Talent Management. Gallery, story, and posts by Nova.","tito.html","TITO","Founding Pet — Irish + Nova Talent Management", tito_body))

# ---------- ACTORS ----------
def _apack(title, desc, tiers):
    th = "".join('<div class="tier"><div class="tn">%s</div><div class="tp">%s</div></div>' % (n, p) for n, p in tiers)
    return _pkg(FBP, title, desc, th, tiers, "Message us to sign up")
def _aala(title, desc, price):
    th = '<div class="tier"><div class="tn">One-time</div><div class="tp">%s</div></div>' % price
    return _pkg(FBP, title, desc, th, [("One-time", price)], "Message us to order")
_PAGECTX = 'actors'
actors_body = card(FBP, "&#127902; FOUNDING ACTOR SLOT — ONE AVAILABLE", "We're looking for our founding actor: representation is FREE for the founder — headshot portfolio, demo reel, casting waves, and our whole machine behind their career. One slot. When it's gone, it's gone.", True)
actors_body += '<div class="sec">On-camera actors — monthly representation</div>'
actors_body += _apack("&#127775; STARTER", "Headshot portfolio page on our site, your socials run daily, and your casting profiles kept current.", [("Starter","$195/mo")])
actors_body += _apack("&#127916; THE FULL MACHINE", "Everything in Starter, plus a professional demo reel built and refreshed by our video factory, casting submission waves, a full press kit, and interview pitching.", [("Full Machine","$495/mo")])
actors_body += _apack("LEGACY", "Everything in Full Machine, plus dedicated placement campaigns, direct producer and director outreach, and press handling. For actors making a serious run.", [("Legacy","$995/mo")])
actors_body += '<p class="note">Hybrid option: <b style="color:#ffd95e">$295/mo + 10%</b> of revenue we generate. You keep 100% ownership of your work, pages, and accounts — we work for you.</p>'
actors_body += '<div class="sec">Actors — one-time packages</div>'
actors_body += _aala("&#127902; DEMO REEL BUILD", "A casting-grade demo reel cut from your footage by our video factory — paced, titled, and ready to submit.", "$149")
actors_body += _aala("&#128196; ACTOR PRESS KIT & EPK", "A complete electronic press kit: bio, headshots, credits, reel links, and contact sheet.", "$99")
actors_body += _aala("&#128248; HEADSHOT PORTFOLIO PAGE", "Your own showcase page on our site — headshots, reel, credits, and booking contact.", "$79")
actors_body += _aala("&#127919; CASTING PITCH WAVE", "We package you and pitch you to casting calls, indie productions, and commercial work in one coordinated wave.", "$149")
actors_body += _aala("&#129529; IMDb & PROFILE CLEANUP", "We fix and unify your IMDb and casting profiles so you look like the professional you are.", "$99")
actors_body += '<div class="sec">Voice actors</div>'
actors_body += _apack("&#127897; VOICE STARTER", "A voice portfolio page with your demos hosted, your socials run daily, and your casting profiles kept current.", [("Voice Starter","$195/mo")])
actors_body += _apack("&#127908; VOICE FULL MACHINE", "Everything in Voice Starter, plus commercial and character demos produced by our studio, your Voices and Voice123 profiles managed, and weekly submission waves.", [("Voice Full Machine","$495/mo")])
actors_body += _apack("VOICE LEGACY", "Everything in Voice Full Machine, plus agent pitching and direct outreach to animation, game, and audiobook casting. The full career run.", [("Voice Legacy","$995/mo")])
actors_body += '<div class="sec">Voice — one-time packages</div>'
actors_body += _aala("&#127897; VOICE DEMO REEL", "A produced commercial or character demo — scripted, directed, mixed, and ready for casting platforms.", "$129")
actors_body += _aala("&#128266; VOICE PORTFOLIO PAGE", "Your own page on our site with playable demos, your range, and booking contact.", "$79")
actors_body += _aala("&#129513; CASTING PLATFORM SETUP", "Voices, Voice123, and ACX profiles built properly — bios, demos, tags, and rates set to get you found.", "$149")
actors_body += '<div class="sec">Stunt performers</div>'
actors_body += card(FBP, "&#128293; FOUNDING STUNT SLOT — ONE AVAILABLE", "We're opening our stunt division and looking for our founding stunt performer: representation on the house — a coordinator-grade stunt reel, coordinator and production outreach, and our whole content factory behind their career. One slot. When it's gone, it's gone.", True)
actors_body += _apack("&#127902; STUNT REEL BUILD", "A stunt reel cut from your footage by our video factory — falls, fights, driving, and wire work paced the way coordinators actually watch them. A reel that books.", [("Per project","Custom quote")])
actors_body += _apack("&#127919; COORDINATOR &amp; PRODUCTION OUTREACH", "We package your credits, certifications, and reel and put them in front of stunt coordinators and productions in one coordinated wave — then we follow up like we mean it.", [("Per wave","Custom quote")])
actors_body += '<div class="sec">For coaches, casting & agencies</div>'
actors_body += _apack("&#129309; WHITE-LABEL REPRESENTATION", "Acting coaches and agencies: we run your roster's pages, reels, and socials under YOUR brand. Your talent, our machine, your name on it.", [("Per-actor monthly","Custom quote")])
actors_body += _apack("&#128176; AGENT NETWORK — EARN 25%", "Bring us a signing actor or voice actor and earn 25% of their first package or first 3 months. Introductions that turn into careers pay.", [("Referral","25%")])
open('actors.html','w').write(page("Actors & Voice Actors — Representation by Irish + Nova","Actor and voice actor representation by Irish + Nova: headshot portfolios, demo reels, casting waves, stunt performers, voice demos, full career management.","actors.html","ACTORS & VOICE","You bring the talent. <b>We bring the industry to you.</b>", actors_body))

# ---------- SINGERS ----------
_PAGECTX = 'singers'
singers_body = card(FBP, "&#127908; FOUNDING SINGER SLOT — ONE AVAILABLE", "We're looking for our founding singer: representation is FREE for the founder — showcase page, performance videos, audition waves, and our whole machine behind their voice. One slot.", True)
singers_body += '<div class="sec">Singers — monthly representation</div>'
singers_body += _apack("&#127775; STARTER", "Your singer showcase page on our site with your best recordings up front, and your socials run daily.", [("Starter","$195/mo")])
singers_body += _apack("&#127916; THE FULL MACHINE", "Everything in Starter, plus performance videos cut from your recordings, your YouTube channel managed, audition and competition submission waves, and collaboration outreach.", [("Full Machine","$495/mo")])
singers_body += _apack("LEGACY", "Everything in Full Machine, plus A&R and label pitching, press, and booking support. For singers making a serious run.", [("Legacy","$995/mo")])
singers_body += '<p class="note">Hybrid option: <b style="color:#ffd95e">$295/mo + 10%</b> of revenue we generate. You keep 100% ownership of your voice, pages, and accounts — we work for you.</p>'
singers_body += '<div class="sec">Singers — one-time packages</div>'
singers_body += _aala("&#128196; SINGER PRESS KIT & EPK", "Bio, photos, your best recordings, and booking contact — one professional kit that opens doors.", "$99")
singers_body += _aala("&#127908; VOCAL DEMO VIDEO", "A performance video cut from your best recording — styled, captioned for reach, and ready to pitch.", "$129")
singers_body += _aala("&#9654; YOUTUBE CHANNEL BUILD", "A proper artist channel: branding, your catalog uploaded and organized, descriptions that get found.", "$249")
singers_body += _aala("&#127919; AUDITION WAVE", "We package you and submit you to singing competitions, shows, and open calls in one coordinated wave.", "$149")
singers_body += _aala("&#128150; FAN CLUB SETUP", "A private fan club space, launch content, and a welcome sequence that turns listeners into loyalists.", "$199")
singers_body += _aala("&#128085; MERCH DESIGN PACK", "Five original merch designs built around your name and image.", "$79")
singers_body += '<div class="sec">For managers & labels</div>'
singers_body += _apack("&#129309; WHITE-LABEL REPRESENTATION", "Managers and labels: we run your singers' socials, videos, and fan clubs under YOUR brand, per artist.", [("Per-artist monthly","Custom quote")])
singers_body += _apack("&#128176; AGENT NETWORK — EARN 25%", "Bring us a signing singer and earn 25% of their first package or first 3 months.", [("Referral","25%")])
open('singers.html','w').write(page("Singers — Representation by Irish + Nova","Singer representation by Irish + Nova: showcase pages, performance videos, audition waves, A&amp;R pitching, and fan clubs — for vocalists making a serious run.","singers.html","THE SINGERS","Your voice carries it. <b>We make sure the world hears it.</b>", singers_body))

# ---------- CREATORS ----------
_PAGECTX = 'creators'
cr_body = card(FBP, "&#128293; FOUNDING CREATOR SLOT — ONE AVAILABLE", "We're looking for our founding creator: representation is FREE for the founder — content machine, clip factory, and brand-deal outreach behind your channel. One slot.", True)
cr_body += '<div class="sec">Creators — monthly representation</div>'
cr_body += _apack("&#127775; STARTER", "A content calendar that never runs dry: your posting run daily by us, profiles cleaned up, and every platform pointed at your growth.", [("Starter","$195/mo")])
cr_body += _apack("&#127916; THE FULL MACHINE", "Everything in Starter, plus our clip factory cutting shorts and reels from your streams and videos daily, brand-deal outreach, and your link hub managed.", [("Full Machine","$495/mo")])
cr_body += _apack("LEGACY", "Everything in Full Machine, plus sponsorship negotiation, a merch line, PR, and full channel management across every platform you touch.", [("Legacy","$995/mo")])
cr_body += '<p class="note">Hybrid option: <b style="color:#ffd95e">$295/mo + 10%</b> of revenue we generate. You keep 100% ownership of your channels and accounts — we work for you.</p>'
cr_body += '<div class="sec">Creators — one-time packages</div>'
cr_body += _aala("&#127902; CLIP PACK — 10 SHORTS", "Ten scroll-stopping clips cut from your existing content, captioned for reach and ready to post everywhere.", "$79")
cr_body += _aala("&#128176; BRAND DEAL PITCH WAVE", "We build your media kit numbers and pitch you to brands in one coordinated wave.", "$149")
cr_body += _aala("&#128196; CREATOR MEDIA KIT", "Rates, stats, audience, and best content — the kit brands ask for, done right.", "$99")
cr_body += _aala("&#9654; CHANNEL REBUILD", "Branding, banners, descriptions, playlists, and links rebuilt so your channel looks like a business.", "$249")
cr_body += _aala("&#128085; MERCH DESIGN PACK", "Five original merch designs built around your brand.", "$79")
open('creators.html','w').write(page("Creators — Representation by Irish + Nova","Creator representation by Irish + Nova: content calendars, a daily clip factory, brand-deal outreach, and sponsorships — for streamers and video creators.","creators.html","THE CREATORS","You make the content. <b>We make it pay.</b>", cr_body))

# ---------- ATHLETES ----------
_PAGECTX = 'athletes'
ath_body = card(FBP, "&#129354; FOUNDING ATHLETE SLOT — ONE AVAILABLE", "We're looking for our founding athlete: representation is FREE for the founder — highlight reels, sponsor waves, and our whole machine behind your career. One slot.", True)
ath_body += '<div class="sec">Athletes — monthly representation</div>'
ath_body += _apack("&#127775; STARTER", "Your athlete profile page on our site, your socials run daily, and your record and story presented like a pro's.", [("Starter","$195/mo")])
ath_body += _apack("&#127916; THE FULL MACHINE", "Everything in Starter, plus highlight reels cut from your footage, sponsor pitch waves, event and fight promotion, and a full press kit.", [("Full Machine","$495/mo")])
ath_body += _apack("LEGACY", "Everything in Full Machine, plus sponsor negotiation, camp and season content coverage, and press handling. For athletes making a serious run.", [("Legacy","$995/mo")])
ath_body += '<p class="note">Hybrid option: <b style="color:#ffd95e">$295/mo + 10%</b> of revenue we generate. You keep 100% ownership of your name, image, and accounts — we work for you.</p>'
ath_body += '<div class="sec">Athletes — one-time packages</div>'
ath_body += _aala("&#127902; HIGHLIGHT REEL", "A sponsor-grade highlight reel cut from your footage — your best moments, paced to hit hard.", "$129")
ath_body += _aala("&#128176; SPONSOR PITCH WAVE", "We package your story and stats and pitch local and national sponsors in one coordinated wave.", "$149")
ath_body += _aala("&#128196; ATHLETE PRESS KIT", "Bio, record, photos, and highlights in one professional kit that opens sponsor doors.", "$99")
ath_body += _aala("&#128100; ATHLETE PROFILE PAGE", "Your own page on our site — story, record, highlights, and sponsor contact.", "$79")
ath_body += _aala("&#128085; MERCH DESIGN PACK", "Five original merch designs built around your name and nickname.", "$79")
open('athletes.html','w').write(page("Athletes — Representation by Irish + Nova","Athlete representation by Irish + Nova: highlight reels, sponsor pitch waves, press kits, and full career management — for fighters, racers, and competitors.","athletes.html","THE ATHLETES","You put in the work. <b>We get you paid for it.</b>", ath_body))

# ---------- COMEDIANS ----------
_PAGECTX = 'comedians'
com_body = card(FBP, "&#127908; FOUNDING COMEDIAN SLOT — ONE AVAILABLE", "We're looking for our founding comedian: representation is FREE for the founder — clip factory, booking waves, and our whole machine behind your act. One slot.", True)
com_body += '<div class="sec">Comedians — monthly representation</div>'
com_body += _apack("&#127775; STARTER", "Your comedian showcase page, your socials run daily, and your best clips posted on a schedule that builds a following.", [("Starter","$195/mo")])
com_body += _apack("&#127916; THE FULL MACHINE", "Everything in Starter, plus set clips edited weekly, booking pitch waves to clubs and shows, and podcast guesting outreach.", [("Full Machine","$495/mo")])
com_body += _apack("LEGACY", "Everything in Full Machine, plus special and taping promotion campaigns, tour support, and press. For comics making a serious run.", [("Legacy","$995/mo")])
com_body += '<p class="note">Hybrid option: <b style="color:#ffd95e">$295/mo + 10%</b> of revenue we generate. You keep 100% ownership of your material, pages, and accounts — we work for you.</p>'
com_body += '<div class="sec">Comedians — one-time packages</div>'
com_body += _aala("&#127902; SET CLIP PACK", "Your best bits cut into shareable clips, captioned for reach and ready to post everywhere.", "$79")
com_body += _aala("&#128196; COMEDY EPK", "Bio, clips, credits, and booking contact — the kit clubs and bookers ask for.", "$99")
com_body += _aala("&#127919; BOOKING PITCH WAVE", "We package you and pitch clubs, shows, and private events in one coordinated wave.", "$149")
com_body += _aala("&#9654; YOUTUBE CHANNEL BUILD", "A proper comedy channel: branding, your sets uploaded and organized, descriptions that get found.", "$249")
com_body += _aala("&#128150; FAN CLUB SETUP", "A private fan space, launch content, and a welcome sequence that turns laughs into loyalists.", "$199")
open('comedians.html','w').write(page("Comedians — Representation by Irish + Nova","Comedian representation by Irish + Nova: set clips, booking pitch waves, channel builds, and fan clubs — for stand-ups ready to fill bigger rooms nightly.","comedians.html","THE COMEDIANS","You're the funny one. <b>We fill the seats.</b>", com_body))

# ---------- PODCASTERS ----------
_PAGECTX = 'podcasters'
pod_body = card(FBP, "&#127897; FOUNDING PODCAST SLOT — ONE AVAILABLE", "We're looking for our founding podcast: representation is FREE for the founder — production support, daily clips, and sponsor outreach behind your show. One slot.", True)
pod_body += '<div class="sec">Podcasters — monthly representation</div>'
pod_body += _apack("&#127775; STARTER", "Your show page on our site, episode clips cut and posted, and your socials run daily.", [("Starter","$195/mo")])
pod_body += _apack("&#127916; THE FULL MACHINE", "Everything in Starter, plus full production support — editing, show notes, daily clips — and guest booking outreach that lands names.", [("Full Machine","$495/mo")])
pod_body += _apack("LEGACY", "Everything in Full Machine, plus sponsor and ad pitching, network outreach, and live event promotion. For shows making a serious run.", [("Legacy","$995/mo")])
pod_body += '<p class="note">Hybrid option: <b style="color:#ffd95e">$295/mo + 10%</b> of revenue we generate. You keep 100% ownership of your show, feeds, and accounts — we work for you.</p>'
pod_body += '<div class="sec">Podcasters — one-time packages</div>'
pod_body += _aala("&#128293; PODCAST LAUNCH PACKAGE", "Artwork, trailer, platform setup everywhere, launch episodes packaged, and a release campaign.", "$299")
pod_body += _aala("&#127902; EPISODE CLIP PACK", "Ten clips and audiograms cut from your episodes, captioned for reach and ready to post.", "$79")
pod_body += _aala("&#127919; GUEST BOOKING WAVE", "We pitch your show to the guests you actually want, in one coordinated wave.", "$149")
pod_body += _aala("&#128196; SHOW MEDIA KIT", "Stats, audience, and rates — the kit sponsors ask for, done right.", "$99")
pod_body += _aala("&#128176; SPONSOR PITCH WAVE", "We package your numbers and pitch sponsors and ad buyers in one coordinated wave.", "$149")
open('podcasters.html','w').write(page("Podcasters — Representation by Irish + Nova","Podcaster representation by Irish + Nova: production support, episode clips, guest booking, and sponsor pitching — full show management that grows audiences.","podcasters.html","THE PODCASTERS","You bring the voice. <b>We bring the audience.</b>", pod_body))

# ---------- GLAMOUR ----------
_PAGECTX = 'glamour'
glam_body = card(FBP, "FOUNDING GLAMOUR SLOT \u2014 ONE AVAILABLE", "We're selecting our founding glamour model: representation is FREE for the founder \u2014 a vintage-glamour showcase page, competition campaigns, promo content, and our whole machine behind her. One slot. When it's gone, it's gone.", True)
glam_body += '<div class="sec">The glamour division</div>'
glam_body += '<p class="note">Glamour is its own lane here \u2014 the classic tradition: vintage pin-up, old-Hollywood portrait, and modern glamour features, run with the same seriousness as a national competition campaign. Timeless beats trendy. Our founding glamour model becomes the face of the division.</p>'
glam_body += card(MODEL_FORM_URL, "GLAMOUR \u2014 SUBMIT YOUR PORTFOLIO", "Send us your portfolio photos here. We build your showcase page from what you send \u2014 you approve everything before it posts. You keep 100% rights to your photos, always.")
glam_body += '<div class="sec">Glamour management \u2014 sign up</div>'
glam_body += _mpack("GLAMOUR STARTER", "Your showcase portfolio page on our site + a weekly promo post across our channels during your competition or feature run.", [("Starter","$95/mo")])
glam_body += _mpack("GLAMOUR CONTENDER", "Everything in Starter, plus daily vote-push content and your socials managed end-to-end while you compete.", [("Contender","$195/mo")])
glam_body += _mpack("GLAMOUR COVER RUN", "The full machine: daily content, promo videos, cross-promotion across our whole model and artist network, and full campaign management to the final round.", [("Cover Run","$395/mo")])
glam_body += '<div class="sec">Glamour \u2014 one-time packages</div>'
glam_body += _aala("GLAMOUR PORTFOLIO PAGE", "Your own showcase page on our site \u2014 your best shots, your story, and booking contact, presented like a feature.", "$79")
glam_body += _aala("GLAMOUR PROMO REEL", "A short, elegant promo video cut from your photos and footage \u2014 styled, scored, and ready to post everywhere.", "$129")
glam_body += _aala("GLAMOUR PRESS KIT", "Bio, best shots, features, and contact in one professional kit that opens doors.", "$99")
open('glamour.html','w').write(page("Glamour \u2014 Managed by Irish + Nova","The glamour division of Irish + Nova Talent Management: vintage pin-up, old-Hollywood portrait, and modern glamour features. Founding glamour slot open.","glamour.html","GLAMOUR","Old-Hollywood polish. <b>Modern machine.</b>", glam_body))
print('glamour.html', os.path.getsize('glamour.html'))

# ---------- DJS ----------
_PAGECTX = 'djs'
dj_body = card(FBP, "FOUNDING DJ SLOT \u2014 ONE AVAILABLE", "We're looking for our founding DJ: representation is FREE for the founder \u2014 press kit, booking waves, set videos, and our whole machine behind the music. One slot.", True)
dj_body += '<div class="sec">DJs \u2014 monthly representation</div>'
dj_body += _apack("DJ STARTER", "Your DJ profile page on our site, your socials run daily, and every gig, mix, and release posted on schedule.", [("Starter","$195/mo")])
dj_body += _apack("THE FULL MACHINE", "Everything in Starter, plus set and mix videos cut and posted by our factory, your YouTube and SoundCloud managed, booking pitch waves to venues and promoters, and a full press kit.", [("Full Machine","$495/mo")])
dj_body += _apack("DJ LEGACY", "Everything in Full Machine, plus tour and residency support, promoter and label outreach, and press handling. For DJs making a serious run.", [("Legacy","$995/mo")])
dj_body += '<p class="note">Hybrid option: <b style="color:#ffd95e">$295/mo + 10%</b> of revenue we generate. You keep 100% ownership of your music, pages, and accounts \u2014 we work for you.</p>'
dj_body += '<div class="sec">DJs \u2014 one-time packages</div>'
dj_body += _aala("DJ PRESS KIT & EPK", "Bio, photos, mixes, and booking contact in one kit promoters actually answer.", "$99")
dj_body += _aala("LIVE SET VIDEO", "Your set cut into a punchy, booking-grade video \u2014 the moments that get you booked again.", "$149")
dj_body += _aala("BOOKING PITCH WAVE", "We package you and pitch venues, promoters, and events in one coordinated wave.", "$149")
dj_body += _aala("MIX SHOWCASE PAGE", "Your own page on our site \u2014 your best mixes up front, with booking contact.", "$79")
open('djs.html','w').write(page("DJs \u2014 Representation by Irish + Nova","DJ representation by Irish + Nova: press kits, booking pitch waves, set videos, and managed socials — for DJs making a serious run at bigger rooms and tours.","djs.html","THE DJS","You bring the sound. <b>We fill the room.</b>", dj_body))
print('djs.html', os.path.getsize('djs.html'))

# ---------- TALENT HUB ----------
_talent_hdr = fileimg('talent-header.jpg', 1100, 'assets/talent-header.jpg')
talent_body = '<img src="' + _talent_hdr + '" alt="Irish + Nova Talent Management" style="width:100%;border-radius:14px;border:1px solid #3a2f12;margin-bottom:14px">'
talent_body += PROOF_TALENT
talent_body += '<p class="note" style="text-align:center;margin-bottom:16px">One management company for every kind of talent. Socials run daily, content built in-house, careers run like businesses. <b style="color:#ffd95e">Pick your lane:</b></p>'
talent_body += card("artists.html","&#127908; ARTISTS","Full-stack representation for musicians — socials, videos, distribution, fan clubs, and the A-list push. One founding-artist slot is open, free for the founder.")
talent_body += card("models.html","MODELS","Our founding models are signed and competing at the top of national Maxim competitions right now. Portfolios, daily vote campaigns, and sign-up packages inside.")
talent_body += card("glamour.html","GLAMOUR","The classic glamour division \u2014 vintage pin-up, old-Hollywood portrait, and modern glamour features. One founding glamour slot is open, free for the founder.")
talent_body += card("djs.html","DJS","Press kits, booking waves, and set videos for DJs. One founding DJ slot is open, free for the founder.")
talent_body += card("actors.html","&#127902; ACTORS & VOICE ACTORS","Demo reels, casting waves, voice demos, and profile management. One founding-actor slot is open, free for the founder.")
talent_body += card("singers.html","&#127908; SINGERS","Showcase pages, performance videos, and audition waves for vocalists. One founding-singer slot is open, free for the founder.")
talent_body += card("creators.html","&#128293; CREATORS","Content calendars, a daily clip factory, and brand-deal outreach for streamers and influencers. One founding-creator slot is open, free for the founder.")
talent_body += card("athletes.html","&#129354; ATHLETES","Highlight reels and sponsor waves for fighters, racers, and competitors. One founding-athlete slot is open, free for the founder.")
talent_body += card("comedians.html","&#127908; COMEDIANS","Set clips, booking waves, and fan building for stand-ups. One founding-comedian slot is open, free for the founder.")
talent_body += card("podcasters.html","&#127897; PODCASTERS","Production support, daily clips, guest booking, and sponsor pitching. One founding-podcast slot is open, free for the founder.")
talent_body += card("models.html","&#128008; PETS","Yes — we manage star pets too. Our founding cats already have their own socials run by us. Pet packages live on the Models page.")
talent_body += '<p class="note">Every division keeps the same promise: talent keeps 100% ownership of their work, pages, and accounts. <b style="color:#ffd95e">We work for the talent.</b></p>'
open('talent.html','w').write(page("Irish + Nova Talent Management","Irish + Nova Talent Management: one agency for artists, models, glamour, DJs, actors, singers, creators, athletes, comedians, podcasters, and star pets.","talent.html","TALENT MANAGEMENT","Every kind of talent. <b>One machine behind them.</b>", talent_body))

# ---------- INDEX ----------
idx_body = PROOF_TALENT
idx_body += '<div class="topbtns">'
idx_body += '<div class="topcol"><a class="topbtn gold" href="https://chris007hanna-cpu.github.io/sleep-app/">&#127769; Free Sleep Sounds App</a></div>'
idx_body += '<div class="topcol"><a class="topbtn" href="https://www.amazon.com/dp/B09K4WZGVD?tag=hannaenterpri-20">&#127911; Sleep Headphones We Recommend</a><div class="affdisc">As an Amazon Associate, we earn from qualifying purchases.</div></div>'
idx_body += '</div>'
idx_body += card("books.html","&#128218; OUR BOOKS — THE WHOLE LIBRARY","19 titles from Hanna Press. 17 live on Google Play Books and direct from our shop, plus the AI Black Belt Field Guides.")
idx_body += card("shop.html","&#128717;&#65039; THE SHOP","Prompt packs, coloring books, wallpaper bundles, planners — buy direct in our own shop, 100% ours. Also on Gumroad, Whop &amp; Payhip.")
idx_body += card("sleep.html","&#127769; SLEEP SOUNDS","10-hour noise videos + the Colors of Noise album.")
idx_body += card("services.html","&#128188; SERVICES — HIRE US","Ghostwriting, KDP formatting, TikTok scripts, YouTube SEO, social media management.")
idx_body += card("artists.html","&#127908; FOR ARTISTS — REPRESENTATION","Musicians: we run your socials, YouTube, distribution, fan club, and press. One founding-artist slot is open.")
idx_body += card("models.html","THE MODELS","Our managed models: Angelica Danielle, Heather Lou, and Leah Hamilton, the Hot Springs Dancing Queen. Portfolios, vote links, and model sign-ups.")
idx_body += card("glamour.html","FOR GLAMOUR MODELS","The classic glamour division \u2014 vintage pin-up, old-Hollywood portrait, and modern glamour features. One founding glamour slot is open.")
idx_body += card("djs.html","FOR DJS","Representation for DJs: press kits, booking waves, and set videos. One founding DJ slot is open.")
idx_body += card("actors.html","&#127902; FOR ACTORS & VOICE ACTORS","Representation for actors and voice talent: demo reels, casting waves, voice demos, and full career management. One founding-actor slot is open.")
idx_body += card("singers.html","&#127908; FOR SINGERS","Representation for vocalists: showcase pages, performance videos, audition waves, and A&R pitching. One founding-singer slot is open.")
idx_body += card("creators.html","&#128293; FOR CREATORS","Representation for streamers and influencers: content machine, clip factory, and brand deals. One founding-creator slot is open.")
idx_body += card("athletes.html","&#129354; FOR ATHLETES","Representation for fighters, racers, and competitors: highlight reels and sponsor waves. One founding-athlete slot is open.")
idx_body += card("comedians.html","&#127908; FOR COMEDIANS","Representation for stand-ups: set clips, booking waves, and fan building. One founding-comedian slot is open.")
idx_body += card("podcasters.html","&#127897; FOR PODCASTERS","Representation for podcasters: production support, daily clips, guests, and sponsors. One founding-podcast slot is open.")
idx_body += card("talent.html","&#11088; IRISH + NOVA TALENT MANAGEMENT","The whole talent division under one roof — artists, models, actors, singers, creators, athletes, comedians, podcasters, and pets.")
idx_body += card("sell.html","&#128176; SELL YOUR STUFF","Got something to sell? Send pics + your price — we list it, handle buyers, you get paid.")
idx_body += card("watch.html","&#127916; WATCH — ALL OUR CHANNELS","Seventeen YouTube channels and three TikToks.")
idx_body += appcard()
for url, t, s, ucid in [
 ("https://www.youtube.com/@AIBlackBeltHQ","&#129355; AI BLACK BELT","Earn your black belt in AI — free lessons, pro systems.","UC1os6Wse_GZEkUw10Y0WxBQ"),
 ("https://www.youtube.com/@BrokeSurvivalGuide","&#9978; BROKE SURVIVAL GUIDE","Real survival skills for when the money runs out, free resources, street skills, and getting back on your feet starting from zero.","UCLIZHhTq6Pr3CZqYZgCqVbg"),
 ("https://www.youtube.com/@DarkTalesRetoldTV","&#128214; DARK TALES RETOLD","Stories after dark.","UCeLSNAQUPYVs9vF6rG4Edcg"),
 ("https://www.youtube.com/@GildedHeartsDramaOfficial","&#127917; GILDED HEARTS DRAMA","Original romance dramas, clean and sweeping.","UCodnwgPUqXfIMeLUTIZFmAw"),
 ("https://www.youtube.com/@MicroFarmerOfficial","&#127793; MICRO FARMER","Small livestock, aquaponics, microgreens, mushrooms, quail and homestead gigs, small scale. The Shrimp Farmer is the flagship series.","UCr4Chp7whht_UR9syZJ-1Ww"),
 ("https://www.youtube.com/@OnePotBrokeKitchen","&#127858; ONE-POT BROKE KITCHEN","Real food, no money.","UCzPkgcxxy2-ZQxwtOHypjeQ"),
 ("https://www.youtube.com/@PaperFirstTrading","&#128200; PAPER FIRST TRADING","The journal proves itself on paper first.","UCjEckDqnLQTCBIT4JaMP0VA"),
 ("https://www.youtube.com/@PawsWhileYouWork","&#128062; PAWS WHILE YOU WORK","Dog TV for the workday: nature worth watching, all day long.","UCOa38iZ_dzxk98hBiQRsl6Q"),
 ("https://www.youtube.com/@PhoneFlipAcademy","&#128241; PHONE FLIP ACADEMY","Buy low, sell high — phones.","UCmOTdy0tWfsEOePjpIA1P3w"),
 ("https://www.youtube.com/channel/UCXD_Tww1wi5pn2n3JxGhLtw","&#129302; ROBOT BRAIN WORKSHOP","Old drawer phones become robot brains.","UCXD_Tww1wi5pn2n3JxGhLtw"),
 ("https://www.youtube.com/@SimpleSurvivalHQ","&#127794; SIMPLE SURVIVAL","Simple survival that actually works. Real skills, no hype.","UCttOpXwbrJTwIOuoAf0GXsw"),
 ("https://www.youtube.com/@ClaimVsRecord","&#9878;&#65039; THE CLAIM VS. THE RECORD","The claim, checked against the real record.","UCEUUYLKRajxVicLbFP2Kflg"),
 ("https://www.youtube.com/@TheCrowDecoded","&#128038; THE CROW DECODED","How smart crows and ravens really are, proven study by study.","UCJ1YbFbuwBjJebnQb9ebboA"),
 ("https://www.youtube.com/@TheInstantRamenChef","&#127836; THE INSTANT RAMEN CHEF!","Making instant ramen awesome — bold upgrades from a normal home kitchen.","UC5nNRc2NdXLV1FXln9TZh9g"),
 ("https://www.youtube.com/@WhatIfMachineTV","&#127744; WHAT IF MACHINE","One change rewrites everything.","UCvnip76il00fnmbQtcuxiFA"),
 ("https://www.youtube.com/@WhatWeDoInDarkness","&#127769; WHAT WE DO IN DARKNESS","Sleep &amp; focus noise.","UC6M4P62to1D6jMt0smdqiNQ"),
 ("https://www.youtube.com/@WrittenInTheStarsDaily","&#10024; WRITTEN IN THE STARS DAILY","Your stars, every day — daily horoscopes.","UCU2K7DdBvh3EgdulrttEXqA"),
]: idx_body += chancard(url, t, s, ucid)
idx_body += '<div class="sec">Follow</div><div class="row">'
for url, t in [("https://www.tiktok.com/@irish00769","&#127925; TikTok"),("https://www.instagram.com/channa00007","&#128248; Instagram"),("https://x.com/Irish00007","&#120143; X"),("https://www.threads.com/@channa00007","&#129525; Threads"),("https://www.facebook.com/Irish00007","&#128216; Facebook")]:
    idx_body += '<a class="card" href="%s"><div class="t">%s</div></a>' % (url, clean_title(t))
idx_body += '</div>'
open('index.html','w').write(page("Irish + Nova — Books, Products, Services &amp; Talent","Irish + Nova in one place: 19 Hanna Press books, AI prompt packs, planners and digital products, sleep sounds, talent management, and done-for-you services.","index.html","IRISH","Author. Builder. <b>Everything in one place.</b>", idx_body))

for f in ['index.html','books.html','shop.html','sleep.html','watch.html','services.html']:
    print(f, os.path.getsize(f))

# ---------- SHOP v2: direct (zero-commission) + every store ----------
def prow(name, price, note="", pv="", href=None):
    _t = clean_title(name)
    if href:
        _t = '<a class="pvlink" href="%s">%s</a>' % (href, _t)
    return '<div class="book" style="text-align:left"><div class="bt">%s</div><div class="tp" style="font-family:Oswald,sans-serif;color:#ffd95e;font-size:1.25rem;margin-top:4px">%s</div><div class="s" style="color:#9fb3a1;font-size:.9rem;margin-top:2px">%s</div>%s</div>' % (_t, price, note, pv)

BOOK_SLUG = {"The Phone Flip Playbook":"phone-flip-playbook","AI Coding Agents 2026":"ai-coding-agents-2026","Embracing the Unknown":"embracing-the-unknown","Digital Product Empire":"digital-product-empire","Faceless Fortune":"faceless-fortune","Fiverr Fast Start":"fiverr-fast-start","Free Money Handbook":"free-money-handbook","Instant Ramen Chef":"instant-ramen-chef","Laugh Attack":"laugh-attack","Marketplace Millions":"marketplace-millions","Mojo 1.0":"mojo-programming","Phone Repair Mastery":"phone-repair-mastery","Side Hustle Stack":"side-hustle-stack","Solid-State EV Buyer's Guide":"solid-state-ev-guide","Surviving on the Street":"street-survival-guide","The $0 Startup":"zero-dollar-startup","Dad Jokes":"dad-jokes"}
PACK_SLUG = {"Lawyers":"ai-prompts-lawyers","Dentists":"ai-prompts-dentists","Mortgage Brokers":"ai-prompts-mortgage-brokers","Real Estate Agents":"ai-prompts-real-estate","Teachers":"ai-prompts-teachers","Fitness Coaches":"ai-prompts-fitness-coaches","Freelancers":"ai-prompts-freelancers","Etsy Sellers":"ai-prompts-etsy-sellers","Insurance Agents":"ai-prompts-insurance-agents","Car Dealers":"ai-prompts-car-dealers","HR Managers":"ai-prompts-hr-managers","Photographers":"ai-prompts-photographers","Property Managers":"ai-prompts-property-managers","Restaurants":"ai-prompts-restaurants"}
PRINT_SLUG = {"Repair Shop in a Box":"repair-shop-in-a-box","Website Template Pack":"website-template-pack","Christmas Command Center":"christmas-command-center","Advent Devotional + Bible-in-a-Year 2027 Tracker Bundle":"advent-devotional-2027-tracker","Bible Verse Coloring Book":"bible-verse-coloring-book","Cozy Christmas Coloring Book":"cozy-christmas-coloring-book","Big Book of Themed Crosswords":"themed-crosswords","Mandala Dreams Coloring Book":"mandala-dreams-coloring","Halloween Wallpaper Mega Bundle":"halloween-wallpaper-mega-bundle","Vision Board Resolution 2027":"vision-board-resolution-2027","Broke-to-Budget Money Planner":"broke-to-budget-planner","Debt Payoff Planner":"debt-payoff-planner","Emergency Fund & Savings Tracker":"emergency-fund-savings-tracker","Reseller & Phone-Flip Profit Tracker":"reseller-phone-flip-profit-tracker","Fantasy Football & Sports Betting Education Kit":"fantasy-betting-education-kit","Know Your Ballot — Voter Readiness Kit":"voter-readiness-kit","Thanksgiving Host Command Center":"thanksgiving-host-command-center","Contest Vote Campaign Kit":"contest-vote-campaign-kit","2027 Gothic Sleep Scenes Printable Wall Calendar":"gothic-sleep-scenes-calendar-2027","Gothic Halloween Coloring Book":"gothic-halloween-coloring-book","Bakery Recipe Cost Calculator":"bakery-recipe-cost-calculator","72-Hour Ready Binder":"survival-72-hour-binder"}
_PACKFOOT = "PDF pack &middot; Personal-use license &mdash; buy once, use forever"
SHOP_BLURBS = {
"ai-prompts-lawyers": (["Client intake & first contact, drafting & document help, research, summaries & case prep.", "Marketing, social & website content, reviews & reputation, practice management & team.", "How it works: replace the [BRACKETED] details with yours, paste into ChatGPT, Claude, or Gemini \u2014 a professional draft in under a minute.", "For: solo attorneys and small firms that handle their own admin and marketing."], _PACKFOOT),
"ai-prompts-dentists": (["Patient emails & reminders, recall & reactivation texts, scheduling messages.", "Social media content, review replies & reputation, plain-English treatment education.", "Practice growth & team prompts \u2014 the areas that eat a front desk's week.", "How it works: fill the [BRACKETS], paste into any AI chat tool, send."], _PACKFOOT),
"ai-prompts-mortgage-brokers": (["Borrower emails & follow-up, realtor & partner outreach scripts.", "Plain-English explainers & education, scripts & objection handling.", "Social media content, market updates, business growth & reviews.", "Fill the [BRACKETS], paste, send \u2014 follow-up that took an hour takes a minute."], _PACKFOOT),
"ai-prompts-real-estate": (["Listing descriptions that sell the life, not just the square footage.", "Buyer & seller emails, scripts & objection handling, market analysis & farming.", "Social media content and business-growth prompts.", "Fill the [BRACKETS] with your listing details and paste into any AI chat tool."], _PACKFOOT),
"ai-prompts-teachers": (["Lesson planning, assessments & rubrics \u2014 the paperwork, drafted.", "Parent communication, classroom management & engagement ideas.", "Differentiation & support, professional & admin tasks.", "Fill the [BRACKETS], paste into any AI chat tool, get your evenings back."], _PACKFOOT),
"ai-prompts-fitness-coaches": (["Training programs and nutrition guidance, drafted fast.", "Client communication, check-ins, retention & community building.", "Content & social media, sales & business prompts.", "Fill the [BRACKETS], paste into any AI chat tool \u2014 coach more, type less."], _PACKFOOT),
"ai-prompts-freelancers": (["Proposals & pitches that win work, pricing & negotiation scripts.", "Client communication, contracts & admin, marketing yourself.", "Productivity & systems for a one-person business.", "Fill the [BRACKETS], paste into any AI chat tool, send with confidence."], _PACKFOOT),
"ai-prompts-etsy-sellers": (["Listing titles & SEO, product descriptions that convert.", "Shop policies & FAQ, review replies & customer service.", "Marketing & social content, product ideas & pricing.", "Fill the [BRACKETS], paste into any AI chat tool, watch the busywork shrink."], _PACKFOOT),
"ai-prompts-wedding-planners": (["Client inquiry & booking replies, vendor coordination & timelines.", "Client communication & planning guidance that keeps couples calm.", "Social media & marketing content, reviews, referrals & reputation.", "Fill the [BRACKETS], paste into any AI chat tool \u2014 polished replies in seconds."], _PACKFOOT),
"ai-prompts-plumbers-hvac": (["Customer calls, booking & follow-up texts, estimate follow-ups.", "Invoices & service explainers customers actually understand.", "Social media & local marketing, review replies, seasonal campaigns & maintenance plans.", "Business growth, hiring & team prompts. Fill the [BRACKETS] and paste."], _PACKFOOT),
"ai-prompts-small-business": (["50 copy-paste prompts built for one-person and tiny-team businesses.", "Social media posts, product descriptions, customer emails.", "Review responses, marketing & ads.", "No marketing department, no agency budget \u2014 replace the [BRACKETS] and go."], "PDF pack &middot; Works with any AI chat tool"),
"ai-prompts-master-bundle": (["20 packs, 1,019 copy-paste prompts in one download. The seasonal Holiday Marketing pack is sold separately for now and joins the bundle after Dec 26.", "Lawyers \u00b7 Dentists \u00b7 Mortgage Brokers \u00b7 Real Estate Agents \u00b7 Plumbers & HVAC \u00b7 Wedding Planners \u00b7 HR Managers \u00b7 Insurance Agents.", "Etsy Sellers \u00b7 Teachers \u00b7 Fitness Coaches \u00b7 Freelancers \u00b7 Small Business \u00b7 Car Dealers \u00b7 Photographers \u00b7 Property Managers \u00b7 Restaurants \u00b7 Short-Term Rental Hosts \u00b7 Traders & Crypto \u00b7 Local Candidates.", "Bought separately, the packs total $380. The bundle is $49 \u2014 own the whole shelf."], "20 PDFs &middot; Personal-use license &mdash; buy once, use forever"),
"repair-shop-in-a-box": (["The complete paperwork system for an independent phone-repair shop \u2014 14 printable US-Letter pages.", "Intake form with condition checklist & signed authorization, 3-minute diagnostic checklist, estimate/quote worksheet.", "Price menu template + pricing worksheet with the parts-markup and labor math, so you price for profit.", "No Fix No Fee policy, repair terms & limited warranty, receipts, pickup & sign-off form, parts tracker, daily job log \u2014 plus 6 copy-paste customer text scripts."], "Printable PDF &middot; Fill the [BRACKETS] once, photocopy forever &middot; Templates, not legal advice"),
"website-template-pack": (["Six complete websites \u2014 each a single HTML file you can edit in Notepad and put online free in about 10 minutes.", "Link Hub (your own link-in-bio page) \u00b7 Author / Book Sales Page \u00b7 Food Truck / Restaurant One-Pager.", "Barber / Salon Page \u00b7 Handyman / Trades Page \u00b7 Coach / Consultant Page.", "Plus a beginner-friendly README: editing steps and free hosting on Netlify, Cloudflare Pages, or GitHub Pages \u2014 custom domain included. No monthly fees, ever."], "6 HTML templates + README &middot; Mobile-first &middot; You own the files"),
"christmas-command-center": (["A 12-page printable planner that runs your whole December \u2014 from the first budget sketch to the last January return.", "Gift tracker, gift-ideas brainstorm, Christmas card list, and a budget sheet with a hard-cap reality check.", "Meal & menu planner, grocery list in eight store sections, and 25 Advent activity cards.", "Stocking-stuffer ideas, a returns & exchanges tracker, and notes for next year."], "13 PDFs \u2014 full planner + every sheet solo &middot; US Letter &middot; Buy once, use every year"),
"advent-devotional-2027-tracker": (["What you get: two printable PDF books in one bundle, delivered together as one download.", "Part A, the 25 Day Advent Devotional: one page for every day from December 1 to December 25, each with a King James scripture passage, an original reflection on the weekly theme of Hope, Peace, Joy, or Love, a short prayer, and one simple action step. A how to use intro and a Christmas Day closing page are included.", "Part B, the Bible in a Year 2027 Reading Tracker: a complete day by day reading plan for all of 2027, Old Testament plus New Testament plus Psalms twice through plus a Proverb a day, with a checkbox for every day, a reflection prompt for every month, a Verses That Hit Me log, and a completion page to sign on December 31.", "How it works: download the bundle, print the pages at home or at any print shop, slip them into a binder, and check the boxes with a pen as you go.", "Timeline: the devotional carries you from December 1 to December 25, and the tracker picks up on January 1 and runs the full year, so one purchase covers the season and the year after it.", "Fit: made for anyone who wants a simple, steady daily rhythm with scripture through Advent and the year ahead. Print friendly US Letter pages.", "Exclusions: digital download only, nothing is shipped. Personal use only. Scripture quotations are from the King James Version, which is in the public domain, and every reflection, prayer, and prompt is original writing made for this bundle. No medical, financial, or income claims of any kind."], "Two printable PDFs, 28 pages each \u00b7 US Letter \u00b7 Buy once, use every year"),
"bible-verse-coloring-book": (["25 original coloring pages \u2014 cross, dove, church, candle, lighthouse, anchor, heart, rainbow, crown, open Bible, vine, lantern, and more.", "Every page pairs its artwork with a beloved KJV verse to color around: Psalm 23:1, Philippians 4:13, Psalm 119:105, Isaiah 40:31, John 15:5, and 20 more.", "Crisp 300-DPI line art on US Letter pages \u2014 beautiful with markers, gel pens, and colored pencils.", "Calm, screen-free devotional time for adults, kids, family time, and church groups."], "Printable PDF &middot; Print favorites again and again"),
"cozy-christmas-coloring-book": (["25 original cozy scenes \u2014 decorated trees, wreaths, a snowman, a gingerbread house, a reindeer, candles, stockings, gift stacks, hot cocoa, snowflakes, an angel, and a Christmas village.", "Five pages carry a KJV Christmas verse \u2014 Luke 2:14, Isaiah 9:6, Luke 2:10, Matthew 1:23, James 1:17.", "Bold, easy-to-color outlines with detailed patterned baubles; 300-DPI US Letter pages.", "Relaxing for adults, friendly for patient kids and family coloring nights."], "Printable PDF &middot; Buy once, color every Christmas"),
"themed-crosswords": (["12 original themed crosswords: Money & Finance, Food & Cooking, Animals, Travel, Science, Music, Sports, Nature, Home Life, Technology, Health & Fitness, Movies & Fun.", "Every puzzle computer-verified: all crossings check out, every answer fits.", "Full answer keys in the back \u2014 no guessing, no frustration.", "Print-friendly black & white with large, clear grids \u2014 perfect for road trips, rainy days, and gifts."], "Printable PDF &middot; Buy once, solve forever"),
"mandala-dreams-coloring": (["25 one-of-a-kind mandala designs, from simple and soothing to richly detailed.", "Designed for stress relief, focus, and pure creative fun.", "Crisp 300-DPI line art on US Letter pages \u2014 prints beautifully at home.", "Great for adults, teens, and patient kids; a thoughtful gift for anyone who needs to unwind."], "Printable PDF &middot; Print favorites again and again"),
"halloween-wallpaper-mega-bundle": (["Two complete Halloween phone themes in one bundle: Cute Ghosts (playful pumpkins, candy, purple moon) and Halloween Nights (dark and spooky).", "8 full-resolution wallpapers \u2014 Android 1440\u00d73120 home & lock screens, plus both iPhone sizes.", "24 matching app icons (12 per theme) and 2 animated video wallpapers.", "README with Android + iPhone setup included. 100% original art \u2014 no copied IP."], "Instant download &middot; ZIP with 42 files &middot; The two themes sell separately at $4.99 each"),
"vision-board-resolution-2027": (["A complete 2027 goal system in one 15-page printable PDF: vision board, Word of the Year + Top 3 Goals, two SMART goal worksheets, a 12-month milestone map, and quarterly focus pages.", "Built to be used all year: a 30-day habit tracker with streak rules, a weekly action page, and a monthly review page.", "A dedicated Money Goals page \u2014 emergency fund target, the one debt to kill, and an income goal with quarterly check-ins.", 'Plus a 20-line resolution checklist and the "27 for 2027" bucket list.'], "Printable PDF &middot; US Letter &middot; Ink-friendly black & gold &middot; Reprint trackers free forever"),
"broke-to-budget-planner": (["A printable budget workbook for people starting from zero \u2014 no shame, no hype, just a system that respects reality.", "52 weekly budget pages \u2014 one for every week of the year.", "Monthly reviews, so you can see what is actually happening with your money.", "Debt payoff trackers and savings goals built right in."], "Printable workbook PDF &middot; Hanna Press Workbooks"),
"survival-72-hour-binder": (["The paper preparedness system from the Simple Survival channel: print it once, fill it in with a pen, and your household plan still works when the power and the phones do not.", "Getting started (pages 2-3): the Start Here setup order and printing instructions, plus a Household Snapshot with meeting points, an out-of-area contact, and your exact water, gas, and electric shutoff locations.", "Section 1, The 72-Hour Kit (pages 4-7): water and food checklist at one gallon per person per day with three days of no-cook food; light, power, and warmth checklist with the channel's three candle rules; health, hygiene, and tools checklist; and a kit map with a fill-in 5-minute grab order.", "Section 2, The 7-Day Stretch (pages 8-10): per-person amounts to stretch three days to seven, a 7-day meal rotation planner built from your real shelf, and water storage and treatment with CDC boiling and bleach amounts.", "Section 3, Go Bags and Car Kit (pages 11-14): adult go bag checklist, kids and babies go bag with a size swap-out log, full car kit checklist, and a four-season swap sheet with a six-point check log.", "Section 4, Contacts and Documents (pages 15-20): family and neighbors directory; services and officials page with Poison Control 1-800-222-1222 already printed; a documents locator that records locations only, never account numbers or passwords; medical snapshots for three people; an insurance and property locator; and a home and vehicles page.", "Section 5, Pets (pages 21-22): pet go bag checklist and a backup care plan for who can reach your animals if you cannot get home.", "Section 6, Power Outage (pages 23-25): the first-hour outage checklist in order, USDA fridge and freezer food safety times, generator and carbon monoxide rules including the 20-foot rule, an outage log, and a no-signal communication plan.", "Section 7, Rotation (pages 26-30): how first-in, first-out rotation works, plus four tracker sheets with 16 lines each for item, stored date, use-by, quantity, and location. Print more whenever you need them.", "Keeping it current (pages 31-35): a twice-a-year check tied to the clock change, a drill log with a time-to-gather column, cut-out fridge and wallet quick reference cards, and two notes pages.", "Format and delivery: one PDF, 35 pages, US Letter, print-ready at 100% scale. Print-and-fill by hand on purpose, because paper works in an outage. Instant download after purchase, and tracker, log, and notes pages reprint free, forever.", "What it does NOT include: no physical binder, folder, or supplies; no food, water, or gear; and no on-screen fillable form fields. It is general preparedness information built on standard public guidance (Ready.gov and FEMA amounts, CDC water treatment, USDA food safety times), and it says so inside."], "Printable binder PDF &middot; Simple Survival &middot; $12"),
"survival-72-hour-binder-group-license": (["What you get: our Group License covers up to 10 households under one $90 purchase. Every household receives the complete 72-Hour Ready Binder PDF, all 35 pages, ready to print and fill in by hand: the 72 hour kit, the 7 day stretch, go bags and car kit, contacts and documents, the pet plan, the power outage plan, and the rotation trackers.", "Also included: the Leader Sheet, a two page printable for whoever runs the group. It covers how to gather the group and hand out the binder, a session by session walk through of all seven binder sections, and a checklist tracker with a row for each of the 10 households.", "How it works: buy direct on this page using the payment options at the top of the Shop, and put 72 Hour Ready Binder Group License plus your email in the payment note. We email both PDFs to you, usually within a few hours and always the same day. From there you share the binder PDF with your households, one copy per household, by email or as printed copies.", "Timeline: most groups walk one section per session and finish in seven short sessions, or hand the binder out at once and let each household work at its own pace. The twice a year check inside the binder keeps every household current long after the sessions end.", "Fit: churches and faith groups, workplace crews, neighborhood and apartment communities, preparedness groups, and extended families who want every household ready on the same simple system.", "Exclusions: the license covers up to 10 households in your own group only. No resale of the files or of printed copies, and no sharing, posting, or sending the files to anyone beyond your 10 households. This is not a commercial license, and it does not cover bundling the binder with any product or service. No physical binder, folder, or supplies are included.", "The binder itself is general preparedness information built on standard public guidance (Ready.gov and FEMA amounts, CDC water treatment, USDA food safety times). It is not medical, legal, or official agency advice, and it says so inside."], "Two printable PDFs &middot; Simple Survival &middot; Group license for up to 10 households &middot; $90"),
"debt-payoff-planner": (["Enter your debts once \u2014 this Excel workbook builds two complete payoff plans automatically.", "Snowball and avalanche side by side, auto-sorted, with your exact debt-free date and total interest under each plan.", "Track up to 15 debts; three example rows show exactly how it works before you enter your own numbers.", "One extra-payment box shows what an extra $25, $50, or $100 a month does to your payoff date and interest."], "Excel workbook &middot; Works in Excel & Google Sheets &middot; For organization \u2014 not financial advice"),
"emergency-fund-savings-tracker": (["A 20-goal savings planner: name each goal, set a target, log contributions \u2014 % funded, amount remaining, months to goal, and status all calculate automatically.", "A 500-row contribution log with a per-goal running balance that updates itself.", "A live dashboard: total saved, overall % funded, per-goal progress bars, your next milestone, and projected finish dates.", "Starts with the emergency fund \u2014 3 pre-filled examples (starter fund, car down payment, Christmas gifts) show how it works."], "Excel workbook &middot; Works in Excel & Google Sheets &middot; For organization \u2014 not financial advice"),
"ai-like-a-pro": (["Stop using AI like a search box. A working course \u2014 51 pages, 7 modules, exercises as you go.", "Prompting Like a Pro: the five-part anatomy of a prompt that works, power frameworks, and 10 core copy-paste templates.", "Your AI Toolkit (including a complete $0 starting stack), AI for Work & Business, AI for Content & Social \u2014 real workflows, not theory.", "Every module ends with a quiz; pass the 25-question final exam at 80% and earn the printable Certificate of Completion."], "PDF course &middot; Learn at your own pace &middot; Certificate included"),
"ai-prompts-insurance-agents": (["52 copy-paste prompts in 6 categories: lead outreach &amp; first contact, needs analysis &amp; quote conversations, follow-up &amp; objection handling, renewals, client care, and referrals &amp; growth.", "First-response texts, voicemail scripts, and new-mover letters that answer leads in minutes, not days.", "Good/better/best quote presentations and deductible &amp; liability explainers clients actually understand \u2014 all figures stay as placeholders for your verified numbers.", "Renewal-review invitations, premium-change explainers, and claims-support emails that keep clients renewing for a decade."], _PACKFOOT),
"ai-prompts-car-dealers": (["52 copy-paste prompts in 6 categories: lead responses &amp; appointment setting, vehicle descriptions &amp; listing copy, follow-up &amp; sold-customer care, service &amp; retention, social &amp; video content, and reviews &amp; referrals.", "\u201cBest price\u201d replies, first-response texts, and no-show recovery messages that get appointments booked.", "Sold-customer check-ins at day 1, 3, and 30, lease-end explainers, and equity-review invitations that bring buyers back.", "Service reminders, declined-work follow-ups, and review systems that protect your rating and fill the shop."], _PACKFOOT),
"ai-prompts-hr-managers": (["52 copy-paste prompts in 6 categories: job posts &amp; role profiles, screening, interviews &amp; selection communication, onboarding &amp; the first 90 days, performance, feedback &amp; reviews, and policies, handbooks &amp; internal communication \u2014 plus engagement, training &amp; retention.", "Screening questions and interview kits that keep hiring consistent and fair \u2014 the prompts draft and structure; they never score people or make the hiring call for you.", "Offer letters, rejection emails, 30-60-90 onboarding plans, and review-cycle wording written in seconds instead of an afternoon.", "Fill the [BRACKETS], paste into any AI chat tool, send. Drafting templates \u2014 not legal advice; final policy and hiring decisions stay yours."], _PACKFOOT),
"ai-prompts-photographers": (["52 copy-paste prompts in 6 categories: inquiry replies &amp; first contact, booking, pricing &amp; objection handling, session prep &amp; client care, albums, prints &amp; product sales, and social media &amp; portfolio marketing \u2014 plus reviews, referrals &amp; studio growth.", "First replies that answer in minutes while you are still on a shoot, and pricing replies that hold your rate without sounding defensive.", "Session-prep emails, gallery-delivery notes, and album and print offers that feel personal, not pasted.", "Fill the [BRACKETS], paste into any AI chat tool, send \u2014 your words, your style, a fraction of the desk time."], _PACKFOOT),
"ai-prompts-property-managers": (["52 copy-paste prompts in 6 categories: listings &amp; leasing marketing, tenant screening &amp; application replies, maintenance requests &amp; vendor coordination, rent reminders &amp; late-rent communication, renewals, inspections &amp; move-in/move-out, and owner reporting &amp; review responses.", "Listing copy, showing confirmations, and application replies that keep units moving and applicants answered the same day.", "Maintenance triage messages, vendor follow-ups, and rent reminders that stay firm, documented, and professional.", "Fill the [BRACKETS], paste into any AI chat tool, send. Communication templates \u2014 not legal advice; lease and notice rules stay yours to verify."], _PACKFOOT),
"ai-prompts-restaurants": (["52 copy-paste prompts in 6 categories: guest replies, reservations &amp; private events, menus, specials &amp; catering copy, holiday, events &amp; promotions, reviews, reputation &amp; guest recovery, and team, hiring &amp; operations communication \u2014 plus local marketing &amp; social media.", "Reservation confirmations, waitlist texts, and private-event replies handled in minutes between services.", "Menu descriptions, daily specials, and catering copy that sells the dish \u2014 plus calm, professional replies to tough reviews.", "Fill the [BRACKETS], paste into any AI chat tool, send \u2014 front-of-house polish without a marketing hire."], _PACKFOOT),
"ibuddy-talk-it-out": (["Sixty plainspoken prompts you paste into any AI chat and talk through like a trusted friend who has time \u2014 and every prompt works on paper too.", "Six sections of 10, matched to the kind of day you're having: Bad Day Reset, Money Stress, Family &amp; People, 3 A.M. Thoughts, Decisions &amp; Crossroads, Gratitude &amp; Grit.", "Plus the 30-Day Pocket Journal: one page a day, five honest answers, and a weekly \u201cWhich way is up\u201d check-in page.", "A journaling and reflection tool \u2014 not therapy, and never pretending to be. In crisis in the US, call or text 988."], "2 PDFs \u2014 60-prompt pack (8 pp) + 30-day printable pocket journal (35 pp)"),
"ishrinku-say-it-here-first": (["Forty vent prompts in 4 sections: The Text I Almost Sent, 3 A.M. Brain, Family &amp; People Stuff, Boss, Money &amp; Other Villains.", "Every section closes with a Second Pass \u2014 the tomorrow-morning rewrite that keeps the spine and loses the shrapnel.", "Plus the printable unsent-letters journal: 25 letter pages with a SEND IT / SOFTEN IT / BURN IT decision bar, and 5 wide-open 3 A.M. pages with a \u201cStill true?\u201d morning-after box.", "A journaling and venting tool \u2014 not therapy, and never pretending to be. In crisis in the US, call or text 988."], "2 PDFs \u2014 40 vent prompts (11 pp) + printable unsent-letters journal (32 pp)"),
"ai-unlocked-power-prompts": (["Sixty copy-paste templates across 6 sections \u2014 the working library we use to brief AI like staff instead of chatting at it like a search box.", "Brief It Like Staff \u00b7 Roles &amp; Expertise \u00b7 Chaining &amp; Workflows \u00b7 Thinking Partners \u00b7 Learning Anything Fast \u00b7 Creators &amp; Business.", "Every template is ready to paste, with [BRACKETS] where your details go and a one-line note on why it works.", "Pick the template that matches the job, replace the brackets, paste it into your AI chat. That's the whole system."], "PDF \u00b7 60 templates \u00b7 Works with ChatGPT, Claude, Gemini, and any AI chat"),
"ai-prompts-short-term-rental-hosts": (["What you get: one 15-page PDF \u2014 50 original copy-paste prompts in 6 categories (9 listings & marketing, 9 guest messages, 8 during-stay problem solving, 8 cleaning & turnover, 8 pricing & direct booking, 8 reviews & growth).", "A worked example shows exactly how one listing prompt turns bracketed facts into a finished listing, plus the one-line customize formula (tone / length / language) for every prompt.", "Includes the replies hosts dread writing: late-night check-ins, broken Wi-Fi, noise reminders, and mixed or negative review responses \u2014 calm, firm, and policy-safe.", "How it works: pick the prompt, replace the [BRACKETED] placeholders with your real property facts, paste into ChatGPT, Claude, Gemini, or any AI chatbot.", "For: Airbnb / Vrbo / Booking.com hosts and co-hosts with 1\u201320 properties who write the same guest messages every week.", "Please note: prompts only \u2014 not hosting software or legal/tax advice; permit, tax, HOA, and platform rules stay as placeholders for you to verify. No income, occupancy, or review-score promises."], _PACKFOOT),
"ai-prompts-traders-crypto": (["What you get: one 15-page PDF \u2014 50 original copy-paste prompts in 6 categories (9 trade journaling &amp; post-trade review, 9 risk rules &amp; position math worksheets, 8 research &amp; red-flag checklists, 8 market news &amp; report summaries, 8 paper trading &amp; learning practice, 8 records, safety &amp; scam defense).", "A How to Use page with the safety rules up front \u2014 never paste a seed phrase, private key, password, or full account number into an AI tool; verify every AI claim against a primary source; nothing here is financial advice \u2014 plus a worked example and the one-line customize formula (tone / length / language).", "Includes the safety core most packs skip: seed-phrase and private-key warnings, a pump-and-dump red-flag checklist, and a pressure-pitch walk-away checklist.", "How it works: pick the prompt, replace the [BRACKETED] placeholders with your own rules, figures, and documents, paste into ChatGPT, Claude, Gemini, or any AI chatbot \u2014 use the output as a draft you verify, never as advice you follow.", "For: beginners learning how markets work, paper traders, and self-directed traders who want clean records, written rule cards, and scam defenses.", "Please note: prompts only \u2014 not a trading course, signals service, or done-for-you research. NOT financial, investment, tax, or legal advice; nothing recommends buying, selling, or holding anything, predicts any price, or promises any return."], _PACKFOOT),
"ai-prompts-local-candidates": (["What you get: one 15-page PDF \u2014 50 original copy-paste prompts in 6 categories (9 stump speech &amp; your story, 9 social media &amp; everyday content, 8 door-knocking, phones &amp; field work, 8 press, forums &amp; debates, 8 fundraising &amp; volunteers, 8 GOTV, compliance &amp; election-week operations).", "A How to Use page with the compliance rules up front \u2014 verify all voting information against your county clerk / official state sources, never publish an unverified endorsement or statistic, disclose AI assistance where required, and treat the pack as drafting help, not legal advice \u2014 plus a worked 90-second stump speech example.", "Field-ready scripts your volunteers can say out loud: 30-second door intro, phone-bank script, opt-in text set, yard-sign ask, plus debrief and data-hygiene worksheets.", "How it works: pick the prompt, replace the [BRACKETED] placeholders with your own verified facts, paste into ChatGPT, Claude, Gemini, or any AI chatbot \u2014 then read the draft aloud and verify every date, figure, and claim before anyone sees it.", "For: first-time candidates for local office running without paid staff, incumbents in small jurisdictions, and campaign volunteers who need consistent, compliance-safe scripts.", "Please note: prompts only \u2014 not campaign consulting, not legal advice, and not a voter-data product. No walk lists, voter files, or targeting data. Election and campaign-finance law varies by state \u2014 rules must come from your state election/ethics authority and your treasurer or counsel. Nonpartisan in method."], _PACKFOOT),
"ai-prompts-holiday-local-business": (["What you get: one 18-page PDF plus the full pack as a plain-text file — 50 copy-paste holiday marketing prompts in 7 sections: gift cards &amp; gift-giving offers (8), holiday hours, events &amp; announcements (7), Thanksgiving &amp; Black Friday (8), the Christmas countdown (8), last-minute shoppers (6), New Year follow-up &amp; the January save (6), and type-specific starters (7) for retail, salon/spa, restaurant/cafe, home services, and fitness.", "Every prompt takes your real details in [BRACKETS] — business name, offer, dates, hours. Fill them in, paste into ChatGPT, Claude, Gemini, or any AI chat tool, and get a finished post, caption, email, sign, or staff script. A worked example is built into the intro.", "Also inside: a quick-start page (how to use the prompts with any AI assistant, and how to adapt the tone so drafts sound like your counter, not a corporation) and a week-by-week posting calendar from mid-November through New Year that names which prompts to run each week.", "For: local shops, salons and spas, restaurants and cafes, home-service crews, gyms and studios — any small team doing its own marketing.", "Please note: prompts are drafting tools only — no posting service, no ad spend, no done-for-you marketing, and no physical product. They never invent your prices, hours, or offers (you supply every fact in the brackets), and they carry no guaranteed results: no promise of sales, bookings, reach, or rankings. Proof every date, price, and hour before you post. AI-use disclosure: this pack was produced with AI assistance and human direction, and all 50 prompts are original to this pack."], _PACKFOOT),
"fantasy-betting-education-kit": (["What you get: one 10-page PDF in three parts — Part 1, the in-season fantasy playbook (weekly rhythm, waiver priority & FAAB, trade worksheet, start/sit floor-vs-ceiling, bye weeks, injury stash, playoff prep, plus a worked week); Part 2, how odds actually work (American odds table, implied-probability formulas, the vig worked in the open, line movement, the parlay multiplication trap); Part 2B, three worked examples; Part 3, bankroll rules & printable worksheets, plus a plain-English glossary.", "Betting literacy with the arithmetic done in the open: at standard -110 prices both sides imply 52.4%, the vig sums to 104.8%, and the break-even line is 52.4% — the kit shows exactly why most bettors lose over time.", "Bankroll rules written before the season: separate entertainment money only, 1-unit flat betting, written stop rules, and a bet log that records every bet — no exceptions, no deleted losses.", "How it works: run Part 1 weekly with the one-page checklist; read Part 2 once, slowly, with a calculator and redo the worked examples with your own numbers; fill in the Part 3 worksheets before the season.", "For: fantasy managers who lose weeks to Sunday-morning panic, and adults who want to understand exactly how sports-betting pricing works before risking a dollar.", "Please note: EDUCATION ONLY — no picks, no tips, no predictions, no betting advice, and nothing guarantees or implies any win, profit, or fantasy result. Sports betting is 21+ and restricted by state law — know your state's law, use only licensed books where you live. Gambling help is free and confidential in the US: call or text 1-800-GAMBLER. Never bet money needed for anything else."], "PDF kit \u00b7 Personal-use license \u2014 buy once, use forever"),
"thanksgiving-host-command-center": (["What you get: one 20-page printable PDF, US Letter — cover, Start Here guide, 4-week countdown, guest list with RSVPs & dietary tracker for about 20 guests, menu planner, potluck worksheet, turkey timeline worksheet, a filled day-of example for a 4 PM dinner, a blank day-of run sheet, grocery lists by store section, seating chart, budget tracker, one-pot & make-ahead tips, calm fixes, leftovers storage chart & meal ideas, and notes pages.", "How it works: print it once, start four weeks out with the countdown, lock the guest list then the menu — turkey size, grocery run, and budget all hang off the headcount — fill the turkey worksheet the week you buy the bird, and copy the filled example timeline onto your own run sheet.", "For: first-time Thanksgiving hosts, returning hosts tired of holding the plan in their head, potluck hosts, hosts tracking guests' dietary needs, and anyone hosting a real dinner on a real budget.", "Please note: printable PDF only, personal use — no physical product ships. Food-safety figures are general USDA-style guidance for planning; verify them against USDA / FoodSafety.gov for your bird and kitchen before relying on them. Turkey is done at a safe minimum internal temperature of 165°F, checked with a food thermometer. Worksheets, not medical, legal, or financial advice. No income claims — the budget page is about spending on dinner.", "Holiday Host Bundle: pair this planner with the Christmas Command Center ($12) — both host systems together for $19 in the bundle tile below."], "Printable PDF &middot; US Letter &middot; Personal-use license &mdash; buy once, use every year"),
"contest-vote-campaign-kit": (["What you get: one 29-page printable PDF workbook, US Letter \u2014 cover, Start Here guide, the Contest Map of how voting rounds work (group, quarterfinals, semifinals, wild card & finals), a one-time Campaign Hub setup checklist, the 8-step Daily Vote Routine, a full 30-day content calendar, 10 fill-in post templates, 4 poster layout specs, 5 story & short-form scripts, DM scripts for warm contacts, follow-ups & thank-yous, group-share scripts & etiquette, round-by-round checklists, the Last-Day Push and Comeback playbooks, a supporter tracker, a daily standings & content log, a full Rules Compliance chapter, and a weekly review worksheet.", "How it works: read the Contest Map and Compliance chapter first, do the one-time hub setup, then run the 20\u201330 minute daily routine \u2014 each day's post comes from the calendar and templates instead of writing copy from scratch; at every round change, switch to that round's checklist, log standings daily, and run the Last-Day Playbook on closing days.", "For: entrants in online public-vote contests (model / cover contests and similar) promoting themselves, first-time entrants who do not know how rounds and wild cards work, returning entrants whose last campaign faded mid-rounds, and managers or partners running a campaign for one entrant.", "Please note: digital PDF only, personal use \u2014 no physical product ships, and the kit does not vote, post, or message for you. No outcome is guaranteed: no advancement, placement, votes, income, or prize is promised. Organic only \u2014 no bought votes, bots, vote farms, multiple accounts, or prohibited vote-exchange schemes are included, taught, or endorsed. Not legal advice: your contest's official rules win on any conflict. Not affiliated with or endorsed by Maxim or any contest organizer. Hands-on management is a separate service, not included."], "Printable PDF &middot; US Letter &middot; Personal-use license &mdash; buy once, use for every contest"),
"gothic-sleep-scenes-calendar-2027": (["What you get: a ZIP with two print-ready PDFs, US Letter and A4, 14 pages each \u2014 cover plus 12 month pages and a back page. January Snowy Cabin, February Monastery at Night, March Wonderland Mushroom Grove, April Bayou at Night, May Harbor Dock, June Pirate Ship at Anchor, July Ghost Train at Midnight, August Sleepy Hollow, September Friendly Graveyard Ghosts, October Pumpkin Patch, November Haunted Hayride, December Christmas Fireplace. Every month page carries a Sunday-start grid with room to write, moon-phase markers (New, First Quarter, Full, Last Quarter) printed on their exact dates \u2014 including August\u2019s second New Moon on Aug 31 \u2014 and a numbered sleep-tracker strip, one moon per night.", "How it works: download the ZIP, pick US Letter or A4, print at 100% (actual size), one month per sheet \u2014 card stock hangs best. Punch two holes at the top or clip the stack to a board, swap the top sheet each month, and shade one tracker moon each night you fall asleep to that month\u2019s Sleep Scene on What We Do In Darkness (YouTube: @WhatWeDoInDarkness). Reprint any month as often as you like.", "For: Sleep Scenes viewers who want their favorite scene on the wall all month, Gothic and dark-cozy decor lovers, moon-phase followers who want the markers without an app, gift buyers in the October\u2013January calendar season (it prints at home, so it is a same-day gift), and anyone keeping a simple paper log of a calm bedtime ritual.", "Please note: printable PDFs only, personal use \u2014 no physical calendar ships and nothing arrives in the mail. Moon-phase dates are Eastern Time, cross-checked against published 2027 lunar tables; a phase landing near midnight Eastern can fall on the previous calendar day in western time zones. The sleep tracker is a personal log for your own enjoyment \u2014 it is not medical advice and makes no health or sleep-improvement claims. All artwork is original to the Sleep Scenes series \u2014 no licensed characters, no copied artwork. Personal-use license: print for yourself and your household, plus one printed copy as a gift; please do not resell or republish the calendar files.", "Gift set: pair it with the Sleep Sounds Audio Pack ($14) \u2014 calendar + sounds together make the $19 gift set; ask us and we will bundle them."], "Printable PDFs &middot; US Letter + A4 &middot; Personal-use license &mdash; print at home, hang all year"),
"gothic-halloween-coloring-book": (["What you get: one print-ready PDF, 31 pages at 8.5x11 US Letter, 300 DPI \u2014 a title page plus 30 original gothic Halloween coloring pages: haunted house, gothic castle, graveyard gate, jack-o'-lantern trio, black cat on a pumpkin, potion shelf, bubbling cauldron, spider web, spell book, moon mandala, raven, owl in a haunted tree, and more. 18 original scenes; scenes that repeat appear as mirrored variations, so no two pages print identically in orientation.", "How it works: download the PDF after checkout, print any page at home or at a copy shop on standard US Letter paper at actual size, and color with markers, gel pens, colored pencils, or crayons \u2014 for markers, put a spare sheet behind the page. Reprint favorites any time; your purchase includes personal reprints of every page.", "For: adults and teens who love gothic and Halloween art and relaxing coloring, parents and teachers who want clean gore-free Halloween pages for kids and classrooms, and Halloween party hosts who want a cheap zero-prep activity table.", "Please note: digital PDF only, personal use \u2014 no physical book ships. Print for yourself, your family, your classroom, or your party; do not resell, share, or upload the digital file or sell prints of the pages. All artwork is original programmatic line art in a bold, simple style \u2014 see the preview pages before buying if you prefer highly intricate art. Spooky-but-friendly: gothic atmosphere without gore."], "Printable PDF &middot; US Letter &middot; 300 DPI &middot; Personal-use license &mdash; buy once, color every Halloween"),
"bakery-recipe-cost-calculator": (["What you get: one Excel workbook (.xlsx) with 5 tabs and live formulas throughout \u2014 Start Here plain-English instructions, a Recipe Calculator with 24 ingredient rows that costs a batch exactly (ingredients, labor, overhead and packaging) down to cost per unit plus a suggested price at your target cost % and a price rounded to the nearest $0.25, an Ingredient Library pre-loaded with 20 common baking staples that reprices every recipe when you update a grocery price, a Price List with 20 product rows whose first row is linked live to the Recipe Calculator, and a 200-row Sales Log that pulls price and cost from the Price List and totals revenue, cost and profit automatically.", "How it works: download the .xlsx, open it in Microsoft Excel or upload it to Google Sheets, explore the pre-loaded vanilla cupcake sample first (about $0.97 per cupcake fully loaded at the sample prices), then update the Library to the prices you actually pay, cost your own recipes, set your prices, and log sales as they happen. Yellow cells are the only ones you type in \u2014 tan cells are formulas and update themselves. No macros, nothing to install.", "For: home bakers and cottage-food sellers pricing for farmers markets, online orders and word-of-mouth sales, new bakery side-hustles that have been pricing by gut feeling or by copying competitors, and bakers who know their recipes are good but do not know which ones actually make money.", "Please note: digital download only \u2014 no physical product ships, and the file is a spreadsheet costing tool, not a cookbook (sample recipes are costing examples). Library prices are typical US grocery examples \u2014 replace them with your own store prices for exact results, and enter recipe quantities in the same unit the Library uses (grams, ml, or each). This tool does the math only: it is not legal, tax, or financial advice, and no income is promised. Cottage-food and home-bakery rules vary by state and city \u2014 check your local law, labeling, and permit requirements before selling."], "Excel workbook \u00b7 Works in Excel & Google Sheets \u00b7 No macros, nothing to install"),
"voter-readiness-kit": (["What you get: one 9-page printable PDF workbook that walks any voter from not sure if they are registered to a written, ready voting plan in about an hour.", "Step 1 is a registration check worksheet: verify status, address, and polling place against the official record. Arkansas timing is stated honestly: the Oct 5, 2026 registration deadline for the Nov 3 general election has passed, and the live hook is the Dec 1, 2026 runoff, registration deadline Nov 2, 2026.", "The voting plan page carries the verified Arkansas dates: early voting Oct 19 to Nov 2, 2026, Election Day Nov 3 (polls 7:30 a.m. to 7:30 p.m.), absentee request deadlines Oct 27 by mail or electronic delivery and Oct 30 in person.", "Then a sample ballot research worksheet you reuse for every race, an absentee tracker, an ID and polling place checklist with a problems at the polls playbook, and blank any state worksheets so the kit works anywhere in the U.S.", "Please note: nonpartisan, start to finish. No candidate, party, or position is promoted anywhere in the kit. It is a planning tool, not legal advice, and every date and rule must be verified against your county clerk, county election office, or secretary of state before you rely on it."], "Free PDF workbook &middot; Personal use license &middot; Share it freely"),
"reseller-phone-flip-profit-tracker": (["What you get: one .xlsx workbook with 7 tabs \u2014 Start Here setup guide, Dashboard, Settings with editable platform fees, Catalog (100 SKU rows), Sales Log (500 rows), automatic Inventory with reorder flags, and Expenses (200 rows).", "Log a sale in seconds: pick the SKU and platform from dropdowns \u2014 item name, fee %, fee $, and unit cost fill themselves in, and Net Profit is calculated for you.", "Dashboard shows gross sales, fees paid, COGS, gross profit, expenses, TRUE NET PROFIT, inventory value at cost, and a profit-by-platform table (eBay, Marketplace, Etsy, Mercari, Whatnot, Local/Cash).", "Pre-loaded with a sample phone-flip business (12 SKUs, 10 sales, 3 expenses) so you see exactly how it connects before clearing it for your own numbers.", "For: phone flippers and multi-platform resellers who need profit AFTER fees, shipping, and parts \u2014 not just sale prices.", "Please note: spreadsheet only \u2014 it does not connect to platforms or import sales; fee defaults are labeled examples to set to your real rates. For business organization \u2014 not tax, accounting, or financial advice."], "Excel workbook \u00b7 Works in Excel & Google Sheets \u00b7 No macros, nothing to install"),
"ai-memory-sync-kit": (["Every AI you use should already know you. One memory vault in your own cloud \u2014 a context capsule boots any new AI in about 60 seconds, and a two-minute update ritual keeps it current.", "Inside: the 00-START-HERE quick-start guide, plus MEMORY, CAPSULE, CATALOG, VERBATIM-MASTER, and CONVERSATION-LOG templates.", "BOOT-PROMPT and UPDATE-PROMPT: the exact prompts to paste at the start and end of every chat.", "Worked examples are included, so you see the finished state before you write a word. Your files live in your cloud, in plain text you own \u2014 no account, no subscription, nothing to cancel."], "Quick-start PDF + templates, delivered as a ZIP \u00b7 Works with any AI chat"),
}
def shop_pv(slug):
    return pv_link(slug)

shop2 = '''<a class="card hero" href="#direct">
<div class="t">BUY DIRECT = WE KEEP 100%</div>
<div class="s">Every marketplace takes a cut &mdash; Amazon up to 70%. Buy straight from us and the price is the same, but Irish keeps it all. Here's how:</div>
<div class="s" style="margin-top:8px"><b style="color:#ffd95e">1.</b> Send payment on <b>Cash App: $Irish0007</b>, <b>Zelle: chris007hanna@gmail.com</b>, <b>Chime: $Irish007</b>, or <b>PayPal: chris007hanna@gmail.com</b><br>
<b style="color:#ffd95e">2.</b> Put the <b>product name + your email</b> in the payment note<br>
<b style="color:#ffd95e">3.</b> We email your files &mdash; usually within a few hours, always same day</div>
<div style="display:flex;gap:14px;margin-top:14px;flex-wrap:wrap">
<div style="flex:1;min-width:150px;text-align:center"><img src="qr-cashapp.png" alt="Cash App QR code" style="width:100%;max-width:190px;border-radius:12px;background:#fff;padding:6px"><div style="margin-top:6px;font-weight:700;color:#fff">Cash App — $Irish0007</div><div style="color:#9fb3a1;font-size:.85rem">Scan to pay</div></div>
<div style="flex:1;min-width:150px;text-align:center"><img src="qr-zelle-full.png" alt="Zelle QR code" style="width:100%;max-width:190px;border-radius:12px;background:#fff;padding:6px"><div style="margin-top:6px;font-weight:700;color:#fff">Zelle</div><div style="color:#9fb3a1;font-size:.85rem">Scan to pay</div></div>
<div style="flex:1;min-width:150px;text-align:center"><img src="qr-chime.png" alt="Chime QR code" style="width:100%;max-width:190px;border-radius:12px;background:#fff;padding:6px"><div style="margin-top:6px;font-weight:700;color:#fff">Chime — $Irish007</div><div style="color:#9fb3a1;font-size:.85rem">Scan to pay</div></div>
<div style="flex:1;min-width:150px;text-align:center"><img src="paypal-qr.png" alt="PayPal QR code" style="width:100%;max-width:190px;border-radius:12px;background:#fff;padding:6px"><div style="margin-top:6px;font-weight:700;color:#fff">PayPal</div><div style="color:#cfe3d2;font-size:.85rem">chris007hanna@gmail.com</div><div style="color:#9fb3a1;font-size:.85rem">Scan to pay</div></div>
</div>
<div style="margin-top:14px;border:1px solid rgba(255,217,94,.35);background:rgba(255,217,94,.06);border-radius:12px;padding:10px 12px;color:#cfe3d2;font-size:.9rem;line-height:1.55;text-align:left"><b style="color:#ffd95e">GOT A CODE FROM ONE OF OUR ADS?</b> On Gumroad, Whop, or Payhip, enter it at checkout. Paying direct here? Put the code in your payment note and pay the discounted price &mdash; we honor every code we publish. (Codes don't stack and don't apply to bundles, which are already priced down.)</div>
</a>
<div class="sec" id="direct">Direct — eBooks (EPUB, yours forever)</div>
<div class="grid">'''
for n, p in [("The Phone Flip Playbook","$2.99"),("AI Coding Agents 2026","$3.99"),("Embracing the Unknown","$2.99"),("Digital Product Empire","$4.99"),("Faceless Fortune","$2.99"),("Fiverr Fast Start","$2.99"),("Free Money Handbook","$2.99"),("Instant Ramen Chef","$2.99"),("Laugh Attack","$2.99"),("Marketplace Millions","$2.99"),("Mojo 1.0","$3.99"),("Phone Repair Mastery","$2.99"),("Side Hustle Stack","$2.99"),("Solid-State EV Buyer's Guide","$3.99"),("Surviving on the Street","$2.99"),("The $0 Startup","$2.99"),("Dad Jokes","$2.99")]:
    shop2 += prow("&#128218; " + n, p, "EPUB ebook — read anywhere", pv_link(BOOK_SLUG[n]), href=pv_href(BOOK_SLUG[n]))
shop2 += '</div><div class="sec">Direct — AI prompt packs</div><div class="grid">'
shop2 += prow("&#128293; AI PROMPTS MASTER BUNDLE — ALL 20 PACKS", "$49", "20 packs in one bundle. 1,019 prompts, $380 value bought separately. Buy direct: pay, put 'Master Bundle' + your email in the note, we email the files same day", shop_pv("ai-prompts-master-bundle"), href=pv_href("ai-prompts-master-bundle"))
_PACK_COUNTS = {"Real Estate Agents": 53, "Teachers": 48, "Fitness Coaches": 48, "Freelancers": 45, "Etsy Sellers": 53}
for n in ["Lawyers","Dentists","Mortgage Brokers","Real Estate Agents","Teachers","Fitness Coaches","Freelancers","Etsy Sellers","HR Managers","Photographers","Property Managers","Restaurants"]:
    shop2 += prow("&#129302; " + str(_PACK_COUNTS.get(n, 52)) + " AI Prompts for " + n, "$19", "Copy-paste prompts that do the busywork", shop_pv(PACK_SLUG[n]), href=pv_href(PACK_SLUG[n]))
shop2 += prow("&#129302; 52 AI Prompts for Wedding Planners", "$19", "Copy-paste prompts that do the busywork", shop_pv("ai-prompts-wedding-planners"), href=pv_href("ai-prompts-wedding-planners"))
shop2 += prow("&#129302; 52 AI Prompts for Plumbers &amp; HVAC Pros", "$19", "Copy-paste prompts that do the busywork", shop_pv("ai-prompts-plumbers-hvac"), href=pv_href("ai-prompts-plumbers-hvac"))
shop2 += prow("&#129302; 50 AI Prompts for Small Business", "$19", "Copy-paste prompts that do the busywork", shop_pv("ai-prompts-small-business"), href=pv_href("ai-prompts-small-business"))
shop2 += prow("&#128737;&#65039; 52 AI Prompts for Insurance Agents", "$19", "Leads, quotes, renewals &amp; referrals in seconds", shop_pv("ai-prompts-insurance-agents"), href=pv_href("ai-prompts-insurance-agents"))
shop2 += prow("&#128663; 52 AI Prompts for Car Dealers", "$19", "Lead replies, listings, service &amp; reviews", shop_pv("ai-prompts-car-dealers"), href=pv_href("ai-prompts-car-dealers"))
shop2 += prow("&#127968; 50 AI Prompts for Short-Term Rental Hosts", "$19", "Listings, guest messages, reviews &amp; pricing help", shop_pv("ai-prompts-short-term-rental-hosts"), href=pv_href("ai-prompts-short-term-rental-hosts"))
shop2 += prow("&#128200; 50 AI Prompts for Traders &amp; Crypto Learners", "$19", "Trade journaling, risk worksheets &amp; paper trading \u2014 education only, not financial advice", shop_pv("ai-prompts-traders-crypto"), href=pv_href("ai-prompts-traders-crypto"))
shop2 += prow("&#128499;&#65039; 50 AI Prompts for Local Candidates &amp; Campaigns", "$19", "Stump speeches, field scripts &amp; GOTV \u2014 compliance chapter built in, not legal advice", shop_pv("ai-prompts-local-candidates"), href=pv_href("ai-prompts-local-candidates"))
shop2 += prow("&#127876; 50 Holiday Marketing Prompts for Local Businesses", "$19", "Gift cards, Black Friday, the countdown &amp; a posting calendar", shop_pv("ai-prompts-holiday-local-business"), href=pv_href("ai-prompts-holiday-local-business"))
shop2 += '</div><div class="sec">Direct — AI power tools</div><div class="grid">'
shop2 += prow("&#128275; AI Unlocked — Power Prompts", "$19", "60 templates that brief AI like staff", shop_pv("ai-unlocked-power-prompts"), href=pv_href("ai-unlocked-power-prompts"))
shop2 += prow("&#129513; AI Memory Sync Kit", "$39", "Every AI you open already knows you", shop_pv("ai-memory-sync-kit"), href=pv_href("ai-memory-sync-kit"))
shop2 += '</div><div class="sec">Direct — journals for loud days</div><div class="grid">'
shop2 += prow("&#128172; iBuddy — Talk It Out Pack", "$12", "60 talk-it-out prompts + 30-day pocket journal", shop_pv("ibuddy-talk-it-out"), href=pv_href("ibuddy-talk-it-out"))
shop2 += prow("&#128293; iShrinkU — Say It Here First", "$12", "40 vent prompts + unsent-letters journal", shop_pv("ishrinku-say-it-here-first"), href=pv_href("ishrinku-say-it-here-first"))
shop2 += '</div><div class="sec">Direct — printables, packs &amp; tools</div><div class="grid">'
for n, p, note in [
 ("Repair Shop in a Box","$12","The full printable system for a phone-repair side business"),
 ("Website Template Pack","$29","Creator + small business site templates"),
 ("Christmas Command Center","$12","The whole holiday, organized"),
 ("Advent Devotional + Bible-in-a-Year 2027 Tracker Bundle","$9","Advent devotional plus a full 2027 Bible reading tracker"),
 ("Bible Verse Coloring Book","$10","25 faith pages, print at home"),
 ("Cozy Christmas Coloring Book","$8","25 cozy scenes &amp; scripture"),
 ("Big Book of Themed Crosswords","$8","Print-and-play puzzle book"),
 ("Mandala Dreams Coloring Book","$9","Relaxing mandala pages"),
 ("Halloween Wallpaper Mega Bundle","$8","Two spooky phone theme packs"),
 ("Vision Board Resolution 2027","$10","Goals, year map, monthly tracking"),
 ("Broke-to-Budget Money Planner","$9","A planner that respects reality"),
 ("Debt Payoff Planner","$8","Snowball your way out"),
 ("Emergency Fund &amp; Savings Tracker","$8","Watch the cushion grow"),
 ("Reseller & Phone-Flip Profit Tracker","$19","Dashboard, sales log, inventory & auto profit after fees"),
 ("Fantasy Football & Sports Betting Education Kit","$10","In-season fantasy playbook + odds, vig & bankroll math — education only, no picks"),
 ("Know Your Ballot — Voter Readiness Kit","FREE","Nonpartisan 9-page workbook: check your registration, research your ballot, make your plan. <a href=\"assets/downloads/voter-readiness-kit.zip\" download style=\"color:#ffd95e;font-weight:700;text-decoration:underline\">Download the free kit (ZIP)</a>"),
 ("Thanksgiving Host Command Center","$9","20-page printable Thanksgiving planner — 4-week countdown, guest & dietary tracker, turkey timeline, day-of run sheet, groceries, seating & budget"),
 ("Contest Vote Campaign Kit","$49","29-page organic vote-campaign system \u2014 30-day calendar, 10 post templates, poster layouts, DM & group scripts, round checklists & compliance chapter"),
 ("2027 Gothic Sleep Scenes Printable Wall Calendar","$9","14-page printable 2027 wall calendar \u2014 12 original Sleep Scenes, moon phases marked on every month & a nightly sleep-tracker strip (US Letter + A4)"),
 ("Gothic Halloween Coloring Book","$9","30 original gothic Halloween coloring pages \u2014 haunted house, castle, graveyard, pumpkins & potions; bold 300-DPI line art, gore-free, print at home"),
 ("Bakery Recipe Cost Calculator","$9","Cost every recipe exactly \u2014 ingredients, labor & packaging to true cost per unit, suggested prices, price list & sales log (Excel / Google Sheets)"),
 ("72-Hour Ready Binder","$12","The printable emergency preparedness binder and family emergency planner from Simple Survival: the 72 hour kit checklist, go bags, car kit, contacts and documents, pet plan, power outage plan, and supply rotation tracker"),
]:
    shop2 += prow(n, p, note, shop_pv(PRINT_SLUG[n.replace('&amp;', '&')]), href=pv_href(PRINT_SLUG[n.replace('&amp;', '&')]))
shop2 += prow("72-Hour Ready Binder Group License (Up to 10 Households)", "$90", "One purchase covers up to 10 households: the full 35 page binder PDF for every household, plus the leader sheet for whoever runs the group. For churches, workplace groups, neighborhood groups, and extended families")
shop2 += flipper("survival-72-hour-binder", back_page("What&#39;s inside", SHOP_BLURBS["survival-72-hour-binder-group-license"][0], SHOP_BLURBS["survival-72-hour-binder-group-license"][1]), "&#128214; 72-HOUR READY BINDER GROUP LICENSE, FULL BREAKDOWN")
shop2 += prow("&#129383;&#127876; Holiday Host Bundle — Thanksgiving + Christmas Command Centers", "$19", "Both host systems in one bundle: the 20-page Thanksgiving Host Command Center ($9) + the 12-page Christmas Command Center ($12) — $21 bought separately, $19 together. Buy direct: pay, put 'Holiday Host Bundle' + your email in the note, we email both PDFs same day")
shop2 += flipper("advent-devotional-2027-tracker", back_page("What&#39;s inside", SHOP_BLURBS["advent-devotional-2027-tracker"][0], SHOP_BLURBS["advent-devotional-2027-tracker"][1]), "&#128214; ADVENT DEVOTIONAL + BIBLE IN A YEAR 2027 TRACKER BUNDLE, FULL BREAKDOWN")
shop2 += '</div><div class="sec">Direct — phone packs: wallpapers, sounds &amp; stickers</div><div class="grid">'
for n, p, note in [
 ("&#127911; Sleep Sounds Audio Pack","$14","Five one-hour noise colors — white, brown, pink, blue &amp; violet MP3s that mask the world so we sleep"),
 ("&#128241; Phone Theme System Pack — Full (26 Themes)","$19","26 complete phone themes in one ZIP (498 files): 312 matching app icons, 52 phone wallpapers, 52 iPhone wallpapers, 52 widget graphics &amp; 26 desktop wallpapers, plus step-by-step install guides for iPhone, Android &amp; Samsung Galaxy (Theme Park route keeps notification badges). 100% original art, personal use. Buy direct: pay, put 'Phone Theme System Pack' + your email in the note, we email the download same day"),
 ("&#127875; Phone Theme System Pack — Fall Mini (3 Themes)","$12","The 3 fall themes from the Full system — Halloween Nights, Cute Ghosts &amp; Fall Gnomes (61 files): 36 icons, phone + iPhone wallpapers, widget graphics, desktop wallpapers &amp; all 3 install guides. Buy direct: pay, put 'Fall Mini Theme Pack' + your email in the note, we email the download same day"),
 ("&#128241; Christmas Glow Wallpaper Pack","$7","Glowing holiday phone theme — Android &amp; iPhone wallpapers plus 12 matching app icons"),
 ("&#127875; Gothmas Wallpaper Bundle","$9","12 gothic Christmas wallpapers — black tree, blood moon &amp; antique gold, Android + iPhone"),
 ("&#127876; Cozy Christmas Morning Wallpaper Pack","$3.99","Warm Christmas-morning phone theme — wallpapers, matching icons &amp; an animated video wallpaper"),
 ("&#128266; Ringtone &amp; Notification Pack","$7","10 original money &amp; hustle tones, MP3 + WAV — royalty-free, Android &amp; iPhone"),
 ("&#128176; Hustle &amp; Money Sticker Pack","$5","12 motivational digital stickers — transparent PNGs for planners, journals &amp; chats"),
 ("&#127912; Printable Wall Art Quotes","$8","50 original home-office affirmation prints — 8x10 at 300 DPI, ready to frame"),
]:
    shop2 += prow(n, p, note)
shop2 += '</div><div class="sec">Direct — trackers, templates &amp; tools</div><div class="grid">'
for n, p, note in [
 ("&#128196; ATS Resume Template Pack","$10","4 editable ATS-safe resume templates (DOCX + PDF) plus our interview-tips guide"),
 ("&#9823;&#65038; The Smart Player's Playbook","$10","Chess openings, poker math &amp; blackjack basic strategy in one 30-page PDF — our complete games kit"),
 ("&#128197; Content Posting Planner","$9","Our 90-day Excel posting system — idea bank, auto-dated calendar &amp; performance log"),
 ("&#128663; Gig Mileage &amp; Expense Tracker","$7","Excel mile log with an IRS deduction estimator and per-app breakdown — tax time, handled"),
 ("&#129534; Invoice &amp; Client Tracker","$9","Excel invoicing system for freelancers — 50 clients, 200 invoices, a dashboard that shows who owes you"),
 ("&#127919; Savings Goal Tracker","$8","20-goal Excel savings planner with a 500-row contribution log and a live progress dashboard"),
 ("&#128270; Subscription Audit Tracker","$8","Spreadsheet that hunts down every subscription we're leaking money to — and what to cut"),
 ("&#128293; Badass Motivational Sticker Pack","$8","25 original die-cut style stickers (transparent PNG) — print-ready for Cricut &amp; Silhouette"),
 ("&#127807; Modern Geometric Nature Stencil Pack","$9","20 original stencil designs as SVG + PNG — cut-ready for Cricut, Silhouette &amp; laser"),
]:
    shop2 += prow(n, p, note)
shop2 += '</div><p class="note">Anything in the stores below can also be bought direct — same deal: pay, note the product + your email, we deliver.</p>'
shop2 += '<div class="sec">Prefer a marketplace? Every store</div>'
shop2 += card("https://irish007.gumroad.com","&#128717;&#65039; GUMROAD","Wallpaper mega packs, prompt packs, coloring books.")
shop2 += card("https://whop.com/irish007/products","&#127978; WHOP STORE","Every digital product, one storefront.")
shop2 += card("https://whatwedoindarkness.bandcamp.com","&#127911; BANDCAMP — SLEEP ALBUM","Colors of Noise: Sleep &amp; Focus, Vol. 1 — $7 or more.")
open('shop.html','w').write(page("AI Prompt Packs and Digital Products by Irish + Nova","Shop Irish + Nova digital products: AI prompt packs, the AI Memory Sync Kit, planners, coloring books, and wallpaper bundles — buy direct or on our stores.","shop.html","THE SHOP","Same products. <b>Your choice of checkout.</b>", shop2, FLIP_JS))
print('shop.html v2 + QR file refs', os.path.getsize('shop.html'))


# ---------- SELL (consignment intake) ----------
FORM = "https://forms.gle/UMgvbjQjLaqozHar9"
sell_body = card(FORM, "&#128247; START HERE — THE 2-MINUTE FORM", "Photos of your stuff, your asking price, and how to reach you. That's all we need to start.", True)
sell_body += '<div class="sec">How it works</div>'
sell_body += card("#", "1&#65039;&#8419; YOU SEND IT", "From anywhere in the country: fill the form — up to 5 photos per item, the price you want, your contact. No account, no fees, no obligation. You keep the item where you are.")
sell_body += card("#", "2&#65039;&#8419; WE SELL IT", "We create the sales posts, post them on Facebook Marketplace and beyond, handle ALL buyer communication and scheduling, and weed out the flakes and scammers.")
sell_body += card("#", "3&#65039;&#8419; YOU GET PAID", "You handle only the pickup. When it sells, we collect a percentage — the split is agreed with you BEFORE anything lists. No sale, no cost to you. Ever.")
sell_body += '<div class="sec">Rather just message us?</div>'
sell_body += card("https://www.facebook.com/Irish00007", "&#128216; MESSAGE ON FACEBOOK", "Send your pics and price in a message instead — same deal, nationwide.")
sell_body += '<p class="note">Serving sellers nationwide. Furniture, tools, electronics, vehicles, collections — if it\'s legal and yours, we\'ll move it.</p>'
sell_body = sell_body.replace('href="#"', 'href="sell.html"')
open('sell.html','w').write(page("Sell Your Stuff — Consignment by Irish", "Sell your stuff nationwide with Irish + Nova: send photos and your price, we list it, handle every buyer, and schedule the pickup — paid when it sells.", "sell.html", "SELL YOUR STUFF", "You set the price. <b>We do the work.</b>", sell_body))
print('sell.html', __import__('os').path.getsize('sell.html'))

# ---------- POST-FIX: course tile on shop ----------
# (Black Belt card REMOVED 2026-11-11, N504: the WATCH generator list at line ~1163
# now emits the AI Black Belt card itself, so the old post-fix insert asserted
# 'AIBlackBeltHQ' absent and always failed. Generator output is byte-identical
# to the old post-fix card: clean_title() strips the leading emoji entity.)
_s = open('shop.html').read()
_rung1 = '<div class="book" style="text-align:left"><div class="bt"><a class="pvlink" href="https://www.udemy.com/course/ai-career-profiles-get-your-linkedin-indeed-resume-worki/">AI Career Profiles \u2014 Get Your LinkedIn, Indeed &amp; Resume Working for You</a></div><div class="tp" style="font-family:Oswald,sans-serif;color:#ffd95e;font-size:1.25rem;margin-top:4px">FREE on Udemy</div><div class="s" style="color:#9fb3a1;font-size:.9rem;margin-top:2px">Rung 1 of the ladder: the free front door. 9 lectures \u00b7 the three-part system (profile, resume, positioning) \u00b7 section quizzes, final exam + certificate</div></div>'
_rung3 = '<div class="book" style="text-align:left"><div class="bt"><a class="pvlink" href="https://www.udemy.com/course/ai-for-realtors-listings-leads-and-follow-up-on-autopilot/">AI for Realtors \u2014 Listings, Leads &amp; Follow-Up on Autopilot</a></div><div class="tp" style="font-family:Oswald,sans-serif;color:#ffd95e;font-size:1.25rem;margin-top:4px">$89.99 on Udemy</div><div class="s" style="color:#9fb3a1;font-size:.9rem;margin-top:2px">Rung 3 of the ladder: the full realtor workflow system. 16 lectures \u00b7 8 sections \u00b7 complete template library \u00b7 fair-housing guardrails \u00b7 final exam + certificate</div></div>'
_rung2note = '<div class="s" style="color:#9fb3a1;font-size:.9rem;margin-top:6px">Rung 2 of the ladder \u00b7 also on Udemy for $39.99: <a class="pvlink" href="https://www.udemy.com/course/ai-like-a-pro-the-practical-ai-mastery-course/">AI Like a Pro on Udemy (instructor link)</a></div>'
_course_sec = '<div class="sec">Direct \u2014 Courses &amp; Certifications \u00b7 The Udemy Ladder</div><div class="grid">' + _rung1 + '<div class="book" style="text-align:left"><div class="bt"><a class="pvlink" href="preview-ai-like-a-pro.html">AI Like a Pro \u2014 The Practical AI Mastery Course</a></div><div class="tp" style="font-family:Oswald,sans-serif;color:#ffd95e;font-size:1.25rem;margin-top:4px">$29 direct</div><div class="s" style="color:#9fb3a1;font-size:.9rem;margin-top:2px">51-page course: 7 modules, quizzes, final exam + printable certificate</div>' + shop_pv("ai-like-a-pro") + _rung2note + '</div>' + _rung3 + '</div>'
_anchor = '<div class="sec" id="direct">Direct \u2014 eBooks'
assert _anchor in _s and 'AI Like a Pro \u2014 The Practical' not in _s
open('shop.html','w').write(_s.replace(_anchor, _course_sec + _anchor, 1))
print('post-fix applied')

# ---------- POST-FIX: Gilded Hearts theatre-masks emoji on watch + index (2026-11-11, N504) ----------
# clean_title() strips leading emoji entities from card titles by design (Oct 12
# "emojis out of card titles"), so the generator cannot emit the verified-live
# theatre-masks emoji on the Gilded Hearts card (Nov 10 emoji fix, deploys #217/#218).
# Re-apply it here so a rebuild reproduces the live pages byte-identically.
for _f in ('watch.html', 'index.html'):
    _g = open(_f).read()
    assert _g.count('>GILDED HEARTS DRAMA<') == 1 and '&#127917; GILDED HEARTS DRAMA' not in _g, _f
    open(_f, 'w').write(_g.replace('>GILDED HEARTS DRAMA<', '>&#127917; GILDED HEARTS DRAMA<', 1))
print('gilded emoji post-fix applied')

# ---------- POST-FIX: Latest Shorts wall on watch (site parity, 2026-11-07) ----------
# Every public Short on the fleet, each tile carrying that Short's OWN thumbnail.
_w2 = open('watch.html').read()
assert 'Latest Shorts' not in _w2
_sh = '<div class="sec">Latest Shorts — every channel</div>'
for _ch, _items in WATCH_SHORTS:
    _sh += '<div class="sec">%s — Shorts</div>' % _ch
    for _vid, _t in _items:
        _sh += '<div class="card"><div class="t"><a href="https://youtube.com/shorts/%s">%s</a></div><div class="s">%s — a Short. Plays right here on this page.</div>%s<noscript><div class="s"><a href="https://youtube.com/shorts/%s">Watch on YouTube</a></div></noscript></div>\n' % (_vid, clean_title(_t.replace('&', '&amp;')), _ch, vidfac(_vid), _vid)
_tk = '<div class="sec">TikTok</div>'
assert _tk in _w2
open('watch.html','w').write(_w2.replace(_tk, _sh + _tk, 1))
print('shorts wall applied')

# ---------- POST-FIX: Coming soon lanes on watch (fleet board, N393, 2026-11-08) ----------
# The 11 designed, not yet created channels go on the board as their own lanes,
# each owing its first piece. No links and no visit buttons: the channels do not
# exist yet, so nothing here claims they do.
_w3 = open('watch.html').read()
assert 'nine more channels in the works' not in _w3
_cs = '<div class="sec">Coming soon: nine more channels in the works</div>'
for _t, _s in [
 ("&#127917; AI DRAMA STORIES", "Long original AI story dramas."),
 ("&#127769; CHILL TAPES", "Lo-fi chill tapes and ambient sets for long listens."),
 ("&#127864; COCKTAIL CRAFT", "One good drink at a time, made at home."),
 ("&#127928; ELIAS CROWE", "Original country story songs."),
 ("&#127920; HOUSE EDGE HONESTLY", "Casino strategy, the math, honestly. No systems, no hype."),
 ("&#129689; POCKET CHANGE AND PACKS", "Check your change: coins and cards, honestly valued."),
 ("&#128188; THE AI BOARDROOM", "A boardroom of AI chiefs debates the business: marketing, money, legal, sales and wild ideas."),
 ("&#128269; THE LEGEND VS. THE RECORD", "Famous legends graded against the real record, one case at a time."),
 ("&#127911; VESPER", "Late night AI DJ sessions."),
]:
    _cs += '<div class="card"><div class="t">%s</div><div class="s">%s</div><div class="s" style="color:#ffd95e">Coming soon. First episode on the way.</div></div>\n' % (_t, _s)
_ls = '<div class="sec">Latest Shorts — every channel</div>'
assert _ls in _w3
open('watch.html','w').write(_w3.replace(_ls, _cs + _ls, 1))
print('coming-soon lanes applied')

# ---------- REAL ESTATE (services tier for agents & brokerages) ----------
_PAGECTX = 'realestate'
re_body = card(FBP, "&#127968; THE MARKETING DEPARTMENT BEHIND TOP AGENTS", "Listings, content, and a personal brand that closes — run end-to-end by Irish + Nova while you show homes and sign contracts. Built for agents and brokerages who want their marketing to look like their listings: premium.", True)
re_body += '<div class="sec">Monthly programs</div>'
re_body += _apack("&#128202; CONTENT STARTER", "Your monthly content calendar, built for you: 30 days of posts planned and written — new listings, just solds, open houses, market stats — plus testimonial posts that turn happy clients into your best advertising. You post; we build the whole month.", [("Content Starter","$195/mo")])
re_body += _apack("&#127916; MONTHLY MANAGEMENT", "Everything in Content Starter, plus we run it all: your social media managed daily, a listing video for every new listing, and a monthly market report video that makes you the expert your market watches.", [("Monthly Management","$495/mo")])
re_body += _apack("LUXURY PARTNER", "The full department for luxury agents and top teams: everything in Monthly Management, plus listing copy written to a luxury standard, open house campaigns, and a personal brand run like a business. Scoped to your volume.", [("Luxury Partner","By consultation")])
re_body += '<p class="note">Every program is built and run by <b style="color:#ffd95e">Irish + Nova</b> — the same team behind 17 books, seventeen YouTube channels, and four online stores. You keep your brand, your pages, and your accounts. We do the work.</p>'
re_body += '<div class="sec">One-time packages</div>'
re_body += _aala("&#127916; LISTING VIDEO", "A vertical promo video for your listing, cut from your photos — ready for Reels, TikTok, and Shorts the day it hits the market.", "$59")
re_body += _aala("&#9997;&#65039; LISTING COPY", "Your MLS description plus a luxury listing narrative that sells the life, not just the square footage.", "$39")
re_body += _aala("&#127881; OPEN HOUSE KIT", "Promo graphics, story posts, and a recap reel after the event — an open house that markets itself.", "$79")
re_body += _aala("&#10024; PROFILE MAKEOVER", "Bio, link page, and branding rebuilt across every platform — one polished presence that matches your price point.", "$149")
re_body += _aala("&#129302; AI TRAINING FOR YOUR OFFICE", "A hands-on workshop for your brokerage: your agents leave using AI for listings, follow-ups, and marketing the same day. Priced per office.", "By consultation")
re_body += '<div class="sec">Live training for realtors</div>'
re_body += _apack("&#127891; AI LIKE A PRO LIVE WORKSHOP FOR REALTORS", "Our AI Like a Pro course taught live for realtors. One 90 minute virtual session for one office, up to 8 agents, built from our AI for Realtors course. Your team learns the five tools that save a listing agent the most time, with prompts for listings, follow up, and open houses, plus a 7 day starter plan.", [("Live session","$195")])
re_body += '<div class="sec">Start here</div>'
re_body += card("https://irish007.gumroad.com/l/qnaju", "&#129302; AI PROMPTS FOR REAL ESTATE AGENTS — $19", "52 copy-paste prompts for listings, follow-ups, and marketing — the fastest way to see how we think. Then let us run it for you.", True)
re_body += card(FBP, "&#128172; MESSAGE US", "Tell us your market and your volume. We'll reply with the right program — no pressure, no pitch deck.")
open('realestate.html','w').write(page("Real Estate Services — Irish + Nova","Real estate marketing by Irish + Nova: social media management, a video for every listing, monthly content calendars, market report videos, and AI training.","realestate.html","FOR REAL ESTATE PROFESSIONALS","You sell the homes. <b>We run the marketing.</b>", re_body))
print('realestate.html', os.path.getsize('realestate.html'))

# ---------- POST-FIX: real estate section on services + card on index ----------
_sv = open('services.html').read()
if 'REAL ESTATE MARKETING' not in _sv:
    _re_sec = '<div class="sec">For real estate professionals</div>'
    _re_sec += _gigcard("&#127968; REAL ESTATE MARKETING — FOR AGENTS &amp; BROKERAGES", "Your marketing department, run by us: social media management, a video for every listing, monthly content calendars, market report videos, and AI training for your office. Built for agents whose marketing should look like their listings.", [("Content Starter","$195/mo"),("Monthly Management","$495/mo"),("Luxury Partner","By consultation")], "realestate.html", "See the real estate packages")
    _anchor_sv = '<p class="note">Every order runs through Fiverr'
    assert _anchor_sv in _sv
    _sv = _sv.replace(_anchor_sv, _re_sec + _anchor_sv, 1)
    # the services closing note must not claim real estate orders run through Fiverr
    _sv = _sv.replace("Every order runs through Fiverr — secure payment, clear packages, no funny business.", "Fiverr orders run through Fiverr — secure payment, clear packages, no funny business. Real estate programs are by consultation.", 1)
    open('services.html','w').write(_sv)
    print('services.html + real estate section', os.path.getsize('services.html'))
_ix = open('index.html').read()
if 'FOR REAL ESTATE PROS' not in _ix:
    _card_anchor = '<a class="card" href="services.html">'
    assert _card_anchor in _ix
    _pos = _ix.index(_card_anchor)
    _end = _ix.index('</a>', _pos) + len('</a>')
    _re_card = '\n' + card("realestate.html", "&#127968; FOR REAL ESTATE PROS", "Agents &amp; brokerages: your socials run for you, a video for every listing, monthly content, AI training. Marketing that matches your listings.")
    open('index.html','w').write(_ix[:_end] + _re_card + _ix[_end:])
    print('index.html + real estate card', os.path.getsize('index.html'))

# ================= AI LIKE A PRO LIVE TEAM WORKSHOP (IM21, 2026-11-06) =================
DETAILS.update({
('*','AI-LIKE-A-PRO-LIVE-TEAM-WORKSHOP'): _D(
 ["One live 90 minute virtual workshop for your team, up to 8 staff, taught live by Irish + Nova on Google Meet",
  "The 5 AI tools that save the most time, picked for your kind of business",
  "The pro prompting method from our AI Like a Pro course: role, context, task, constraints, format",
  "Prompts written for your business type, ready to copy and use the same day",
  "Live practice on real work: email, documents, research, and customer replies",
  "The safety rules: what never goes into an AI, so your business and your customers stay protected",
  "A 7 day starter plan so the habits stick after the session ends"],
 "Small teams and local businesses, up to 8 staff per session, who want everyone using AI for real work instead of one person experimenting alone. No tech background needed.",
 ["Done for you builds or AI setups (see AI Setup For Your Business and our Local Business services)",
  "Ongoing support after the session (scoped separately if you want it)",
  "The AI Like a Pro course itself (the $29 course in our Shop is the self paced version)",
  "AI platform subscriptions charged by the AI providers (the session runs on free tools first)",
  "Guaranteed income or productivity results (we teach the method; nobody honest can promise the outcome)"],
 price="$195 flat per session",
 how=["Message us with your business type and roughly what your team does all day.",
  "We confirm your session time and the flat $195 price in writing before anything starts.",
  "Pay by PayPal or Cash App to hold your slot.",
  "We meet live on Google Meet for 90 minutes: your team follows along, practices on real work, and leaves with the prompts and the 7 day starter plan."],
 timeline="Sessions are booked and scheduled in advance, at a time we agree in writing. One booking is one 90 minute session for one team of up to 8 staff.",
 noguar=True),
})

# ---------- LOCAL BUSINESS GROWTH (Google profile + booking assistant + websites) ----------
_PAGECTX = 'localbusiness'
lb_body = card(FBP, "&#128270; THE BUSINESSES GOOGLE CAN'T SEE DON'T GET CALLED", "If your business has no Google profile — or a dead one — you're invisible to everyone searching &ldquo;near me&rdquo; on their phone. We fix that: your Google Business Profile built properly, a website we build and manage for you, and an assistant that answers questions and books the job while you're working. Set up once. Working for you every day.", True)
lb_body += '<div class="sec">The core — your website, built &amp; managed</div>'
lb_body += _apack("&#127760; WEBSITE BUILDING &amp; MANAGEMENT", "Your home base online: a fast, real website you own — services, prices, photos, menus, booking — designed and built by us, then managed by us. New photos, seasonal specials, menu changes, holiday hours: send it to us, it's live the same day. Never stale, never a do-it-yourself headache.", [("Build &amp; Manage","By consultation")])
lb_body += '<p class="note">Everything below <b style="color:#ffd95e">stacks onto your website package</b> — or stands on its own. Start with one piece; add the rest when you&rsquo;re ready.</p>'
lb_body += '<div class="sec">Stackable add-ons</div>'
lb_body += _aala("&#128506;&#65039; GOOGLE BUSINESS PROFILE SETUP", "The listing that shows up in Google Maps and &ldquo;near me&rdquo; searches — categories, services, photos, hours, and attributes set up properly, so customers find you first, not your competitor. One-time setup; we handle the whole build.", "$295")
lb_body += _aala("&#128270; GOOGLE BUSINESS PROFILE RESCUE AUDIT", "Start here if you already have a listing. We read your public Google listing the way customers see it and send you a PDF scorecard plus a plain English fix list, with the three highest impact fixes first. Built only from your public listing. No login needed, and no ranking promises. The audit finds the gaps. Our Setup service fixes them.", "$49")
lb_body += _apack("&#129302; THE BOOKING &amp; FAQ ASSISTANT", "An assistant attached to your Google profile and your website that answers the basics — hours, prices, services, directions — and books appointments straight into your calendar. 24/7, including the 9 PM customer who would have called the next name on the list.", [("Assistant","From $149/mo")])
lb_body += _apack("&#128722; ONLINE ORDERING — YOUR OWN PAGE", "For food trucks and restaurants: ordering on your OWN page — menu, order, payment through your own payment apps, and a QR code on the truck — instead of handing roughly 30% of every order to DoorDash and Uber Eats. One flat monthly instead. Trucks add daily location posts: &ldquo;today we're here.&rdquo;", [("Setup","$395"),("Monthly","$99/mo")])
lb_body += _apack("&#11088; REVIEW FUNNEL", "A QR code at the counter, on the receipt, or on the truck window that walks happy customers straight to leaving you a Google review. Reviews are what rank your profile — this makes them automatic.", [("Add-on","$49/mo"),("Full Stack","Included")])
lb_body += '<div class="sec">Monthly programs</div>'
lb_body += _apack("&#128270; GET FOUND", "For businesses Google can't see yet: your Google Business Profile set up and optimized, plus the review funnel running every day. One-time setup, small monthly, found everywhere it matters.", [("Setup","$295"),("Monthly","$49/mo")])
lb_body += _apack("&#129302; GET BOOKED", "Everything in Get Found, plus the Booking &amp; FAQ Assistant on your profile and your site — answering questions and booking appointments around the clock while you do the actual work.", [("Setup","$295"),("Assistant","From $149/mo")])
lb_body += _apack("THE FULL STACK", "The whole front desk: your website built and managed by us, Google profile, booking assistant, online ordering where it fits, and the review funnel included. One team running your entire online presence.", [("Full Stack","By consultation")])
lb_body += '<div class="sec">Live training for your team</div>'
lb_body += _apack("&#127891; AI LIKE A PRO LIVE TEAM WORKSHOP", "Our AI Like a Pro course, taught live to your team: one 90 minute virtual session for up to 8 staff, built around the work your business actually does. Your team leaves with the tools, the prompts, and a 7 day starter plan.", [("Live session","$195")])
lb_body += '<p class="note">Every program is built and run by <b style="color:#ffd95e">Irish + Nova</b> — the same team behind 17 books, seventeen YouTube channels, and four online stores. You keep your business, your pages, and your accounts. We do the work.</p>'
lb_body += '<div class="sec">Built for your trade</div>'
lb_body += card(FBP, "&#129463; DENTISTS &amp; DOCTORS", "Your front desk, extended: the assistant answers hours, insurance, and location questions and books the appointment before the patient calls the next office. One new patient covers the fee — and the assistant never takes a medical detail. It just books.")
lb_body += _apack("&#9878;&#65039; LAWYERS — INTAKE THAT BOOKS CONSULTS", "The intake assistant answers FAQs, captures case-type basics, and books consultations — it never gives legal advice. Your Google profile and the review funnel run underneath: attorneys live on reviews, and ours collects them automatically. Our pilot vertical — the one we're proving first.", [("Setup","$395"),("Intake Assistant","$249/mo"),("Full Practice","$595/mo")])
lb_body += card(FBP, "&#128295; PLUMBERS &amp; TRADES", "Plumbers, HVAC, electricians: &ldquo;near me&rdquo; at 9 PM is a customer with a burst pipe and a card in hand. The assistant grabs the job details and books it while you're still on the last job.")
lb_body += card(FBP, "&#128666; FOOD TRUCKS &amp; SMALL RESTAURANTS", "Your own online ordering — menu, order, payment — with a QR code on the truck, instead of a ~30% cut to the delivery apps. Flat monthly, and daily &ldquo;today we're here&rdquo; location posts that bring the line to you.")
lb_body += card(FBP, "&#128136; SALONS, BARBERS &amp; AUTO", "Booking-native trades run on appointments: chairs and bays filled by an assistant that books, confirms, and answers while your hands are busy.")
lb_body += '<div class="sec">Start here</div>'
lb_body += card(FBP, "&#128172; MESSAGE US", "Tell us your trade and your town. We'll reply with the right stack for your business — no pressure, no pitch deck.", True)
open('localbusiness.html','w').write(page("Local Business Growth — Irish + Nova","Local business growth by Irish + Nova: Google Business Profile setup, a 24/7 booking and FAQ assistant, review funnels, and websites built and managed.","localbusiness.html","FOR LOCAL BUSINESSES","Get found on Google. <b>Get booked around the clock.</b>", lb_body))
print('localbusiness.html', os.path.getsize('localbusiness.html'))

# ---------- POST-FIX: local business section on services + card on index ----------
_sv2 = open('services.html').read()
if 'LOCAL BUSINESS GROWTH' not in _sv2:
    _lb_sec = '<div class="sec">For local businesses</div>'
    _lb_sec += _gigcard("&#127978; LOCAL BUSINESS GROWTH — GET FOUND, GET BOOKED", "For shops, trades, clinics, and food trucks: a Google Business Profile that gets you found, an assistant that answers questions and books appointments 24/7, online ordering without the delivery-app cut, and a website we build and manage for you. Every piece stacks onto a website package — or stands on its own.", [("GBP Setup","$295"),("Assistant","From $149/mo"),("Ordering","$395 + $99/mo")], "localbusiness.html", "See the local business packages")
    _note_at = _sv2.rfind('<p class="note">')
    assert _note_at > 0
    open('services.html','w').write(_sv2[:_note_at] + _lb_sec + _sv2[_note_at:])
    print('services.html + local business section', os.path.getsize('services.html'))
_ix2 = open('index.html').read()
if 'FOR LOCAL BUSINESSES' not in _ix2:
    _re_anchor = '<a class="card" href="realestate.html">'
    assert _re_anchor in _ix2
    _pos2 = _ix2.index(_re_anchor)
    _end2 = _ix2.index('</a>', _pos2) + len('</a>')
    _lb_card = '\n' + card("localbusiness.html", "&#127978; FOR LOCAL BUSINESSES", "Shops, trades, clinics &amp; food trucks: get found on Google, get booked around the clock. Google profiles, a 24/7 booking assistant, online ordering, websites managed.")
    open('index.html','w').write(_ix2[:_end2] + _lb_card + _ix2[_end2:])
    print('index.html + local business card', os.path.getsize('index.html'))

# ---------- POST-FIX: The Irish + Nova Guarantee (local business page + services line) ----------
_lbg = open('localbusiness.html').read()
if 'IRISH + NOVA GUARANTEE' not in _lbg:
    _guar = '<div class="sec">Our promise</div>\n'
    _guar += card(FBP, "THE IRISH + NOVA GUARANTEE", "<b>More business than you can handle &mdash; or we work for free.</b><br><br>Your Google profile built and live within 14 days, or your setup fee comes back.<br><br>If your Google calls, direction requests, and bookings don&rsquo;t climb within 60 days, your monthly pauses &mdash; we work free until it moves.", True)
    _anchor_lb = '<div class="sec">Start here</div>'
    assert _anchor_lb in _lbg
    open('localbusiness.html','w').write(_lbg.replace(_anchor_lb, _guar + _anchor_lb, 1))
    print('localbusiness.html + guarantee', os.path.getsize('localbusiness.html'))
_sv3 = open('services.html').read()
if 'Irish + Nova Guarantee' not in _sv3:
    _gig_end = '<div class="cta">See the local business packages &rarr;</div></a>'
    assert _gig_end in _sv3
    _gline = '\n<p class="note">Backed by <a href="localbusiness.html" style="color:#ffd95e">The Irish + Nova Guarantee</a> &mdash; more business than you can handle, or we work for free.</p>'
    open('services.html','w').write(_sv3.replace(_gig_end, _gig_end + _gline, 1))
    print('services.html + guarantee line', os.path.getsize('services.html'))

# ---------- VIRTUAL SERVICES (done-for-you, delivered online) ----------
_PAGECTX = 'virtual'
v_body = card(FBP, "DONE-FOR-YOU VIRTUAL SERVICES", "Every service on this page is delivered 100% online by Irish + Nova: the same team behind 17 books, seventeen YouTube channels, and four online stores. You keep your accounts, your files, and your work. We do the work.", True)
v_body += '<div class="sec">The services</div>'
v_body += _gigcard("AUDIOBOOK PRODUCTION", "Your book, professionally narrated and mastered &mdash; ACX-ready files, handled end to end. We've produced 16 audiobooks with this exact pipeline.", [("Per finished hour","From $149")], FBP, "Message us")
v_body += _gigcard("BECOME AN AUTHOR", "A book with your name on it sells everything else you do. We write it, format it, design the cover, and walk it onto Amazon through Hanna Press.", [("Full package","From $1,495")], FBP, "Message us")
v_body += _gigcard("PODCAST PRODUCTION", "You record. We cut it, write the notes, pull the clips, and post it everywhere.", [("Per episode","From $79"),("Monthly (4 episodes)","$279")], FBP, "Message us")
v_body += _gigcard("YOUTUBE CHANNEL MANAGEMENT", "We run seventeen channels of our own. Uploads, titles, thumbnails, Shorts &mdash; your channel, handled.", [("Monthly","From $395/mo")], FBP, "Message us")
v_body += _gigcard("VIRTUAL FRONT OFFICE", "Inbox triage, scheduling, and follow-ups for owners drowning in their own messages.", [("Monthly","From $295/mo")], FBP, "Message us")
v_body += _gigcard("RESUME &amp; LINKEDIN MAKEOVER", "Fast-turn and sharp &mdash; built to get the interview.", [("Resume","$79"),("LinkedIn profile","$59"),("Both","$119")], FBP, "Message us")
v_body += _gigcard("AI LIKE A PRO LIVE TEAM WORKSHOP", "Our AI Like a Pro course, taught live to your team: one 90 minute virtual session for up to 8 staff, built around the work your business actually does. Your team leaves with the tools, the prompts, and a 7 day starter plan.", [("Live session","$195")], FBP, "Message us")
v_body += '<p class="note">Every engagement starts with a conversation &mdash; tell us what&rsquo;s eating your time.</p>'
v_body += '<div class="sec">Keep exploring</div>'
v_body += card("services.html", "ALL SERVICES", "Ghostwriting, formatting, design, store setup, and more: every way to hire Irish + Nova in one place.")
v_body += card(FBP, "MESSAGE US", "Tell us the job and the deadline. We reply with the right package: no pressure, no pitch deck.")
open('virtual.html','w').write(page("Virtual Services \u2014 Irish + Nova","Virtual services by Irish + Nova, done for you from anywhere: audiobook production, author packages, podcast production, YouTube management, front office.","virtual.html","VIRTUAL SERVICES","Done for you. <b>From anywhere.</b>", v_body))
print('virtual.html', os.path.getsize('virtual.html'))

# ---------- POST-FIX: virtual services section on services ----------
_sv4 = open('services.html').read()
if 'VIRTUAL SERVICES \u2014 DONE FOR YOU' not in _sv4:
    _v_sec = '<div class="sec">Virtual services</div>'
    _PAGECTX = 'services'
    _v_sec += '<div class="card"><a class="clink" href="virtual.html"><div class="t">VIRTUAL SERVICES \u2014 DONE FOR YOU, FROM ANYWHERE</div><div class="s">Audiobook Production &mdash; <b style="color:#ffd95e">From $149</b><br>Become an Author &mdash; <b style="color:#ffd95e">From $1,495</b><br>Podcast Production &mdash; <b style="color:#ffd95e">From $79/episode</b><br>YouTube Channel Management &mdash; <b style="color:#ffd95e">From $395/mo</b><br>Virtual Front Office &mdash; <b style="color:#ffd95e">From $295/mo</b><br>Resume &amp; LinkedIn Makeover &mdash; <b style="color:#ffd95e">From $59</b></div><div class="cta">See the virtual services &rarr;</div></a>' + _panel("VIRTUAL SERVICES \u2014 DONE FOR YOU, FROM ANYWHERE", [("Audiobook Production","From $149"),("Become an Author","From $1,495"),("Podcast Production","From $79/episode"),("YouTube Channel Management","From $395/mo"),("Virtual Front Office","From $295/mo"),("Resume &amp; LinkedIn Makeover","From $59")], "virtual.html") + '</div>'
    _note_at4 = _sv4.rfind('<p class="note">')
    assert _note_at4 > 0
    open('services.html','w').write(_sv4[:_note_at4] + _v_sec + _sv4[_note_at4:])
    print('services.html + virtual section', os.path.getsize('services.html'))

# ---------- POST-FIX: referral bonus (local business page + services page) ----------
_REF_HEAD = "SEND US A BUSINESS \u2014 GET $50"
_REF_BODY = "Know a business that needs what we do? Send them our way. When they sign up and pay their first invoice, you get $50 \u2014 cash, not credit. Just have them tell us you sent them (or introduce us), and the bonus is yours when their first payment lands. No limit on how many businesses you can send."
_lbr = open('localbusiness.html').read()
if 'SEND US A BUSINESS' not in _lbr:
    _ref_lb = '<div class="sec">Referrals</div>\n'
    _ref_lb += card(FBP, _REF_HEAD, _REF_BODY, True)
    _anchor_ref = '<div class="sec">Start here</div>'
    assert _anchor_ref in _lbr
    open('localbusiness.html','w').write(_lbr.replace(_anchor_ref, _ref_lb + _anchor_ref, 1))
    print('localbusiness.html + referral bonus', os.path.getsize('localbusiness.html'))
_svr = open('services.html').read()
if 'SEND US A BUSINESS' not in _svr:
    _ref_sv = '<div class="sec">Referrals</div>\n'
    _ref_sv += card(FBP, _REF_HEAD, _REF_BODY, True)
    _note_ref = _svr.rfind('<p class="note">')
    assert _note_ref > 0
    open('services.html','w').write(_svr[:_note_ref] + _ref_sv + _svr[_note_ref:])
    print('services.html + referral bonus', os.path.getsize('services.html'))

# ---------- PER-ITEM LOOK-INSIDE PREVIEW PAGES ----------
_PV_SHOP_TITLES = {
    "ai-prompts-lawyers": "52 AI Prompts for Lawyers",
    "ai-prompts-dentists": "52 AI Prompts for Dentists",
    "ai-prompts-mortgage-brokers": "52 AI Prompts for Mortgage Brokers",
    "ai-prompts-real-estate": "53 AI Prompts for Real Estate Agents",
    "ai-prompts-teachers": "48 AI Prompts for Teachers",
    "ai-prompts-fitness-coaches": "48 AI Prompts for Fitness Coaches",
    "ai-prompts-freelancers": "45 AI Prompts for Freelancers",
    "ai-prompts-etsy-sellers": "53 AI Prompts for Etsy Sellers",
    "ai-prompts-wedding-planners": "52 AI Prompts for Wedding Planners",
    "ai-prompts-plumbers-hvac": "52 AI Prompts for Plumbers &amp; HVAC Pros",
    "ai-prompts-small-business": "50 AI Prompts for Small Business",
    "ai-prompts-master-bundle": "AI Prompts Master Bundle &mdash; All 20 Packs",
    "repair-shop-in-a-box": "Repair Shop in a Box",
    "christmas-command-center": "Christmas Command Center",
    "advent-devotional-2027-tracker": "Advent Devotional + Bible-in-a-Year 2027 Tracker Bundle",
    "bible-verse-coloring-book": "Bible Verse Coloring Book",
    "cozy-christmas-coloring-book": "Cozy Christmas Coloring Book",
    "themed-crosswords": "Big Book of Themed Crosswords",
    "mandala-dreams-coloring": "Mandala Dreams Coloring Book",
    "vision-board-resolution-2027": "Vision Board Resolution 2027",
    "broke-to-budget-planner": "Broke-to-Budget Money Planner",
    "ai-like-a-pro": "AI Like a Pro \u2014 The Practical AI Mastery Course",
    "ai-prompts-insurance-agents": "52 AI Prompts for Insurance Agents",
    "ai-prompts-car-dealers": "52 AI Prompts for Car Dealers",
    "ai-prompts-hr-managers": "52 AI Prompts for HR Managers",
    "ai-prompts-photographers": "52 AI Prompts for Photographers",
    "ai-prompts-property-managers": "52 AI Prompts for Property Managers",
    "ai-prompts-restaurants": "52 AI Prompts for Restaurants",
    "ibuddy-talk-it-out": "iBuddy \u2014 Talk It Out Pack",
    "ishrinku-say-it-here-first": "iShrinkU \u2014 Say It Here First",
    "ai-unlocked-power-prompts": "AI Unlocked \u2014 Power Prompts",
    "ai-prompts-short-term-rental-hosts": "50 AI Prompts for Short-Term Rental Hosts",
    "ai-prompts-traders-crypto": "50 AI Prompts for Traders &amp; Crypto Learners",
    "ai-prompts-local-candidates": "50 AI Prompts for Local Candidates &amp; Campaigns",
    "ai-prompts-holiday-local-business": "50 Holiday Marketing Prompts for Local Businesses",
    "reseller-phone-flip-profit-tracker": "Reseller & Phone-Flip Profit Tracker",
    "fantasy-betting-education-kit": "Fantasy Football & Sports Betting Education Kit",
    "voter-readiness-kit": "Know Your Ballot \u2014 Voter Readiness Kit",
    "thanksgiving-host-command-center": "Thanksgiving Host Command Center",
    "contest-vote-campaign-kit": "Contest Vote Campaign Kit",
    "gothic-sleep-scenes-calendar-2027": "2027 Gothic Sleep Scenes Printable Wall Calendar",
    "gothic-halloween-coloring-book": "Gothic Halloween Coloring Book",
    "bakery-recipe-cost-calculator": "Bakery Recipe Cost Calculator",
    "survival-72-hour-binder": "72-Hour Ready Binder: Emergency Preparedness Binder and Family Emergency Planner",
    "ai-memory-sync-kit": "AI Memory Sync Kit",
}
_PV_TITLES = {}
for _pslug, (_pt, _pfmt) in PV_BOOK_META.items():
    _PV_TITLES[_pslug] = (_pt, _pfmt, "books.html", "Books")
for _pslug, _pt in _PV_SHOP_TITLES.items():
    _plines, _pfoot = SHOP_BLURBS[_pslug]
    _PV_TITLES[_pslug] = (_pt, _pfoot, "shop.html", "Shop")
import itertools as _it
def _pv_desc(t):
    # Fitted 150-160 char Look Inside description: full title, or the part before
    # the subtitle dash when the full title is too long to fit the range.
    plain = _html.unescape(t)
    if len(plain) > 34 and ' \u2014 ' in plain:
        plain = plain.split(' \u2014 ')[0]
    core = 'Look Inside ' + plain + ', from Irish + Nova'
    clauses = [' \u2014 flip through the cover, first pages, and back cover',
               ', straight from the real product',
               '. See every page before you buy a thing',
               '. Then grab the full version in our Shop',
               ' \u2014 buy direct and we keep 100%']
    combos = []
    for r in range(len(clauses), 0, -1):
        for combo in _it.combinations(range(len(clauses)), r):
            d = core + ''.join(clauses[i] for i in combo)
            if not d.endswith(('.', '%')):
                d += '.'
            combos.append(d)
    # Prefer a fit on BOTH counts: the decoded text (what search engines
    # read) and the HTML-escaped string the scripted SEO audit measures
    # in the written file (& -> &amp; adds 4 chars, ' -> &#x27; adds 5).
    for d in combos:
        if 150 <= len(d) <= 160 and 150 <= len(_html.escape(d, quote=True)) <= 160:
            return d
    for d in combos:
        if 150 <= len(_html.escape(d, quote=True)) <= 160:
            return d
    return core + ''.join(clauses)  # fallback; audit flags it
def _pv_head(t):
    _d = _html.escape(_pv_desc(t), quote=True)
    return ('<!DOCTYPE html>\n<html lang="en"><head><meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>' + t + ' &mdash; Look Inside | Irish + Nova</title>\n'
            '<meta name="description" content="' + _d + '">\n'
            '<meta property="og:type" content="website"><meta property="og:title" content="' + t + ' &mdash; Look Inside | Irish + Nova"><meta property="og:description" content="' + _d + '">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
            '<style>' + CSS + '\n'
            '.pwrap{max-width:940px;margin:0 auto;padding:26px 16px 52px}\n'
            '.pnav{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px}\n'
            '.backlink{display:inline-block;font-family:\'Oswald\',sans-serif;font-size:.85rem;letter-spacing:.08em;text-transform:uppercase;color:#ffd95e;border:1px solid #37402f;border-radius:8px;padding:8px 14px;background:#0b0f0b;text-decoration:none}\n'
            '.backlink:hover{border-color:#d4af37}\n'
            '.bigflip .fp{border-radius:10px}\n'
            '.bigflip .fbtn{font-size:1rem;padding:11px 22px}\n'
            '.bigflip .fcount{font-size:1rem}\n'
            '.bigflip .ftext{font-size:1rem;padding:20px 18px}\n'
            '.sharebar{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin:2px 0 20px}\n'
            '.sharebtn{font-family:\'Oswald\',sans-serif;font-size:.85rem;letter-spacing:.08em;text-transform:uppercase;color:#111;background:#d4af37;border:1px solid #d4af37;border-radius:8px;padding:9px 16px;cursor:pointer}\n'
            '.sharebtn:hover{background:#ffd95e}\n'
            '.sharebtn.alt{background:#0b0f0b;color:#ffd95e}\n'
            '.sharebtn.alt:hover{border-color:#d4af37}\n'
            '</style></head><body><div class="pwrap">\n')
_pv_count = 0
for _pslug in sorted(_PV_TITLES):
    if not pv_has(_pslug):
        continue
    _pt, _pfmt, _bhref, _blabel = _PV_TITLES[_pslug]
    if _bhref == "books.html":
        _bhtml = back_page(_pt, book_desc(_pslug), _pfmt)
        _buynote = 'The full book is available in <a href="shop.html" style="color:#ffd95e">the Shop</a> and on our stores &mdash; Amazon links are on the <a href="books.html" style="color:#ffd95e">Books</a> page.'
    else:
        _blines, _ = SHOP_BLURBS[_pslug]
        _bhtml = back_page("What&#39;s inside", _blines, _pfmt)
        _buynote = 'The full product is available in <a href="shop.html" style="color:#ffd95e">the Shop</a> and on our stores &mdash; buy direct (we keep 100%) or on Gumroad, Whop, and Payhip.'
    _pnav = ('<div class="pnav"><a class="backlink" href="' + _bhref + '">&larr; Back to ' + _blabel + '</a>'
             '<a class="backlink" href="index.html">&#127968; Main Page</a></div>\n')
    _out = _pv_head(_pt)
    _out += _pnav
    _out += ('<header><img src="assets/logo.jpg" alt="Irish shamrock coin logo">\n'
             '<h1>' + _pt + '</h1><p class="tag">&#128214; Look Inside &mdash; <b>flip through it</b></p></header>\n')
    _out += ('<div class="sharebar"><button type="button" class="sharebtn" onclick="pvShare()">&#8599; Share This</button>'
             '<button type="button" class="sharebtn alt" id="pvcopy" onclick="pvCopy()">Copy Link</button></div>\n'
             '<script>\n'
             'function pvShare(){if(navigator.share){navigator.share({title:document.title,url:location.href}).catch(function(){});}else{pvCopy();}}\n'
             'function pvCopy(){var u=location.href;var b=document.getElementById("pvcopy");var done=function(){if(b){var o="Copy Link";b.textContent="\\u2713 Link Copied";setTimeout(function(){b.textContent=o;},1800);}};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(u).then(done).catch(function(){pvCopyOld(u);done();});}else{pvCopyOld(u);done();}}\n'
             'function pvCopyOld(u){var ta=document.createElement("textarea");ta.value=u;ta.style.position="fixed";ta.style.opacity="0";document.body.appendChild(ta);ta.select();try{document.execCommand("copy");}catch(e){}document.body.removeChild(ta);}\n'
             '</script>\n')
    _out += big_flipper(_pslug, _bhtml)
    _out += '<div class="card" style="margin-top:22px"><div class="t">LIKE WHAT YOU SEE?</div><div class="s">' + _buynote + '</div></div>\n'
    _out += _pnav
    _out += ('<footer><a href="index.html">&larr; All our links</a> &middot; <a href="legal.html">Legal</a><br><br>Site run by <b style="color:#d4af37">Nova &#128176;</b> &mdash; Irish&#39;s AI partner.</footer>\n'
             '</div>' + FLIP_JS + '</body></html>')
    open('preview-%s.html' % _pslug, 'w').write(linkify(_out, 'preview-%s.html' % _pslug))
    _pv_count += 1
print('preview pages', _pv_count)

# ---------- POST-FIX: voter kit preview page gets the free-download note (it is a free lead magnet, not a store product) ----------
_vp = open('preview-voter-readiness-kit.html').read()
_vp_old = 'The full product is available in <a href="shop.html" style="color:#ffd95e">the Shop</a> and on our stores &mdash; buy direct (we keep 100%) or on Gumroad, Whop, and Payhip.'
_vp_new = 'This kit is FREE, no checkout and no cost: <a href="assets/downloads/voter-readiness-kit.zip" download style="color:#ffd95e;font-weight:700;text-decoration:underline">download the full kit now (ZIP, 9-page PDF inside)</a>. Share it with anyone who needs to get vote-ready.'
assert _vp_old in _vp
open('preview-voter-readiness-kit.html', 'w').write(_vp.replace(_vp_old, _vp_new, 1))
print('voter preview free-note applied')

# ---------- POST-FIX: Advent bundle gets its exact store product links (Whop + Gumroad, both live at $9; added 2026-11-06, QA FAIL 12 website leg) ----------
_ADV_WHOP = "https://whop.com/irish007/advent-devotional-bible-in-a-year-2027-tracker-bundle/"
_ADV_GUM = "https://irish007.gumroad.com/l/jiiooh"
_advp = open('preview-advent-devotional-2027-tracker.html').read()
_advp_old = 'The full product is available in <a href="shop.html" style="color:#ffd95e">the Shop</a> and on our stores &mdash; buy direct (we keep 100%) or on Gumroad, Whop, and Payhip.'
_advp_new = ('The full bundle is $9 in <a href="shop.html" style="color:#ffd95e">the Shop</a>, where buying direct means we keep 100%, and it is also live on '
 '<a href="' + _ADV_WHOP + '" style="color:#ffd95e;font-weight:700;text-decoration:underline">Whop</a> and on '
 '<a href="' + _ADV_GUM + '" style="color:#ffd95e;font-weight:700;text-decoration:underline">Gumroad</a> at the same $9.')
assert _advp_old in _advp
open('preview-advent-devotional-2027-tracker.html', 'w').write(_advp.replace(_advp_old, _advp_new, 1))
_sh9 = open('shop.html').read()
_adv_foot = 'Two printable PDFs, 28 pages each \u00b7 US Letter \u00b7 Buy once, use every year</div>'
assert _sh9.count(_adv_foot) == 1
_adv_links = ('<p style="margin-top:8px">Get it for $9 on '
 '<a href="' + _ADV_WHOP + '" style="color:#ffd95e;font-weight:700">Whop</a> or on '
 '<a href="' + _ADV_GUM + '" style="color:#ffd95e;font-weight:700">Gumroad</a>, or buy direct from us above and we keep 100%.</p></div>')
open('shop.html', 'w').write(_sh9.replace(_adv_foot, 'Two printable PDFs, 28 pages each \u00b7 US Letter \u00b7 Buy once, use every year' + _adv_links, 1))
print('advent store links applied')

# ---------- POST-FIX: memory sync kit preview page gets the done-for-you setup add-on section ----------
_kit = open('preview-ai-memory-sync-kit.html').read()
_kit_anchor = '<div class="card" style="margin-top:22px"><div class="t">LIKE WHAT YOU SEE?</div>'
assert _kit_anchor in _kit
_kit_prev_ctx = _PAGECTX
_PAGECTX = 'services'
_kit_panel = _panel("AI MEMORY SYNC SETUP, DONE FOR YOU", [("Standard Setup","$149"),("Plus Setup","$295")], "services.html")
_PAGECTX = _kit_prev_ctx
assert _kit_panel
_kit_sec = ('<div class="card" style="margin-top:22px"><div class="t">DONE-FOR-YOU SETUP: WE BUILD YOUR VAULT WITH YOU</div>'
 '<div class="s">The kit is written so you can set it up yourself, and some owners would rather be running it today. Book a setup and we build your vault with you on a short guided call: <b>Standard Setup, $149</b>, your primary AI connected and loaded, or <b>Plus Setup, $295</b>, with a second AI connected and synced plus a month of weekly check-ins. The same setup is also listed on our <a href="services.html" style="color:#ffd95e">Services</a> page.</div>'
 + _kit_panel + '</div>\n')
open('preview-ai-memory-sync-kit.html','w').write(_kit.replace(_kit_anchor, _kit_sec + _kit_anchor, 1))
print('kit preview setup add-on applied')

# ---------- POST-FIX: survival binder preview page names the Group License (IM22, added 2026-11-06; license lives in the Shop at $90 for up to 10 households) ----------
_sbp = open('preview-survival-72-hour-binder.html').read()
_sbp_old = 'The full product is available in <a href="shop.html" style="color:#ffd95e">the Shop</a> and on our stores &mdash; buy direct (we keep 100%) or on Gumroad, Whop, and Payhip.'
_sbp_new = ('The full binder is $12 in <a href="shop.html" style="color:#ffd95e">the Shop</a>, and buying direct means we keep 100%. It is also on Gumroad, Whop, and Payhip at the same $12. '
 'Bringing a group? The <a href="shop.html" style="color:#ffd95e;font-weight:700;text-decoration:underline">Group License</a> covers up to 10 households for $90 and adds the leader sheet for whoever runs the group.')
assert _sbp_old in _sbp
open('preview-survival-72-hour-binder.html', 'w').write(_sbp.replace(_sbp_old, _sbp_new, 1))
print('survival binder preview group license note applied')

# ---------- M22 SHOP SLICE (2026-11-13): survival binder + Advent preview images now served as files ----------
# The two post-fix blocks that embedded assets/previews/*.jpg as data URIs are DELETED:
# the 10 JPGs are pushed to GitHub (assets/previews/) and the flipper() file refs stay.
# A rebuild reproduces shop.html + both preview pages byte-identically with file refs.

# ---------- POST-FIX: cart (client-side cart + gifts + share on shop + books) ----------
_CART_SNIPPET = r'''
<style>
.in-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
.in-btn{background:#ffd95e;color:#0c130e;border:0;border-radius:8px;padding:8px 12px;font-weight:700;font-size:.85rem;cursor:pointer;font-family:inherit}
.in-btn.ghost{background:transparent;color:#ffd95e;border:1px solid #ffd95e}
.in-btn:active{transform:scale(.97)}
#in-cartbar{position:fixed;left:50%;transform:translateX(-50%);bottom:14px;z-index:9998;background:#ffd95e;color:#0c130e;font-weight:800;border-radius:999px;padding:11px 18px;box-shadow:0 6px 24px rgba(0,0,0,.55);cursor:pointer;display:none;font-size:.95rem;white-space:nowrap}
#in-overlay{position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:9999;display:none;overflow:auto}
#in-panel{background:#101a13;color:#e8f0e9;max-width:560px;margin:4vh auto;border:1px solid #2c4234;border-radius:14px;padding:20px 18px 24px;font-size:.95rem}
.in-phead{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.in-ptitle{font-family:Oswald,sans-serif;font-size:1.35rem;color:#ffd95e;letter-spacing:.04em}
.in-x{background:transparent;border:1px solid #2c4234;color:#e8f0e9;border-radius:8px;width:34px;height:34px;cursor:pointer;font-size:1rem}
.in-item{border:1px solid #2c4234;border-radius:10px;padding:10px 12px;margin-bottom:10px}
.in-irow{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.in-irow+.in-irow{margin-top:8px}
.in-ititle{font-weight:700}
.in-iprice{color:#ffd95e;font-weight:700}
.in-qty{display:flex;align-items:center;gap:8px}
.in-qty button{background:#1d2f23;color:#ffd95e;border:1px solid #2c4234;border-radius:6px;width:28px;height:28px;cursor:pointer;font-size:1rem;line-height:1}
.in-gifttoggle{cursor:pointer;color:#9fb3a1;font-size:.88rem}
.in-remove{background:transparent;border:0;color:#ff9d8a;cursor:pointer;font-size:.85rem}
.in-giftfields{margin-top:8px;display:flex;flex-direction:column;gap:6px}
.in-giftfields input{background:#0c130e;border:1px solid #2c4234;border-radius:6px;color:#e8f0e9;padding:7px 9px;font-size:.88rem}
.in-trow{display:flex;justify-content:space-between;margin-top:6px}
.in-trow.total{font-size:1.12rem;font-weight:800;color:#ffd95e;border-top:1px solid #2c4234;padding-top:8px;margin-top:10px}
.in-disc{color:#8fe3a8}
.in-coderow{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}
.in-coderow input{flex:1;min-width:140px;background:#0c130e;border:1px solid #2c4234;border-radius:6px;color:#e8f0e9;padding:8px 10px;text-transform:uppercase}
.in-codemsg{font-size:.85rem;margin-top:6px;color:#9fb3a1}
.in-note{font-size:.84rem;color:#9fb3a1;line-height:1.45}
#in-summary{background:#0c130e;border:1px solid #2c4234;border-radius:8px;padding:10px 12px;white-space:pre-wrap;word-break:break-word;font-size:.82rem;max-height:220px;overflow:auto}
.in-btnrow{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
#in-sharepop{position:fixed;z-index:10000;background:#101a13;border:1px solid #ffd95e;border-radius:10px;padding:8px;display:none;box-shadow:0 8px 28px rgba(0,0,0,.6)}
#in-sharepop a,#in-sharepop button{display:block;width:100%;text-align:left;background:transparent;border:0;color:#e8f0e9;padding:7px 10px;font-size:.9rem;cursor:pointer;text-decoration:none;box-sizing:border-box}
#in-sharepop a:hover,#in-sharepop button:hover{background:#1d2f23}
</style>
<script>
/* IN-CART-V1 */
(function(){
"use strict";
var LS='in_cart_v1', CODES={FIRST15:0.15, THANKS20:0.20}, MAXQ=99;
var CART='\uD83D\uDED2', GIFT='\uD83C\uDF81', MAIL='\uD83D\uDCE7', HOME='\uD83C\uDFE0', SHARE='\u2197', OK='\u2713', XX='\u2715';
function qs(s,r){return (r||document).querySelector(s);}
function qsa(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s));}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function money(n){return '$'+(Math.round(n*100)/100).toFixed(2);}
function load(){try{var c=JSON.parse(localStorage.getItem(LS));if(c&&typeof c==='object'&&c.items)return{items:c.items,code:c.code||null};}catch(e){}return{items:{},code:null};}
var cart=load();
function save(){try{localStorage.setItem(LS,JSON.stringify(cart));}catch(e){}}
function isBundle(t){return /bundle/i.test(t);}
function totals(){var sub=0,elig=0,n=0,k,it;for(k in cart.items){it=cart.items[k];sub+=it.price*it.qty;if(!isBundle(it.title))elig+=it.price*it.qty;n+=it.qty;}var rate=(cart.code&&CODES[cart.code])?CODES[cart.code]:0;var disc=Math.round(elig*rate*100)/100;return{sub:sub,disc:disc,total:sub-disc,n:n,rate:rate};}
function addItem(title,price){var it=cart.items[title];if(it){it.qty=Math.min(MAXQ,it.qty+1);}else{cart.items[title]={title:title,price:price,qty:1,gift:{on:false,email:'',from:'',note:''}};}save();renderBar();}
/* floating bar */
var bar=document.createElement('div');bar.id='in-cartbar';document.body.appendChild(bar);
bar.addEventListener('click',function(){openPanel();});
function renderBar(){var t=totals();if(t.n>0){bar.style.display='block';bar.textContent=CART+' Cart ('+t.n+') \u2014 '+money(t.total)+' \u2014 View Cart';}else{bar.style.display='none';}}
/* share popover */
var pop=document.createElement('div');pop.id='in-sharepop';document.body.appendChild(pop);
document.addEventListener('click',function(e){if(pop.style.display==='block'&&!pop.contains(e.target))pop.style.display='none';});
function shareFor(title,url,btn){
  if(navigator.share){navigator.share({title:title,url:url}).catch(function(){});return;}
  var u=encodeURIComponent(url), t=encodeURIComponent(title);
  pop.innerHTML='<button type="button" id="in-sh-copy">Copy Link</button>'
    +'<a target="_blank" rel="noopener" href="https://www.facebook.com/sharer/sharer.php?u='+u+'">Facebook</a>'
    +'<a target="_blank" rel="noopener" href="https://twitter.com/intent/tweet?url='+u+'&text='+t+'">X</a>'
    +'<a target="_blank" rel="noopener" href="https://wa.me/?text='+t+'%20'+u+'">WhatsApp</a>';
  var r=btn.getBoundingClientRect();
  pop.style.display='block';pop.style.left=Math.max(6,r.left)+'px';pop.style.top=(r.bottom+6)+'px';
  var cp=qs('#in-sh-copy',pop);
  cp.addEventListener('click',function(){copyText(url);cp.textContent='Copied '+OK;setTimeout(function(){pop.style.display='none';},700);});
}
function copyText(txt){
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).catch(function(){});return;}
  var ta=document.createElement('textarea');ta.value=txt;document.body.appendChild(ta);ta.select();try{document.execCommand('copy');}catch(e){}document.body.removeChild(ta);
}
/* panel */
var overlay=document.createElement('div');overlay.id='in-overlay';
overlay.innerHTML='<div id="in-panel">'
 +'<div class="in-phead"><span class="in-ptitle">YOUR CART</span><button type="button" class="in-x" id="in-close">'+XX+'</button></div>'
 +'<div id="in-items"></div>'
 +'<p class="in-note" id="in-empty">Your cart is empty \u2014 tap '+CART+' Add to Cart on anything you like, then come back here.</p>'
 +'<div id="in-checkout">'
 +'<div class="in-trow"><span>Subtotal</span><span id="in-sub"></span></div>'
 +'<div class="in-trow in-disc" id="in-discrow" style="display:none"><span id="in-disclabel"></span><span id="in-disc"></span></div>'
 +'<div class="in-trow total"><span>TOTAL</span><span id="in-total"></span></div>'
 +'<div class="in-coderow"><input id="in-code" type="text" placeholder="Discount code" autocomplete="off"><button type="button" class="in-btn" id="in-apply">Apply</button></div>'
 +'<div class="in-codemsg" id="in-codemsg"></div>'
 +'<p class="in-note">Codes don\'t apply to bundles \u2014 bundles are already priced down.</p>'
 +'<p class="in-note" style="margin-top:12px">Pay the TOTAL with any method below and put <b>ORDER + your email</b> in the payment note \u2014 we match it up and deliver. Then tap '+MAIL+' Send Order so we have your items in writing. Prefer a store checkout? Each product is also on <a href="https://irish007.gumroad.com" style="color:#ffd95e">Gumroad</a> / <a href="https://whop.com/irish007/products" style="color:#ffd95e">Whop</a> / <a href="https://payhip.com/irish007" style="color:#ffd95e">Payhip</a>, where codes redeem automatically. Selected products are also on <a href="https://ko-fi.com/irish45412" style="color:#ffd95e">Ko-fi</a>. Gifts are emailed to the recipient with your note, from us.</p>'
 +'<p class="in-note">Cash App <b>$Irish0007</b> \u00B7 Zelle <b>chris007hanna@gmail.com</b> \u00B7 Chime <b>$Irish007</b> \u00B7 PayPal <b>chris007hanna@gmail.com</b> <span id="in-qrwrap"></span></p>'
 +'<div class="in-btnrow"><a class="in-btn" id="in-send" style="text-decoration:none;display:inline-block" href="#">'+MAIL+' Send Order</a><button type="button" class="in-btn ghost" id="in-copy">Copy Order Summary</button><span class="in-codemsg" id="in-copymsg"></span></div>'
 +'<pre id="in-summary" style="margin-top:10px"></pre>'
 +'</div>'
 +'<div class="in-btnrow"><button type="button" class="in-btn" id="in-keep">Keep Shopping</button><button type="button" class="in-btn ghost" id="in-home">'+HOME+' Main Page</button></div>'
 +'</div>';
document.body.appendChild(overlay);
var itemsEl=qs('#in-items',overlay), emptyEl=qs('#in-empty',overlay), checkoutEl=qs('#in-checkout',overlay);
if(document.getElementById('direct')){qs('#in-qrwrap',overlay).innerHTML=' \u00B7 <a href="#direct" id="in-qr" style="color:#ffd95e">See the QR codes</a>';}
function openPanel(){renderPanel();overlay.style.display='block';}
function closePanel(){overlay.style.display='none';}
overlay.addEventListener('click',function(e){if(e.target===overlay)closePanel();});
qs('#in-close',overlay).addEventListener('click',closePanel);
qs('#in-keep',overlay).addEventListener('click',closePanel);
qs('#in-home',overlay).addEventListener('click',function(){window.location.href='index.html';});
var qrLink=qs('#in-qr',overlay);if(qrLink){qrLink.addEventListener('click',closePanel);}
function itemRow(it){
  var g=it.gift||{on:false,email:'',from:'',note:''};var k=esc(it.title);
  var h='<div class="in-item"><div class="in-irow"><div class="in-ititle">'+k+'</div><div class="in-iprice">'+money(it.price*it.qty)+'</div></div>'
   +'<div class="in-irow"><div class="in-qty"><button type="button" data-a="minus" data-k="'+k+'">\u2212</button><span>'+it.qty+'</span><button type="button" data-a="plus" data-k="'+k+'">+</button></div>'
   +'<label class="in-gifttoggle"><input type="checkbox" data-a="gift" data-k="'+k+'"'+(g.on?' checked':'')+'> '+GIFT+' This is a gift</label>'
   +'<button type="button" class="in-remove" data-a="remove" data-k="'+k+'">Remove</button></div>';
  if(g.on){h+='<div class="in-giftfields">'
   +'<input type="email" data-g="email" data-k="'+k+'" placeholder="Recipient email" value="'+esc(g.email||'')+'">'
   +'<input type="text" data-g="from" data-k="'+k+'" placeholder="From (your name, optional)" value="'+esc(g.from||'')+'">'
   +'<input type="text" data-g="note" data-k="'+k+'" placeholder="Gift note (optional)" value="'+esc(g.note||'')+'">'
   +'</div>';}
  return h+'</div>';
}
function summaryText(){
  var t=totals(),L=[],i=0,k,it;
  L.push('ORDER \u2014 Irish + Nova website');L.push('--------------------------------');
  for(k in cart.items){it=cart.items[k];i++;L.push(i+'. '+it.title+' \u00D7'+it.qty+' \u2014 '+money(it.price*it.qty));
    if(it.gift&&it.gift.on){L.push('   '+GIFT+' GIFT \u2192 '+(it.gift.email||'(no email given)')+(it.gift.from?' | From: '+it.gift.from:'')+(it.gift.note?' | Note: '+it.gift.note:''));}}
  L.push('Subtotal: '+money(t.sub));
  if(t.disc>0)L.push('Discount ('+cart.code+', bundles excluded): \u2212'+money(t.disc));
  L.push('TOTAL: '+money(t.total));L.push('Payment note: ORDER + your email');
  return L.join('\n');
}
function renderPanel(){
  var t=totals(),keys=Object.keys(cart.items);
  itemsEl.innerHTML=keys.map(function(k){return itemRow(cart.items[k]);}).join('');
  emptyEl.style.display=keys.length?'none':'block';
  checkoutEl.style.display=keys.length?'block':'none';
  qs('#in-sub',overlay).textContent=money(t.sub);
  var dr=qs('#in-discrow',overlay);
  if(t.disc>0){dr.style.display='flex';qs('#in-disclabel',overlay).textContent='Discount ('+cart.code+')';qs('#in-disc',overlay).textContent='\u2212'+money(t.disc);}
  else{dr.style.display='none';}
  qs('#in-total',overlay).textContent=money(t.total);
  var msg=qs('#in-codemsg',overlay);
  if(cart.code){msg.textContent=OK+' '+cart.code+' applied \u2014 '+(CODES[cart.code]*100)+'% off non-bundle items. Tap Apply with an empty box to clear.';}
  updateSummary();renderBar();
}
function updateSummary(){
  var s=summaryText();
  qs('#in-summary',overlay).textContent=s;
  qs('#in-send',overlay).href='mailto:chris007hanna@gmail.com?subject='+encodeURIComponent('Website Order')+'&body='+encodeURIComponent(s);
}
itemsEl.addEventListener('click',function(e){
  var el=e.target,a=el.getAttribute&&el.getAttribute('data-a');if(!a)return;
  var key=el.getAttribute('data-k'),it=cart.items[key];if(!it)return;
  if(a==='plus'){it.qty=Math.min(MAXQ,it.qty+1);}
  else if(a==='minus'){it.qty=Math.max(1,it.qty-1);}
  else if(a==='remove'){delete cart.items[key];}
  else{return;}
  save();renderPanel();
});
itemsEl.addEventListener('change',function(e){
  var el=e.target;if(el.getAttribute&&el.getAttribute('data-a')==='gift'){var it=cart.items[el.getAttribute('data-k')];if(it){it.gift=it.gift||{on:false,email:'',from:'',note:''};it.gift.on=el.checked;save();renderPanel();}}
});
itemsEl.addEventListener('input',function(e){
  var el=e.target,f=el.getAttribute&&el.getAttribute('data-g');if(!f)return;
  var it=cart.items[el.getAttribute('data-k')];if(!it)return;
  it.gift=it.gift||{on:false,email:'',from:'',note:''};it.gift[f]=el.value;save();updateSummary();
});
qs('#in-apply',overlay).addEventListener('click',function(){
  var v=qs('#in-code',overlay).value.replace(/\s+/g,'').toUpperCase(),msg=qs('#in-codemsg',overlay);
  if(!v){cart.code=null;save();renderPanel();msg.textContent='Code cleared.';return;}
  if(CODES[v]){cart.code=v;save();renderPanel();}
  else{msg.textContent='That code isn\'t active right now.';}
});
qs('#in-copy',overlay).addEventListener('click',function(){
  copyText(summaryText());qs('#in-copymsg',overlay).textContent='Copied '+OK;
});
/* card wiring */
function parseTp(txt){var m=/^\s*\$(\d+(?:\.\d{1,2})?)\s*$/.exec(txt||'');return m?parseFloat(m[1]):null;}
function mkAdd(title,price,label){
  var b=document.createElement('button');b.type='button';b.className='in-btn';b.textContent=label;
  b.addEventListener('click',function(){addItem(title,price);var old=b.textContent;b.textContent=OK+' Added!';setTimeout(function(){b.textContent=old;},900);});
  return b;
}
qsa('.book').forEach(function(card){
  var bt=card.querySelector('.bt');if(!bt)return;
  var title=bt.textContent.replace(/\s+/g,' ').trim();if(!title)return;
  var pv=card.querySelector('a.pvlink');var url=pv?pv.href:location.href.split('#')[0];
  var wrap=document.createElement('div');wrap.className='in-actions';
  var tp=card.querySelector('.tp');var price=tp?parseTp(tp.textContent):null;
  if(price!==null){wrap.appendChild(mkAdd(title,price,CART+' Add to Cart'));}
  else{qsa('a.buy',card).forEach(function(a){
    var t=a.textContent.replace(/\s+/g,' ').trim();var m=/\$(\d+(?:\.\d{1,2})?)\s*$/.exec(t);if(!m)return;
    var label=t.replace(/\$[\d.]+\s*$/,'').trim()||'Edition';
    wrap.appendChild(mkAdd(title+' ('+label+')',parseFloat(m[1]),CART+' Add '+label));
  });}
  var sh=document.createElement('button');sh.type='button';sh.className='in-btn ghost';sh.textContent=SHARE+' Share';
  sh.addEventListener('click',function(ev){ev.preventDefault();ev.stopPropagation();shareFor(title,url,sh);});
  wrap.appendChild(sh);
  var anchor=card.querySelector('a.lookbtn')||card.querySelector('details.pv');
  if(anchor){card.insertBefore(wrap,anchor);}else{card.appendChild(wrap);}
});
renderBar();
})();
</script>
'''
for _cf in ('shop.html', 'books.html') + tuple(BOOK_DETAIL_FILES):
    _ch = open(_cf).read()
    if 'IN-CART-V1' not in _ch:
        assert '</body>' in _ch, _cf
        _head, _tail = _ch.rsplit('</body>', 1)
        open(_cf, 'w').write(_head + _CART_SNIPPET + '</body>' + _tail)
        print(_cf + ' + cart', os.path.getsize(_cf))

# ============ SERVICES EXPANSION — CAR DEALERS / PROPERTY / RENTAL HOSTS / INSURANCE (2026-10-13) ============
def _guarantee_card():
    return card(FBP, "THE IRISH + NOVA GUARANTEE", "<b>More business than you can handle &mdash; or we work for free.</b><br><br>Your Google profile built and live within 14 days, or your setup fee comes back.<br><br>If your Google calls, direction requests, and bookings don&rsquo;t climb within 60 days, your monthly pauses &mdash; we work free until it moves.", True)
def _audit_card():
    return card(FBP, "FREE GOOGLE PRESENCE AUDIT", "We pull up your business on Google exactly the way a customer sees it and show you what&rsquo;s missing &mdash; the categories, the photos, the unanswered questions costing you calls. Free, no strings, and yours to keep either way.")
def _svc_msg_card(desc):
    return card(FBP, "MESSAGE US — WE BUILD IT", desc)

# ---- Car Dealers ----
_PAGECTX = 'cardealers'
cd_body = card(FBP, "EVERY LEAD ANSWERED IN 60 SECONDS — OR THE NEXT LOT GETS THE SALE", "A buyer who messages your lot at 9 P.M. buys from whoever answers first. We build the machine that answers first — every time, day or night — and keeps your sold customers coming back for service and their next car.", True)
cd_body += '<div class="sec">The stack</div>'
cd_body += _aala("SETUP — PROFILE, ASSISTANT &amp; FUNNEL LIVE", "Your Google Business Profile built properly for sales and service, the lead assistant connected, and the review funnel in place. One-time setup — we handle the whole build.", "$395")
cd_body += _apack("LEAD ASSISTANT", "An assistant on your profile and your website that answers inventory questions 24/7 — price, availability, trade-ins, financing basics — and books the test drive while your team sleeps.", [("Lead Assistant","$299/mo")])
cd_body += _apack("FULL LOT", "Everything in Lead Assistant, plus service-drive retention — oil-change and tire reminders that book the bay — sold-customer follow-up sequences that bring buyers back, and the review funnel run for you every day.", [("Full Lot","$695/mo")])
cd_body += '<div class="sec">Our word</div>' + _guarantee_card()
cd_body += '<div class="sec">Start here</div>'
cd_body += card("preview-ai-prompts-car-dealers.html", "&#128663; SEE THE PLAYBOOK — 52 AI PROMPTS FOR CAR DEALERS, $19", "The prompt pack we built for dealers: lead replies, listing copy, sold-customer care, service retention. Run it yourself — or let us run the whole machine for you.")
cd_body += _audit_card()
cd_body += _svc_msg_card("Tell us about your lot — sales, service, or both — and we&rsquo;ll map your setup. No pitch deck, no pressure: a straight answer on what we&rsquo;d build first.")
open('cardealers.html','w').write(page("Car Dealer Services — Irish + Nova", "Car dealer services by Irish + Nova: a 24/7 lead assistant that books test drives, Google profile, service retention, and a review funnel that fills lots.", "cardealers.html", "Car Dealers", "Sales &amp; service, answered around the clock.", cd_body))
print('cardealers.html', os.path.getsize('cardealers.html'))

# ---- Property Management ----
_PAGECTX = 'propertymanagement'
pm_body = card(FBP, "VACANCIES FILLED, TENANTS ANSWERED — WHILE YOU RUN THE BUILDINGS", "Tenants message at 2 A.M. Prospects drive by at noon. We build the front office that never closes: tenant questions answered, maintenance logged with photos, showings scheduled, and owners kept in the loop.", True)
pm_body += '<div class="sec">The stack</div>'
pm_body += _aala("SETUP — PROFILE, ASSISTANT &amp; FUNNEL LIVE", "Your Google Business Profile built properly, the tenant assistant connected, and the review funnel in place. One-time setup — we handle the whole build.", "$395")
pm_body += _apack("TENANT ASSISTANT", "Answers tenant FAQs and takes maintenance requests with photos, 24/7 — the 2 A.M. leak gets logged and routed, not lost. Vacancy showings scheduled automatically, with an application checklist that collects everything before you ever pick up the phone.", [("Tenant Assistant","$249/mo")])
pm_body += _apack("FULL PORTFOLIO", "Everything in Tenant Assistant for up to 50 doors, plus lease-renewal reminder sequences and a monthly one-page owner report produced for you — the summary your owners actually read.", [("Full Portfolio","$595/mo")])
pm_body += '<p class="note">More than 50 doors? Per-door pricing by consultation — tell us the count and we&rsquo;ll quote it straight.</p>'
pm_body += '<div class="sec">Our word</div>' + _guarantee_card()
pm_body += '<div class="sec">Start here</div>'
pm_body += _audit_card()
pm_body += _svc_msg_card("Tell us how many doors you run and what eats your week — we&rsquo;ll map the setup and quote it straight.")
open('propertymanagement.html','w').write(page("Property Management Services — Irish + Nova", "Property management services by Irish + Nova: a 24/7 tenant assistant, maintenance intake with photos, showings scheduled, renewals, and owner reports.", "propertymanagement.html", "Property Management", "The front office that never closes.", pm_body))
print('propertymanagement.html', os.path.getsize('propertymanagement.html'))

# ---- Airbnb / VRBO Hosts ----
_PAGECTX = 'rentalhosts'
rh_body = card(FBP, "FIVE-STAR GUEST CARE ON AUTOPILOT — AND BOOKINGS THE PLATFORMS DON&rsquo;T TAX", "Guests expect hotel-speed answers from a house. We build the system that delivers them — check-ins, recommendations, turnover coordination — plus your own booking page, so repeat guests skip the platform cut entirely.", True)
rh_body += '<div class="sec">The stack</div>'
rh_body += _aala("LISTING MAKEOVER", "Your listing rewritten to sell the stay: copy that answers guest questions before they&rsquo;re asked, your photos reordered so the best shots land first, and titles worked the way a marketer works them.", "$149")
rh_body += _apack("GUEST ASSISTANT", "The whole five-star routine, automated per property: booking confirmations, check-in instructions, house rules, local recommendations, a mid-stay check-in, the checkout nudge, and timed review requests that turn happy stays into five-star reviews — plus turnover coordination with cleaner checklists and an auto-message on every booking.", [("Per property","$99/mo")])
rh_body += _apack("DIRECT-BOOKING WEBSITE", "Your own booking page: guests book direct and you keep the 15%+ the platforms take from every stay. One flat monthly instead of a cut of every booking, forever.", [("Setup","$495"),("Monthly","$99/mo")])
rh_body += _apack("MULTI-PROPERTY HOSTS", "Several properties? We run the guest assistant, the review engine, and direct booking across the whole portfolio, scoped to your doors.", [("Multi-property","By consultation")])
rh_body += '<div class="sec">Our word</div>' + _guarantee_card()
rh_body += '<div class="sec">Start here</div>'
rh_body += _audit_card()
rh_body += _svc_msg_card("Tell us about your place — one cabin or a whole portfolio — and we&rsquo;ll map what we&rsquo;d build first.")
open('rentalhosts.html','w').write(page("Airbnb & VRBO Host Services — Irish + Nova", "Airbnb and VRBO host services by Irish + Nova: listing makeovers, a guest assistant running the five-star routine, and direct-booking sites with no OTA cut.", "rentalhosts.html", "Airbnb &amp; VRBO Hosts", "Five-star care, run for you.", rh_body))
print('rentalhosts.html', os.path.getsize('rentalhosts.html'))

# ---- Insurance Agents ----
_PAGECTX = 'insurance'
ins_body = card(FBP, "THE MONEY IS IN RENEWALS — WE RUN THE FOLLOW-UP", "Agencies don&rsquo;t lose clients on price. They lose them on silence. We build the system that answers every lead fast, walks every client to renewal, and asks for the referral at exactly the right moment.", True)
ins_body += '<div class="sec">The stack</div>'
ins_body += _aala("SETUP — PROFILE, ASSISTANT &amp; FUNNEL LIVE", "Your Google Business Profile built properly, the quote-intake assistant connected, and the review funnel in place. One-time setup — we handle the whole build.", "$295")
ins_body += _apack("ASSISTANT + RENEWALS", "A quote-intake assistant that captures the basics and books the conversation, plus renewal-reminder sequences that reach every client before a policy lapses. The follow-up that keeps a book renewing.", [("Assistant + Renewals","$199/mo")])
ins_body += _apack("FULL AGENCY", "Everything in Assistant + Renewals, plus seasonal campaigns run for you — Medicare AEP, ACA open enrollment, storm season — and a referral engine: insurance is a referral business, and we make asking automatic.", [("Full Agency","$495/mo")])
ins_body += '<div class="sec">Our word</div>' + _guarantee_card()
ins_body += '<div class="sec">Start here</div>'
ins_body += card("preview-ai-prompts-insurance-agents.html", "&#128737;&#65039; SEE THE PLAYBOOK — 52 AI PROMPTS FOR INSURANCE AGENTS, $19", "The prompt pack we built for agents: lead outreach, quote explainers, renewal reviews, referrals. Run it yourself — or let us run the whole machine for you.")
ins_body += _audit_card()
ins_body += _svc_msg_card("Tell us about your book — lines you write, size of the agency — and we&rsquo;ll map your setup. Straight answers, no pressure.")
open('insurance.html','w').write(page("Insurance Agent Services — Irish + Nova", "Insurance agent services by Irish + Nova: a quote-intake assistant, renewal reminder sequences, seasonal campaigns, and a referral engine for your book.", "insurance.html", "Insurance Agents", "Renewals run. Referrals asked. Nothing slips.", ins_body))
print('insurance.html', os.path.getsize('insurance.html'))

# ---- services.html sections for the four new verticals ----
_sv6 = open('services.html').read()
if 'FOR CAR DEALERS' not in _sv6:
    _x_sec = '<div class="sec">For car dealers</div>'
    _PAGECTX = 'cardealers'
    _x_sec += _gigcard("&#128663; CAR DEALERS — LEADS ANSWERED IN 60 SECONDS", "Google profile, a 24/7 lead assistant that books test drives, service-drive retention, and a review funnel. The lot that answers first wins the sale.", [("Setup","$395"),("Lead Assistant","$299/mo"),("Full Lot","$695/mo")], "cardealers.html", "See the dealer packages")
    _x_sec += '<div class="sec">For property managers</div>'
    _PAGECTX = 'propertymanagement'
    _x_sec += _gigcard("&#127970; PROPERTY MANAGEMENT — THE FRONT OFFICE THAT NEVER CLOSES", "A tenant assistant on duty 24/7, maintenance logged with photos, showings scheduled, renewals chased, and a monthly owner report produced for you.", [("Setup","$395"),("Tenant Assistant","$249/mo"),("Full Portfolio","$595/mo")], "propertymanagement.html", "See the property packages")
    _x_sec += '<div class="sec">For Airbnb &amp; VRBO hosts</div>'
    _PAGECTX = 'rentalhosts'
    _x_sec += _gigcard("&#127968; RENTAL HOSTS — FIVE-STAR CARE, BOOKINGS THE PLATFORMS DON&rsquo;T TAX", "Listing makeovers, a guest assistant that runs the whole stay, and your own direct-booking page — keep the 15%+ the platforms take from every stay.", [("Listing Makeover","$149"),("Guest Assistant","$99/mo"),("Direct-Booking Site","$495 + $99/mo")], "rentalhosts.html", "See the host packages")
    _x_sec += '<div class="sec">For insurance agents</div>'
    _PAGECTX = 'insurance'
    _x_sec += _gigcard("&#128737;&#65039; INSURANCE — THE MONEY IS IN RENEWALS", "Quote-intake assistant, renewal-reminder sequences, seasonal campaigns, and a referral engine. We run the follow-up so no client quietly lapses.", [("Setup","$295"),("Assistant + Renewals","$199/mo"),("Full Agency","$495/mo")], "insurance.html", "See the insurance packages")
    _sv6 = _sv6[:_sv6.rfind('<p class="note">')] + _x_sec + _sv6[_sv6.rfind('<p class="note">'):]
    open('services.html','w').write(_sv6)

# ---- index.html cards for the four new verticals ----
_ix6 = open('index.html').read()
if 'FOR CAR DEALERS' not in _ix6:
    _a6 = '<a class="card" href="localbusiness.html"'
    _p6 = _ix6.find(_a6)
    _e6 = _ix6.find('</a>', _p6) + 4
    _x6 = card("cardealers.html", "&#128663; FOR CAR DEALERS", "Sales &amp; service: leads answered in 60 seconds around the clock, test drives booked, service bays filled, reviews collected.")
    _x6 += card("propertymanagement.html", "&#127970; FOR PROPERTY MANAGERS", "Tenant questions answered and maintenance logged 24/7, showings scheduled, renewals chased, owners reported to monthly.")
    _x6 += card("rentalhosts.html", "FOR AIRBNB &amp; VRBO HOSTS", "Five-star guest care on autopilot — plus your own booking page, so repeat guests skip the platform cut.")
    _x6 += card("insurance.html", "FOR INSURANCE AGENTS", "Quote intake and renewal follow-up run for you — the money is in renewals, and we never let one slip.")
    _ix6 = _ix6[:_e6] + _x6 + _ix6[_e6:]
    open('index.html','w').write(_ix6)


# ============ SERVICES EXPANSION ROUND 2 — HOTELS / TAXI & LIMO / RESTAURANTS (2026-10-13) ============
# ---- Hotels & Motels ----
_PAGECTX = 'hotels'
ht_body = card(FBP, "&#127976; DIRECT BOOKINGS THE PLATFORMS DON&rsquo;T TAX — GUESTS CARED FOR LIKE CLOCKWORK", "Every OTA booking hands 15&ndash;25% of the room to a platform. We build the two machines that fix your economics: a guest assistant that answers like your best front-desk hire, around the clock — and your own booking page, so guests book direct and you keep the whole rate.", True)
ht_body += '<div class="sec">The stack</div>'
ht_body += _aala("&#128273; SETUP — PROFILE, ASSISTANT &amp; REVIEW ENGINE LIVE", "Your Google profile built properly — the listing travelers actually find — the guest messaging assistant connected, and the review engine in place: timed requests that turn happy stays into the five-star reviews that rank you. One-time setup; we handle the whole build.", "$395")
ht_body += _apack("&#128172; GUEST MESSAGING ASSISTANT", "The front desk that never sleeps, per property: pre-arrival messages with check-in details and parking, amenity and Wi-Fi answers, late-checkout offers, local tips your guests actually use, and a warm mid-stay check-in — every message in your voice, answered in seconds, at 2 P.M. or 2 A.M.", [("Per property","$149/mo")])
ht_body += _apack("&#127760; DIRECT-BOOKING WEBSITE", "Your own booking page: live rates, real availability, payment through your own accounts. Skip the 15&ndash;25% OTA commission on every direct stay — one flat monthly instead of a cut of every room, forever.", [("Setup","$495"),("Monthly","$99/mo")])
ht_body += _apack("&#127976; FULL PROPERTY", "The whole front office run for you: Google profile, guest messaging assistant, direct-booking website, and the review engine worked daily — plus seasonal and event content that fills the slow weeks before your competitors notice them.", [("Full Property","$595/mo")])
ht_body += '<div class="sec">Our word</div>' + _guarantee_card()
ht_body += '<div class="sec">Start here</div>'
ht_body += _audit_card()
ht_body += _svc_msg_card("Tell us about your property — rooms, market, which platforms you&rsquo;re on — and we&rsquo;ll map what we&rsquo;d build first. Straight answers, no pressure.")
open('hotels.html','w').write(page("Hotel &amp; Motel Services — Irish + Nova", "Hotel and motel services by Irish + Nova: a guest messaging assistant, review engine, Google profile, and a direct-booking website that skips OTA fees.", "hotels.html", "Hotels &amp; Motels", "Full rooms. Direct bookings. <b>Five-star reviews.</b>", ht_body))
print('hotels.html', os.path.getsize('hotels.html'))

# ---- Taxi & Limo Services ----
_PAGECTX = 'taxi'
tx_body = card(FBP, "&#128663; THE PHONE THAT NEVER SLEEPS BOOKS THE RIDES", "A rider who can&rsquo;t get an answer books the next company — or an app. We build the booking machine that answers first: rides booked on your website and by text, quotes given in seconds, and corporate accounts courted like they matter — because they do.", True)
tx_body += '<div class="sec">The stack</div>'
tx_body += _aala("&#128273; SETUP — PROFILE, BOOKING ASSISTANT &amp; REVIEW FUNNEL LIVE", "Your Google profile built properly for &ldquo;taxi near me&rdquo; and airport searches, the booking assistant connected to your site, and the review funnel in place. One-time setup; we handle the whole build.", "$295")
tx_body += _apack("&#128172; BOOKING ASSISTANT", "A booking and dispatch intake assistant on web and text: it takes the ride details, gives an instant quote for airport runs and events, confirms the booking, and sends the reminders that kill no-shows — 24/7, including the 4 A.M. airport run nobody wants to answer for.", [("Booking Assistant","$199/mo")])
tx_body += _apack("&#128188; FULL FLEET", "Everything in Booking Assistant, plus the account business built for you: corporate-account content and outreach that lands the hotels, offices, and event venues — and the review funnel run daily, so your rating climbs while the fleet rolls.", [("Full Fleet","$495/mo")])
tx_body += '<div class="sec">Our word</div>' + _guarantee_card()
tx_body += '<div class="sec">Start here</div>'
tx_body += _audit_card()
tx_body += _svc_msg_card("Tell us about your fleet — cars, coverage, airport work or events — and we&rsquo;ll map your setup. No pitch deck, no pressure: a straight answer on what we&rsquo;d build first.")
open('taxi.html','w').write(page("Taxi &amp; Limo Services — Irish + Nova", "Taxi and limo services by Irish + Nova: a booking and dispatch assistant on web and text, instant quotes for airport runs and events, and a review funnel.", "taxi.html", "Taxi &amp; Limo Services", "Booked around the clock. <b>Quoted in seconds.</b>", tx_body))
print('taxi.html', os.path.getsize('taxi.html'))

# ---- Restaurants & Hospitality ----
_PAGECTX = 'restaurants'
rs_body = card(FBP, "&#127869;&#65039; FULL TABLES — WITHOUT PAYING FOR EVERY SEAT TWICE", "The big reservation platforms charge you for every cover they seat — your regulars included. Ours is one flat monthly: reservations and the waitlist handled on your own page and profile, catering and private events captured instead of missed, and reviews collected like clockwork.", True)
rs_body += '<div class="sec">The stack</div>'
rs_body += _aala("&#128273; SETUP — PROFILE, ASSISTANT &amp; REVIEW FUNNEL LIVE", "Your Google profile built properly — hours, menus, photos, the listing hungry people actually find — the reservations assistant connected, and the review funnel in place. One-time setup; we handle the whole build.", "$295")
rs_body += _apack("&#128197; RESERVATIONS ASSISTANT", "Reservations and the waitlist, handled for you: bookings taken on your website and your Google profile, confirmations and day-of reminders that cut no-shows, and the waitlist worked in real time. One flat monthly — never a per-cover fee, never a charge for your own regulars.", [("Reservations Assistant","$149/mo")])
rs_body += _apack("&#127881; FULL HOUSE", "Everything in Reservations Assistant, plus the high-ticket inquiries captured: catering intake and private-events intake that answer in seconds and book the consult, menu and seasonal content posted for you, and the review funnel run daily.", [("Full House","$495/mo")])
rs_body += '<div class="sec">Our word</div>' + _guarantee_card()
rs_body += '<div class="sec">Start here</div>'
rs_body += _audit_card()
rs_body += _svc_msg_card("Tell us about your room — seats, service style, catering or events — and we&rsquo;ll map what we&rsquo;d build first. Straight answers, no pressure.")
open('restaurants.html','w').write(page("Restaurant Services — Irish + Nova", "Restaurant services by Irish + Nova: a reservations and waitlist assistant for one flat monthly, no per-cover fees — plus catering intake and review funnel.", "restaurants.html", "Restaurants &amp; Hospitality", "Full tables. <b>Flat monthly — no per-cover fees.</b>", rs_body))
print('restaurants.html', os.path.getsize('restaurants.html'))

# ---- services.html sections for the three new verticals ----
_sv7 = open('services.html').read()
if 'FOR HOTELS &amp; MOTELS' not in _sv7:
    _y_sec = '<div class="sec">For hotels &amp; motels</div>'
    _PAGECTX = 'hotels'
    _y_sec += _gigcard("&#127976; HOTELS &amp; MOTELS — DIRECT BOOKINGS, FIVE-STAR CARE", "A guest messaging assistant that answers in seconds around the clock, a review engine that fills your profile with five stars, and your own direct-booking website — skip the 15&ndash;25% OTA commission, one flat monthly instead.", [("Setup","$395"),("Guest Assistant","$149/mo"),("Full Property","$595/mo")], "hotels.html", "See the hotel packages")
    _y_sec += '<div class="sec">For taxi &amp; limo services</div>'
    _PAGECTX = 'taxi'
    _y_sec += _gigcard("&#128663; TAXI &amp; LIMO — THE PHONE THAT NEVER SLEEPS", "A booking and dispatch assistant on web and text that quotes airport runs and events in seconds, corporate-account content, and a review funnel that climbs while the fleet rolls.", [("Setup","$295"),("Booking Assistant","$199/mo"),("Full Fleet","$495/mo")], "taxi.html", "See the taxi &amp; limo packages")
    _y_sec += '<div class="sec">For restaurants &amp; hospitality</div>'
    _PAGECTX = 'restaurants'
    _y_sec += _gigcard("&#127869;&#65039; RESTAURANTS — RESERVATIONS WITHOUT PER-COVER FEES", "Reservations and the waitlist handled on your own page for one flat monthly — never a per-cover charge — plus catering and private-events intake and a review funnel.", [("Setup","$295"),("Reservations Assistant","$149/mo"),("Full House","$495/mo")], "restaurants.html", "See the restaurant packages")
    _note_at7 = _sv7.rfind('<p class="note">')
    assert _note_at7 > 0
    open('services.html','w').write(_sv7[:_note_at7] + _y_sec + _sv7[_note_at7:])
    print('services.html + hotels/taxi/restaurants sections', os.path.getsize('services.html'))

# ---- index.html cards for the three new verticals ----
_ix7 = open('index.html').read()
if 'FOR HOTELS &amp; MOTELS' not in _ix7:
    _a7 = '<a class="card" href="insurance.html"'
    _p7 = _ix7.find(_a7)
    assert _p7 > 0
    _e7 = _ix7.find('</a>', _p7) + 4
    _x7 = card("hotels.html", "&#127976; FOR HOTELS &amp; MOTELS", "Guest messaging on autopilot, five-star reviews on schedule, and direct bookings that skip the 15&ndash;25% platform cut.")
    _x7 += card("taxi.html", "&#128663; FOR TAXI &amp; LIMO SERVICES", "Bookings taken on web and text around the clock, instant airport and event quotes, corporate accounts courted.")
    _x7 += card("restaurants.html", "&#127869;&#65039; FOR RESTAURANTS", "Reservations and the waitlist handled for one flat monthly — never a per-cover fee — plus catering and private events.")
    _ix7 = _ix7[:_e7] + _x7 + _ix7[_e7:]
    open('index.html','w').write(_ix7)
    print('index.html + hotels/taxi/restaurants cards', os.path.getsize('index.html'))


# ============ LEGAL & DISCLOSURES PAGE (2026-10-13) ============
def _legal_sec(t, s, hero=False):
    return '<div class="card%s"><div class="t">%s</div><div class="s">%s</div></div>\n' % (" hero" if hero else "", clean_title(t), s)

lg_body = _legal_sec("HOW WE OPERATE &mdash; IN WRITING", "No fine-print games. This page says plainly how we make money, what we promise, what we don&rsquo;t, and how we handle your information. Questions about anything on this page: <b>chris007hanna@gmail.com</b>.", True)
lg_body += '<div class="sec">Making money, disclosed</div>'
lg_body += _legal_sec("AFFILIATE DISCLOSURE", "We earn commissions, and we&rsquo;d rather tell you than hide it. Some links on this site and in our content are affiliate links: when you buy through them, we earn a commission at no extra cost to you. That includes Amazon &mdash; as an Amazon Associate, we earn from qualifying purchases, and our Amazon links carry our Associates tag (hannaenterpri-20). We also run affiliate programs on our own stores that pay partners 30% when their referrals buy &mdash; and when we promote one of our own store links, we may be the house on both sides of that deal. Referral arrangements too: we pay a $50 bonus when someone sends us a business that signs up and pays its first invoice. If a link can earn us money, assume it does.")
lg_body += _legal_sec("EARNINGS DISCLAIMER", "Nothing on this site &mdash; no product, service, book, post, or testimonial &mdash; is a promise or guarantee of income, sales, rankings, or results. What a tool or service does for one business says nothing certain about yours; results vary with your market, your effort, and your timing. Standings, placements, and numbers we publish (competition rankings, catalog counts, store counts) are factual as of the day they are posted and change over time. Anyone who promises you guaranteed income is selling you something. It isn&rsquo;t us.")
lg_body += '<div class="sec">How things are made</div>'
lg_body += _legal_sec("AI DISCLOSURE", "We work with AI, openly. Our books, digital products, media, and this site&rsquo;s content are created with AI assistance &mdash; drafted, designed, and produced with AI tools under our direction, and reviewed before they ship. Our clients and our talent roster always know who they are working with: Irish + Nova, a human and his AI partner. We never use AI to fake reviews, testimonials, or results.")
lg_body += '<div class="sec">Buying from us</div>'
lg_body += _legal_sec("DIGITAL PRODUCT TERMS", "Digital products are delivered by download on our store platforms, and &mdash; when you buy direct from this site &mdash; by email once your payment is confirmed. Buying direct works like this: you pay through Cash App, Zelle, Chime, or PayPal and email us your order; we send your files. Your purchase is a license for your personal use only: you may not resell, share, redistribute, or give away the files or access. <b>Refunds:</b> if a file arrives broken or never arrives and we can&rsquo;t fix it, we refund you in full. Otherwise, digital sales are final &mdash; so read the description and flip through the free Look Inside preview before you buy.")
lg_body += _legal_sec("TEMPLATES DISCLAIMER", "Any contract, form, or document templates we sell are general templates provided for convenience. They are <b>not legal advice</b>, they are not a substitute for an attorney, and using one does not create an attorney&ndash;client relationship with anyone. Laws differ by state and by situation &mdash; have your own attorney review any template before you rely on it.")
lg_body += '<div class="sec">Working with us</div>'
lg_body += _legal_sec("SERVICES TERMS &amp; THE GUARANTEE", "<b>The Irish + Nova Guarantee: More business than you can handle &mdash; or we work for free.</b> Your Google profile built and live within 14 days, or your setup fee comes back. If your Google calls, direction requests, and bookings don&rsquo;t climb within 60 days, your monthly billing pauses &mdash; we work free until it moves. The Guarantee applies to our local-business growth services as published on the service pages.<br><br><b>Scope limits, in plain terms:</b> our booking and FAQ assistants book appointments and answer common questions only &mdash; they never collect or handle medical details. Legal-practice intake captures contact details and case basics only; it never provides legal advice, and nothing an assistant says creates an attorney&ndash;client relationship. Our working hours are Mon&ndash;Sat 9 AM&ndash;7 PM CT unless your plan says otherwise; the assistants keep answering around the clock.")
lg_body += '<div class="sec">Wellness products</div>'
lg_body += _legal_sec("WELLNESS DISCLAIMER &mdash; IBUDDY &amp; ISHRINKU", "iBuddy and iShrinkU are journaling and self-reflection products. They are <b>not therapy</b>, not counseling, and not medical care, and they are not a substitute for professional help. If you are in crisis or thinking about harming yourself, call or text <b>988</b> &mdash; the US Suicide &amp; Crisis Lifeline, free, confidential, 24/7. Please reach out. The journal can wait.")
lg_body += '<div class="sec">Your information</div>'
lg_body += _legal_sec("PRIVACY", "When you buy direct from this site or send us a form (consignment intake, model portfolio, or a message), we receive your email address and the order or form details you give us. We use them for one thing: delivering what you bought and providing the service you asked about. We never sell your personal data, and we don&rsquo;t hand it to marketers. The contests and votes we support run on those platforms&rsquo; own sites (Maxim, Miss USA, and others), under their rules and their privacy policies. If you want your information deleted, email <b>chris007hanna@gmail.com</b> and we delete it.")
lg_body += _legal_sec("COPYRIGHT", "&copy; Irish + Nova / Hanna Press. Our site content, books, products, artwork, and media are ours or used with permission. Link to us freely; please don&rsquo;t republish, resell, or redistribute our content or files. For permissions, or to report infringement, email <b>chris007hanna@gmail.com</b>.")
lg_body += '<p class="note">Plain-language summary of how we operate; not a substitute for professional legal advice.</p>'
open('legal.html','w').write(page("Legal &amp; Disclosures — Irish + Nova", "Legal and disclosures from Irish + Nova: affiliate and earnings disclaimers, AI disclosure, digital product and service terms, privacy, and copyright.", "legal.html", "Legal &amp; Disclosures", "Straight talk. <b>In writing.</b>", lg_body))
print('legal.html', os.path.getsize('legal.html'))

print('PANELS MISSING:', len(_MISSING), _MISSING)

# ---- singers.html roster card: Mello Streams (2026-10-18) ----
_sg = open('singers.html').read()
if 'mello-streams.html' not in _sg:
    _mello_sec = '<div class="sec">On our roster</div>'
    _mello_sec += card("mello-streams.html", "&#127908; MELLO STREAMS", "Southern California singer, composer, and producer with 20+ original singles on Spotify, Apple Music, and YouTube, and our whole team on her promotion. Hear her on her showcase page.")
    _at = _sg.find('<div class="sec">Singers')
    assert _at > 0
    _sg = _sg[:_at] + _mello_sec + _sg[_at:]
    open('singers.html','w').write(_sg)
    print('singers.html + Mello Streams roster card', os.path.getsize('singers.html'))

# ============ SLEEP SCENES FOR BUSINESS (2026-10-19) ============
# Commercial ambient video licenses: original tranquil scenes produced fresh
# for business spaces, priced per screen. NOT the sleep channel catalog.
DETAILS.update({
('*','SPA-AND-SALON-CALM'): _D(
 ["A set of tranquil scenes produced fresh for spa and salon spaces",
  "Jungle rain and rainforest green, filmed slow and calm",
  "Waterfall and gentle stream scenes in bright to soft daylight",
  "An original tranquil score composed for this package: soft piano, strings, and nature sound woven low",
  "Looping video files that play all day without attention",
  "A private playlist link as a second way to play the set",
  "Seasonal refreshes while your subscription is active"],
 "Day spas, bathhouses, massage practices, salons, and nail studios with a screen in treatment or waiting areas that should feel calm, pleasant, and properly licensed.",
 ["Screens, TVs, projectors, or any playback hardware: this is a content license only, and your business uses its own screens",
  "Playing the scenes anywhere outside the licensed business, or posting them to public channels such as YouTube or social media",
  "Other locations: each business location, and each screen, is licensed separately"],
 how=["Message us with your business, your rooms, and how many screens you want covered.",
  "We confirm your package, your screen count, and your price in writing before anything starts.",
  "We produce your scenes fresh for business spaces and deliver them as looping video files plus a private playlist link.",
  "Press play on your own screens. Your subscription keeps the license active and the seasonal refreshes coming."],
 timeline="Your first scene set is produced fresh when your subscription starts, and new subscribers are scheduled in the order subscriptions come in. Once produced, the set is delivered and plays the same day. From there the set is refreshed seasonally while your subscription stays active, and billing runs month to month per screen. Cancel anytime.",
 price="Package price: $29/mo per screen"),
('*','WAITING-ROOM-AND-OFFICE'): _D(
 ["A set of gentle scenes produced fresh for waiting rooms and offices",
  "Seasonal scenes in bright to soft daylight: spring green, summer water, autumn fields, winter firelight",
  "Calm original music at a friendly level, composed for daytime rooms",
  "Nothing dark, spooky, or startling, ever",
  "Looping video files that play all day without attention",
  "A private playlist link as a second way to play the set",
  "Seasonal refreshes while your subscription is active"],
 "Dental and medical waiting rooms, orthodontics, clinics, auto service lounges, barbershops, and offices where people sit with time to pass and the room should feel easy.",
 ["Screens, TVs, projectors, or any playback hardware: this is a content license only, and your business uses its own screens",
  "Playing the scenes anywhere outside the licensed business, or posting them to public channels such as YouTube or social media",
  "Other locations: each business location, and each screen, is licensed separately"],
 how=["Message us with your business, your rooms, and how many screens you want covered.",
  "We confirm your package, your screen count, and your price in writing before anything starts.",
  "We produce your scenes fresh for business spaces and deliver them as looping video files plus a private playlist link.",
  "Press play on your own screens. Your subscription keeps the license active and the seasonal refreshes coming."],
 timeline="Your first scene set is produced fresh when your subscription starts, and new subscribers are scheduled in the order subscriptions come in. Once produced, the set is delivered and plays the same day. From there the set is refreshed seasonally while your subscription stays active, and billing runs month to month per screen. Cancel anytime.",
 price="Package price: $29/mo per screen"),
('*','HOTEL-AND-LOBBY-NIGHTS'): _D(
 ["A set of cinematic night scenes produced fresh for hotel and lodge spaces",
  "Firelight and fireplace pieces made for evening lobbies",
  "Veranda and porch style scenes with quiet evening air",
  "Water at night: slow harbor and lakeside pieces with an original score kept soft and low",
  "Looping video files that play all evening and all night",
  "A private playlist link as a second way to play the set",
  "Seasonal refreshes while your subscription is active"],
 "Hotels, lodges, inns, and resorts with a lobby, lounge, or bar screen that runs into the evening and deserves better than a news channel.",
 ["Screens, TVs, projectors, or any playback hardware: this is a content license only, and your business uses its own screens",
  "Playing the scenes anywhere outside the licensed business, or posting them to public channels such as YouTube or social media",
  "Other locations: each business location, and each screen, is licensed separately"],
 how=["Message us with your property, your lobby and lounge spaces, and how many screens you want covered.",
  "We confirm your package, your screen count, and your price in writing before anything starts.",
  "We produce your scenes fresh for business spaces and deliver them as looping video files plus a private playlist link.",
  "Press play on your own screens. Your subscription keeps the license active and the seasonal refreshes coming."],
 timeline="Your first scene set is produced fresh when your subscription starts, and new subscribers are scheduled in the order subscriptions come in. Once produced, the set is delivered and plays the same day. From there the set is refreshed seasonally while your subscription stays active, and billing runs month to month per screen. Cancel anytime.",
 price="Package price: $29/mo per screen"),
('*','SLEEP-SCENES-FOR-BUSINESS'): _D(
 ["Three packages: Spa and Salon Calm, Waiting Room and Office, and Hotel and Lobby Nights",
  "Original tranquil scenes produced fresh for business spaces, each with its own original score",
  "A commercial license to play the scenes on the screens inside your business",
  "Looping video files plus a private playlist link for every package",
  "Full breakdowns on the Sleep Scenes for Business page"],
 "Spas, salons, waiting rooms, clinics, service lounges, hotels, and lodges that run ambient video and want it licensed and made for the room.",
 ["Nothing is ordered from this card: the Sleep Scenes for Business page carries the full breakdowns"],
 how=["Open the Sleep Scenes for Business page for the full breakdown of each package.",
  "Message us with your business and your screen count.",
  "We confirm your package and your price in writing before anything starts."]),
})

_PAGECTX = 'sleepbiz'
def _bizpack(title, desc, tiers):
    th = "".join('<div class="tier"><div class="tn">%s</div><div class="tp">%s</div></div>' % (n, p) for n, p in tiers)
    return _pkg(FBP, title, desc, th, tiers, "Message us to sign up")

ssfb_body = card(FBP, "YOUR SCREENS, LICENSED AND TRANQUIL", "Spas, salons, waiting rooms, and hotel lobbies run ambient video all day, and pressing play on a streaming video inside a business is not a commercial license. We do it properly: original tranquil scenes produced fresh for business spaces, with original music, licensed to play on the screens inside your business for one flat monthly per screen.", True)
ssfb_body += '<div class="sec">The packages</div>'
ssfb_body += _bizpack("&#127754; SPA AND SALON CALM", "Rain, water, and soft green places, produced fresh for treatment rooms, soaking spaces, and salon chairs: jungle rain, waterfalls, and gentle streams under a tranquil original score.", [("Per Screen","$29/mo")])
ssfb_body += _bizpack("&#128203; WAITING ROOM AND OFFICE", "Gentle seasonal scenes in bright to soft daylight, produced fresh for waiting rooms, clinics, service lounges, and offices: calm, friendly, and easy to have on all day.", [("Per Screen","$29/mo")])
ssfb_body += _bizpack("&#127769; HOTEL AND LOBBY NIGHTS", "Cinematic night scenes produced fresh for lobbies and lounges: firelight, verandas, and quiet evening water with an original score kept soft and low, made to sit beautifully behind conversation.", [("Per Screen","$29/mo")])
ssfb_body += '<div class="sec">The license, in plain terms</div>'
ssfb_body += _legal_sec("WHAT THE LICENSE COVERS", "Playing our scenes on screens inside the licensed business, for your guests, clients, patients, and staff. One subscription covers one screen. Add a screen, add a subscription.")
ssfb_body += _legal_sec("HOW IT PLAYS", "Every package arrives as looping video files for your screens plus a private playlist link, so the scenes can run all day without your team tending them.")
ssfb_body += _legal_sec("YOUR SCREENS, YOUR HARDWARE", "This is a content license. The subscription covers the scenes and the right to play them; your business provides its own screens and players. No hardware is included or sold.")
ssfb_body += _legal_sec("FRESH SCENES OVER TIME", "The scene sets are refreshed seasonally while your subscription is active, so the room does not sit on the same loop all year.")
ssfb_body += _legal_sec("CANCEL ANYTIME", "Month to month, per screen. Tell us to stop and the subscription ends at the close of the paid month. No long contract, no cancellation fee.")
ssfb_body += '<div class="sec">Start here</div>'
ssfb_body += _svc_msg_card("Tell us about your space: what kind of business, how many screens, and the feel you want on them. We will match the package, confirm it in writing, and produce your first scene set.")
ssfb_body += card("services.html", "ALL OUR SERVICES", "Everything else we do for businesses: websites built and managed, Google profiles, booking assistants, and more.")
ssfb_body += card("sleep.html", "OUR SLEEP CHANNEL", "The What We Do In Darkness channel, where our scene craft lives at night. The business scenes on this page are produced separately, fresh for business spaces.")
open('sleep-scenes-for-business.html','w').write(page("Sleep Scenes for Business: Commercial Ambient Video License | Irish + Nova", "License tranquil scenes made fresh for business spaces: spa and salon calm, gentle waiting room loops, and cinematic lobby nights, $29 a month per screen.", "services.html", "SLEEP SCENES FOR BUSINESS", "Tranquil scenes, made for the screens in your business. <b>Licensed for commercial play.</b>", ssfb_body))
print('sleep-scenes-for-business.html', os.path.getsize('sleep-scenes-for-business.html'))

# ---- services.html cross-link section ----
_sv8 = open('services.html').read()
if 'SLEEP SCENES FOR BUSINESS' not in _sv8:
    _PAGECTX = 'services'
    _z_sec = '<div class="sec">For businesses with screens</div>'
    _z_sec += _gigcard("&#127916; SLEEP SCENES FOR BUSINESS", "A commercial license for tranquil ambient scenes, produced fresh for business spaces and priced per screen: spa calm, gentle waiting room loops, and cinematic lobby nights.", [("Spa and Salon Calm","$29/mo"),("Waiting Room and Office","$29/mo"),("Hotel and Lobby Nights","$29/mo")], "sleep-scenes-for-business.html", "See the business packages")
    _note_at8 = _sv8.rfind('<p class="note">')
    assert _note_at8 > 0
    open('services.html','w').write(_sv8[:_note_at8] + _z_sec + _sv8[_note_at8:])
    print('services.html + sleep scenes for business section', os.path.getsize('services.html'))


# ============ CAREER PROFILES: LINKEDIN AND INDEED (2026-10-19) ============
# Career profile building for job seekers: LinkedIn and Indeed profiles
# built and updated around the job the client wants, with photo treatment,
# banner design, resume writing, and recruiter search keyword tuning.
# Proof of concept: our own LinkedIn rebuild (headline, banner, About).
DETAILS.update({
('*','ONE-PLATFORM-REFRESH'): _D(
 ["Your choice of platform: LinkedIn or Indeed, built around the job you want",
  "A headline written for your target role, in the words recruiters actually search",
  "A summary section written fresh: your experience, your strengths, your direction",
  "Your current role entry built out in full, with earlier roles cleaned up and consistent",
  "LinkedIn builds include a custom banner designed for your profile",
  "Indeed builds include a profile photo treatment: crop, light, and a clean presentation",
  "Keyword tuning throughout, matched to real postings for your target job",
  "A draft of everything sent to you for approval before anything goes live"],
 "Job seekers with one platform that matters most, career changers aiming at a new title, and anyone whose headline still describes the job they are leaving.",
 ["The second platform (see Both Platforms)",
  "A resume rewrite (see Full Job Search Kit)",
  "Applications sent for you, and any promise of interviews or offers: hiring decisions belong to employers, always"],
 how=["Message us with the job you want and your work history: past roles, employers, and what you did in each.",
  "We write and design everything, then send you the full draft to approve before anything touches your account.",
  "You sign in to your own account and we guide the update, or you grant access while we are on the call. Your account stays yours.",
  "You review the finished profile and tell us any final tweaks."],
 timeline="Most refreshes are delivered in 2 to 3 business days once your work history and your target job reach us. We confirm your delivery day in writing before we start.",
 price="One Platform Refresh: $79"),
('*','BOTH-PLATFORMS'): _D(
 ["Everything in One Platform Refresh, on both LinkedIn and Indeed",
  "Headline and summary written once, then tuned for each platform, so both profiles tell the same story",
  "A custom banner designed for LinkedIn and a profile photo treatment for your Indeed profile",
  "Keyword tuning on both profiles, matched to real postings for your target job",
  "Job target setup on both platforms: your desired titles, locations, and work types saved for you",
  "Job alert tuning on both platforms, so matching roles reach you early",
  "Drafts of everything sent to you for approval before anything goes live"],
 "Active job seekers who want every door open at once, and professionals whose LinkedIn and Indeed profiles currently tell two different stories.",
 ["A resume rewrite (see Full Job Search Kit)",
  "Applications sent for you, and any promise of interviews or offers: hiring decisions belong to employers, always",
  "Ongoing profile management after delivery (ask us if you want monthly help)"],
 how=["Message us with the jobs you want and your work history: past roles, employers, and what you did in each.",
  "We write and design everything for both platforms, then send you the full drafts to approve before anything touches your accounts.",
  "You sign in to your own accounts and we guide the updates, or you grant access while we are on the call. Your accounts stay yours.",
  "You review both finished profiles and tell us any final tweaks."],
 timeline="Most two platform builds are delivered in 3 to 5 business days once your work history and your target jobs reach us. We confirm your delivery day in writing before we start.",
 price="Both Platforms: $129"),
('*','FULL-JOB-SEARCH-KIT'): _D(
 ["Everything in Both Platforms: LinkedIn and Indeed built, consistent, and keyword tuned",
  "A full resume rewrite, written for your target role from your real work history",
  "Resume keywords tuned for applicant tracking systems, the software that screens applications before a person reads them",
  "Your resume delivered as a clean document you can send anywhere",
  "Profile photo treatment and a custom banner designed for LinkedIn",
  "A short list of live roles that fit your target, picked as your first applications",
  "Drafts of everything sent to you for approval before anything goes live"],
 "Job seekers who want the whole kit finished in one pass: profiles, resume, and a first set of roles to go after.",
 ["Applications sent for you: you apply, with a kit built to be found",
  "Interview coaching and salary negotiation (not part of this kit)",
  "Any promise of interviews, offers, or employer timelines: no one honest can promise those"],
 how=["Message us with the jobs you want and your work history: past roles, employers, and what you did in each.",
  "We build both profiles and send you the drafts to approve, then write the resume to match.",
  "You sign in to your own accounts and we guide the updates, or you grant access while we are on the call. Your accounts stay yours.",
  "You review the finished profiles and resume, and get your starter list of roles."],
 timeline="Most kits are delivered in 5 to 7 business days once your work history and your target jobs reach us: profiles first, then the resume, then your starter list. We confirm your delivery day in writing before we start.",
 price="Full Job Search Kit: $199"),
('*','LINKEDIN-AND-INDEED-PROFILES-THAT-GET-SEEN'): _D(
 ["Three packages: One Platform Refresh $79, Both Platforms $129, and the Full Job Search Kit $199",
  "Headlines and summaries written for the job you want, in the words recruiters search",
  "Banner design, profile photo treatment, and keyword tuning across your profiles",
  "A full resume rewrite in the Kit, tuned for applicant tracking systems",
  "Full breakdowns on the Career Profiles page"],
 "Anyone job hunting whose LinkedIn or Indeed profile undersells them, or still describes the job they are leaving.",
 ["Nothing is ordered from this card: the Career Profiles page carries the full breakdowns"],
 how=["Open the Career Profiles page for the full breakdown of each package.",
  "Message us with the job you want and your work history.",
  "We write and build, you approve, and only then does anything post to your accounts."],
 timeline="Packages run in days, not weeks: Refresh in 2 to 3 business days, Both Platforms in 3 to 5, and the Full Job Search Kit in 5 to 7. We confirm your delivery day in writing before we start.",
 price="One Platform Refresh $79 \u00b7 Both Platforms $129 \u00b7 Full Job Search Kit $199"),
})

_PAGECTX = 'careers'
def _careerpack(title, desc, tiers):
    th = "".join('<div class="tier"><div class="tn">%s</div><div class="tp">%s</div></div>' % (n, p) for n, p in tiers)
    return _pkg(FBP, title, desc, th, tiers, "Message us to start")

cp_body = card(FBP, "RECRUITERS SEARCH. WE MAKE SURE THEY FIND YOU.", "Most profiles describe the job someone is leaving. Recruiters search by the job they are filling: titles, skills, and the exact words used in real postings. We rebuild your LinkedIn and Indeed profiles around the job you want, with headlines, summaries, banners, and keywords tuned to that search. We run this process on ourselves first: our own LinkedIn was rebuilt top to bottom, new headline, new banner, full About, and our Indeed right behind it. Same process, same care, on yours.", True)
cp_body += '<div class="sec">The packages</div>'
cp_body += _careerpack("&#128100; ONE PLATFORM REFRESH", "One platform, done properly: LinkedIn or Indeed, rebuilt around your target job, from the headline down to the keywords.", [("One Platform Refresh","$79")])
cp_body += _careerpack("&#127919; BOTH PLATFORMS", "Both platforms, one story: LinkedIn and Indeed rebuilt together and kept consistent, with your job targets and alerts set for you.", [("Both Platforms","$129")])
cp_body += _careerpack("&#128230; FULL JOB SEARCH KIT", "The whole kit: both platforms plus a full resume rewrite tuned for screening software, and a first list of roles worth applying to.", [("Full Job Search Kit","$199")])
cp_body += '<div class="sec">How we work, in plain terms</div>'
cp_body += _legal_sec("YOU BRING THE HISTORY", "You send your work history and the jobs you want: past roles, employers, and what you actually did in each. The truer the raw material, the stronger the profile. We write from what you give us; we never invent employers, dates, or credentials.")
cp_body += _legal_sec("YOU APPROVE BEFORE ANYTHING POSTS", "We write and build everything as a draft first. You read it, mark your changes, and approve it. Nothing goes onto your accounts until you say yes.")
cp_body += _legal_sec("YOUR ACCOUNTS STAY YOURS", "Your logins stay with you. You sign in, and we guide the update, or you grant access while we are on the call together. We do not keep your passwords, and we never need them once the work is done.")
cp_body += _legal_sec("NO GUARANTEES, EVER", "We make your profiles findable, current, and strong. We cannot promise interviews, offers, or a job, and neither can anyone else who is being honest with you. Hiring decisions belong to employers.")
cp_body += _legal_sec("TURNAROUND, IN DAYS", "One Platform Refresh: 2 to 3 business days. Both Platforms: 3 to 5 business days. Full Job Search Kit: 5 to 7 business days. The clock starts when your work history and target jobs reach us, and we confirm your delivery day in writing before we start.")
cp_body += '<div class="sec">Start here</div>'
cp_body += _svc_msg_card("Tell us the job you want and send your work history. We will confirm your package, your price, and your delivery day in writing before anything starts.")
cp_body += card("services.html", "ALL OUR SERVICES", "Every way to hire Irish + Nova in one place: websites, AI setup, content, design, and more.")
open('career-profiles.html','w').write(page("LinkedIn and Indeed Profile Building, Banner Design and Resume Writing | Irish + Nova", "We build LinkedIn and Indeed profiles around the job you want: headlines, summaries, banners, photo treatment, and keyword tuned resumes. Packages from $79.", "services.html", "LINKEDIN AND INDEED PROFILES THAT GET SEEN", "Built around the job you want. <b>Written to be found.</b>", cp_body))
print('career-profiles.html', os.path.getsize('career-profiles.html'))

# ---- services.html section, placed with the AI services area ----
_sv9 = open('services.html').read()
if 'career-profiles.html' not in _sv9:
    _PAGECTX = 'services'
    _c_sec = '<div class="sec">For job seekers</div>'
    _c_sec += _gigcard("&#128188; LINKEDIN AND INDEED PROFILES THAT GET SEEN", "Profiles built around the job you want: headlines and summaries in the words recruiters search, banner design, profile photo treatment, keyword tuning, and a full resume rewrite in the Kit.", [("One Platform Refresh","$79"),("Both Platforms","$129"),("Full Job Search Kit","$199")], "career-profiles.html", "See the career packages")
    _anchor9 = '<div class="sec">For musicians</div>'
    assert _sv9.count(_anchor9) == 1
    open('services.html','w').write(_sv9.replace(_anchor9, _c_sec + _anchor9, 1))
    print('services.html + career profiles section', os.path.getsize('services.html'))


# ============ IM10: LOCAL BUSINESS HOLIDAY-READY REFRESH (2026-10-22) ============
# One-time $79 seasonal service: Google Business Profile audit and holiday
# update (holiday hours, regular hours verified, photos, attributes,
# services, holiday posts), Facebook/Instagram tune-up aligned to the
# profile, four ready-to-post holiday graphics, one-page change summary.
# Approved by Irish 2026-10-22. Board checks recorded in work queue N154.
DETAILS.update({
('*','HOLIDAY-READY-REFRESH'): _D(
 ["Full Google Business Profile audit: your profile checked the way a customer sees it, covering hours, photos, attributes, services, and posts",
  "Holiday hours set correctly on Google for every special day on your schedule, and your regular hours verified against how you actually trade",
  "Photos refreshed: your best current shots moved up front and tired, dark, or outdated photos retired from the top spots",
  "Attributes and services checked and corrected, the details customers filter by when they pick who to visit",
  "Holiday posts switched on, with your first seasonal Google post written and published with your approval",
  "Social profile tune-up: Facebook and Instagram bio, cover, and holiday hours aligned with your Google profile, so every surface tells the same story",
  "Four ready-to-post holiday graphics made for your business, carrying your name, your hours, and your offers, delivered as files you can post anywhere",
  "A one-page summary of everything we changed, plus what to watch through the rest of the season"],
 "Local shops, salons, cafes, restaurants, and service businesses whose Google hours and photos have not been touched since last season, and any owner too busy serving customers to babysit their own profiles.",
 ["Paid advertising or ad spend of any kind",
  "A website rebuild or a brand-new website: we build those, but they are a separate service",
  "Guaranteed results: we never promise more calls, visits, sales, or a higher search ranking. A current, accurate profile removes reasons for customers to pass you by, and that is the honest promise",
  "Ongoing monthly management after delivery: available separately, just ask"],
 how=["Message us with your business links (Google, Facebook, and Instagram) and your holiday schedule: special hours, closures, and seasonal events.",
  "Add us as a manager on your Google Business Profile. It takes about two minutes, we walk you through it, no password is ever shared, and you can remove us the day we finish.",
  "We audit and update: Google profile first, then your socials, then your graphics and your summary.",
  "You receive the one-page summary of every change, your four graphics files, and one revision round on the summary items."],
 timeline="Delivered within 3 business days once your links, holiday schedule, and manager access reach us. Booking by November 20 secures delivery before the holiday rush; later bookings get a delivery day confirmed in writing before we start.",
 price="Holiday-Ready Refresh: $79 one time"),
('*','LOCAL-BUSINESS-HOLIDAY-READY-REFRESH'): _D(
 ["Google Business Profile audit, with holiday hours set and regular hours verified",
  "Photos refreshed, attributes and services checked, and holiday posts enabled",
  "Facebook and Instagram bio, cover, and holiday hours aligned with your Google profile",
  "Four ready-to-post holiday graphics carrying your business name and your hours",
  "A one-page summary of every change: the full breakdown lives on the Holiday Refresh page"],
 "Local shops, salons, cafes, restaurants, and service businesses heading into the season with last year's hours still showing.",
 ["Nothing is ordered from this card: the Holiday Refresh page carries the full breakdown",
  "No ad spend, no website rebuild, and no guaranteed sales or ranking: that is stated plainly on the package page"],
 how=["Open the Holiday Refresh page for the full breakdown.",
  "Message us with your business links and your holiday schedule.",
  "We audit, update, and deliver within 3 business days."],
 timeline="Delivered within 3 business days once your links, holiday schedule, and manager access reach us. Booking by November 20 secures delivery before the holiday rush.",
 price="Holiday-Ready Refresh $79 one time"),
})

_PAGECTX = 'services'
def _hrpack(title, desc, tiers):
    th = "".join('<div class="tier"><div class="tn">%s</div><div class="tp">%s</div></div>' % (n, p) for n, p in tiers)
    return _pkg(FBP, title, desc, th, tiers, "Message us to start")

hr_body = card(FBP, "WHEN CUSTOMERS SEARCH THIS SEASON, YOUR HOURS ARE THE FIRST THING THEY CHECK.", "Every season, customers drive to businesses that Google says are open and find the lights off, because last year's holiday hours never got updated. The Holiday-Ready Refresh is our one-time seasonal pass over the places customers actually check: we audit your Google Business Profile and set your holiday hours right, verify your regular hours, refresh your photos, check your attributes and services, switch on holiday posts, and line up your Facebook and Instagram to match. You also get four ready-to-post holiday graphics with your name and hours on them, and a one-page summary of everything we changed. One flat price, delivered in 3 business days, and booked by November 20 to land before the holiday rush.", True)
hr_body += '<div class="sec">The package</div>'
hr_body += _hrpack("&#127876; HOLIDAY-READY REFRESH", "One seasonal pass over your Google profile and socials: audit, holiday hours, photos, attributes, services, and posts, plus graphics and a written summary of every change.", [("Holiday-Ready Refresh","$79")])
hr_body += '<div class="sec">How we work, in plain terms</div>'
hr_body += _legal_sec("WHAT WE NEED FROM YOU", "Three things: your business links (Google, Facebook, Instagram), your holiday schedule (special hours, closures, seasonal events), and manager access to your Google Business Profile. Adding us as a manager takes about two minutes and we walk you through it. No password is ever shared, and you can remove us the moment we are done.")
hr_body += _legal_sec("EVERY CHANGE, IN WRITING", "Nothing changes silently. Your one-page summary lists everything we touched: hours set, photos moved, attributes corrected, posts published. If something in the summary is not right, one revision round on those items is included.")
hr_body += _legal_sec("NO GUARANTEED RESULTS, IN PLAIN WORDS", "A current, accurate profile removes reasons for customers to pass you by. It does not promise more calls, more visits, more sales, or a higher place in search, and we do not promise those things: they depend on your market, your reviews, and the season. Anyone who guarantees them is selling you a story.")
hr_body += _legal_sec("TIMELINE, IN DAYS", "Delivered within 3 business days once your links, holiday schedule, and manager access reach us. Bookings made by November 20 are delivered before the holiday rush; after that date we confirm your delivery day in writing before we start.")
hr_body += _legal_sec("ONE FLAT PRICE", "The Refresh is $79, once. No monthly fee, no setup fee, no surprise add-ons. Ongoing management exists if you want it later, and it is quoted separately, in writing, only if you ask.")
hr_body += '<div class="sec">Start here</div>'
hr_body += _svc_msg_card("Tell us your business name and send your profile links and holiday schedule. We confirm the flat $79 and your delivery day in writing before anything starts.")
hr_body += card("legal.html", "SERVICE TERMS &amp; DISCLAIMERS", "How we operate, our services terms, and our disclaimers, in writing, before you spend a dollar.")
hr_body += card("localbusiness.html", "MORE FOR LOCAL BUSINESSES", "Google profile builds, lead-answering setups, and ongoing local services.")
hr_body += card("services.html", "ALL OUR SERVICES", "Every way to hire Irish + Nova in one place: websites, AI setup, content, design, and more.")
open('holiday-refresh.html','w').write(page("Google Business Profile Holiday Hours & Holiday-Ready Refresh for Local Businesses | Irish + Nova", "Irish + Nova holiday-proof your Google profile and socials: holiday hours set, photos refreshed, posts ready. One flat $79, delivered in 3 business days.", "services.html", "HOLIDAY-READY REFRESH FOR LOCAL BUSINESS", "Holiday hours right. Profiles tuned. Posts ready. <b>One flat price: $79.</b>", hr_body))
print('holiday-refresh.html', os.path.getsize('holiday-refresh.html'))

# ---- services.html section, placed ahead of the local business services ----
_sv10 = open('services.html').read()
if 'holiday-refresh.html' not in _sv10:
    _PAGECTX = 'services'
    _h_sec = '<div class="sec">New for the holiday season</div>'
    _h_sec += _gigcard("&#127876; LOCAL BUSINESS HOLIDAY-READY REFRESH", "Your Google profile and socials set for the season: holiday hours right, photos refreshed, attributes and services checked, holiday posts on, plus four ready-to-post graphics and a one-page summary of every change.", [("Holiday-Ready Refresh","$79")], "holiday-refresh.html", "See the holiday refresh")
    _anchor10 = '<div class="sec">For local businesses</div>'
    assert _sv10.count(_anchor10) == 1
    open('services.html','w').write(_sv10.replace(_anchor10, _h_sec + _anchor10, 1))
    print('services.html + holiday refresh section', os.path.getsize('services.html'))

print('LINKIFY STATS:', dict(sorted(_LK_STATS.items(), key=lambda kv: -kv[1])))
