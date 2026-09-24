import base64

with open('C:/Users/palsi/OneDrive/Desktop/Portfolio/photo.webp', 'rb') as f:
    photo_b64 = 'data:image/webp;base64,' + base64.b64encode(f.read()).decode()

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pallavi Singh | Product Manager Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --bg: #F6F4EF;
  --fg: #1C1B19;
  --fg2: #4A4740;
  --fg3: #5E5A51;
  --accent: #1F5F5B;
  --border: #DDD8CD;
  --border2: #EAE6DD;
  --white: #FFFFFF;
  --card: #EFECE5;
}
body {
  font-family: 'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif;
  background: var(--bg);
  color: var(--fg);
  -webkit-font-smoothing: antialiased;
  font-size: 16px;
  line-height: 1.6;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

/* NAV */
.nav {
  position: sticky; top: 0; z-index: 100;
  background: rgba(246,244,239,0.96);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border);
  display: flex; justify-content: space-between; align-items: center;
  padding: 1.5rem 6rem;
}
.nav-name { font-family: 'Fraunces', Georgia, serif; font-size: 1.25rem; font-weight: 600; color: var(--fg); text-decoration: none; }
.nav-name:hover { text-decoration: none; }
.nav-links { display: flex; gap: 2.25rem; list-style: none; }
.nav-links a { font-size: 0.9375rem; font-weight: 500; color: var(--fg); }
.nav-links a.accent { color: var(--accent); }
.nav-links a:hover { text-decoration: none; opacity: 0.65; }

/* HERO */
.hero {
  display: flex; align-items: center; gap: 5rem;
  padding: 6rem;
  max-width: 1440px; margin: 0 auto;
}
.hero-left { flex: 1; display: flex; flex-direction: column; gap: 1.5rem; max-width: 700px; }
.hero-right { flex-shrink: 0; }
.status-badge {
  display: inline-flex; align-items: center; gap: 0.45rem;
  font-size: 0.8rem; color: var(--fg3);
}
.status-dot {
  width: 7px; height: 7px; border-radius: 50%; background: #22c55e;
  animation: pulse 2.5s ease-in-out infinite;
}
@keyframes pulse {
  0%,100% { box-shadow: 0 0 0 0 rgba(34,197,94,0.4); }
  50% { box-shadow: 0 0 0 5px rgba(34,197,94,0); }
}
.hero-title {
  font-family: 'Fraunces', Georgia, serif;
  font-size: clamp(1.75rem, 3vw, 2.625rem);
  line-height: 1.08; font-weight: 500; letter-spacing: -0.02em;
}
.hero-bio { font-size: 1rem; line-height: 1.75; color: var(--fg2); margin-bottom: 1.25rem; }
.hero-bio strong { color: var(--fg); font-weight: 600; }
.cred-row { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 10px; margin-bottom: 1.25rem; }
.cred-card { background: var(--surface,#fff); border: 1px solid var(--border); border-radius: 12px; padding: 0.875rem 1rem; }
.cred-label { font-size: 0.6875rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--fg3); margin-bottom: 0.35rem; }
.cred-value { font-size: 0.9rem; font-weight: 500; color: var(--fg); line-height: 1.4; }
@media(max-width:600px){ .cred-row { grid-template-columns: 1fr; } }
.hero-cta { display: flex; gap: 1rem; margin-top: 0.5rem; flex-wrap: wrap; }
.btn-primary {
  display: inline-flex; align-items: center; height: 48px; padding: 0 24px;
  background: var(--accent); color: var(--white);
  border-radius: 8px; font-weight: 500; font-size: 0.9375rem;
}
.btn-primary:hover { opacity: 0.85; text-decoration: none; }
.btn-outline {
  display: inline-flex; align-items: center; height: 48px; padding: 0 24px;
  border: 1px solid var(--fg); color: var(--fg);
  border-radius: 8px; font-weight: 500; font-size: 0.9375rem;
}
.btn-outline:hover { opacity: 0.65; text-decoration: none; }
.photo-wrap {
  width: 340px; height: 400px;
  border-radius: 16px; overflow: hidden;
  background: var(--card);
}
.photo-wrap img { width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block; }

/* SECTION COMMONS */
.section { padding: 7rem 6rem 0; }
.section-inner { max-width: 1440px; margin: 0 auto; }
.section-head { display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 2rem; }
.section-title { font-family: 'Fraunces', Georgia, serif; font-size: 2.5rem; font-weight: 500; }
.section-sub { font-size: 1rem; color: var(--fg3); }

/* SKILLS TICKER */
.ticker-section { padding: 4rem 0 0; }
.ticker-container {
  overflow: hidden; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
  background: var(--white);
}
.ticker-row {
  display: flex; white-space: nowrap; width: max-content;
  border-bottom: 1px solid var(--border);
  padding: 12px 0;
}
.ticker-row:last-child { border-bottom: none; }
.ticker-row.left { animation: scrollL 70s linear infinite; }
.ticker-row.right { animation: scrollR 90s linear infinite; }
.ticker-row:hover { animation-play-state: paused; }
@keyframes scrollL { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
@keyframes scrollR { 0% { transform: translateX(-50%); } 100% { transform: translateX(0); } }
.ticker-hint { font-size: 0.8rem; color: var(--fg3); padding: 0.75rem 6rem; }

/* SKILL TOOLTIP */
#skill-tt {
  position: fixed; background: var(--white); border: 1px solid var(--border);
  border-radius: 12px; padding: 14px 18px;
  min-width: 220px; max-width: 300px;
  opacity: 0; pointer-events: none;
  transition: opacity 0.15s; z-index: 1000;
  box-shadow: 0 4px 20px rgba(0,0,0,0.10);
}

/* FEATURED 2x2 */
.featured-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2rem; }
.featured-card {
  background: var(--white); border: 1px solid var(--border);
  border-radius: 16px; overflow: hidden;
  display: flex; flex-direction: column;
  transition: box-shadow 0.2s;
}
.featured-card:hover { box-shadow: 0 4px 24px rgba(0,0,0,0.08); }
.card-media {
  height: 240px; background: var(--fg); color: #D9D4C9;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  gap: 12px; font-size: 14px;
}
.card-body { padding: 2rem; display: flex; flex-direction: column; gap: 1rem; flex: 1; }
.pill-row { display: flex; gap: 0.5rem; flex-wrap: wrap; }
.pill {
  padding: 5px 12px; border-radius: 999px;
  font-size: 0.75rem; font-weight: 600;
}
.pill-live { background: #D8EDE3; color: #1C5A3C; }
.pill-beyond { background: #E8DEF3; color: #4B2A73; }
.pill-proto { background: #FBEBD3; color: #7A4A0C; }
.pill-mvp { background: #DCE8F6; color: #1D4575; }
.pill-data { background: #F4DDDA; color: #7A2A20; }
.pill-ent { background: #ECEAE4; color: #3D3A34; }
.card-title { font-family: 'Fraunces', Georgia, serif; font-size: 1.875rem; font-weight: 500; }
.card-desc { font-size: 1rem; line-height: 1.55; color: var(--fg2); }
.card-metric { font-size: 0.9375rem; font-weight: 600; color: var(--accent); }
.card-details {
  display: flex; flex-direction: column; gap: 0.5rem;
  padding-top: 1rem; border-top: 1px solid var(--border2);
  font-size: 0.875rem; line-height: 1.5;
}
.card-details strong { color: var(--fg); font-weight: 600; }
.card-link { font-size: 0.9375rem; font-weight: 600; margin-top: auto; padding-top: 0.5rem; }

/* CLIENT WORK */
.client-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2rem; }
.client-card {
  background: var(--white); border: 1px solid var(--border);
  border-radius: 16px; padding: 2.25rem;
  display: flex; flex-direction: column; gap: 1rem;
}
.client-header { display: flex; justify-content: space-between; align-items: center; }
.client-eyebrow { font-size: 0.8125rem; font-weight: 600; color: var(--fg3); text-transform: uppercase; letter-spacing: 0.08em; }
.client-title { font-family: 'Fraunces', Georgia, serif; font-size: 1.875rem; font-weight: 500; }
.client-desc { font-size: 1rem; line-height: 1.55; color: var(--fg2); }
.client-bullets {
  display: flex; flex-direction: column; gap: 0.5rem;
  font-size: 0.875rem; line-height: 1.5;
  padding-top: 1rem; border-top: 1px solid var(--border2);
}
.client-bullets strong { color: var(--fg); }
.proto-pair {
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem;
  padding-top: 1rem; border-top: 1px solid var(--border2);
}
.proto-box {
  background: var(--bg); border-radius: 10px; padding: 1rem;
  display: flex; flex-direction: column; gap: 6px;
}
.proto-box-title { font-size: 0.9375rem; font-weight: 600; }
.proto-box-desc { font-size: 0.8125rem; line-height: 1.5; color: var(--fg2); }
.client-metric { font-size: 0.875rem; font-weight: 600; color: var(--accent); }

/* EVERYTHING I'VE BUILT */
.filter-bar { display: flex; gap: 0.625rem; flex-wrap: wrap; }
.filter-btn {
  padding: 8px 16px; border-radius: 999px;
  font-size: 0.8125rem; font-weight: 600; cursor: pointer; border: none;
  transition: background 0.15s, color 0.15s;
}
.filter-btn.active { background: var(--accent); color: var(--white); }
.filter-btn:not(.active) { background: var(--white); border: 1px solid var(--border); color: #3D3A34; }
.all-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.5rem; }
.all-card {
  background: var(--white); border: 1px solid var(--border);
  border-radius: 12px; padding: 1.75rem;
  display: flex; flex-direction: column; gap: 0.75rem;
  transition: box-shadow 0.2s;
}
.all-card:hover { box-shadow: 0 2px 16px rgba(0,0,0,0.07); }
.all-card-title { font-size: 1.25rem; font-weight: 600; }
.all-card-desc { font-size: 0.9375rem; line-height: 1.5; color: var(--fg2); }
.all-card-metric { font-size: 0.875rem; font-weight: 600; color: var(--accent); }
.all-card-link { font-size: 0.875rem; font-weight: 600; margin-top: auto; }

/* SKILLS MATRIX */
.matrix-wrap { background: var(--white); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; }
.matrix { display: grid; grid-template-columns: 240px repeat(9, minmax(0, 1fr)); font-size: 0.875rem; }
.matrix-cell { padding: 14px 8px; }
.matrix-cell.label { padding: 14px 20px; }
.matrix-head { background: var(--card); font-weight: 600; }
.matrix-row-label { padding: 14px 20px; border-top: 1px solid var(--border2); }
.matrix-dot { border-top: 1px solid var(--border2); text-align: center; }
.dot-on { color: var(--accent); }
.dot-off { color: #B8B2A6; }
.matrix-legend { font-size: 0.8125rem; color: var(--fg3); margin-top: 0.75rem; }

/* CASE STUDIES */
.case-study {
  display: none;
  padding: 5rem 6rem;
  border-top: 1px solid var(--border);
}
.case-study.cs-active {
  display: block;
}
.case-inner { max-width: 760px; margin: 0 auto; }
.case-back { font-size: 0.875rem; color: var(--fg3); margin-bottom: 2rem; display: inline-flex; align-items: center; gap: 0.4rem; }
.case-back:hover { color: var(--fg); text-decoration: none; }
.case-tag {
  display: inline-block; font-size: 0.7rem; font-weight: 600;
  letter-spacing: 0.07em; text-transform: uppercase;
  padding: 0.2rem 0.65rem; border-radius: 4px;
  background: #D8EDE3; color: #1C5A3C; margin-bottom: 0.75rem;
}
.case-title {
  font-family: 'Fraunces', Georgia, serif;
  font-size: clamp(1.5rem, 3vw, 2.2rem);
  font-weight: 500; letter-spacing: -0.02em; line-height: 1.2; margin-bottom: 0.75rem;
}
.case-meta {
  display: flex; flex-wrap: wrap; gap: 1.5rem;
  font-size: 0.875rem; color: var(--fg3);
  margin-bottom: 2rem; padding-bottom: 2rem; border-bottom: 1px solid var(--border);
}
.case-meta strong { color: var(--fg); font-weight: 600; }
.case-body h2 { font-family: 'Fraunces', Georgia, serif; font-size: 1.4rem; font-weight: 500; margin: 2.5rem 0 0.75rem; color: var(--fg); padding-top: 2rem; border-top: 1px solid var(--border2); }
.case-body h2:first-child { border-top: none; padding-top: 0; }
.case-body p { font-size: 0.95rem; color: var(--fg2); line-height: 1.75; margin-bottom: 1rem; }
.case-body ul { padding-left: 1.25rem; margin-bottom: 1rem; }
.case-body li { font-size: 0.95rem; color: var(--fg2); line-height: 1.75; margin-bottom: 0.4rem; }
.case-body strong { color: var(--fg); font-weight: 600; }
.case-body a { color: var(--accent); }
.impact-box {
  background: var(--bg); border-radius: 10px;
  padding: 1.25rem 1.5rem; margin: 1.5rem 0;
  display: flex; flex-wrap: wrap; gap: 1.5rem;
  border: 1px solid var(--border);
}
.impact-stat { display: flex; flex-direction: column; gap: 0.2rem; }
.impact-stat .num { font-size: 1.75rem; font-weight: 700; letter-spacing: -0.03em; font-family: 'Fraunces', Georgia, serif; }
.impact-stat .lbl { font-size: 0.75rem; color: var(--fg3); text-transform: uppercase; letter-spacing: 0.06em; }

/* FOOTER */
.footer {
  margin: 7rem 6rem 0;
  padding: 3.5rem 4rem;
  background: var(--fg); color: #F6F4EF;
  border-radius: 20px;
  display: flex; justify-content: space-between; align-items: center;
  gap: 2rem; flex-wrap: wrap;
  margin-bottom: 3rem;
}
.footer-left { display: flex; flex-direction: column; gap: 0.625rem; }
.footer-title { font-family: 'Fraunces', Georgia, serif; font-size: 2.25rem; font-weight: 500; }
.footer-links { font-size: 1rem; color: #CFC9BD; }
.footer-links a { color: #CFC9BD; }
.footer-links a:hover { color: #F6F4EF; text-decoration: none; }
.btn-resume {
  display: inline-flex; align-items: center; height: 52px; padding: 0 28px;
  background: #F6F4EF; color: var(--fg);
  border-radius: 8px; font-weight: 600; font-size: 0.9375rem; white-space: nowrap;
}
.btn-resume:hover { opacity: 0.85; text-decoration: none; }

/* RESPONSIVE */
@media (max-width: 900px) {
  .nav { padding: 1rem 1.5rem; }
  .nav-links { display: none; }
  .hero { flex-direction: column-reverse; padding: 2.5rem 1.5rem; gap: 2rem; }
  .photo-wrap { width: 200px; height: 240px; }
  .section { padding: 4rem 1.5rem 0; }
  .case-study { padding: 3rem 1.5rem; }
  .featured-grid, .client-grid { grid-template-columns: 1fr; }
  .all-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .footer { margin: 3rem 1.5rem 1.5rem; padding: 2rem 1.5rem; flex-direction: column; align-items: flex-start; }
  .matrix { overflow-x: auto; display: block; }
}
@media (max-width: 540px) {
  .all-grid { grid-template-columns: 1fr; }
  .proto-pair { grid-template-columns: 1fr; }
}
@media (prefers-reduced-motion: reduce) {
  .ticker-row { animation: none; }
  .status-dot { animation: none; }
}
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav">
  <a class="nav-name" href="#">Pallavi Singh</a>
  <ul class="nav-links">
    <li><a href="#best">Best of my work</a></li>
    <li><a href="#client">Pro bono client work</a></li>
    <li><a href="#all">Other AI Products &amp; Analytics</a></li>
    <li><a href="#contact" class="accent">Contact</a></li>
  </ul>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-left">
    <div class="status-badge"><span class="status-dot"></span> Open to new roles</div>
    <p style="font-size:1.25rem;font-weight:700;color:var(--fg);margin:0 0 0.35rem;">Hi, I&rsquo;m Pallavi</p>
    <h1 class="hero-title">I find the problem hiding inside the process</h1>
    <p class="hero-bio">Seven years across SAP, ServiceNow, and Fortune 500 delivery taught me to read patterns in data and operational chaos before anyone else in the room calls it a problem. I ship internal tools, API integrations, and AI agents. I work at both ends, with engineers on what is technically feasible and with users on what actually matters.</p>
    <div class="cred-row">
      <div class="cred-card">
        <div class="cred-label">Building since</div>
        <div class="cred-value">2016 - automations before AI was the word for it</div>
      </div>
      <div class="cred-card">
        <div class="cred-label">Current stack</div>
        <div class="cred-value">Claude APIs &middot; AI agents &middot; MCP connectors &middot; ships code</div>
      </div>
      <div class="cred-card">
        <div class="cred-label">Currently building</div>
        <div class="cred-value">Snaccly, a microlearning app - live, and validated with real users</div>
      </div>
    </div>
    <div class="hero-cta">
      <a class="btn-primary" href="#best">See my best work</a>
      <a class="btn-outline" href="https://drive.google.com/file/d/1JxCzEhHRlZUxnuM70DABE5CfXVKU9Ii6/view?usp=sharing" target="_blank">Resume</a>
    </div>
  </div>
  <div class="hero-right">
    <div class="photo-wrap">
      <img src="__PHOTO__" alt="Pallavi Singh">
    </div>
  </div>
</section>

<!-- SKILLS TICKER -->
<section class="ticker-section">
  <div style="max-width:1440px;margin:0 auto;padding:0 6rem;">
    <div style="display:flex;flex-direction:column;gap:0.5rem;margin-bottom:1.25rem;">
      <h2 class="section-title" style="font-family:'Fraunces',Georgia,serif;font-size:2.5rem;font-weight:500;">Technical skills</h2>
    </div>
  </div>
  <div class="ticker-container">
    <div id="r1" class="ticker-row left"></div>
    <div id="r2" class="ticker-row right"></div>
  </div>
  <div class="ticker-hint">Click any skill for context &middot; Hover to pause</div>
</section>

<div id="skill-tt">
  <div id="tt-n" style="font-size:15px;font-weight:600;color:#1C1B19;margin-bottom:4px;"></div>
  <div id="tt-s" style="font-size:14px;color:#1F5F5B;margin-bottom:8px;"></div>
  <div id="tt-r" style="font-size:13px;color:#4A4740;line-height:1.5;"></div>
</div>

<!-- BEST OF MY WORK -->
<section class="section" id="best">
  <div class="section-inner">
    <div class="section-head">
      <h2 class="section-title">Best of my work</h2>
    </div>
    <div class="featured-grid">

      <!-- Snaccly -->
      <article class="featured-card">
        <div class="card-media">
          <svg width="48" height="48" viewBox="0 0 48 48" fill="none" stroke="#D9D4C9" stroke-width="2"><circle cx="24" cy="24" r="22"></circle><path d="M20 16 L32 24 L20 32 Z"></path></svg>
          <span>Demo video coming soon</span>
        </div>
        <div class="card-body">
          <div class="pill-row">
            <span class="pill pill-beyond">Beyond MVP</span>
            <span class="pill pill-ent">Consumer AI &middot; B2C</span>
          </div>
          <h3 class="card-title">Snaccly</h3>
          <p class="card-desc">AI literacy platform that teaches complex concepts in 60 seconds. One Byte at a time.</p>
          <div class="proto-pair" style="margin:0.75rem 0;">
            <div class="proto-box">
              <div class="proto-box-title">Product depth</div>
              <div class="proto-box-desc">100 Bytes across 6 tracks. Gamified with XP, streaks, hearts, and challenge mode. Built with consumer psychology principles and A/B experimentation.</div>
            </div>
            <div class="proto-box">
              <div class="proto-box-title">Full product build</div>
              <div class="proto-box-desc">Vanilla JS app, Astro marketing site, Supabase backend, server-side scoring, audio narration, cloud sync. Live at app.snacclyai.com.</div>
            </div>
          </div>
          <div class="card-metric">100+ concepts &middot; 6 tracks &middot; Live app &middot; Pro and Team pricing tiers &middot; app.snacclyai.com</div>
          <div style="display:flex;gap:0.75rem;flex-wrap:wrap;margin-top:0.75rem;">
            <a href="https://app.snacclyai.com/" target="_blank" class="card-link">View app &rarr;</a>
            <a href="#case-snaccly" class="card-link" style="background:transparent;color:var(--accent);border:1.5px solid var(--accent);">Read case study &rarr;</a>
          </div>
        </div>
      </article>

      <!-- InsightLoop -->
      <article class="featured-card">
        <div class="card-media">
          <svg width="48" height="48" viewBox="0 0 48 48" fill="none" stroke="#D9D4C9" stroke-width="2"><circle cx="24" cy="24" r="22"></circle><path d="M20 16 L32 24 L20 32 Z"></path></svg>
          <span>Demo video coming soon</span>
        </div>
        <div class="card-body">
          <div class="pill-row" style="margin-bottom:0.5rem;">
            <span class="pill pill-mvp">MVP</span>
            <span class="pill pill-ent">Enterprise AI &middot; Evals &middot; AI Agent</span>
          </div>
          <h3 class="card-title">InsightLoop</h3>
          <p class="card-desc">Enterprise knowledge workers spending hours synthesizing research across 15+ sources. InsightLoop reads, ranks, and cites for them.</p>
          <div class="proto-pair" style="margin:0.75rem 0;">
            <div class="proto-box">
              <div class="proto-box-title">Built and Deployed on MuleRun</div>
              <div class="proto-box-desc">Prompt-engineered with Claude across multiple iterations. Published to the MuleRun marketplace with a source-tiering eval framework that weights peer-reviewed journals above grey literature.</div>
            </div>
            <div class="proto-box">
              <div class="proto-box-title">Validated with Real Users</div>
              <div class="proto-box-desc">96% adoption in a 27-student DBA cohort. Weekly research time cut from 5 hours to under 1 hour. Doctoral researchers used as the first validation cohort.</div>
            </div>
          </div>
          <div class="card-metric">96% cohort adoption &middot; 27 DBA students &middot; 5h to under 1h weekly</div>
          <div style="display:flex;gap:0.75rem;flex-wrap:wrap;margin-top:0.75rem;">
            <a href="https://mulerun.com/chat?template=1db82c25-152d-4527-9857-22c3a1720f6b" target="_blank" class="card-link">Try the agent &rarr;</a>
            <a href="#case-insightloop" class="card-link" style="background:transparent;color:var(--accent);border:1.5px solid var(--accent);">Read case study &rarr;</a>
          </div>
        </div>
      </article>

      <!-- Accenture Payroll -->
      <article class="featured-card">
        <div class="card-media">
          <svg width="48" height="48" viewBox="0 0 48 48" fill="none" stroke="#D9D4C9" stroke-width="2"><circle cx="24" cy="24" r="22"></circle><path d="M20 16 L32 24 L20 32 Z"></path></svg>
          <span>Demo video coming soon</span>
        </div>
        <div class="card-body">
          <div class="client-header" style="margin-bottom:0.5rem;">
            <span class="client-eyebrow">Accenture &middot; SAP &middot; Payroll</span>
            <span class="pill pill-mvp">Enterprise Delivery</span>
          </div>
          <h3 class="card-title">Nordic Payroll Fix</h3>
          <p class="card-desc">$8M payroll for 100K employees across 3 Nordic countries at risk from a silent race condition hiding in legacy config.</p>
          <div style="font-size:0.8125rem;font-weight:600;color:#5E5A51;text-transform:uppercase;letter-spacing:0.07em;margin-bottom:0.5rem;">2 phases delivered</div>
          <div class="proto-pair">
            <div class="proto-box">
              <div class="proto-box-title">Root Cause Discovery</div>
              <div class="proto-box-desc">31-day race condition in SAP batch scheduling. Found in config, not code, after engineering spent months in the codebase.</div>
            </div>
            <div class="proto-box">
              <div class="proto-box-title">System Remediation</div>
              <div class="proto-box-desc">Idempotency keys at the API gateway, concurrency lockouts, and a full orphan job lifecycle audit.</div>
            </div>
          </div>
          <div class="client-metric">$8M safeguarded &middot; 100K employees &middot; 0 payroll failures</div>
          <a href="#case-payroll" class="card-link" style="font-size:0.9375rem;font-weight:600;">Read case study &rarr;</a>
        </div>
      </article>

      <!-- Capgemini -->
      <article class="featured-card">
        <div class="card-media">
          <svg width="48" height="48" viewBox="0 0 48 48" fill="none" stroke="#D9D4C9" stroke-width="2"><circle cx="24" cy="24" r="22"></circle><path d="M20 16 L32 24 L20 32 Z"></path></svg>
          <span>Demo video coming soon</span>
        </div>
        <div class="card-body">
          <div class="client-header" style="margin-bottom:0.5rem;">
            <span class="client-eyebrow">Capgemini &middot; Fortune 500 &middot; Enterprise SaaS</span>
            <span class="pill pill-mvp">Enterprise Delivery</span>
          </div>
          <h3 class="card-title">Enterprise AI Program</h3>
          <p class="card-desc">18 years of manual contract work across 20+ delivery teams. No automation. No system. No one had mapped it yet.</p>
          <div style="font-size:0.8125rem;font-weight:600;color:#5E5A51;text-transform:uppercase;letter-spacing:0.07em;margin-bottom:0.5rem;">6 use cases shipped</div>
          <div class="proto-pair">
            <div class="proto-box">
              <div class="proto-box-title">The Pitch</div>
              <div class="proto-box-desc">Interviewed senior leads, catalogued 6 repeatable use cases, and pitched an org-wide GenAI program. Nobody asked for it.</div>
            </div>
            <div class="proto-box">
              <div class="proto-box-title">The Build</div>
              <div class="proto-box-desc">Built and scaled 6 automation use cases in Python across 20+ teams. SLA validation dropped from weeks to days.</div>
            </div>
          </div>
          <div class="client-metric">20+ teams &middot; 6 use cases shipped &middot; 80% SLA cycle reduction &middot; 2 hrs to 2 min incident alerts</div>
          <a href="#case-capgemini" class="card-link" style="font-size:0.9375rem;font-weight:600;">Read case study &rarr;</a>
        </div>
      </article>

    </div>
  </div>
</section>

<!-- PRO BONO CLIENT WORK -->
<section class="section" id="client">
  <div class="section-inner">
    <div class="section-head">
      <h2 class="section-title">Pro bono client work</h2>
    </div>
    <div class="client-grid">

      <!-- Londr -->
      <div class="client-card">
        <div class="client-header">
          <span class="client-eyebrow">Growth Product Strategy</span>
          <span class="pill pill-proto">Strategy</span>
        </div>
        <h3 class="client-title">Londr</h3>
        <p class="client-desc">A gig-economy laundry marketplace with healthy margins and a broken growth engine.</p>
        <div style="font-size:0.8125rem;font-weight:600;color:#5E5A51;text-transform:uppercase;letter-spacing:0.07em;margin-bottom:0.5rem;">2 growth systems designed</div>
        <div class="proto-pair">
          <div class="proto-box">
            <div class="proto-box-title">Zero-CAC Growth Loop</div>
            <div class="proto-box-desc">Turned washers into the acquisition channel. Referral system targeting ~$10 CAC.</div>
          </div>
          <div class="proto-box">
            <div class="proto-box-title">Licensing Framework</div>
            <div class="proto-box-desc">3,300 US market zones mapped. $837K ARR projected by Year 5.</div>
          </div>
        </div>
        <div class="client-metric">6 deliverables &middot; 52-hour sprint &middot; Head of Product &amp; Strategy role offered</div>
        <a href="#case-londr" class="card-link" style="font-size:0.9375rem;font-weight:600;">Read case study &rarr;</a>
      </div>

      <!-- PID Floors -->
      <div class="client-card">
        <div class="client-header">
          <span class="client-eyebrow">Build &middot; AI automation</span>
          <span class="pill pill-proto">Prototype</span>
        </div>
        <h3 class="client-title">PID Floors</h3>
        <p class="client-desc">A luxury flooring brand with a non-technical team and back-office bottlenecks costing them in sales velocity.</p>
        <div style="font-size:0.8125rem;font-weight:600;color:#5E5A51;text-transform:uppercase;letter-spacing:0.07em;">2 prototypes delivered</div>
        <div class="proto-pair">
          <div class="proto-box">
            <div class="proto-box-title">In-store consultant assistant</div>
            <div class="proto-box-desc">AI catalog matching across 1,000+ SKUs. Shortlist in seconds.</div>
          </div>
          <div class="proto-box">
            <div class="proto-box-title">Inbox Intelligence</div>
            <div class="proto-box-desc">Every inbound email auto-triaged, categorized, prioritized, and draft-replied in Airtable.</div>
          </div>
        </div>
        <div class="client-metric">$300K to $800K annual efficiency run rate &middot; 2 prototypes &middot; built in 4 hours &middot; AI Implementation Strategist role offered</div>
        <a href="#case-pid-floors" class="card-link" style="font-size:0.9375rem;font-weight:600;">Read case study &rarr;</a>
      </div>

    </div>
  </div>
</section>

<!-- EVERYTHING I'VE BUILT -->
<section class="section" id="all">
  <div class="section-inner">
    <div class="section-head">
      <h2 class="section-title">Other AI Products &amp; Analytics Projects</h2>
      <p class="section-sub">Filter by stage</p>
    </div>
    <div class="filter-bar" style="margin-bottom:1.5rem;">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="Concept">Concept</button>
      <button class="filter-btn" data-filter="Prototype">Prototype</button>
      <button class="filter-btn" data-filter="MVP">MVP</button>
      <button class="filter-btn" data-filter="Live">Live</button>
      <button class="filter-btn" data-filter="Beyond MVP">Beyond MVP</button>
      <button class="filter-btn" data-filter="Data">Data</button>
    </div>
    <div class="all-grid">

      <!-- Customer Analytics -->
      <div class="all-card" data-stage="Data">
        <div style="display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;">
          <span class="pill pill-data" style="align-self:flex-start;">Data</span>
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;">Tableau &middot; Python &middot; Excel</span>
        </div>
        <h3 class="all-card-title">Customer Analytics</h3>
        <p class="all-card-desc">4.8M+ support calls across shared and dedicated queues. Found the vendor and staffing decisions hiding in the data.</p>
        <div class="proto-pair" style="margin:0.75rem 0;">
          <div class="proto-box">
            <div class="proto-box-title">End-to-end pipeline</div>
            <div class="proto-box-desc">Python and Excel analysis of 4.8M+ calls. 3 Tableau dashboards covering volume, SLA, outages, and 2025 forecast.</div>
          </div>
          <div class="proto-box">
            <div class="proto-box-title">Staffing decisions influenced</div>
            <div class="proto-box-desc">Q1 to Q2 2025 forecast built with event-based adjustments. Translated into vendor allocation and headcount plans.</div>
          </div>
        </div>
        <div class="all-card-metric">4.8M+ data points &middot; 3 Tableau dashboards &middot; 2 versions (Python + Excel) &middot; staffing and vendor recommendations</div>
        <div style="display:flex;gap:1rem;margin-top:auto;padding-top:0.75rem;flex-wrap:wrap;">
          <a href="https://github.com/pallavising48/customer-support-analytics" target="_blank" class="all-card-link">View on GitHub &rarr;</a>
          <a href="https://public.tableau.com/views/CustomerSupport2024Overview/2024Overview" target="_blank" class="all-card-link" style="color:var(--fg3);">View dashboards &rarr;</a>
        </div>
      </div>

      <!-- Instagram Curated -->
      <div class="all-card" data-stage="Prototype">
        <div style="display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;">
          <span class="pill pill-proto" style="align-self:flex-start;">Prototype</span>
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;">Full PRD</span>
        </div>
        <h3 class="all-card-title">Instagram Curated</h3>
        <p class="all-card-desc">A feature pitch for Instagram's Following feed. Category and time-based content curation for users who want control over what they see and when.</p>
        <div class="proto-pair" style="margin:0.75rem 0;">
          <div class="proto-box">
            <div class="proto-box-title">Full PM deliverables</div>
            <div class="proto-box-desc">PRD, competitive analysis, user personas, and success metrics. Built as a real product pitch.</div>
          </div>
          <div class="proto-box">
            <div class="proto-box-title">Working prototype</div>
            <div class="proto-box-desc">Interactive mobile prototype built on Replit. Demo video showing the full feature flow.</div>
          </div>
        </div>
        <div class="all-card-metric">Feature pitch &middot; Full PRD &middot; Working prototype &middot; Competitive analysis</div>
        <div style="display:flex;gap:1rem;margin-top:auto;padding-top:0.75rem;flex-wrap:wrap;">
          <a href="https://mobile-prototype-builder.replit.app/" target="_blank" class="all-card-link">View prototype &rarr;</a>
          <a href="https://youtube.com/shorts/m9Xhm1gYfKY" target="_blank" class="all-card-link" style="color:var(--fg3);">Watch demo &rarr;</a>
          <a href="#case-instagram-curated" class="all-card-link" style="color:var(--fg3);">View case study &rarr;</a>
        </div>
      </div>

      <!-- Move Mitra -->
      <div class="all-card" data-stage="MVP">
        <div style="display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;">
          <span class="pill pill-mvp" style="align-self:flex-start;">MVP</span>
        </div>
        <h3 class="all-card-title">Move Mitra</h3>
        <p class="all-card-desc">A bilingual knee-safety app for women 40+ who are afraid to start moving.</p>
        <div class="proto-pair" style="margin:0.75rem 0;">
          <div class="proto-box">
            <div class="proto-box-title">Customer-Validated Build</div>
            <div class="proto-box-desc">8 discovery interviews before a line of code. Fear identified as the primary barrier, not knowledge.</div>
          </div>
          <div class="proto-box">
            <div class="proto-box-title">Bilingual by Design</div>
            <div class="proto-box-desc">English and Hindi support built for the age group. Language as a trust signal, not a feature.</div>
          </div>
        </div>
        <div class="all-card-metric">Live app &middot; 2 languages &middot; 30-day structured program &middot; PRD and UX brief published</div>
        <div style="display:flex;gap:1rem;margin-top:auto;padding-top:0.75rem;flex-wrap:wrap;">
          <a href="https://gentle-move-buddy.lovable.app/" target="_blank" class="all-card-link">View app &rarr;</a>
          <a href="#case-move-mitra-prd" class="all-card-link" style="color:var(--fg3);">View PRD &rarr;</a>
          <a href="#case-move-mitra-ux" class="all-card-link" style="color:var(--fg3);">View design brief &rarr;</a>
        </div>
      </div>

      <!-- Cipher -->
      <div class="all-card" data-stage="Prototype">
        <div style="display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;">
          <span class="pill pill-proto" style="align-self:flex-start;">Prototype</span>
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;">Microsoft Agents League Hackathon</span>
        </div>
        <h3 class="all-card-title">Cipher</h3>
        <p class="all-card-desc">M&amp;A integration teams spend the first 90 days manually reviewing documents across two disconnected company tenants. Cipher does it in seconds.</p>
        <div class="proto-pair" style="margin:0.75rem 0;">
          <div class="proto-box">
            <div class="proto-box-title">Cross-tenant reasoning</div>
            <div class="proto-box-desc">Two independent Microsoft Foundry projects across separate Azure tenants. Queries both companies simultaneously.</div>
          </div>
          <div class="proto-box">
            <div class="proto-box-title">M&amp;A risk synthesis</div>
            <div class="proto-box-desc">Vendor overlap, people gaps, and 90-day financial risk — cited, grounded, cross-company.</div>
          </div>
        </div>
        <div class="all-card-metric">2 agents &middot; 2 Azure tenants &middot; 3 risk scenarios &middot; Microsoft Agents League Hackathon</div>
        <div style="display:flex;gap:1rem;margin-top:auto;padding-top:0.75rem;flex-wrap:wrap;">
          <a href="https://github.com/pallavising48/cipher-m2a-integration" target="_blank" class="all-card-link">View on GitHub &rarr;</a>
          <a href="https://youtu.be/KA9bT1WTiGs" target="_blank" class="all-card-link" style="color:var(--fg3);">Watch demo &rarr;</a>
        </div>
      </div>


    </div>
  </div>
</section>

<!-- SKILLS MATRIX -->
<section class="section">
  <div class="section-inner">
    <div class="section-head">
      <h2 class="section-title">What each piece of work showcases</h2>
    </div>
    <div class="matrix-wrap">
      <div class="matrix">
        <div class="matrix-cell label matrix-head">Skill</div>
        <div class="matrix-cell matrix-head" style="text-align:center;">InsightLoop</div>
        <div class="matrix-cell matrix-head" style="text-align:center;">Snaccly</div>
        <div class="matrix-cell matrix-head" style="text-align:center;">Cipher</div>
        <div class="matrix-cell matrix-head" style="text-align:center;">Move Mitra</div>
        <div class="matrix-cell matrix-head" style="text-align:center;">Cust. Analytics</div>
        <div class="matrix-cell matrix-head" style="text-align:center;">Insta Curated</div>
        <div class="matrix-cell matrix-head" style="text-align:center;">Client Work</div>
        <div class="matrix-cell matrix-head" style="text-align:center;">Capgemini</div>
        <div class="matrix-cell matrix-head" style="text-align:center;">Accenture</div>

        <div class="matrix-row-label">Build without engineering</div>
        <div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div>

        <div class="matrix-row-label">Scoping and feature decisions</div>
        <div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div>

        <div class="matrix-row-label">AI evals and quality</div>
        <div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div>

        <div class="matrix-row-label">Working with data directly</div>
        <div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div>

        <div class="matrix-row-label">Iteration after launch</div>
        <div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div>

        <div class="matrix-row-label">Client and stakeholder delivery</div>
        <div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div>

        <div class="matrix-row-label">Cross-functional leadership</div>
        <div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div>

        <div class="matrix-row-label">Enterprise platform depth</div>
        <div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-off">&#9675;</div><div class="matrix-dot dot-on">&#9679;</div><div class="matrix-dot dot-on">&#9679;</div>
      </div>
    </div>
    <p class="matrix-legend">&#9679; strong evidence &nbsp;&nbsp; &#9675; not the focus</p>
  </div>
</section>

<!-- ===== CASE STUDIES ===== -->

<!-- Case Study: Snaccly -->
<section class="case-study" id="case-snaccly">
  <div class="case-inner">
    <a class="case-back" href="#best">&larr; Back to best work</a>
    <span class="case-tag">Founder &middot; Consumer AI &middot; B2C &middot; Beyond MVP</span>
    <h2 class="case-title">Snaccly: Building a Gamified AI Literacy Platform from Zero</h2>
    <div class="case-meta">
      <span><strong>Role:</strong> Founder and Product Lead</span>
      <span><strong>Stack:</strong> Vanilla JS &middot; Astro &middot; Supabase &middot; Vercel &middot; Web Speech API</span>
      <span><strong>Status:</strong> MVP v1 Live &mdash; app.snacclyai.com</span>
    </div>
    <div style="margin:1.75rem 0 0.5rem;">
      <div style="font-size:0.6875rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:0.75rem;">At a Glance</div>
      <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));background:var(--accent);border-radius:12px;overflow:hidden;">
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">100</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Bytes in the library</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">6</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Learning tracks</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">60s</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Target per Byte</span>
        </div>
        <div style="padding:1.5rem 1.25rem;display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">50+</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Customer interviews</span>
        </div>
      </div>
    </div>
    <div class="case-body">
      <h2>The Problem</h2>
      <p>Non-technical professionals — marketers, consultants, PMs, HR, analysts — hear AI terms in meetings and don't know what they mean. They're capable and busy. They know they're behind and they're not looking for a lecture. Existing options were either too technical (courses, papers) or too shallow (Twitter threads and listicles). Nobody was building first-hand, skill-based AI literacy in a format that actually fit into a commute.</p>

      <h2>Who It's For</h2>
      <p>Validated through 50+ customer interviews and Reddit sentiment analysis across communities with 500K+ daily visitors, the product serves three personas:</p>
      <ul>
        <li><strong>The curious worker:</strong> Marketers, PMs, consultants, HR, sales — anyone who hears AI terms in meetings and wants to follow along confidently.</li>
        <li><strong>The early-career professional:</strong> New grads and students who need AI literacy to be competitive in their field.</li>
        <li><strong>The manager:</strong> Team leads who need enough vocabulary to evaluate AI proposals without a technical co-pilot.</li>
      </ul>
      <p>Snaccly is not a coding course. It builds vocabulary and intuition, not implementation skills. The tone stays plain English throughout.</p>

      <h2>The Core Mechanic: The Byte</h2>
      <p>Every lesson is a Byte — a four-beat sequence designed to fit inside sixty seconds. The progression forces understanding before retrieval:</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0 1.5rem;">
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">01 &mdash; Definition</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">One plain-English sentence. No jargon, no hedging. A 60-second countdown timer runs during the definition screen.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">02 &mdash; Analogy</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">"In everyday life..." — one sentence mapping the concept to something familiar. Makes abstract terms stick.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">03 &mdash; Common Mistake</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">One sentence on how people misuse or misunderstand the concept. Addresses the actual confusion, not a theoretical one.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">04 &mdash; Quiz</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">Two scenario questions, 60 seconds each. Scored server-side. Options shuffled on display. Correct answer is always position [0] in the raw data.</div>
        </div>
      </div>

      <h2>The 6 Learning Tracks</h2>
      <p>100 Bytes across 6 tracks. Concepts within each track are sequenced so every term used in a definition was taught in an earlier Byte — prerequisite ordering built into the content architecture:</p>
      <ul>
        <li><strong>AI Basics (23 Bytes):</strong> The foundation everyone needs</li>
        <li><strong>Working With AI (15 Bytes):</strong> Get dramatically better results</li>
        <li><strong>Generative AI (7 Bytes):</strong> Create with AI: images, video, code</li>
        <li><strong>AI Tools (6 Bytes):</strong> What each tool is actually for</li>
        <li><strong>AI Technology (31 Bytes):</strong> How AI works under the surface</li>
        <li><strong>AI at Work (8 Bytes):</strong> Speak credibly about AI in any context</li>
      </ul>

      <h2>Gamification Layer</h2>
      <p>Designed using consumer psychology principles, with A/B experimentation on retention mechanisms:</p>
      <ul>
        <li><strong>XP:</strong> Awarded per quiz question answered. Visible in the Profile tab.</li>
        <li><strong>Streaks:</strong> Day-streak tracked via cloud sync. Pushed as the primary retention hook.</li>
        <li><strong>Hearts:</strong> 5 lives, lost on wrong answers. Recharge over time. Creates stakes without being punishing.</li>
        <li><strong>Challenge Mode:</strong> Duel vs. AI bot, 10 seconds per question. Turns passive learning into active competition.</li>
        <li><strong>Badges:</strong> Awarded for track completion and milestones. Shareable social signal.</li>
        <li><strong>Confetti:</strong> Canvas animation fires on correct answers. Immediate positive reinforcement.</li>
      </ul>

      <h2>What's Live (MVP v1)</h2>
      <ul>
        <li>Learn Map with 6 tracks and progress bars</li>
        <li>Byte Cards: definition + analogy + common mistake, 60s timer</li>
        <li>Quiz: 2 questions per Byte, server-side scoring, alarm animation on timeout</li>
        <li>Audio narration via Web Speech API, with persistent sound toggle</li>
        <li>Challenge Mode: duel vs AI bot, 10s per question</li>
        <li>Profile + badges: XP, streak, hearts, track completion</li>
        <li>Term lookup (FAB): floating search button opens bottom sheet, logs missed terms</li>
        <li>Cloud sync: progress, XP, streaks via Supabase auth</li>
        <li>Dark mode toggle, opt-in, persisted to localStorage</li>
        <li>Astro marketing site at snacclyai.com (dark theme, server-rendered for SEO)</li>
      </ul>

      <h2>Tech Stack</h2>
      <p>No build step for the app — JS and CSS are served directly, cache-busted via <code>?v=N</code> query strings. All content lives in a single <code>bytes.json</code> file compiled at build time by a Python script. Quiz scoring never touches the browser. AI search never generates at runtime — a term not in the library returns a miss and gets logged.</p>
      <ul>
        <li><strong>App:</strong> Vanilla JS (no framework, no build step)</li>
        <li><strong>Marketing site:</strong> Astro, server-rendered</li>
        <li><strong>Backend / Auth:</strong> Supabase</li>
        <li><strong>Hosting:</strong> Vercel</li>
        <li><strong>Text-to-speech:</strong> Web Speech API</li>
        <li><strong>Content pipeline:</strong> Python build script</li>
      </ul>

      <h2>Business Model</h2>
      <ul>
        <li><strong>Free:</strong> Track 1 (AI Basics) in full, Track 2 preview (first 3 Bytes), term lookup, limited challenge mode</li>
        <li><strong>Pro ($8/mo):</strong> All 6 tracks, full challenge mode, cloud sync, priority access to new tracks</li>
        <li><strong>Team ($6/user/mo, min 5 seats):</strong> Everything in Pro + manager dashboard (Phase 2) + team fluency reports</li>
      </ul>
      <p>Acquisition loops: SEO via public dictionary (one page per concept), shareable fluency check result card, search miss logging as content queue and email capture.</p>

      <h2>What's Next</h2>
      <p>Phase 2 ships the full website dictionary (one server-rendered page per concept, structured data for SEO), the shareable Fluency Check (10 questions, OG card, email capture), and the Pro paywall via Stripe. The north star for the paywall gate: retention data must show the product has earned monetization before it asks for it.</p>

      <div style="margin-top:2rem;padding-top:1.5rem;border-top:1px solid var(--border);display:flex;gap:1rem;flex-wrap:wrap;">
        <a href="https://app.snacclyai.com/" target="_blank" class="btn-primary" style="display:inline-block;background:var(--accent);color:#fff;padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;">Try the app &rarr;</a>
        <a href="https://snacclyai.com" target="_blank" style="display:inline-block;color:var(--accent);padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;border:1px solid var(--accent);">Visit marketing site &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- Case Study: Accenture Payroll -->
<section class="case-study" id="case-payroll">
  <div class="case-inner">
    <a class="case-back" href="#best">&larr; Back to best work</a>
    <span class="case-tag">Accenture &middot; SAP &middot; Workday</span>
    <h2 class="case-title">Safeguarded $8M in Payroll Operations for 100K Employees Across 3 Nordic Countries</h2>
    <div class="case-meta">
      <span><strong>Role:</strong> Application Development Analyst</span>
      <span><strong>Stack:</strong> SAP HCM, Workday, API Gateway</span>
      <span><strong>Scope:</strong> Sweden, Norway, Denmark</span>
    </div>
    <div style="margin:1.75rem 0 0.5rem;">
      <div style="font-size:0.6875rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:0.75rem;">Impact at a Glance</div>
      <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));background:var(--accent);border-radius:12px;overflow:hidden;">
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">$8M</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Payroll Safeguarded</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">100K</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Employees Protected</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">0</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Payroll Failures</span>
        </div>
        <div style="padding:1.5rem 1.25rem;display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">3</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Nordic Countries</span>
        </div>
      </div>
    </div>
    <div class="case-body">
      <h2>The Problem</h2>
      <p>A SAP HCM to Workday integration was generating duplicate payroll postings across Sweden, Norway, and Denmark, putting $8M in payroll for 100,000 employees at financial and compliance risk. Engineering had spent months in the codebase looking for a logic flaw. There wasn't one.</p>

      <h2>The Root-Cause Breakthrough</h2>
      <p>I pivoted the investigation away from code and manually audited the SAP batch job execution rules, finding a legacy scheduling conflict buried in the initial migration config:</p>
      <ul>
        <li><strong>Job A (Standard):</strong> Set to run on the last day of the month.</li>
        <li><strong>Job B (Legacy/Redundant):</strong> Hardcoded by a previous engineer to run on the 31st.</li>
      </ul>
      <p>On months with 31 days, both jobs fired simultaneously. Since each payload was individually valid, the system processed both, creating silent cross-border duplicate postings. A 31-day race condition hiding in plain sight.</p>

      <h2>The Remediation</h2>
      <p><strong>Immediate fix.</strong> Deprecated the orphan batch job and standardised all payroll syncs to a single cron schedule bound to dynamic month-end parameters.</p>
      <p><strong>Architectural guardrails.</strong> Introduced idempotency validation at the API gateway layer (duplicate payloads rejected via unique transaction hash) and a system-level concurrency lockout so overlapping sync requests are blocked until the active process terminates.</p>
      <p><strong>Operational governance.</strong> Initiated a lifecycle review of all automated pipelines to locate and remove orphan schedules. Built monitoring dashboards that alert on data volume spikes of more than 15% during any execution window.</p>

      <h2>Stakeholder Leadership</h2>
      <p>Managed four groups simultaneously: Engineering (translated business risk into technical requirements), Finance and Payroll Executives (abstracted system logs into operational risk timelines), Regional HR Leaders across 3 countries (communication loops on localised impacts), and Legal and Compliance (GDPR adherence and multi-jurisdictional payroll regulation throughout).</p>

      <div style="margin-top:1.5rem;padding-top:1.5rem;border-top:1px solid var(--border2);">
        <a href="https://app.notion.com/p/Safeguarded-8M-in-payroll-operations-for-100K-employees-across-3-Nordic-countries-3dd501561dd280398712df349ed101c9?source=copy_link" target="_blank" style="font-size:0.875rem;font-weight:600;color:var(--fg3);">View full case study &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- Case Study: Capgemini -->
<section class="case-study" id="case-capgemini">
  <div class="case-inner">
    <a class="case-back" href="#best">&larr; Back to best work</a>
    <span class="case-tag">Capgemini &middot; Enterprise AI Automation</span>
    <h2 class="case-title">Building an Enterprise AI Program That Reached 20+ Delivery Teams</h2>
    <div class="case-meta">
      <span><strong>Role:</strong> Technical Product Manager</span>
      <span><strong>Stack:</strong> Python, ServiceNow APIs, SAP SolMan, Airtable, SQL, Power BI, NLP tooling</span>
      <span><strong>Type:</strong> Internal AI Program · Enterprise Delivery</span>
    </div>
    <div style="margin:1.75rem 0 0.5rem;">
      <div style="font-size:0.6875rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:0.75rem;">Impact at a Glance</div>
      <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));background:var(--accent);border-radius:12px;overflow:hidden;">
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">20+</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Delivery Teams Reached</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">6</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Use Cases Prioritized and Built</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">$990K</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Penalty Risk Eliminated</span>
        </div>
        <div style="padding:1.5rem 1.25rem;display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">80%</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">SLA Validation Cycle Reduction</span>
        </div>
      </div>
    </div>
    <div class="case-body">
      <h2>The Context</h2>
      <p>I was embedded in enterprise service delivery at Capgemini, managing SLA frameworks and contract performance for Fortune 500 clients. A single missed SLA could trigger hundreds of thousands in service credit penalties. The stakes were real.</p>
      <p>Nobody asked me to fix the underlying problem. But I could see the pattern clearly: 18 years of institutional contract knowledge sitting in people's heads, and the same manual work repeated from scratch on every engagement.</p>

      <h2>The Investigation</h2>
      <p>Before pitching anything, I interviewed senior team members across functions and catalogued every manual, repeatable task I could find:</p>
      <ul>
        <li>Contract intake and SLA categorization done fresh every engagement</li>
        <li>SLA methodology documents rebuilt from scratch each time</li>
        <li>Simulation reports nobody had thought to build before I invented them on my second project</li>
        <li>Scorecards generated manually by two FTEs working outside 9 to 5 hours across India and the US</li>
        <li>Test case generation taking 3 to 4 weeks per engagement with two people</li>
        <li>Daily dashboard reports requiring overnight coordination between offshore and onshore teams</li>
      </ul>
      <p>Six categories. All manual. All repeatable. All automatable. I brought it to an org-wide GenAI meeting and framed it as a risk reduction and velocity program, not a technology experiment. The mandate landed.</p>

      <h2>The Build: 6 Use Cases</h2>
      <p>Piloted use cases 1 and 3 with my own team first, then scaled simultaneously across 20+ towers with customized versions per sub-tower.</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.5rem 0;">
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">01</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">Contract Analysis and Intake</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Automated extraction of stakeholder contacts, timelines, and SLA categorization from contract documents. Trained on 18 years of contract data. Before: manual read-through of 40 to 60 SLAs per engagement. After: structured intake with human review on exceptions only.</p>
        </div>
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">02</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">Simulation Reports</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Auto-generated SLA performance simulations using contractual SLAs and live client data. When I first built these manually on my second project, stakeholder sign-off on KPIs accelerated by 67% (3 months to 1 month). Automation made that repeatable at zero marginal effort.</p>
        </div>
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">03</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">SLA Methodology Document Draft</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Generated from discussion data and contract inputs. Structured first draft covering SLA definitions, measurement standards, negotiated exceptions, and penalty clauses, for human review before client delivery. Before: 1 month, 2 to 3 FTEs. After: 1 week.</p>
        </div>
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">04</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">SLA Scorecard</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Weekly and monthly SLA performance reporting, previously compiled manually. After automation: generated and reviewed rather than built from scratch. Before: 2 weeks per cycle. After: 2 to 3 days with human review.</p>
        </div>
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">05</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">SLA Test Case Generation</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Auto-generated test cases based on SLA type and contractual inputs. One of the highest-volume time sinks in the delivery cycle. Before: 3 to 4 weeks per engagement, 2 people. After: 3 to 4 days.</p>
        </div>
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">06</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">Daily Operational Dashboard</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Automated daily reporting that previously required two FTEs working outside business hours across India and the US. Before: 2 FTEs, 2 hours daily, overnight coordination. After: 1 FTE, 30 minutes, no overnight dependency.</p>
        </div>
      </div>
      <div style="text-align:center;margin:-0.5rem 0 1rem;">
        <a href="https://app.notion.com/p/ENTERPRISE-AI-AUTOMATION-CAPGEMINI-3e5501561dd280198b91fe3469b23fc4?source=copy_link" target="_blank" style="font-size:0.875rem;font-weight:600;color:var(--fg3);">View full case study &rarr;</a>
      </div>

      <h2>The Outcome</h2>
      <p style="font-size:1rem;font-weight:600;color:var(--accent);margin-bottom:0.75rem;">20+ teams adopted. $990K penalty risk eliminated. SLA validation cut by 80%.</p>
      <ul>
        <li>Major incident notification latency reduced from hours to approximately 2 minutes</li>
        <li>SLA methodology document turnaround cut by 75% (1 month to 1 week)</li>
        <li>Onboarding reporting turnaround reduced by 87% (1 to 3 months to 2 weeks)</li>
        <li>Stakeholder sign-off accelerated by 67% (3 months to 1 month)</li>
      </ul>

      <h2>What I Learned</h2>
      <p>The hardest part was not the build. It was convincing people that the pattern I had spotted was real and worth acting on. Eighteen years of institutional knowledge sitting in people's heads does not feel like a problem until someone maps it. Once I mapped it, the case was obvious. The skill was knowing to look, knowing how to ask, and knowing how to frame what I found so that the people who could act on it would.</p>
    </div>
  </div>
</section>

<!-- Case Study: InsightLoop -->
<section class="case-study" id="case-insightloop">
  <div class="case-inner">
    <a class="case-back" href="#best">&larr; Back to best work</a>
    <span class="case-tag">Founder &middot; Enterprise AI Agent &middot; Evals</span>
    <h2 class="case-title">InsightLoop: From Customer Discovery to Live Enterprise AI Agent</h2>
    <div class="case-meta">
      <span><strong>Role:</strong> Founder and Product Lead</span>
      <span><strong>Stack:</strong> MuleRun &middot; Claude API &middot; Prompt Engineering</span>
      <span><strong>Stage:</strong> MVP Shipped &mdash; mulerun.com</span>
    </div>
    <div style="margin:1.75rem 0 0.5rem;">
      <div style="font-size:0.6875rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:0.75rem;">Impact at a Glance</div>
      <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));background:var(--accent);border-radius:12px;overflow:hidden;">
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">96%</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Cohort adoption rate</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">27</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">DBA students validated</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">5h&rarr;&lt;1h</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Weekly research time</span>
        </div>
        <div style="padding:1.5rem 1.25rem;display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">1 day</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">From idea to live on MuleRun</span>
        </div>
      </div>
    </div>
    <div class="case-body">
      <h2>The Problem</h2>
      <p>Enterprise knowledge workers spend 30 to 40 percent of their time finding and synthesizing information before they can act on it. Research workflows are fragmented across departments, stateless across sessions, and siloed across teams. A strategy team's competitive analysis never reaches the product team. An analyst's findings disappear when they move to a new role. There is no institutional research memory.</p>
      <p>The problem is not that existing tools are bad. It is that they each solve a different, adjacent problem:</p>
      <ul>
        <li><strong>Hebbia:</strong> Deep document analysis — but $10K per seat, finance and legal only.</li>
        <li><strong>Glean:</strong> Finding information already inside your company — but no synthesis of new external research.</li>
        <li><strong>Perplexity Enterprise:</strong> Real-time web search with cited answers — but no multi-step workflows or session memory.</li>
        <li><strong>AlphaSense:</strong> Market intelligence for finance — but no use for Product, HR, Legal, or R&amp;D.</li>
      </ul>

      <h2>What I Built</h2>
      <p>InsightLoop is a cross-functional AI research agent running structured, cited research workflows for any enterprise team, in any domain, for any audience. Built and published on MuleRun's Knowledge Network in a single day. A 4-step workflow that turns any research question into a sourced executive brief:</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0 1.5rem;">
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">01 &mdash; Decompose</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">Breaks any research question into 5 focused, non-overlapping sub-questions with rationale and coverage logic.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">02 &mdash; Gather</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">2&ndash;3 credible sources per sub-question: T1/T2/T3 tier, date, URL, key data point. 10&ndash;15 sources per session.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">03 &mdash; Synthesize</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">3&ndash;5 cross-cutting insights connecting findings across sub-questions. Flags contradictions without being prompted.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">04 &mdash; Brief</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">Audience-specific executive brief under 600 words. Strategic implications, key risks, 5 next research topics.</div>
        </div>
      </div>

      <h2>Key Product Decisions</h2>
      <ul>
        <li><strong>Customer discovery before building.</strong> Before writing a single prompt, I called a senior at T-Mobile working on SpaceX satellite services and asked directly: is there a recurring, high-effort task your team does that an AI agent could solve? She described research fragmentation — findings that don't persist anywhere useful once the report is done. She confirmed the pain was real. That is customer discovery.</li>
        <li><strong>Task environment over Agent Builder.</strong> MuleRun's Agent Builder was in beta and unstable. I chose the proven Task environment. Reliability over architectural elegance for a prototype. Zero platform bugs across all test sessions.</li>
        <li><strong>Test InsightLoop on its own market first.</strong> If the agent researched the competitive landscape for AI research tools and produced accurate output, I would know whether the quality was real — because I already knew that market. It produced verified data from a16z, Bessemer, MIT, Menlo Ventures, and Gartner. Three statistics spot-checked at source URLs. All three confirmed accurate. Self-validating prototype.</li>
        <li><strong>Contradiction detection as core, not optional.</strong> Enterprise users don't trust AI tools that present all findings with equal authority. In Session 2 on HR burnout, the agent caught unprompted that PMC peer-reviewed research shows wellness apps have 40%+ attrition, while Wellhub CEO surveys show 82% positive ROI. It resolved the tension: CEOs measure satisfaction, not sustained burnout reduction. A measurement gap, not a contradiction. That is senior analyst behavior — without guidance.</li>
        <li><strong>Prompt engineering as product design.</strong> After three test sessions I audited the InsightLoop prompt and found 8 specific break points. Three fixed immediately. Most critical: T1/T2/T3 source tier labels were AI-inferred based on source appearance, not verified against any domain standard. A blog called "Coffee Industry Trends 2026" was labelled T1. The corrected prompt adds explicit domain rules, a verification step, and an under-source flag. These are product decisions, not engineering ones.</li>
      </ul>

      <h2>What Was Validated (3 Eval Sessions)</h2>
      <ul>
        <li><strong>Session 1 — AI Research Tools Market (PM audience):</strong> 15 sources, T1/T2 dominant (a16z, Bessemer, MIT, Gartner). 3 statistics spot-checked. All verified. Contradiction detected unprompted. Verdict: <strong>Pass.</strong></li>
        <li><strong>Session 2 — Knowledge Worker Burnout (CPO audience):</strong> 15 sources including Gallup, Harvard, Nature Human Behavior. Contradiction caught: wellness apps show 40%+ attrition in PMC data vs. 82% positive ROI in CEO surveys. Resolved analytically. Brief: 578 words. Verdict: <strong>Pass.</strong></li>
        <li><strong>Session 3 — Seattle Cafe Success Indicators (cafe owner audience):</strong> 8 sources, 6 mislabeled. A trade blog labelled T1. A Medium article labelled T2. Root cause: tier inference fails when T1/T2 sources are scarce. This directly produced a Phase 2 requirement: domain whitelist for verified tier classification. Verdict: <strong>Partial fail — use case boundary documented.</strong></li>
      </ul>
      <p>Use case boundary: InsightLoop performs well on topics where T1/T2 institutional sources are abundant — enterprise, financial, regulatory, research-heavy domains. For hyper-local or niche consumer questions, users should apply additional verification.</p>

      <h2>What I Learned</h2>
      <ul>
        <li><strong>Prompt engineering is product design.</strong> The 8 break points in the InsightLoop prompt were not bugs in someone else's code. They were gaps in the product spec. Fixing them required the same thinking as writing a PRD: what should the system do in this edge case? Constraint setting, step gating, output format spec, failure handling — these are product decisions.</li>
        <li><strong>Know the difference between validated and hypothesis.</strong> The core workflow is validated. The tier classification system is partially fixed by prompt, not fully fixed by architecture. Cross-team memory and pricing require customer discovery. Any sharp interviewer will ask where the evidence ends and the assumption begins.</li>
        <li><strong>Testing where a product fails is more valuable than only testing where it succeeds.</strong> Session 3 was uncomfortable. But the Session 3 finding directly produced a Phase 2 engineering requirement.</li>
      </ul>

      <h2>Roadmap</h2>
      <ul>
        <li><strong>Phase 0&ndash;1 (Done, March 2026):</strong> 4-step workflow, source tiering, contradiction detection, proactive suggestions, published to MuleRun.</li>
        <li><strong>Phase 2 (Months 1&ndash;2):</strong> Customer discovery interviews first. Domain whitelist for enforced tier classification. Cross-session memory, SSO, team sharing — if discovery validates demand.</li>
        <li><strong>Phase 3 (Months 2&ndash;4):</strong> Internal document upload as T4 source tier. Topic watchlist with proactive alerts. SOC 2 audit start.</li>
        <li><strong>Phase 4 (Months 4&ndash;9):</strong> Enterprise tier, data residency, API access. Extended by SOC 2 observation period (6-month minimum) and enterprise sales cycles.</li>
      </ul>

      <div style="margin-top:2rem;padding-top:1.5rem;border-top:1px solid var(--border);display:flex;gap:1rem;flex-wrap:wrap;">
        <a href="https://mulerun.com/chat?template=1db82c25-152d-4527-9857-22c3a1720f6b" target="_blank" class="btn-primary" style="display:inline-block;background:var(--accent);color:#fff;padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;">Try the agent &rarr;</a>
        <a href="https://app.notion.com/p/InsightLoop-332501561dd280b8abf8e9f83f17bb4a" target="_blank" style="display:inline-block;color:var(--fg3);padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;border:1px solid var(--border);">Open full case study in Notion &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- Case Study: PID Floors -->
<section class="case-study" id="case-pid-floors">
  <div class="case-inner">
    <a class="case-back" href="#client">&larr; Back to client work</a>
    <span class="case-tag">Pro Bono &middot; AI Product Strategy</span>
    <h2 class="case-title">Driving $800K in Annual Value for a Luxury B2B Brand via AI Prototyping</h2>
    <div class="case-meta">
      <span><strong>Role:</strong> AI Product Strategy Advisor</span>
      <span><strong>Stack:</strong> Claude API, Lovable, Make.com, Airtable</span>
      <span><strong>Type:</strong> B2B Discovery Sprint</span>
    </div>
    <div style="margin:1.75rem 0 0.5rem;">
      <div style="font-size:0.6875rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:0.75rem;">Impact at a Glance</div>
      <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));background:var(--accent);border-radius:12px;overflow:hidden;">
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">$800K</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Annual Efficiency Run Rate</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">2</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Live Prototypes Built</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">30&ndash;360</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Day Roadmap Delivered</span>
        </div>
        <div style="padding:1.5rem 1.25rem;display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">4 hrs</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Total Build Time</span>
        </div>
      </div>
    </div>
    <div class="case-body">
      <h2>The Context</h2>
      <p>PID Floors is a high-end luxury flooring manufacturer with multiple showrooms, a global supply network, and custom warehousing. They compete on personalized service. Back-office friction was slowing response times on high-value architecture and design deals.</p>

      <h2>The Friction I Found</h2>
      <p>During discovery, I identified two major operational bottlenecks:</p>
      <ul>
        <li><strong>Catalog translation:</strong> Sales consultants manually matched 1,000+ custom SKUs to client briefs, creating lag and inconsistent results.</li>
        <li><strong>Inbound Pipeline Overhead:</strong> High volumes of complex trade emails (bids, material quotes, sample routing) congested shared back-office channels, stalling response velocity.</li>
      </ul>

      <h2>The Build: 2 Working Prototypes</h2>
      <p>Instead of writing a consulting report, I treated the business as my sandbox and built two live technical artifacts.</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.5rem 0;">
        <!-- Prototype 1 -->
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.5rem;display:flex;flex-direction:column;gap:0.75rem;">
          <div style="display:flex;align-items:center;gap:0.5rem;">
            <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;">Prototype 01</span>
          </div>
          <div style="font-family:'Fraunces',Georgia,serif;font-size:1.125rem;font-weight:500;color:var(--fg);line-height:1.3;">In-store Consultant Assistant</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Built a flooring recommendation platform using the Claude API. The app takes customer inputs (mood boards, regional factors, square footage, budget) and returns the best product matches with written reasoning.</p>
          <div style="display:flex;gap:1rem;margin-top:auto;padding-top:0.5rem;border-top:1px solid var(--border2);flex-wrap:wrap;">
            <a href="https://luxe-flooring-alchemy.lovable.app/" target="_blank" style="font-size:0.8125rem;font-weight:600;color:var(--accent);">View prototype &rarr;</a>
            <a href="https://app.notion.com/p/In-store-Consultant-Assistant-AI-Powered-Guided-Product-Selection-381501561dd2809d852fe41d0004c313?source=copy_link" target="_blank" style="font-size:0.8125rem;font-weight:600;color:var(--fg3);">Full case study &rarr;</a>
          </div>
        </div>
        <!-- Prototype 2 -->
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.5rem;display:flex;flex-direction:column;gap:0.75rem;">
          <div style="display:flex;align-items:center;gap:0.5rem;">
            <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;">Prototype 02</span>
          </div>
          <div style="font-family:'Fraunces',Georgia,serif;font-size:1.125rem;font-weight:500;color:var(--fg);line-height:1.3;">Inbox Intelligence</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Built a live automated workflow using Make.com, Gmail webhooks, and Airtable. Incoming trade emails are categorized by intent and urgency, logged to Airtable, and returned with a pre-drafted reply ready for human approval.</p>
          <div style="display:flex;gap:1rem;margin-top:auto;padding-top:0.5rem;border-top:1px solid var(--border2);flex-wrap:wrap;">
            <a href="https://us2.make.com/public/shared-scenario/xKol0aQ6EPQ/integration-gmail-http-json-airtable" target="_blank" style="font-size:0.8125rem;font-weight:600;color:var(--accent);">View workflow &rarr;</a>
            <a href="https://app.notion.com/p/Inbox-Intelligence-AI-Powered-Email-Triage-and-Routing-381501561dd28047b961ed6f58ea875f?source=copy_link" target="_blank" style="font-size:0.8125rem;font-weight:600;color:var(--fg3);">Full case study &rarr;</a>
          </div>
        </div>
      </div>

      <h2>Financial Modeling and Roadmap Impact</h2>
      <p>I embedded both prototypes into a 30 to 90 to 360 day product roadmap showing how the organization could move from internal tool adoption to data-mature system intelligence.</p>
      <p><strong>Data strategy foundations.</strong> Automating data capture via system APIs eliminates duplicate entry overhead across Microsoft Dynamics, HubSpot, and Airtable. Recoverable overhead that compounds as volume grows.</p>
      <p><strong>Projected value.</strong> Modeled across the full engagement scope, the roadmap projected $300K to $800K in annualized efficiency gains through faster sales velocity and reduced data entry overhead.</p>

      <h2>The Outcome</h2>
      <p style="font-size:1rem;font-weight:600;color:var(--accent);margin-bottom:0.75rem;">$300K to $800K annual efficiency run rate modelled across 30 to 360 days</p>
      <p>The engagement delivered two live prototypes, a 30 to 360 day product roadmap, and a financial model projecting $300K to $800K in annualized efficiency gains.</p>
      <p style="background:var(--accent);color:#fff;padding:1rem 1.25rem;border-radius:8px;font-weight:600;margin-top:1rem;">At the close of the engagement, I was offered the AI Implementation Strategist role at their NYC office.</p>

      <h2>What's Next</h2>
      <p>The prototypes are a foundation. The next layer of the roadmap covers:</p>
      <p><strong>Innovation Studio:</strong> live inventory integration so recommendations reflect actual stock availability, one-click CRM record creation from consultant notes, a customer-facing kiosk mode for self-exploration before meeting a rep, image-based mood board input for visual matching, and expansion to furniture and lighting verticals on the same engine.</p>
      <p><strong>Inbox Intelligence:</strong> Gmail draft auto-creation so reps review and send without leaving their inbox, daily summary digests pushed to WhatsApp or SMS, automatic task creation in Asana for high-priority follow-ups within 24 hours, and CRM sync to Dynamics 365 or HubSpot so high-value inquiries auto-create contact records.</p>
    </div>
  </div>
</section>

<!-- Case Study: Londr -->
<section class="case-study" id="case-londr">
  <div class="case-inner">
    <a class="case-back" href="#client">&larr; Back to client work</a>
    <span class="case-tag">Pro Bono &middot; Growth Product Strategy</span>
    <h2 class="case-title">Transforming a B2C Marketplace Supply-Side into a Zero-CAC Growth Engine</h2>
    <div class="case-meta">
      <span><strong>Role:</strong> Growth Product Strategy Advisor</span>
      <span><strong>Stack:</strong> Growth Loop Design, Financial Modelling, Market Segmentation, Unit Economics</span>
      <span><strong>Type:</strong> 52-Hour Strategy Sprint</span>
    </div>
    <div style="margin:1.75rem 0 0.5rem;">
      <div style="font-size:0.6875rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:0.75rem;">Impact at a Glance</div>
      <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));background:var(--accent);border-radius:12px;overflow:hidden;">
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">$0</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Projected CAC via Supply-Side Loop</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">3,300</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">US Market Zones Mapped</span>
        </div>
        <div style="padding:1.5rem 1.25rem;border-right:1px solid rgba(255,255,255,0.15);display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">$837K</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Projected ARR by Year 5</span>
        </div>
        <div style="padding:1.5rem 1.25rem;display:flex;flex-direction:column;gap:0.4rem;">
          <span style="font-family:'Fraunces',Georgia,serif;font-size:2.25rem;font-weight:600;color:#fff;line-height:1;">6</span>
          <span style="font-size:0.75rem;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.3;">Deliverables in 52 Hours</span>
        </div>
      </div>
    </div>
    <div class="case-body">
      <h2>The Context</h2>
      <p>Londr is a US-based on-demand laundry marketplace. Unit economics were healthy: 33 to 36% contribution margins per bag, a structural loss rate under 0.4%, and a confirmed customer spending $120 to $130 per month. The business model worked. The growth engine did not. The founder brought me in to diagnose what was holding the business back and build the architecture to fix it.</p>

      <h2>The Friction I Found</h2>
      <ul>
        <li><strong>Demand and supply imbalance.</strong> 10:1 washer-to-customer ratio. Supply was built without building demand.</li>
        <li><strong>No acquisition engine.</strong> No referral program, no SEO, no B2B pipeline, no segment targeting. One paused Google Ads campaign.</li>
        <li><strong>Volatile revenue model.</strong> 100% transactional B2C revenue. A licensing arm existed on paper with no activation plan.</li>
        <li><strong>Thin washer net pay.</strong> $13 to $23 net per bag after costs. Churn risk if washers felt the economics did not work for them.</li>
      </ul>

      <h2>What I Delivered</h2>
      <p>Six deliverables across the full growth surface in 52 hours.</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.5rem 0;">
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">01</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">Marketplace Health Diagnostic</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">As-is audit of unit economics and operational risk. Confirmed healthy margins and a 0.4% loss rate. Growth risk, not product risk, was the problem.</p>
        </div>
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">02</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">Customer Segmentation Report</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Identified dual-income urban professionals and B2B accounts (Airbnbs, hotels, studios) worth 5 to 6x individual customer value. Corrected geographic assumptions using real rental data across US metros.</p>
        </div>
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">03</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">Zero-CAC Supply-Side Growth Loop</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Designed a referral model that turns washers into the acquisition channel. Points-based leaderboard rewards washers for referred customers. Estimated CAC: ~$10 per customer acquired.</p>
        </div>
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">04</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">Customer Acquisition Strategy</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Multi-channel playbook: Google Ads relaunch, SEO location pages, B2B partnerships, subscription tiers, route-density discounts, and loyalty program.</p>
        </div>
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">05</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">Licensing Monetization Framework</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">3,300 US market zones mapped across 4 demographic tiers. 10-year pro forma projects $837K ARR by Year 5 at 155 cumulative zones. Key finding: licensee count is the highest-leverage variable, not fee level.</p>
        </div>
        <div style="background:var(--white);border:1.5px solid var(--border);border-radius:12px;padding:1.375rem;display:flex;flex-direction:column;gap:0.5rem;">
          <span style="font-size:0.65rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--accent);background:rgba(31,95,91,0.08);padding:0.2rem 0.5rem;border-radius:4px;align-self:flex-start;">06</span>
          <div style="font-weight:600;font-size:0.9375rem;color:var(--fg);">Washer Growth Playbook</div>
          <p style="font-size:0.875rem;line-height:1.6;color:var(--fg2);margin:0;">Tactical field guide for washers to build their own customer base across 5 channels. Designed for inclusion in the washer onboarding kit.</p>
        </div>
      </div>
      <div style="text-align:center;margin:-0.5rem 0 1rem;">
        <a href="https://app.notion.com/p/Transforming-a-B2C-Marketplace-Supply-Side-into-a-Zero-CAC-Growth-Engine-3de501561dd280a28b82fdc3ba5f5a41?source=copy_link" target="_blank" style="font-size:0.875rem;font-weight:600;color:var(--fg3);">View full case study &rarr;</a>
      </div>

      <h2>The Outcome</h2>
      <p style="font-size:1rem;font-weight:600;color:var(--accent);margin-bottom:0.75rem;">$837K projected ARR by Year 5 &middot; 6 deliverables &middot; Head of Product &amp; Strategy role offered</p>
      <p>The sprint delivered a complete growth architecture across six deliverables. The licensing model projects $27K ARR in Year 1 scaling to $837K by Year 5. The zero-CAC referral loop provides a path to closing the demand gap without paid acquisition spend.</p>
      <p style="background:var(--accent);color:#fff;padding:1rem 1.25rem;border-radius:8px;font-weight:600;margin-top:1rem;">At the close of the engagement, the founder offered me the Head of Product and Strategy role.</p>

      <h2>What's Next</h2>
      <ul>
        <li>Activate the washer-driven referral program to begin closing the demand gap</li>
        <li>Relaunch Google Ads with segment-informed targeting and zip-code-level budget allocation</li>
        <li>Build the B2B pipeline starting with Airbnb hosts and fitness studios</li>
        <li>Formalize the licensing activation plan and identify the first 5 target market zones</li>
        <li>Build the data layer to replace manual customer profiling with automated segment identification</li>
      </ul>
    </div>
  </div>
</section>

<!-- Case Study: Instagram Curated -->
<section class="case-study" id="case-instagram-curated">
  <div class="case-inner">
    <a class="case-back" href="#all">&larr; Back to projects</a>
    <span class="case-tag">Consumer Product Concept &middot; Feature Pitch &middot; Prototype Built</span>
    <h2 class="case-title">Instagram Curated: A Feature Pitch for a More Intentional Following Feed</h2>
    <div class="case-meta">
      <span><strong>Type:</strong> Solo Product Concept</span>
      <span><strong>Deliverables:</strong> PRD, Competitive Analysis, Prototype, Demo Video</span>
      <span><strong>Stack:</strong> Replit</span>
    </div>
    <div class="case-body">
      <h2>The Problem</h2>
      <p>Instagram's Following feed shows everything from everyone you follow, in an order you didn't choose. For users who follow a mix of friends, creators, news, and brands, the feed becomes noise. There's no way to say "I want cooking content right now" or "I only want to see friends this morning." Content control is all-or-nothing: follow or unfollow, nothing in between.</p>

      <h2>The Idea</h2>
      <p>Instagram Curated adds a lightweight content filtering layer to the existing Following feed. Users tag accounts they follow with categories — Food, Travel, News, Friends, Work — and choose which categories to surface at any given time. A time-of-day toggle lets them set a default mode: quiet mornings, social evenings. No new algorithm. No new feed. Just intentional control over what's already there.</p>

      <h2>What I Built</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0 1.5rem;">
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">01 &mdash; PRD</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">Full product requirements document: problem framing, user stories, acceptance criteria, edge cases, and success metrics. Written for a real internal pitch.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">02 &mdash; Competitive Analysis</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">Mapped how Twitter Lists, TikTok filters, LinkedIn feed controls, and Pinterest boards handle content curation. Identified the whitespace Instagram occupies.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">03 &mdash; Working Prototype</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">Interactive mobile prototype built on Replit. Shows the full flow: category tagging, filter activation, time-of-day toggle, and curated feed preview.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">04 &mdash; Monetization Strategy</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">Explored where Curated creates advertiser value: verified category reach, intent-based placement, and creator analytics for niche audience segments.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;grid-column:1/-1;">
          <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">05 &mdash; Case Study</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">End-to-end writeup: product thinking, design decisions, trade-offs, and what I'd validate first if this were a real 0-to-1 project inside Meta.</div>
        </div>
      </div>

      <h2>Why This Matters as a Portfolio Piece</h2>
      <p>This project shows PM work without a team, a budget, or a company behind it. The insight came from being a real user who wanted something that didn't exist. The deliverables — PRD, competitive analysis, prototype, monetization thinking — are the same artifacts a PM would produce for an internal pitch. The goal wasn't to build for the sake of building. It was to think like a product person about a problem that affects hundreds of millions of users.</p>

      <div style="margin-top:2rem;padding-top:1.5rem;border-top:1px solid var(--border);display:flex;gap:1rem;flex-wrap:wrap;">
        <a href="https://mobile-prototype-builder.replit.app/" target="_blank" class="btn-primary" style="display:inline-block;background:var(--accent);color:#fff;padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;">View prototype &rarr;</a>
        <a href="https://youtube.com/shorts/m9Xhm1gYfKY" target="_blank" style="display:inline-block;color:var(--accent);padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;border:1px solid var(--accent);">Watch demo &rarr;</a>
        <a href="https://app.notion.com/p/Instagram-Curated-376501561dd2811b90def5c28b3d442a" target="_blank" style="display:inline-block;color:var(--fg3);padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;border:1px solid var(--border);">Open full case study in Notion &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- Case Study: Move Mitra PRD -->
<section class="case-study" id="case-move-mitra-prd">
  <div class="case-inner">
    <a class="case-back" href="#all">&larr; Back to projects</a>
    <span class="case-tag">Product Requirements Document &middot; Consumer Health &middot; Bilingual</span>
    <h2 class="case-title">Move Mitra PRD: Building for a User Nobody Else Is Building For</h2>
    <div class="case-meta">
      <span><strong>Product:</strong> Move Mitra</span>
      <span><strong>Stack:</strong> Lovable &middot; Claude API</span>
      <span><strong>Type:</strong> Solo 0-to-1 Build</span>
    </div>
    <div class="case-body">
      <h2>The Problem</h2>
      <p>Women 40+ with knee pain aren't held back by lack of knowledge. They're held back by fear. Fear of making it worse. Fear of looking stupid in a gym. Fear that movement at their age means injury. Every existing fitness app assumes the user wants to push harder. This one assumes the user is scared — and starts there.</p>
      <p>8 discovery interviews before a line of code was written. The finding that changed the design direction: <em>daughters are the gatekeepers</em>. Women in this age group don't discover apps themselves — their daughters find them. The product had to earn the daughter's trust first.</p>

      <h2>Key Discovery Findings</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0 1.5rem;">
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-weight:700;font-size:0.875rem;color:var(--fg);margin-bottom:0.4rem;">Fear, not knowledge</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">Interviewees knew what they should do. They didn't do it because they were afraid to start. The app needed to lower anxiety, not just lower barriers.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-weight:700;font-size:0.875rem;color:var(--fg);margin-bottom:0.4rem;">Hindi is non-negotiable</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">For this demographic, English-only UI signals "not for me." Hindi isn't a nice-to-have. It's the trust signal that gets someone to open the app on day two.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-weight:700;font-size:0.875rem;color:var(--fg);margin-bottom:0.4rem;">The gym is not viable</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">Every exercise had to work at home, without equipment. Gym imagery anywhere in the app was a disqualifier — it signals a world they don't belong to.</div>
        </div>
        <div style="background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.25rem;">
          <div style="font-weight:700;font-size:0.875rem;color:var(--fg);margin-bottom:0.4rem;">Daughters as decision-makers</div>
          <div style="font-size:0.875rem;color:var(--fg2);line-height:1.5;">Daughters find, evaluate, and install health apps for their mothers. The product pitch has two audiences: the daughter's logic and the mother's comfort.</div>
        </div>
      </div>

      <h2>The 30-Day Program</h2>
      <p>The program is structured to build confidence before it builds strength. Each week has a single focus — one thing to walk away with:</p>
      <ul>
        <li><strong>Week 1 — Feel Safe:</strong> Micro-movements only. No pain, no strain. The goal is a single day of "that wasn't scary."</li>
        <li><strong>Week 2 — Build Strength:</strong> Gentle resistance. Exercises add resistance only once pain check-ins trend positive.</li>
        <li><strong>Week 3 — Move Freely:</strong> Range of motion work. More complex movement patterns introduced gradually.</li>
        <li><strong>Week 4 — Walk Confidently:</strong> Full sequences. By week four, the user has a daily routine they own.</li>
      </ul>

      <h2>Core Features</h2>
      <ul>
        <li><strong>Bilingual toggle:</strong> Switch between English and Hindi mid-session. Native copy, not auto-translated text.</li>
        <li><strong>Daily pain check-in:</strong> 0–10 scale before each session. If pain is above threshold, the app suggests a lighter session — never overrides the user.</li>
        <li><strong>Safe Mode:</strong> A one-tap override that pauses the program and shows only rest + gentle stretch options. User is always in control.</li>
        <li><strong>Micro-education clips:</strong> Short, calm explanations of why each exercise helps the knee. Builds trust through knowledge, not jargon.</li>
      </ul>

      <h2>Success Metrics</h2>
      <p>The north star metric is Day 7 retention. If someone completes one full week, they're likely to complete the program. Supporting metrics: pain trend improvement (tracked via daily check-ins), language preference adoption (Hindi vs. English ratio), and Safe Mode usage rate as a signal of user anxiety level.</p>

      <div style="margin-top:2rem;padding-top:1.5rem;border-top:1px solid var(--border);display:flex;gap:1rem;flex-wrap:wrap;">
        <a href="https://gentle-move-buddy.lovable.app/" target="_blank" class="btn-primary" style="display:inline-block;background:var(--accent);color:#fff;padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;">View live app &rarr;</a>
        <a href="#case-move-mitra-ux" style="display:inline-block;color:var(--accent);padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;border:1px solid var(--accent);">Read UX design brief &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- Case Study: Move Mitra UX Design Brief -->
<section class="case-study" id="case-move-mitra-ux">
  <div class="case-inner">
    <a class="case-back" href="#all">&larr; Back to projects</a>
    <span class="case-tag">UX Design Brief &middot; Consumer Health &middot; Psychological Safety</span>
    <h2 class="case-title">Move Mitra UX Brief: Designing to Reduce Anxiety Before Asking for Effort</h2>
    <div class="case-meta">
      <span><strong>Product:</strong> Move Mitra</span>
      <span><strong>Stack:</strong> Lovable &middot; Claude API</span>
      <span><strong>Type:</strong> Solo 0-to-1 Build</span>
    </div>
    <div class="case-body">
      <h2>The Design Principle</h2>
      <p>Every design decision in Move Mitra starts from a single question: <em>does this reduce anxiety, or does it add to it?</em> Most fitness apps are aspirational — they show what users could become. Move Mitra shows what users can do today, safely. The visual language, the copy tone, the interaction patterns — all of it is calibrated to feel calm before it feels capable.</p>

      <h2>Bilingual by Design, Not by Translation</h2>
      <p>Hindi support is not a localization feature. It's a core product decision. Auto-translated text signals that you were an afterthought. Native Hindi copy — written for the register and idiom of the 40+ age group — signals that you were the primary user.</p>
      <p>The toggle is always visible. Switching language is instant and persistent. The app remembers which language the user chose and opens with it on the next session. This is a trust feature, not a language feature.</p>

      <h2>Onboarding: Three Screens, Under Two Minutes</h2>
      <p>No account required to start. No email gate. The first screen reads: <em>"Knee pain? Don't worry. Let's start moving safely together."</em> That's the entire value proposition in two sentences. The onboarding flow has three steps:</p>
      <ul>
        <li><strong>Screen 1:</strong> Language preference. English or Hindi. No other setup.</li>
        <li><strong>Screen 2:</strong> A single question — "Where is your pain today, from 0 to 10?" — to calibrate the first session.</li>
        <li><strong>Screen 3:</strong> Week 1, Day 1 of the program begins immediately.</li>
      </ul>
      <p>There is no "create your profile" step. No age, weight, or fitness level asked. The app adapts based on daily pain check-ins, not intake forms.</p>

      <h2>Safe Mode: Control That Feels Like Care</h2>
      <p>Safe Mode is a one-tap option that appears on every exercise screen. Tapping it pauses the current session and shows only gentle stretches and rest guidance. The key design decision: the app never activates Safe Mode automatically. The user has to choose it. This preserves agency — the feeling that you are in control of your body — which was the primary emotional barrier identified in research.</p>

      <h2>Visual Design Decisions</h2>
      <ul>
        <li><strong>Warm greens:</strong> Calming, not clinical. Avoid hospital or pharmaceutical blues.</li>
        <li><strong>Minimum 16px text:</strong> Non-negotiable for this age group. Comfort over density.</li>
        <li><strong>No gym imagery:</strong> Every illustration shows home settings — a chair, a mat, a floor. No dumbbells, no equipment, no aspirational bodies.</li>
        <li><strong>Heart icon brand mark:</strong> Signals care, not performance.</li>
        <li><strong>Physiotherapy-validated exercises:</strong> All movements reviewed for safety. This is noted in the app — it matters to the daughter doing the research.</li>
      </ul>

      <h2>What This Design Brief Proves</h2>
      <p>Every product decision has a research reason behind it. The bilingual toggle came from interviews. The onboarding length came from the finding that this age group abandons long setup flows. Safe Mode came from "I'm afraid to make it worse." The visual choices came from user feedback on what felt welcoming versus what felt like work.</p>
      <p>Design without research is decoration. This brief is the documentation of why every pixel exists.</p>

      <div style="margin-top:2rem;padding-top:1.5rem;border-top:1px solid var(--border);display:flex;gap:1rem;flex-wrap:wrap;">
        <a href="https://gentle-move-buddy.lovable.app/" target="_blank" class="btn-primary" style="display:inline-block;background:var(--accent);color:#fff;padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;">View live app &rarr;</a>
        <a href="#case-move-mitra-prd" style="display:inline-block;color:var(--accent);padding:0.65rem 1.25rem;border-radius:8px;font-weight:600;font-size:0.875rem;text-decoration:none;border:1px solid var(--accent);">Read the PRD &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer class="footer" id="contact">
  <div class="footer-left">
    <h2 class="footer-title">Thanks for taking the time to visit my portfolio</h2>
    <div class="footer-links">
      <a href="mailto:pallavi.singh.career@gmail.com">pallavi.singh.career@gmail.com</a>
      &nbsp;&middot;&nbsp;
      <a href="https://www.linkedin.com/in/singh-pallavi-singh/" target="_blank">LinkedIn</a>
      &nbsp;&middot;&nbsp;
      <a href="https://github.com/pallavising48?tab=repositories" target="_blank">GitHub</a>
      &nbsp;&middot;&nbsp;Seattle, WA
    </div>
  </div>
  <a class="btn-resume" href="https://drive.google.com/file/d/1JxCzEhHRlZUxnuM70DABE5CfXVKU9Ii6/view?usp=sharing" target="_blank">Download resume</a>
</footer>

<script>
(function(){
var r1s=[
{n:"Claude APIs",c:"AI",s:5,r:"Build with it daily across projects, skills, and MCP integrations."},
{n:"Prompt Engineering",c:"AI",s:5,r:"Core to every build. Eval work across InsightLoop and Snaccly confirms depth."},
{n:"Agentic Workflow Design",c:"AI",s:4,r:"Cipher multi-agent system and InsightLoop 4-step pipeline."},
{n:"Microsoft Foundry",c:"AI",s:4,r:"Cross-tenant Foundry architecture with Entra B2B in Cipher."},
{n:"Cursor / Lovable / Replit",c:"AI",s:4,r:"Building MVPs end to end without engineering support."},
{n:"n8n / Make.com",c:"AI",s:3,r:"Automation work in PID Floors and other client builds."},
{n:"MuleRun",c:"AI",s:3,r:"InsightLoop deployed and live on MuleRun."},
{n:"Zero-to-One Dev",c:"Product",s:5,r:"Every build in this portfolio started from a blank slate."},
{n:"Roadmapping",c:"Product",s:5,r:"Londr phased roadmap, InsightLoop Phase 2, Move Mitra community phase."},
{n:"GTM Strategy",c:"Product",s:4,r:"InsightLoop pricing model, Londr acquisition and segmentation strategy."},
{n:"AI Enablement",c:"Product",s:4,r:"20+ Capgemini delivery teams scaled via training."},
{n:"KPI / SLA Frameworks",c:"Product",s:4,r:"7+ years of enterprise delivery."},
{n:"Market Research",c:"Product",s:4,r:"Londr customer segmentation, Move Mitra user persona work."},
{n:"Competitive Analysis",c:"Product",s:3,r:"Referenced in Londr and InsightLoop strategy work."},
];
var r2s=[
{n:"SAP S/4HANA",c:"Enterprise",s:5,r:"7+ years hands-on across Capgemini, Vistex, and Accenture."},
{n:"Vistex GTMS",c:"Enterprise",s:5,r:"Direct role at Vistex with deep product and delivery experience."},
{n:"ServiceNow",c:"Enterprise",s:4,r:"Used across Accenture and Capgemini for SLA and incident management."},
{n:"Airtable",c:"Enterprise",s:4,r:"PID Floors inbox intelligence system built on Airtable."},
{n:"JIRA / Asana",c:"Enterprise",s:4,r:"Standard PM tooling across 7+ years of delivery."},
{n:"Salesforce",c:"Enterprise",s:3,r:"Live simulation reports and client dashboards at Capgemini."},
{n:"Figma",c:"Enterprise",s:3,r:"Used in design and portfolio work."},
{n:"API Integrations",c:"Dev & Data",s:4,r:"InsightLoop retrieval pipeline and PID Floors inbox automation."},
{n:"GitHub",c:"Dev & Data",s:4,r:"Cipher repo and regular version control across builds."},
{n:"Advanced Excel",c:"Dev & Data",s:4,r:"Financial modeling in Londr unit economics and Capgemini SLA scorecards."},
{n:"Python",c:"Dev & Data",s:3,r:"Azure and Python environment setup for Cipher."},
{n:"SQL",c:"Dev & Data",s:3,r:"Customer Analytics project and DBA coursework."},
{n:"Tableau / Power BI",c:"Dev & Data",s:3,r:"Built SLA scorecards and delivery dashboards at Capgemini."},
{n:"Google Analytics",c:"Dev & Data",s:3,r:"LR Brand Consulting SEO and traffic analysis."},
];
function stars(n){return"\u2605".repeat(n)+"\u2606".repeat(5-n);}
var tt=document.getElementById("skill-tt");
function buildRow(id,skills){
  var row=document.getElementById(id);
  if(!row)return;
  var doubled=skills.concat(skills);
  doubled.forEach(function(s){
    var c=document.createElement("span");
    c.style.cssText="display:inline-flex;align-items:center;gap:10px;padding:8px 24px;border-right:1px solid #DDD8CD;cursor:pointer;flex-shrink:0;font-family:'IBM Plex Sans','Helvetica Neue',sans-serif;";
    c.innerHTML='<span style="font-size:14px;font-weight:600;color:#1C1B19;">'+s.n+'</span><span style="font-size:12px;color:#1F5F5B;">'+stars(s.s)+'</span><span style="font-size:11px;color:#9B968C;">'+s.c+'</span>';
    c.addEventListener("mouseenter",function(){c.style.background="#F6F4EF";});
    c.addEventListener("mouseleave",function(){c.style.background="";});
    c.addEventListener("click",function(e){
      e.stopPropagation();
      document.getElementById("tt-n").textContent=s.n;
      document.getElementById("tt-s").textContent=stars(s.s)+" "+s.s+"/5";
      document.getElementById("tt-r").textContent=s.r;
      var x=Math.min(e.clientX-140,window.innerWidth-320);
      var y=Math.max(e.clientY-130,10);
      tt.style.left=x+"px";tt.style.top=y+"px";tt.style.opacity="1";tt.style.pointerEvents="auto";
    });
    row.appendChild(c);
  });
}
buildRow("r1",r1s);
buildRow("r2",r2s);
document.addEventListener("click",function(){tt.style.opacity="0";tt.style.pointerEvents="none";});

// Filter bar
var btns=document.querySelectorAll(".filter-btn");
var cards=document.querySelectorAll(".all-card");
btns.forEach(function(btn){
  btn.addEventListener("click",function(){
    btns.forEach(function(b){b.classList.remove("active");});
    btn.classList.add("active");
    var f=btn.dataset.filter;
    cards.forEach(function(card){
      card.style.display=(f==="all"||card.dataset.stage===f)?"flex":"none";
    });
  });
});
})();

(function(){
  function showView(){
    var hash=location.hash;
    var caseEl=hash?document.querySelector(hash):null;
    var isCase=!!(caseEl&&caseEl.classList.contains('case-study'));
    document.querySelectorAll('section:not(.case-study),footer').forEach(function(el){
      el.style.display=isCase?'none':'';
    });
    document.querySelectorAll('.case-study').forEach(function(el){
      el.style.display=(isCase&&el===caseEl)?'block':'none';
    });
    if(isCase){window.scrollTo(0,0);}
    else if(hash){var t=document.querySelector(hash);if(t)setTimeout(function(){t.scrollIntoView();},50);}
  }
  window.addEventListener('hashchange',showView);
  showView();
})();
</script>
</body>
</html>"""

html = html_template.replace('__PHOTO__', photo_b64)

with open('C:/Users/palsi/OneDrive/Desktop/Portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Done. File size: {len(html):,} chars')
