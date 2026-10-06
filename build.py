"""Build a dependency-free project portfolio for GitHub Pages. Run: python3 build.py."""
import json,html,re
from pathlib import Path
R=Path(__file__).resolve().parent
BASE='https://kaushikb258.github.io'
NAME='Kaushik Balakrishnan'
def esc(s):return html.escape(str(s),quote=True)
def page(title,description,body,path='/'):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="color-scheme" content="light"><link rel="canonical" href="{BASE}{path}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}{path}"><link rel="icon" type="image/svg+xml" href="/assets/favicon.svg"><link rel="stylesheet" href="/assets/site.css"></head><body><a class="skip" href="#main">Skip to content</a><div class="wrap"><header class="site-header"><a class="brand" href="/" aria-label="Kaushik Balakrishnan home"><span aria-hidden="true">KB</span><div class="name">{NAME}</div></a><nav class="nav" aria-label="Main navigation"><a href="/#projects">Projects</a><a class="optional" href="https://github.com/kaushikb258">GitHub</a></nav></header>{body}<footer class="footer"><span>Kaushik Balakrishnan, PhD · Personal projects</span><a href="https://github.com/kaushikb258">GitHub</a></footer></div></body></html>'''
def build():
 projects=json.loads((R/'projects.json').read_text());cards=[];paths=['/'];slugs=set()
 for p in projects:
  slug=p['slug']
  if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug) or slug in slugs:raise ValueError('Invalid or duplicate project slug')
  slugs.add(slug);path=f'/projects/{slug}/';paths.append(path)
  metrics='<div class="metrics-mini"><div><strong>96%</strong><span>LIBERO-Spatial</span></div><div><strong>83%</strong><span>MimicGen Square D0</span></div></div><span class="small">Selected simulator success rates · 100 episodes each</span>' if slug=='pi0-fast' else ''
  cards.append(f'''<article class="project-card"><div class="project-content"><div class="project-meta">{esc(p['category'])} &nbsp; / &nbsp; {p['year']}</div><h3><a href="{path}">{esc(p['title'])}</a></h3><p>{esc(p['summary'])}</p><div class="actions"><a class="button" href="{path}">Explore project</a><a class="text-link" href="{esc(p['code'])}">Code on GitHub</a></div></div><div class="project-visual"><div class="visual-label"><span>Inside the experiment</span><span>{esc(p.get('visual_label',p['short_title']))}</span></div><a href="{path}" aria-label="Explore {esc(p['short_title'])}"><img src="{esc(p['image'])}" alt="{esc(p['image_alt'])}" width="512" height="256"></a>{metrics}</div></article>''')
  source=R/p['body']
  if source.exists():
   route=R/path.strip('/');route.mkdir(parents=True,exist_ok=True)
   body=f'''<main id="main"><div class="project-hero"><div class="breadcrumb"><a href="/">All projects</a> / {esc(p['short_title'])}</div><p class="eyebrow">{esc(p['category'])} · {p['year']}</p><h1>{esc(p['title'])}</h1><p class="lede">{esc(p['summary'])}</p><div class="actions"><a class="button" href="{esc(p['code'])}">View code</a><a class="button secondary" href="{esc(p['models'])}">Download models</a></div></div>{source.read_text()}</main>'''
   (route/'index.html').write_text(page(p['short_title']+' | '+NAME,p['summary'],body,path))
 home='''<main id="main"><section class="hero"><p class="eyebrow">Kaushik Balakrishnan, PhD</p><h1>Robotics Projects on a Single GPU</h1><p class="lede">Experiments in robot learning, from fine-tuning vision-language-action models to improving the motions they execute.</p></section><section id="projects" aria-labelledby="projects-title"><div class="section-heading"><h2 id="projects-title">Selected projects</h2><span class="small">Experiments, results, and the code behind them</span></div>'''+''.join(cards)+'''</section><p class="archive-note">This collection grows one project at a time. Each project has its own page, with the approach, results, and resources to explore further.</p></main>'''
 (R/'index.html').write_text(page('Robotics Projects on a Single GPU | '+NAME,'Robotics projects on a single GPU by Kaushik Balakrishnan, PhD. Explore experiments, simulator results, open-source code, and trained models.',home))
 (R/'404.html').write_text(page('Page not found | '+NAME,'Return to the project portfolio.','<main id="main" class="hero"><p class="eyebrow">404</p><h1>Page not found.</h1><p>The project may have moved.</p><a class="button" href="/">Browse projects</a></main>','/404.html'))
 (R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}{p}</loc></url>' for p in paths)+'</urlset>')
 (R/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+BASE+'/sitemap.xml\n')
 print('Built home page and available project pages.')
if __name__=='__main__':build()
