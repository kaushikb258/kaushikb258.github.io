# Robotics Projects on a Single GPU

Public portfolio: https://kaushikb258.github.io/

This site uses plain HTML and CSS, hosted on GitHub Pages. No paid hosting, framework, package installation, or database is required. Python's standard library builds the home page and the individual project pages.

## Local editing

```bash
cd /home/kb/kaushikb258.github.io
python3 build.py
python3 -m http.server 8765
```

Open http://localhost:8765. Generated HTML is committed so GitHub Pages serves it directly. Shared styles are in `assets/site.css`; header, footer, and page generation are in `build.py`.

## Add a project

1. Add a new record to `projects.json` with a unique `slug`, `title`, `short_title`, `year`, `category`, `summary`, `image`, `image_alt`, `body`, `code`, and `models` URL. Copy an existing record as a starting point. List projects in the desired home-page order.
2. Create its content file, e.g. `content/new-project.html`. This is an HTML fragment placed inside the shared page layout. Reuse the `project-layout` and `article` classes from `content/pi0-fast.html`. The model URL can be replaced with another resource URL; adapt the resource button in `build.py` if a project has no downloadable models.
3. Add its images or videos to `assets/`, using descriptive filenames.
4. Run `python3 build.py`. It generates `/projects/<slug>/index.html` and adds the project card to the home page and sitemap.
5. Preview the home page and the new project page, then commit and push:

```bash
git add projects.json content assets build.py index.html projects sitemap.xml robots.txt 404.html
git commit -m "Add new project"
git push origin main
```

GitHub Pages publishes the root of `main`. `.nojekyll` disables Jekyll processing. Page URLs remain stable as projects are added over time. If a project is removed or renamed, remove its old generated directory separately.

## First project: pi0-FAST

- Code: https://github.com/kaushikb258/pi0_fast
- Models: https://huggingface.co/kaushikb258/pi0-fast-libero-mimicgen
- Selected residual-controller results: LIBERO 96/100 and MimicGen 83/100.
- The page retains the evaluation caveats from the code/model release. Older LIBERO video footage is explicitly labeled and is not presented as the final controller run.
- Simulator media comes from the author's local evaluation/presentation artifacts. Upstream projects are credited on the project page.

The name is drawn from the author's public GitHub profile. No personal contact information is added. Fonts use Google Fonts with local sans-serif fallbacks.

## Presentation figures

`assets/residual-controller.png`, `vla-loss.png`, and `action-ema.png` reuse the original presentation images unchanged. The editable SVG architecture and FAST figures are rendered from the locally verified original `VLA_FAST_ChatGPT_handoff.md` handout; a saved architecture image was not available. Full-size image links are available on the project page.
