# /// script
# requires-python = ">=3.10"
# dependencies = [
#      "marimo>=0.23.2",
#      "rdkit>=2023.9.1",
#      "pandas>=2.0.0",
#      "numpy>=1.24.0",
#      "datasets>=2.14.0",
#      "scikit-learn>=1.3.0",
#      "altair>=5.0.0",
#      "pillow>=10.0.0",
#      "anywidget>=0.9.0",
#      "wigglystuff>=0.3.0",
#      "marimo-chem-utils"
# ]
# ///

import marimo

__generated_with = "0.25.0"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _():
    """Import marimo only."""
    import marimo as mo

    return (mo,)


# Cell 1
@app.cell(hide_code=True)
def _(mo):
    """Introduction Header"""
    banner = """
    <style>
                    :root {
                        --cyp-ink: #17212b;
                        --cyp-muted: #607080;
                        --cyp-line: #dce5ea;
                        --cyp-paper: #ffffff;
                        --cyp-wash: #f5f8f9;
                        --cyp-teal: #0f766e;
                        --cyp-teal-soft: #e7f5f2;
                        --cyp-coral: #d95f4f;
                        --cyp-coral-soft: #fff0ed;
                        --cyp-blue: #2d6cdf;
                        --cyp-shadow: 0 18px 45px rgba(23, 33, 43, 0.07);
                    }
                    .cyp-shell { color: var(--cyp-ink); font-family: "Avenir Next", "Helvetica Neue", sans-serif; }
                    .cyp-section { margin: 30px 0 14px; padding-top: 4px; }
                    .cyp-section__eyebrow { color: var(--cyp-teal); font-size: 0.72rem; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase; }
                    .cyp-section__title { color: var(--cyp-ink); font-size: 1.65rem; font-weight: 800; letter-spacing: 0; line-height: 1.15; margin: 5px 0 0; }
                    .cyp-section__rule { background: linear-gradient(90deg, var(--cyp-teal), rgba(15,118,110,0)); height: 2px; margin-top: 12px; width: 100%; }
                    .cyp-status { align-items: center; background: var(--cyp-paper); border: 1px solid var(--cyp-line); border-radius: 10px; box-shadow: var(--cyp-shadow); display: flex; gap: 14px; margin: 10px 0 24px; padding: 15px 18px; }
                    .cyp-status__mark { align-items: center; background: var(--cyp-teal-soft); border-radius: 50%; color: var(--cyp-teal); display: flex; flex: 0 0 30px; font-size: 0.9rem; font-weight: 900; height: 30px; justify-content: center; }
                    .cyp-status__title { color: var(--cyp-ink); font-size: 0.96rem; font-weight: 800; margin: 0; }
                    .cyp-status__detail { color: var(--cyp-muted); font-size: 0.84rem; line-height: 1.45; margin: 2px 0 0; }
                    .cyp-note { background: var(--cyp-wash); border-left: 3px solid var(--cyp-teal); border-radius: 0 8px 8px 0; color: var(--cyp-muted); padding: 14px 18px; }
                    .cyp-launch { align-items: center; background: linear-gradient(135deg, #f0faf8, #ffffff); border: 1px solid #b9ded8; border-radius: 10px; box-shadow: 0 12px 30px rgba(15, 118, 110, 0.08); display: flex; flex: 1 1 420px; gap: 22px; justify-content: space-between; margin: 0; padding: 18px 20px; }
                    .cyp-launch__copy { min-width: 0; }
                    .cyp-launch__eyebrow { color: var(--cyp-teal); font-size: 0.7rem; font-weight: 850; letter-spacing: 0.14em; text-transform: uppercase; }
                    .cyp-launch__title { color: var(--cyp-ink); font-size: 1.05rem; font-weight: 800; margin: 4px 0 3px; }
                    .cyp-launch__detail { color: var(--cyp-muted); font-size: 0.84rem; line-height: 1.45; margin: 0; }
                    @media (max-width: 640px) { .cyp-launch { align-items: stretch; flex-direction: column; gap: 14px; } }
                    .cyp-footer { border-top: 1px solid var(--cyp-line); color: var(--cyp-muted); margin-top: 42px; padding: 28px 0 12px; }
                    .cyp-footer strong { color: var(--cyp-ink); }
                    .cyp-metric-grid { display: grid; gap: 12px; grid-template-columns: repeat(4, minmax(0, 1fr)); margin: 14px 0 22px; }
                    .cyp-metric-heading { color: var(--cyp-muted); font-size: 0.74rem; font-weight: 800; letter-spacing: 0.1em; margin: 18px 0 8px; text-transform: uppercase; }
                    .cyp-metric { background: var(--cyp-paper); border: 1px solid var(--cyp-line); border-radius: 9px; padding: 16px; }
                    .cyp-metric__value { color: var(--cyp-ink); font-size: 1.4rem; font-weight: 850; }
                    .cyp-metric__label { color: var(--cyp-muted); font-size: 0.72rem; font-weight: 700; letter-spacing: 0.05em; margin-top: 4px; text-transform: uppercase; }
                    .cyp-close-grid { display: grid; gap: 14px; grid-template-columns: minmax(0, 1.35fr) minmax(260px, 0.65fr); margin-top: 18px; }
                    .cyp-close-card { background: var(--cyp-paper); border: 1px solid var(--cyp-line); border-radius: 10px; box-shadow: 0 12px 30px rgba(23, 33, 43, 0.05); padding: 20px; }
                    .cyp-close-card--tint { background: linear-gradient(145deg, #f0faf8, #ffffff); border-color: #b9ded8; }
                    .cyp-close-card--disclosure { background: linear-gradient(145deg, #eef5ff, #ffffff); border-color: #bfd3f4; }
                    .cyp-close-label { color: var(--cyp-teal); font-size: 0.7rem; font-weight: 850; letter-spacing: 0.12em; margin-bottom: 8px; text-transform: uppercase; }
                    .cyp-close-title { color: var(--cyp-ink); font-size: 1.12rem; font-weight: 800; margin: 0 0 12px; }
                    .cyp-close-copy { color: var(--cyp-muted); font-size: 0.88rem; line-height: 1.55; margin: 0; }
                    .cyp-close-list { display: grid; gap: 9px; list-style: none; margin: 14px 0 0; padding: 0; }
                    .cyp-close-list li { color: var(--cyp-muted); font-size: 0.88rem; line-height: 1.45; padding-left: 18px; position: relative; }
                    .cyp-close-list li::before { color: var(--cyp-teal); content: "✓"; font-weight: 900; left: 0; position: absolute; }
                    .cyp-close-links { display: grid; gap: 7px; margin: 0; }
                    .cyp-close-links a { color: var(--cyp-teal); font-size: 0.86rem; font-weight: 750; text-decoration: none; }
                    .cyp-close-links a:hover { text-decoration: underline; }
                    .cyp-disclosure { border-left: 3px solid var(--cyp-coral); color: var(--cyp-muted); font-size: 0.84rem; line-height: 1.55; margin-top: 14px; padding-left: 12px; }
                    .cyp-closing-block { border-top: 1px solid var(--cyp-line); margin-top: 20px; padding-top: 18px; }
                    .cyp-closing-block:first-child { border-top: 0; margin-top: 0; padding-top: 0; }
                    .cyp-closing-heading { color: var(--cyp-ink); font-size: 1.05rem; font-weight: 800; margin: 0 0 8px; }
                    .cyp-closing-copy { color: var(--cyp-muted); font-size: 0.9rem; line-height: 1.6; margin: 0; max-width: 900px; }
                    .cyp-closing-list { color: var(--cyp-muted); display: grid; gap: 8px; line-height: 1.5; margin: 12px 0 0; padding-left: 20px; }
                    .cyp-closing-links { columns: 2; column-gap: 32px; display: block; margin-top: 12px; }
                    .cyp-closing-links a { color: var(--cyp-teal); display: block; font-size: 0.88rem; font-weight: 750; margin-bottom: 7px; text-decoration: none; }
                    .cyp-closing-links a:hover { text-decoration: underline; }
                    .cyp-disclosure-wide { align-items: center; background: linear-gradient(100deg, #eaf2ff, #f7faff); border: 1px solid #b9cfee; border-radius: 10px; box-shadow: 0 12px 32px rgba(45, 108, 223, 0.08); display: flex; gap: 18px; margin-top: 22px; padding: 18px 20px; }
                    .cyp-disclosure-wide__mark { align-items: center; background: #d7e6ff; border-radius: 50%; color: #2d6cdf; display: flex; flex: 0 0 34px; font-size: 0.78rem; font-weight: 900; height: 34px; justify-content: center; }
                    .cyp-disclosure-wide__title { color: #1e4f9a; font-size: 0.9rem; font-weight: 850; margin: 0 0 4px; }
                    .cyp-disclosure-wide__copy { color: #58708f; font-size: 0.82rem; line-height: 1.5; margin: 0; }
                    @media (max-width: 640px) { .cyp-closing-links { columns: 1; } .cyp-disclosure-wide { align-items: flex-start; } }
                    @media (max-width: 760px) { .cyp-close-grid { grid-template-columns: 1fr; } }
                    @media (max-width: 760px) { .cyp-metric-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } .cyp-section__title { font-size: 1.35rem; } }
          .cyp-hero {
                        font-family: "Avenir Next", "Helvetica Neue", sans-serif;
            margin-bottom: 28px;
          }
          .cyp-hero-container {
            display: grid;
            grid-template-columns: 1.4fr 0.8fr;
            gap: 28px;
            background: linear-gradient(145deg, #ffffff 0%, #f5f8f9 100%);
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 36px;
            box-shadow: var(--cyp-shadow);
            position: relative;
            overflow: hidden;
          }
          .cyp-hero-container::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 4px;
            background: linear-gradient(90deg, var(--cyp-teal), #55a89e, var(--cyp-coral));
          }
          .cyp-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 9999px;
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            color: #1d4ed8;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
          }
          .cyp-badge a { color: inherit; text-decoration: none; }
          .cyp-badge a:hover { text-decoration: underline; text-underline-offset: 3px; }
          .cyp-launch { align-items: center; background: linear-gradient(135deg, #f0faf8, #ffffff); border: 1px solid #b9ded8; border-radius: 10px; box-shadow: 0 12px 30px rgba(15, 118, 110, 0.08); display: flex; flex: 1 1 420px; gap: 22px; justify-content: space-between; margin: 0 0 28px; padding: 18px 20px; }
          .cyp-launch__eyebrow { color: #0f766e; font-size: 0.7rem; font-weight: 850; letter-spacing: 0.14em; text-transform: uppercase; }
          .cyp-launch__title { color: #17212b; font-size: 1.05rem; font-weight: 800; margin: 4px 0 3px; }
          .cyp-launch__detail { color: #607080; font-size: 0.84rem; line-height: 1.45; margin: 0; }
          @media (max-width: 640px) { .cyp-launch { align-items: stretch; flex-direction: column; gap: 14px; } }
          .cyp-title {
            font-size: 2.6rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            line-height: 1.15;
            margin: 20px 0 14px;
            color: #0f172a;
          }
          .cyp-desc {
            font-size: 1.05rem;
            line-height: 1.65;
            color: #475569;
            margin: 0 0 24px;
            max-width: 95%;
          }
          .cyp-specs {
            display: flex;
            gap: 24px;
            margin-bottom: 24px;
          }
          .cyp-spec-item {
            display: flex;
            flex-direction: column;
            border-left: 3px solid #cbd5e1;
            padding-left: 14px;
          }
          .cyp-spec-value { font-weight: 700; color: #0f172a; font-size: 1.15rem; }
          .cyp-spec-label { font-size: 0.75rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 700; margin-top: 2px;}

          .cyp-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.025);
            display: flex;
            flex-direction: column;
          }
          .cyp-card-header {
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #64748b;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
          }
                    .cyp-byline { color: #607080; font-size: 0.86rem; line-height: 1.55; margin-top: 18px; }
                    .cyp-byline a { color: var(--cyp-teal); font-weight: 800; text-decoration: none; }
                    .cyp-byline a:hover { text-decoration: underline; }
                    .cyp-method-list { display: grid; gap: 8px; margin: 16px 0 20px; }
                    .cyp-method-item { align-items: baseline; color: #475569; display: flex; font-size: 0.82rem; gap: 10px; line-height: 1.4; }
                    .cyp-method-item b { color: var(--cyp-teal); font-size: 0.72rem; letter-spacing: 0.08em; }
          @media (max-width: 960px) {
            .cyp-hero-container { grid-template-columns: 1fr; }
          }
        </style>

        <div class="cyp-hero">
          <div class="cyp-hero-container">

            <div>
              <div class="cyp-badge">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
                <a target="_blank" rel="noopener noreferrer" href="https://marimo.io/pages/events/notebook-competition-3">molab Competition #3</a>
                <span aria-hidden="true">|</span>
                <a target="_blank" rel="noopener noreferrer" href="https://github.com/Mohit5Upadhyay/cyp-activity-cliff-explorer-molab">Mohit Upadhyay</a>
              </div>
              <h1 class="cyp-title">CYP3A4 Activity Cliff Explorer</h1>
              <p class="cyp-desc">
                How much can measured CYP3A4 inhibition change among structurally related molecules?
                This interactive notebook makes <strong>activity cliffs</strong> inspectable and audits where
                a simple molecular-descriptor model misses those changes.
              </p>

              <div class="cyp-specs">
                <div class="cyp-spec-item">
                  <span class="cyp-spec-value">QC-filtered</span>
                  <span class="cyp-spec-label">OpenADMET data</span>
                </div>
                <div class="cyp-spec-item">
                  <span class="cyp-spec-value">CYP3A4_pIC50</span>
                  <span class="cyp-spec-label">Analyzed endpoint</span>
                </div>
                <div class="cyp-spec-item">
                  <span class="cyp-spec-value">Scaffold</span>
                  <span class="cyp-spec-label">Held-out validation</span>
                </div>
              </div>

              <div style="font-size: 0.85rem; color: #64748b; display: flex; align-items: center; gap: 8px; font-weight: 500;">
                <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#10b981; box-shadow: 0 0 8px rgba(16,185,129,0.6);"></span>
                Rigorous Bemis-Murcko scaffold-isolated validation enforced.
              </div>
            </div>

            <div class="cyp-card">
              <div class="cyp-card-header">
                <span>The ML Blind Spot</span>
                <span style="background:#f1f5f9; padding:3px 8px; border-radius:4px; font-size:0.7rem; color:#0f172a;">pIC50 Variance</span>
              </div>
              <p style="font-size: 0.88rem; color: #475569; margin: 0 0 20px; line-height: 1.55;">
                Baseline models relying on 1D/2D descriptors cannot "see" 3D binding topology. They falsely predict similar activity for near-identical structures, missing the cliff entirely.
              </p>

              <svg viewBox="0 0 300 130" style="width: 100%; height: auto; background: #f8fafc; border-radius: 8px; border: 1px solid #e2e8f0; padding: 10px;">
                <line x1="40" y1="25" x2="280" y2="25" stroke="#cbd5e1" stroke-dasharray="3 3"/>
                <line x1="40" y1="65" x2="280" y2="65" stroke="#cbd5e1" stroke-dasharray="3 3"/>
                <line x1="40" y1="105" x2="280" y2="105" stroke="#cbd5e1" stroke-dasharray="3 3"/>

                <text x="32" y="28" font-size="10" font-family="monospace" fill="#64748b" text-anchor="end">High</text>
                <text x="32" y="108" font-size="10" font-family="monospace" fill="#64748b" text-anchor="end">Low</text>

                <path d="M 50 25 L 130 25 L 160 105 L 270 105" fill="none" stroke="#94a3b8" stroke-width="2.5" stroke-linejoin="round"/>
                <path d="M 130 25 L 160 105" fill="none" stroke="#ef4444" stroke-width="3.5" stroke-linejoin="round"/>

                <circle cx="130" cy="25" r="5.5" fill="#0ea5e9"/>
                <circle cx="160" cy="105" r="5.5" fill="#ef4444"/>

                <text x="130" y="13" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">Variant A</text>
                <text x="160" y="123" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">Variant B</text>

                <path d="M 130 25 L 270 25" fill="none" stroke="#0ea5e9" stroke-width="2.5" stroke-dasharray="5 4"/>
                <text x="215" y="17" font-size="9" font-weight="800" fill="#0ea5e9" text-anchor="middle">ML Prediction (Blind)</text>
                <text x="215" y="96" font-size="9" font-weight="800" fill="#ef4444" text-anchor="middle">Experimental Reality</text>
              </svg>
            </div>

          </div>
        </div>
    """

    hero_banner = mo.Html(banner)
    hero_banner
    return (hero_banner,)


# Cell 2
@app.cell(hide_code=True)
def _(mo):
    scientific_map_view = mo.vstack([
        mo.Html("""
        <div class="cyp-section">
            <div class="cyp-section__eyebrow">Before you run it / the scientific map</div>
            <h2 class="cyp-section__title">What is this explorer measuring?</h2>
            <div class="cyp-section__rule"></div>
        </div>
        <div class="cyp-close-grid">
            <div class="cyp-close-card cyp-close-card--tint">
                <div class="cyp-close-label">The question</div>
                <h3 class="cyp-close-title">Can a tiny structural change create a large activity change?</h3>
                <p class="cyp-close-copy">An <strong>activity cliff</strong> is a sharp structure-activity discontinuity: molecules with a closely related structure can show very different measured biological activity. This notebook searches for candidate cliffs among molecules that share a Bemis-Murcko scaffold, then lets you inspect the structures and the model error.</p>
            </div>
            <div class="cyp-close-card cyp-close-card--disclosure">
                <div class="cyp-close-label">The honest boundary</div>
                <h3 class="cyp-close-title">Evidence first, mechanism second</h3>
                <p class="cyp-close-copy">The data can show a measured potency gap and a descriptor-model failure. The 3D viewer helps you form a structural hypothesis, but this notebook does not establish a binding pose, enzyme mechanism, or clinical risk.</p>
            </div>
        </div>
        """),
        mo.md(r"""
        ### Abbreviations, decoded

        | Term | Meaning here |
        | --- | --- |
        | **CYP3A4** | Cytochrome P450 3A4, an enzyme involved in the metabolism of many drugs. The notebook studies measured inhibition of this enzyme. |
        | **IC$_{50}$** | Half-maximal inhibitory concentration: the concentration required to reduce measured enzyme activity by 50% in an assay. |
        | **pIC$_{50}$** | The negative base-10 logarithm of IC$_{50}$, conventionally with IC$_{50}$ expressed in molar units. |
        | **QC** | Quality control. Rows flagged as failed or problematic by the available assay fields are excluded before analysis. |
        | **SMILES** | A text representation of a molecular structure. The notebook canonicalizes it so equivalent structures can be compared consistently. |
        | **Bemis–Murcko scaffold** | The molecule's central ring-and-linker framework after peripheral substituents are removed. It is used here to group related molecules. |
        | **1D/2D descriptors** | Scalar molecular summaries such as molecular weight, LogP, TPSA, hydrogen-bond counts, ring counts, and rotatable bonds. |
        | **3D conformation** | A spatial arrangement of atoms. The viewer generates an illustrative conformer; it is not an experimentally determined protein-bound pose. |
        | **ML / QSAR** | Machine learning / quantitative structure-activity relationship: learning a relationship between molecular features and measured activity. |
        """).callout(kind="info"),
        mo.md(r"""
        ### The mathematics of potency

        IC$_{50}$ and potency move in opposite directions: a **lower IC$_{50}$ means a smaller concentration is needed**, so the inhibitor is more potent. The logarithmic endpoint used here reverses that visual direction:

        $$\mathrm{pIC}_{50} = -\log_{10}\left(\mathrm{IC}_{50}\ [\mathrm{M}]\right)$$

        Therefore, **higher pIC$_{50}$ means higher potency**. A difference in pIC$_{50}$ is a fold-change in IC$_{50}$:

        $$\Delta\mathrm{pIC}_{50} = \mathrm{pIC}_{50,A} - \mathrm{pIC}_{50,B}$$
        $$\frac{\mathrm{IC}_{50,B}}{\mathrm{IC}_{50,A}} = 10^{\Delta\mathrm{pIC}_{50}}$$

        For example, a 2-unit pIC$_{50}$ gap corresponds to a 100-fold IC$_{50}$ ratio. The notebook reports the dataset's `CYP3A4_pIC50` values directly; it does not convert them back to IC$_{50}$ without knowing the dataset's concentration units.
        """).callout(kind="info"),
        mo.md(r"""
        ### How this notebook finds a cliff

        For each scaffold $s$, the workflow collects the valid CYP3A4 pIC$_{50}$ measurements $y_i$ for its molecules and computes the sample variance:

        $$\bar{y}_s = \frac{1}{n_s}\sum_{i=1}^{n_s} y_i$$
        $$\mathrm{CliffScore}(s) = \mathrm{Var}(y_s) = \frac{1}{n_s-1}\sum_{i=1}^{n_s}(y_i - \bar{y}_s)^2$$

        Larger variance means a wider spread of measured activity inside that shared scaffold group, so the scaffold is ranked as a **candidate** activity cliff. This is a screening score, not a universal clinical or mechanistic definition of a cliff. The current workflow requires at least three measured molecules per scaffold.
        """).callout(kind="info"),
        mo.md(r"""
        ### Why compare 1D/2D descriptors with 3D structure?

        The baseline Random Forest sees only the 1D/2D descriptor vector $x$ and learns an estimate $\hat{y} = f(x)$ for pIC$_{50}$. It does **not** receive a 3D conformer, protein structure, binding pose, or explicit spatial interaction features. Two molecules can therefore look similar to this baseline while differing in measured activity.

        The 3D view is useful for **inspection and hypothesis generation**: a small substituent change may alter shape, steric contacts, orientation, or accessibility in a protein pocket. Those are plausible reasons for an activity cliff, but the viewer alone cannot prove which explanation is correct. The experiment here is narrower and testable: compare the measured pIC$_{50}$ with the descriptor-only prediction on a molecule selected from a high-variance scaffold.
        """).callout(kind="neutral"),
        mo.Html("""
        <div class="cyp-close-card" style="margin-top: 4px;">
            <div class="cyp-close-label">How the project helps</div>
            <h3 class="cyp-close-title">It turns an aggregate score into an inspectable scientific question.</h3>
            <p class="cyp-close-copy">Instead of reporting only one model metric, the explorer connects four evidence layers: QC-filtered OpenADMET measurements, scaffold-level variance, 2D structural differences with a generated 3D view, and held-out predictions. Scaffold-isolated splitting keeps the test scaffolds separate from training, so the audit asks whether the baseline transfers to unseen chemical cores rather than rewarding memorization.</p>
            <div class="cyp-disclosure">Use the result to prioritize molecules or hypotheses for further assay and structural investigation. It is an educational and exploratory analysis, not a clinical, regulatory, or production prediction system.</div>
        </div>
        """),
    ], gap=0.8)
    scientific_map_view
    return (scientific_map_view,)


# Cell 3
@app.cell(hide_code=True)
def _(mo):
    start_analysis = mo.ui.run_button(
    label="Start analysis",
    kind="success",
    )
    mo.hstack([
    mo.Html("""
                <div class="cyp-launch">
                    <div class="cyp-launch__copy">
                        <div class="cyp-launch__eyebrow">Ready when you are</div>
                        <div class="cyp-launch__title">Run the complete activity-cliff workflow</div>
                        <p class="cyp-launch__detail">Load the CYP dataset, extract scaffolds, train the honest baseline, and unlock the interactive explorer.</p>
                    </div>
                </div>
                """),
        start_analysis,
    ], justify="space-between", align="center", wrap=True, gap=0.8)
    return (start_analysis,)


# Cell 4
@app.cell(hide_code=True)
def _(mo):
    """All backend functions - data engine, scaffolds, ML, visuals, widgets."""
    import pandas as pd
    import numpy as np
    import logging
    from rdkit import Chem
    from rdkit.Chem import AllChem, Descriptors, Lipinski, Draw, rdFMCS
    from rdkit.Chem.Scaffolds import MurckoScaffold
    from datasets import load_dataset
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, r2_score
    from PIL import Image
    import altair as alt
    from wigglystuff import GraphWidget
    from typing import Dict, List, Tuple, Optional
    import base64
    import html as html_lib
    import marimo_chem_utils as mcu

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    CYP_ENDPOINT = "CYP3A4_pIC50"

    def load_cyp_data(use_cache: bool = True) -> pd.DataFrame:
        logger.info("Loading CYP inhibition dataset from HuggingFace...")
        try:
            ds = load_dataset("openadmet/Octant_CYP_inhibition_reactivity_blog_release", "inhibition", split="train", cache_dir=None if use_cache else ".cache")
            return ds.to_pandas()
        except Exception as e:
            logger.error(f"Failed to load dataset: {e}")
            raise

    def canonicalize_smiles(smiles: str) -> Optional[str]:
        if pd.isna(smiles) or not smiles: return None
        try:
            mol = Chem.MolFromSmiles(smiles)
            return Chem.MolToSmiles(mol, canonical=True) if mol else None
        except: return None

    def prepare_dataset(df: pd.DataFrame, smiles_column: str = "smiles") -> pd.DataFrame:
        df['canonical_smiles'] = df[smiles_column].apply(canonicalize_smiles)
        return df[df['canonical_smiles'].notna()].copy()

    def filter_qc_passed(df: pd.DataFrame) -> pd.DataFrame:
        initial_count = len(df)
        result = df.copy()
        if 'qc_flag_primary' in result.columns:
            result = result[result['qc_flag_primary'].astype(str).str.upper() == 'PASS']
        if 'drc_qc_status' in result.columns:
            result = result[result['drc_qc_status'].astype(str).str.upper() == 'PASS']
        if 'rollover_status' in result.columns:
            result = result[~result['rollover_status'].astype(str).str.upper().isin(['TRUE', 'YES'])]
        removed = initial_count - len(result)
        logger.info(f"QC filter: removed {removed} of {initial_count} rows ({len(result)} remain)")
        return result

    def get_bemis_murcko_scaffold(smiles: str) -> Optional[str]:
        if pd.isna(smiles) or not smiles: return None
        try:
            mol = Chem.MolFromSmiles(smiles)
            if mol is None: return None
            scaffold = MurckoScaffold.GetScaffoldForMol(mol)
            return Chem.MolToSmiles(scaffold) if scaffold else None
        except: return None

    def extract_scaffolds(df: pd.DataFrame, smiles_column: str = "canonical_smiles") -> pd.DataFrame:
        df['scaffold'] = df[smiles_column].apply(get_bemis_murcko_scaffold)
        return df[df['scaffold'].notna()].copy()

    def compute_scaffold_cliff_score(df: pd.DataFrame, endpoint: str = CYP_ENDPOINT, min_molecules: int = 3) -> pd.DataFrame:
        scaffold_stats = []
        grouped = df.groupby('scaffold')
        for scaffold, group in grouped:
            valid_data = group[endpoint].dropna()
            if len(valid_data) < min_molecules: continue
            var = valid_data.var()
            if var == 0 or pd.isna(var): continue
            scaffold_stats.append({
                'scaffold': scaffold,
                'n_molecules': len(valid_data),
                f'{endpoint}_mean': valid_data.mean(),
                f'{endpoint}_std': valid_data.std(),
                f'{endpoint}_range': valid_data.max() - valid_data.min(),
                'cliff_score': var
            })
        result = pd.DataFrame(scaffold_stats)
        if len(result) > 0: result = result.sort_values('cliff_score', ascending=False)
        return result

    def rank_cliff_scaffolds(df: pd.DataFrame, endpoint: str = CYP_ENDPOINT, top_k: int = 15, min_molecules: int = 3) -> Tuple[pd.DataFrame, pd.DataFrame]:
        scaffold_stats = compute_scaffold_cliff_score(df, endpoint=endpoint, min_molecules=min_molecules)
        if len(scaffold_stats) == 0: return pd.DataFrame(), df
        top_scaffolds = scaffold_stats.head(top_k).copy()
        for idx, row in top_scaffolds.iterrows():
            scaffold_mols = df[df['scaffold'] == row['scaffold']]
            top_scaffolds.at[idx, 'example_smiles'] = scaffold_mols['canonical_smiles'].iloc[0]
        top_scaffolds = top_scaffolds.rename(columns={'cliff_score': 'avg_cliff_score'})
        return top_scaffolds, df

    def get_scaffold_molecules(df: pd.DataFrame, scaffold: str, endpoint: str = None) -> pd.DataFrame:
        result = df[df['scaffold'] == scaffold].copy()
        if endpoint and endpoint in result.columns: result = result.sort_values(endpoint)
        return result

    def compute_molecular_descriptors(smiles: str) -> Optional[Dict[str, float]]:
        if pd.isna(smiles) or not smiles: return None
        try:
            mol = Chem.MolFromSmiles(smiles)
            if mol is None: return None
            return {
                'MolWt': Descriptors.MolWt(mol), 'LogP': Descriptors.MolLogP(mol), 'TPSA': Descriptors.TPSA(mol),
                'NumHDonors': Lipinski.NumHDonors(mol), 'NumHAcceptors': Lipinski.NumHAcceptors(mol),
                'NumRotatableBonds': Lipinski.NumRotatableBonds(mol), 'NumAromaticRings': Lipinski.NumAromaticRings(mol),
                'NumAliphaticRings': Lipinski.NumAliphaticRings(mol), 'NumSaturatedRings': Lipinski.NumSaturatedRings(mol),
                'RingCount': Lipinski.RingCount(mol), 'FractionCSP3': Lipinski.FractionCSP3(mol), 'NumHeteroatoms': Lipinski.NumHeteroatoms(mol),
            }
        except: return None

    # Reset index before concat so descriptor rows align correctly with df rows
    def add_descriptor_columns(df: pd.DataFrame, smiles_column: str = "canonical_smiles") -> pd.DataFrame:
        df_clean = df.reset_index(drop=True)
        descriptors_list = df_clean[smiles_column].apply(compute_molecular_descriptors)
        descriptors_df = pd.DataFrame(descriptors_list.tolist())
        result = pd.concat([df_clean, descriptors_df], axis=1).dropna(subset=descriptors_df.columns)
        return result

    def scaffold_based_split(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame]:
        unique_scaffolds = list(df['scaffold'].unique())
        train_scaffolds, test_scaffolds = train_test_split(unique_scaffolds, test_size=test_size, random_state=random_state)
        return df[df['scaffold'].isin(train_scaffolds)].copy(), df[df['scaffold'].isin(test_scaffolds)].copy()

    class CliffModelAuditor:
        DESCRIPTOR_FEATURES = ['MolWt', 'LogP', 'TPSA', 'NumHDonors', 'NumHAcceptors', 'NumRotatableBonds', 'NumAromaticRings', 'NumAliphaticRings', 'NumSaturatedRings', 'RingCount', 'FractionCSP3', 'NumHeteroatoms']
        def __init__(self, train_df: pd.DataFrame, test_df: pd.DataFrame, endpoints: List[str], random_state: int = 42):
            self.train_df, self.test_df, self.endpoints, self.random_state = train_df, test_df, endpoints, random_state
            self.models, self.train_predictions, self.test_predictions, self.metrics = {}, {}, {}, {}
            self._train_all_models()

        def _train_all_models(self):
            for endpoint in self.endpoints:
                X_train, y_train = self.train_df[self.DESCRIPTOR_FEATURES].values, self.train_df[endpoint].values
                X_test, y_test = self.test_df[self.DESCRIPTOR_FEATURES].values, self.test_df[endpoint].values
                train_mask, test_mask = ~np.isnan(y_train), ~np.isnan(y_test)

                model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=self.random_state, n_jobs=-1)
                model.fit(X_train[train_mask], y_train[train_mask])
                self.models[endpoint] = model

                train_pred, test_pred = np.full(len(y_train), np.nan), np.full(len(y_test), np.nan)
                train_pred[train_mask] = model.predict(X_train[train_mask])
                test_pred[test_mask] = model.predict(X_test[test_mask])

                self.train_predictions[endpoint], self.test_predictions[endpoint] = train_pred, test_pred
                self.metrics[endpoint] = {
                    'train_mae': mean_absolute_error(y_train[train_mask], train_pred[train_mask]),
                    'test_mae': mean_absolute_error(y_test[test_mask], test_pred[test_mask]),
                    'train_r2': r2_score(y_train[train_mask], train_pred[train_mask]),
                    'test_r2': r2_score(y_test[test_mask], test_pred[test_mask]),
                    'n_train': len(y_train[train_mask]), 'n_test': len(y_test[test_mask])
                }

        def predict_molecule(self, smiles: str, endpoint: str) -> Optional[float]:
            if endpoint not in self.models: return None
            descriptors = compute_molecular_descriptors(smiles)
            if not descriptors: return None
            try:
                features = np.array([[descriptors[feat] for feat in self.DESCRIPTOR_FEATURES]])
                return float(self.models[endpoint].predict(features)[0])
            except: return None

        def get_test_results(self, endpoint: str = None) -> pd.DataFrame:
            result = self.test_df.copy()
            for ep in ([endpoint] if endpoint else self.endpoints):
                if ep in self.test_predictions:
                    result[f'{ep}_predicted'] = self.test_predictions[ep]
                    result[f'{ep}_error'] = np.abs(result[ep] - result[f'{ep}_predicted'])
            return result

        def get_metrics_summary(self) -> pd.DataFrame:
            return pd.DataFrame([{'endpoint': ep, **m} for ep, m in self.metrics.items()])

    def train_cliff_models(df: pd.DataFrame, endpoints: List[str], test_size: float = 0.2, random_state: int = 42) -> Tuple[CliffModelAuditor, pd.DataFrame, pd.DataFrame]:
        df_with_descriptors = add_descriptor_columns(df)
        train_df, test_df = scaffold_based_split(df_with_descriptors, test_size=test_size, random_state=random_state)
        valid_endpoints = [ep for ep in endpoints if ep in df.columns]
        auditor = CliffModelAuditor(train_df, test_df, valid_endpoints, random_state)
        return auditor, train_df, test_df

    def find_mcs_and_highlight(smiles1: str, smiles2: str) -> Tuple[Optional[str], List, List]:
        try:
            mol1, mol2 = Chem.MolFromSmiles(smiles1), Chem.MolFromSmiles(smiles2)
            if not mol1 or not mol2: return None, [], []
            mcs_result = rdFMCS.FindMCS([mol1, mol2], timeout=2, atomCompare=rdFMCS.AtomCompare.CompareElements, bondCompare=rdFMCS.BondCompare.CompareOrder, ringMatchesRingOnly=True)
            if mcs_result.numAtoms == 0: return None, list(range(mol1.GetNumAtoms())), list(range(mol2.GetNumAtoms()))
            mcs_mol = Chem.MolFromSmarts(mcs_result.smartsString)
            return mcs_result.smartsString, list(set(range(mol1.GetNumAtoms())) - set(mol1.GetSubstructMatch(mcs_mol))), list(set(range(mol2.GetNumAtoms())) - set(mol2.GetSubstructMatch(mcs_mol)))
        except: return None, [], []

    def render_structure_pair(smiles1: str, smiles2: str, label1: str = "Molecule 1", label2: str = "Molecule 2", highlight_differences: bool = True) -> Optional[Image.Image]:
        try:
            mol1, mol2 = Chem.MolFromSmiles(smiles1), Chem.MolFromSmiles(smiles2)
            if not mol1 or not mol2: return None
            highlight_atoms = [[], []]
            if highlight_differences: _, highlight_atoms[0], highlight_atoms[1] = find_mcs_and_highlight(smiles1, smiles2)
            return Draw.MolsToGridImage([mol1, mol2], molsPerRow=2, subImgSize=(400, 300), legends=[label1, label2], highlightAtomLists=highlight_atoms, useSVG=False)
        except: return None

    def highlight_structure_difference(smiles1: str, smiles2: str, value1: float, value2: float, endpoint: str = "Activity") -> Optional[Image.Image]:
        return render_structure_pair(smiles1, smiles2, f"{endpoint}: {value1:.2f}", f"{endpoint}: {value2:.2f}", highlight_differences=True)

    def create_dumbbell_chart(predicted: float, actual: float, endpoint: str, molecule_name: str = "Selected Molecule") -> alt.Chart:
        data = pd.DataFrame([{'type': 'Predicted', 'value': predicted, 'order': 0}, {'type': 'Actual', 'value': actual, 'order': 1}])

        max_y = max(8.0, max(predicted, actual) + 1.2)
        y_scale = alt.Scale(domain=[0, max_y])

        line = alt.Chart(data).mark_line(color='gray', strokeWidth=2).encode(
            x=alt.X('order:Q', scale=alt.Scale(domain=[-0.6, 1.8]), axis=None),
            y=alt.Y('value:Q', scale=y_scale, title=f'{endpoint} Activity')
        )
        points = alt.Chart(data).mark_circle(size=200).encode(
            x=alt.X('order:Q', axis=None),
            y=alt.Y('value:Q', scale=y_scale, title=f'{endpoint} Activity'),
            color=alt.Color('type:N', scale=alt.Scale(domain=['Predicted', 'Actual'], range=['#1f77b4', '#d62728']), legend=alt.Legend(title='Type')),
            tooltip=['type:N', 'value:Q']
        )
        text = alt.Chart(data).mark_text(align='left', dx=10, fontSize=12, fontWeight='bold', clip=False).encode(
            x=alt.X('order:Q', axis=None),
            y=alt.Y('value:Q', scale=y_scale),
            text=alt.Text('value:Q', format='.2f'),
            color=alt.Color('type:N', legend=None, scale=alt.Scale(domain=['Predicted', 'Actual'], range=['#1f77b4', '#d62728']))
        )
        return (line + points + text).properties(width=300, height=300, title={"text": f"{molecule_name}", "subtitle": f"Prediction Error: {abs(predicted - actual):.2f}"}).configure_axis(grid=True, gridColor='lightgray')

    def create_global_scatter(
            df: pd.DataFrame,
            endpoint: str,
            prediction_col: str = None,
            color_cliff_molecules: bool = True,
            cliff_scaffolds: List[str] = None
        ):
            import marimo_chem_utils as mcu
            import altair as alt

            if prediction_col is None:
                prediction_col = f'{endpoint}_predicted'

            plot_df = df[[endpoint, prediction_col, 'canonical_smiles']].dropna().copy()
            plot_df = mcu.add_image_column(plot_df, smiles_column='canonical_smiles')

            if color_cliff_molecules and cliff_scaffolds is not None and 'scaffold' in df.columns:
                plot_df['is_cliff'] = df.loc[plot_df.index, 'scaffold'].isin(cliff_scaffolds)
            else:
                plot_df['is_cliff'] = False

            plot_df['error'] = (plot_df[endpoint] - plot_df[prediction_col]).abs()

            min_val = min(plot_df[endpoint].min(), plot_df[prediction_col].min()) - 0.5
            max_val = max(plot_df[endpoint].max(), plot_df[prediction_col].max()) + 0.5

            ref_df = pd.DataFrame({'x': [min_val, max_val], 'y': [min_val, max_val]})
            identity_line = alt.Chart(ref_df).mark_line(
                color='#ef4444', strokeDash=[5, 5], strokeWidth=2, opacity=0.7
            ).encode(
                x='x:Q',
                y='y:Q'
            )

            scatter = alt.Chart(plot_df).mark_circle(size=70, opacity=0.75).encode(
                x=alt.X(
                    prediction_col,
                    title=f'Predicted {endpoint}',
                    scale=alt.Scale(domain=[min_val, max_val])
                ),
                y=alt.Y(
                    endpoint,
                    title=f'Actual {endpoint}',
                    scale=alt.Scale(domain=[min_val, max_val])
                ),
                color=alt.Color(
                    'is_cliff:N',
                    scale=alt.Scale(domain=[False, True], range=['#0284c7', '#dc2626']),
                    legend=alt.Legend(
                        title="Molecule Type",
                        labelExpr="datum.value ? 'Activity Cliff' : 'Standard Test'"
                    )
                ),
                tooltip=[
                    alt.Tooltip('image'),
                    alt.Tooltip(endpoint, title='Actual Potency', format='.2f'),
                    alt.Tooltip(prediction_col, title='Predicted', format='.2f'),
                    alt.Tooltip('error:Q', title='Abs Error', format='.2f'),
                ]
            )

            final_chart = (identity_line + scatter).properties(
                width=500,
                height=450,
                title={
                    "text": "Model Predictions vs. Reality (Held-Out Test Scaffolds)",
                    "subtitle": "Dashed Red Line: Ideal Parity (y=x) | Hover over points to inspect structures"
                }
            ).interactive()

            return mo.ui.altair_chart(final_chart)

    def create_3d_viewer(smiles: str, color_scheme: str = 'cyanCarbon', w: int = 350, h: int = 300) -> str:
        try:
            mol = Chem.MolFromSmiles(smiles)
            if mol is None: return "<div>Invalid SMILES for 3D mapping</div>"
            mol = Chem.AddHs(mol)
            if AllChem.EmbedMolecule(mol, maxAttempts=10, randomSeed=42) != 0:
                AllChem.Compute2DCoords(mol)
            else:
                try: AllChem.MMFFOptimizeMolecule(mol)
                except: pass

            mb_b64 = base64.b64encode(Chem.MolToMolBlock(mol).encode('utf-8')).decode('utf-8')
            html_content = f"""<!DOCTYPE html><html><head><script src="https://3dmol.csb.pitt.edu/build/3Dmol-min.js"></script></head><body style="margin:0; padding:0; overflow:hidden; background:white;"><div id="container" style="width: {w}px; height: {h}px; position: relative;"></div><script>window.onload = function() {{ if (typeof $3Dmol === 'undefined') {{ document.getElementById('container').innerHTML = '<div style="color:red; padding:20px;">3Dmol.js failed to load.</div>'; return; }} let viewer = $3Dmol.createViewer(document.getElementById('container'), {{backgroundColor: 'white'}}); viewer.addModel(atob("{mb_b64}"), "sdf"); viewer.setStyle({{}}, {{stick: {{colorscheme: '{color_scheme}'}}}}); viewer.zoomTo(); viewer.render(); }};</script></body></html>"""
            return f'<iframe srcdoc="{html_lib.escape(html_content, quote=True)}" style="border: 0; width: {w}px; height: {h}px; overflow: hidden;" sandbox="allow-scripts allow-same-origin"></iframe>'
        except Exception as e: return f"<div style='padding:20px; background:#fee2e2; color:#991b1b; border-radius:8px;'>3D rendering failed: {e}</div>"

    def create_scaffold_graph(df: pd.DataFrame, scaffold: str, endpoint: str, threshold: Optional[float] = None, max_molecules: int = 30) -> GraphWidget:
        scaffold_mols = df[df['scaffold'] == scaffold].copy()
        if len(scaffold_mols) == 0: return GraphWidget(nodes=[], edges=[])

        scaffold_mols = scaffold_mols.sort_values(endpoint)
        if len(scaffold_mols) > max_molecules:
            half = max_molecules // 2
            scaffold_mols = pd.concat([scaffold_mols.head(half), scaffold_mols.tail(half)])

        nodes, edges = [{'id': 'scaffold_center', 'name': 'Scaffold', 'size': 20, 'color': '#888888', 'data': {'type': 'scaffold', 'smiles': str(scaffold)}}], []
        threshold = float(scaffold_mols[endpoint].median()) if threshold is None else threshold
        endpoint_max, endpoint_min = float(scaffold_mols[endpoint].max()), float(scaffold_mols[endpoint].min())

        for idx, row in scaffold_mols.iterrows():
            smiles, value = str(row.get('canonical_smiles', '')), row[endpoint]
            is_valid = pd.notna(value)
            val_float = float(value) if is_valid else None
            node_id = f'mol_{str(idx)}'

            if is_valid:
                intensity = min(1.0, (val_float - threshold) / (endpoint_max - threshold + 0.01)) if val_float >= threshold else min(1.0, (threshold - val_float) / (threshold - endpoint_min + 0.01))
                color = f'rgb(255, {int(100 - intensity * 100)}, {int(100 - intensity * 100)})' if val_float >= threshold else f'rgb({int(100 - intensity * 100)}, {int(100 - intensity * 100)}, 255)'
            else: color = '#cccccc'

            nodes.append({'id': node_id, 'name': f'{val_float:.2f}' if is_valid else 'N/A', 'size': 10, 'color': color, 'data': {'type': 'molecule', 'smiles': smiles, 'value': val_float, 'endpoint': str(endpoint), 'index': str(idx)}})
            edges.append({'source': 'scaffold_center', 'target': node_id})

        return GraphWidget(nodes=nodes, edges=edges, directed=False, bounded=True, width=None, height=500)

    def get_selected_molecule_data(graph: GraphWidget, df: pd.DataFrame) -> Optional[Dict]:
        if not graph.selected_nodes: return None
        node_id = graph.selected_nodes[0]
        node_data = next((node.get('data', {}) for node in graph.nodes if node['id'] == node_id), None)
        if not node_data or node_data.get('type') != 'molecule': return None
        return {'smiles': str(node_data.get('smiles')), 'value': node_data.get('value'), 'endpoint': str(node_data.get('endpoint'))}

    return (
        CYP_ENDPOINT,
        create_3d_viewer,
        create_dumbbell_chart,
        create_global_scatter,
        create_scaffold_graph,
        extract_scaffolds,
        filter_qc_passed,
        get_selected_molecule_data,
        highlight_structure_difference,
        load_cyp_data,
        np,
        pd,
        prepare_dataset,
        rank_cliff_scaffolds,
        train_cliff_models,
    )


# Cell 5
@app.cell(hide_code=True)
def _(filter_qc_passed, load_cyp_data, mo, prepare_dataset, start_analysis):
    mo.stop(
        not start_analysis.value,
        mo.Html("""
        <div class="cyp-note">
          <strong>Analysis is paused.</strong><br>
          Click <strong>Start analysis</strong> above when you are ready to load the dataset and train the baseline model.
        </div>
        """),
    )
    mo.Html("""
        <div class="cyp-section">
            <div class="cyp-section__eyebrow">01 / foundation</div>
            <h2 class="cyp-section__title">Load and quality-control the dataset</h2>
            <div class="cyp-section__rule"></div>
        </div>
        """)
    df_raw = load_cyp_data()
    df_prepared = prepare_dataset(df_raw, smiles_column="standardized_smiles")
    df = filter_qc_passed(df_prepared)

    foundation_view = mo.Html(f"""
        <div class="cyp-status">
            <div class="cyp-status__mark">01</div>
            <div><p class="cyp-status__title">Dataset loaded successfully</p>
            <p class="cyp-status__detail">{len(df):,} QC-passed molecules are ready for scaffold-aware analysis.</p></div>
        </div>
    """)
    mo.Html(f"""
        <div class="cyp-metric-heading">Dataset snapshot</div>
        <div class="cyp-metric-grid">
            <div class="cyp-metric"><div class="cyp-metric__value">{len(df):,}</div><div class="cyp-metric__label">QC-passed molecules</div></div>
            <div class="cyp-metric"><div class="cyp-metric__value">{len(df_prepared):,}</div><div class="cyp-metric__label">Valid structures</div></div>
            <div class="cyp-metric"><div class="cyp-metric__value">{len(df.columns)}</div><div class="cyp-metric__label">Data columns</div></div>
            <div class="cyp-metric"><div class="cyp-metric__value">QC</div><div class="cyp-metric__label">Filter applied</div></div>
        </div>
        """)
    foundation_view
    return (df,)


# Cell 6
@app.cell(hide_code=True)
def _(df, extract_scaffolds, mo):
    df_scaffolds = extract_scaffolds(df)
    scaffold_stats = df_scaffolds['scaffold'].value_counts()
    scaffold_view = mo.vstack([
            mo.Html("""
            <div class="cyp-section">
                <div class="cyp-section__eyebrow">02 / chemical organization</div>
                <h2 class="cyp-section__title">Extract Bemis-Murcko scaffolds</h2>
                <div class="cyp-section__rule"></div>
            </div>
            """),
            mo.Html(f"""
            <div class="cyp-status">
                <div class="cyp-status__mark">02</div>
                <div><p class="cyp-status__title">Scaffolds extracted</p>
                <p class="cyp-status__detail">Molecules are grouped by their shared Bemis-Murcko core before any sampling or modeling.</p></div>
            </div>
            """),
            mo.Html(f"""
            <div class="cyp-metric-heading">Scaffolds Extracted</div>
            <div class="cyp-metric-grid">
                <div class="cyp-metric"><div class="cyp-metric__value">{len(scaffold_stats):,}</div><div class="cyp-metric__label">Unique scaffolds</div></div>
                <div class="cyp-metric"><div class="cyp-metric__value">{scaffold_stats.iloc[0]}</div><div class="cyp-metric__label">Largest scaffold</div></div>
                <div class="cyp-metric"><div class="cyp-metric__value">{scaffold_stats.median():.0f}</div><div class="cyp-metric__label">Median size</div></div>
                <div class="cyp-metric"><div class="cyp-metric__value">{(scaffold_stats >= 5).sum()}</div><div class="cyp-metric__label">Scaffolds with 5+ molecules</div></div>
            </div>
            """)
        ])

    scaffold_view
    return (df_scaffolds,)


# Cell 7
@app.cell(hide_code=True)
def _(CYP_ENDPOINT, df_scaffolds, mo, rank_cliff_scaffolds):
    top_scaffolds, df_ranked = rank_cliff_scaffolds(
        df_scaffolds,
        endpoint=CYP_ENDPOINT,
        top_k=50,
        min_molecules=3
    )

    # Guard: stop gracefully if no scaffolds meet the threshold
    mo.stop(
        len(top_scaffolds) == 0,
        mo.md("⚠️ **No scaffolds met the minimum molecule threshold.** Try lowering `min_molecules`.").callout(kind="danger")
    )

    display_scaffolds = top_scaffolds[['scaffold', 'n_molecules', 'avg_cliff_score']].copy()
    display_scaffolds['rank'] = range(1, len(display_scaffolds) + 1)
    display_scaffolds = display_scaffolds[['rank', 'scaffold', 'n_molecules', 'avg_cliff_score']]
    display_scaffolds.columns = ['Rank', 'Scaffold SMILES', 'Molecules', 'Cliff Score']

    cliff_view = mo.vstack([
            mo.Html("""
            <div class="cyp-section">
                <div class="cyp-section__eyebrow">03 / signal discovery</div>
                <h2 class="cyp-section__title">Rank the activity cliffs</h2>
                <div class="cyp-section__rule"></div>
            </div>
            """),
            mo.Html(f"""
            <div class="cyp-status">
                <div class="cyp-status__mark">03</div>
                <div><p class="cyp-status__title">Activity cliffs identified</p>
                <p class="cyp-status__detail">The ranking emphasizes high within-scaffold variance in CYP3A4 inhibition potency.</p></div>
            </div>
            """),
            mo.Html(f"""
            <div class="cyp-metric-heading">Activity Cliffs Identified</div>
            <div class="cyp-metric-grid">
                <div class="cyp-metric"><div class="cyp-metric__value">{CYP_ENDPOINT}</div><div class="cyp-metric__label">Endpoint analyzed</div></div>
                <div class="cyp-metric"><div class="cyp-metric__value">{len(top_scaffolds)}</div><div class="cyp-metric__label">Ranked candidates</div></div>
                <div class="cyp-metric"><div class="cyp-metric__value">Variance</div><div class="cyp-metric__label">Ranking signal</div></div>
                <div class="cyp-metric"><div class="cyp-metric__value">3+</div><div class="cyp-metric__label">Minimum molecules</div></div>
            </div>
            <div class="cyp-note">Select one ranked scaffold below to open its molecular neighborhood and inspect the activity cliff.</div>
            """)
        ])

    cliff_view
    return df_ranked, display_scaffolds, top_scaffolds


# Cell 8
@app.cell(hide_code=True)
def _(CYP_ENDPOINT, df_ranked, mo, train_cliff_models):
    auditor, train_df, test_df = train_cliff_models(
        df_ranked,
        endpoints=[CYP_ENDPOINT],
        test_size=0.2,
        random_state=42
    )

    metrics = auditor.get_metrics_summary()

    # Confirm zero scaffold overlap between train and test
    scaffold_overlap = len(set(train_df['scaffold']) & set(test_df['scaffold']))

    baseline_view = mo.vstack([
            mo.Html("""
            <div class="cyp-section">
                <div class="cyp-section__eyebrow">04 / honest baseline</div>
                <h2 class="cyp-section__title">Train the scaffold-isolated ML auditor</h2>
                <div class="cyp-section__rule"></div>
            </div>
            """),
            mo.Html(f"""
            <div class="cyp-status">
                <div class="cyp-status__mark">04</div>
                <div><p class="cyp-status__title">Model trained successfully</p>
                <p class="cyp-status__detail">One Random Forest was trained once on molecular descriptors with scaffold overlap checked explicitly.</p></div>
            </div>
            """),
            mo.Html(f"""
            <div class="cyp-metric-heading">Model Trained Successfully</div>
            <div class="cyp-metric-grid">
                <div class="cyp-metric"><div class="cyp-metric__value">{CYP_ENDPOINT}</div><div class="cyp-metric__label">Endpoint modeled</div></div>
                <div class="cyp-metric"><div class="cyp-metric__value">{len(train_df):,}</div><div class="cyp-metric__label">Train molecules / {train_df['scaffold'].nunique()} scaffolds</div></div>
                <div class="cyp-metric"><div class="cyp-metric__value">{len(test_df):,}</div><div class="cyp-metric__label">Test molecules / {test_df['scaffold'].nunique()} scaffolds</div></div>
                <div class="cyp-metric"><div class="cyp-metric__value">{scaffold_overlap}</div><div class="cyp-metric__label">Scaffold overlap</div></div>
            </div>
            <div class="cyp-note"><strong>Leakage check passed.</strong> The model is evaluated on held-out scaffolds it never saw during training.</div>
            """)
        ])

    baseline_view
    return auditor, metrics


# Cell 9
@app.cell(hide_code=True)
def _(metrics, mo):
    metrics_display = metrics.copy()
    metrics_display = metrics_display.round(3)
    mo.Html("""
        <div class="cyp-section">
            <div class="cyp-section__eyebrow">05 / measurement</div>
            <h2 class="cyp-section__title">Model performance metrics</h2>
            <div class="cyp-section__rule"></div>
        </div>
        """)
    return (metrics_display,)


# Cell 10
@app.cell(hide_code=True)
def _(metrics_display, mo):
    mo.ui.table(
        metrics_display,
        selection=None,
        label="Model Performance (RandomForest on Molecular Descriptors)"
    )
    return


# Cell 11
@app.cell(hide_code=True)
def _(mo):
    interactive_intro_view = mo.vstack([
    mo.Html("""
    <div class="cyp-section">
            <div class="cyp-section__eyebrow">06 / interactive investigation</div>
            <h2 class="cyp-section__title">Explore a cliff by scaffold and molecule</h2>
            <div class="cyp-section__rule"></div>
        </div>
    """),
    mo.md("""
    Now comes the interesting part. Select a scaffold from the table below to:

    1. **See its molecular variants** in an interactive network graph
    2. **Click any molecule** to see detailed structure comparison
    3. **Watch the model fail** on structurally similar molecules
    4. **Understand why** simple descriptors miss these cliffs

    The graph colors molecules by their actual experimental activity:
    - 🔴 Red = High activity
    - 🔵 Blue = Low activity

    Click any molecule node to see the detailed breakdown!
    """),
    ])

    interactive_intro_view
    return (interactive_intro_view,)


# Cell 12
@app.cell(hide_code=True)
def _(CYP_ENDPOINT, mo, rank_cliff_scaffolds, test_df):
    test_top_scaffolds, _ = rank_cliff_scaffolds(
        test_df,
        endpoint=CYP_ENDPOINT,
        top_k=15,
        min_molecules=3
    )

    if len(test_top_scaffolds) == 0:
        scaffold_selector = None
        scaffold_table_display = mo.md(
            "⚠️ **No test-set scaffolds meet `min_molecules=3`.** "
            "Try lowering `min_molecules` to 2."
        ).callout(kind="danger")
    else:
        test_display_scaffolds = test_top_scaffolds[['scaffold', 'n_molecules', 'avg_cliff_score']].copy()
        test_display_scaffolds['rank'] = range(1, len(test_display_scaffolds) + 1)
        test_display_scaffolds = test_display_scaffolds[['rank', 'scaffold', 'n_molecules', 'avg_cliff_score']]
        test_display_scaffolds.columns = ['Rank', 'Scaffold SMILES', 'Molecules', 'Cliff Score']

        scaffold_selector = mo.ui.table(
            test_display_scaffolds,
            selection="single",
            label="Select a held-out test scaffold to explore"
        )
        scaffold_table_display = scaffold_selector

    scaffold_table_display
    return (scaffold_selector, test_top_scaffolds)


# Cell 13
@app.cell(hide_code=True)
def _(mo, scaffold_selector, test_top_scaffolds):
    selected_scaffold_info = None
    selected_scaffold = None

    if scaffold_selector.value is not None and len(scaffold_selector.value) > 0:
        selected_scaffold = scaffold_selector.value.iloc[0]['Scaffold SMILES']
        scaffold_row = test_top_scaffolds[test_top_scaffolds['scaffold'] == selected_scaffold].iloc[0]

        selected_scaffold_info = mo.Html(f"""
        <div class="cyp-note">
        <strong>Selected scaffold</strong><br>
        <span style="font-size:0.86rem;color:#607080;"><strong>SMILES:</strong> {selected_scaffold}</span>

        <br><strong>Molecules:</strong> {scaffold_row['n_molecules']:.0f}
        &nbsp;&nbsp; <strong>Cliff score:</strong> {scaffold_row['avg_cliff_score']:.2f}
        </div>
        """)
    else:
        selected_scaffold_info = mo.md("👆 **Select a scaffold from the table above to begin exploration**")

    selected_scaffold_info
    return (selected_scaffold,)


# Cell 14
@app.cell(hide_code=True)
def _(CYP_ENDPOINT, create_scaffold_graph, df_ranked, mo, selected_scaffold):
    graph_widget = None
    graph_container = None

    if selected_scaffold:
        graph = create_scaffold_graph(
            df_ranked,
            scaffold=selected_scaffold,
            endpoint=CYP_ENDPOINT,
            max_molecules=30
        )

        graph_widget = mo.ui.anywidget(graph)

        graph_container = mo.vstack([
            mo.Html(f"""
                        <div class="cyp-section">
                            <div class="cyp-section__eyebrow">Scaffold neighborhood</div>
                            <h2 class="cyp-section__title">Molecular network</h2>
                            <div class="cyp-section__rule"></div>
                        </div>
            """),
            mo.md(f"""
            Center node = scaffold structure

            Outer nodes = variants colored by **{CYP_ENDPOINT}** activity

            🔴 Red = high activity | 🔵 Blue = low activity

            **Click any molecule node for detailed analysis** ⬇️
            """),
            graph_widget
        ])
    else:
        graph_container = mo.md("")

    graph_container
    return (graph_widget,)


# Cell 15
@app.cell(hide_code=True)
def _(df_ranked, get_selected_molecule_data, graph_widget, mo, pd):
    selected_molecule = None
    molecule_data = None

    if graph_widget and graph_widget.value:
        graph_obj = graph_widget.widget
        molecule_data = get_selected_molecule_data(graph_obj, df_ranked)

        if molecule_data:
            selected_molecule = molecule_data['smiles']
            val = molecule_data.get('value')
            val_str = f"{val:.2f}" if pd.notna(val) and val is not None else "N/A (Not Tested)"

            display_info = mo.Html(f"""
            <div class="cyp-note">
            <strong>Molecule selected</strong><br>
            <span style="font-size:0.86rem;color:#607080;"><strong>SMILES:</strong> {selected_molecule}</span>

            <br><strong>{molecule_data['endpoint']}:</strong> {val_str}
            </div>
            """)
        else:
            display_info = mo.md("_Click a molecule node in the graph above_")
    else:
        display_info = mo.md("_Waiting for graph interaction..._")

    display_info
    return molecule_data, selected_molecule


# Cell 16
@app.cell(hide_code=True)
def _(
    create_3d_viewer,
    df_ranked,
    highlight_structure_difference,
    mo,
    molecule_data,
    np,
    selected_molecule,
    selected_scaffold,
):
    comparison_container = None
    analog_smiles = None
    endpoint = None
    selected_value = None

    if selected_molecule and molecule_data:
        endpoint = molecule_data['endpoint']
        selected_value = molecule_data['value']

        if selected_value is None:
            comparison_container = mo.md(
                f"⚠️ **Missing Data:** The selected molecule (`{selected_molecule}`) was not tested for {endpoint} activity. "
                "Please click a colored node (Red or Blue) to analyze an activity cliff."
            ).callout(kind="warn")
        else:
            scaffold_mols = df_ranked[df_ranked['scaffold'] == selected_scaffold].copy()
            scaffold_mols = scaffold_mols[scaffold_mols['canonical_smiles'] != selected_molecule]
            scaffold_mols = scaffold_mols[scaffold_mols[endpoint].notna()]

            if len(scaffold_mols) > 0:
                scaffold_mols['activity_diff'] = np.abs(scaffold_mols[endpoint] - selected_value)
                scaffold_mols = scaffold_mols.sort_values('activity_diff', ascending=False)

                analog = scaffold_mols.iloc[0]
                analog_smiles = analog['canonical_smiles']
                analog_value = analog[endpoint]

                structure_img = highlight_structure_difference(selected_molecule, analog_smiles, selected_value, analog_value, endpoint=endpoint)

                viewer_selected = create_3d_viewer(selected_molecule, color_scheme="cyanCarbon", w=320, h=280)
                viewer_analog = create_3d_viewer(analog_smiles, color_scheme="magentaCarbon", w=320, h=280)

                activity_delta = selected_value - analog_value
                selected_is_more_potent = activity_delta > 0
                equal_potency = np.isclose(activity_delta, 0.0)
                potency_ratio = 10 ** abs(activity_delta)
                if equal_potency:
                    potency_statement = f"The molecule with pIC50 {selected_value:.2f} and the molecule with pIC50 {analog_value:.2f} have the same measured potency in this calculation."
                elif selected_is_more_potent:
                    potency_statement = f"The molecule with pIC50 {selected_value:.2f} shows much stronger measured CYP3A4 inhibitory potency than the molecule with pIC50 {analog_value:.2f}. The {activity_delta:.2f}-log-unit difference corresponds to an approximately {potency_ratio:,.0f}-fold difference in the implied IC50 values."
                else:
                    potency_statement = f"The molecule with pIC50 {analog_value:.2f} shows much stronger measured CYP3A4 inhibitory potency than the molecule with pIC50 {selected_value:.2f}. The {abs(activity_delta):.2f}-log-unit difference corresponds to an approximately {potency_ratio:,.0f}-fold difference in the implied IC50 values."

                potency_callout = mo.md(
                    f"""
                    **Potency calculation from the measured `{endpoint}` values**

                    A higher pIC50 means higher potency because pIC50 is the negative logarithm of IC50:

                    $$\\Delta\\mathrm{{pIC}}_{{50}} = pIC50_{{selected}} - pIC50_{{analog}} = {selected_value:.2f} - {analog_value:.2f} = {activity_delta:.2f}$$
                    $$\\text{{IC50 ratio}} = 10^{{|\\Delta\\mathrm{{pIC}}_{{50}}|}} = 10^{{|{activity_delta:.2f}|}} \\approx {potency_ratio:,.0f}$$

                    {potency_statement}

                    This is a potency ratio inferred from the logarithmic pIC50 difference. It does not claim a mechanism or a specific binding pose.
                    """
                ).callout(kind="info")

                comparison_container = mo.vstack([
                    mo.Html(f"""
                    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-top: 20px;">
                        <div class="cyp-section__eyebrow">Structural evidence</div>
                        <h3 style="margin: 5px 0 8px; color: #17212b; font-size: 1.35rem;">The activity cliff, visualized</h3>
                        <p style="color: #475569; margin-bottom: 16px;"><strong>Red highlights (left)</strong> mark the exact structural differences. <strong>Spin the 3D models (right)</strong> to physically inspect how this tiny change alters the topology and breaks enzyme binding.</p>
                        <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                            <tr style="border-bottom: 2px solid #e2e8f0;">
                                <th style="text-align: left; padding: 8px;">Molecule</th>
                                <th style="text-align: right; padding: 8px;">{endpoint} Activity</th>
                                <th style="text-align: right; padding: 8px;">Difference</th>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0;">
                                <td style="padding: 8px;"><strong>Selected Variant (Cyan)</strong></td>
                                <td style="text-align: right; padding: 8px; font-weight: bold; color: #0284c7;">{selected_value:.2f}</td>
                                <td style="text-align: right; padding: 8px;">-</td>
                            </tr>
                            <tr>
                                <td style="padding: 8px;"><strong>Comparison Analog (Magenta)</strong></td>
                                <td style="text-align: right; padding: 8px; font-weight: bold; color: #c026d3;">{analog_value:.2f}</td>
                                <td style="text-align: right; padding: 8px; font-weight: bold; color: #dc2626;">{abs(selected_value - analog_value):.2f}</td>
                            </tr>
                        </table>
                    </div>
                    """),
                    potency_callout,
                    mo.hstack([
                        mo.vstack([mo.md("**2D Structural Difference**").center(), mo.image(structure_img) if structure_img else mo.md("")]),
                        mo.vstack([mo.md("**3D: Selected Variant**").center(), mo.Html(viewer_selected)]),
                        mo.vstack([mo.md("**3D: Comparison Analog**").center(), mo.Html(viewer_analog)])
                    ], justify="space-around", align="center")
                ])
            else:
                comparison_container = mo.md("_No suitable analog found for comparison_").callout(kind="warn")
    else:
        comparison_container = mo.md("👈 **Select a colored node from the network graph above to reveal its 3D Activity Cliff analysis.**").callout(kind="info")

    comparison_container
    return endpoint, selected_value


# Cell 17
@app.cell(hide_code=True)
def _(
    auditor,
    create_dumbbell_chart,
    endpoint,
    mo,
    selected_molecule,
    selected_value,
):
    prediction_container = None

    if selected_molecule and endpoint:
        if selected_value is None:
            prediction_container = mo.md("")
        else:
            predicted = auditor.predict_molecule(selected_molecule, endpoint)

            if predicted is not None:
                error = abs(predicted - selected_value)
                prediction_delta = predicted - selected_value
                implied_ic50_ratio = 10 ** error
                predicted_more_potent = prediction_delta > 0
                prediction_direction = "higher predicted potency" if predicted_more_potent else "lower predicted potency" if prediction_delta < 0 else "the same predicted potency"

                dumbbell = create_dumbbell_chart(
                    predicted=predicted,
                    actual=selected_value,
                    endpoint=endpoint,
                    molecule_name="Selected Variant"
                )

                prediction_container = mo.vstack([
                    mo.Html(f"""
                                        <div class="cyp-section">
                                            <div class="cyp-section__eyebrow">07 / failure analysis</div>
                                            <h2 class="cyp-section__title">Model audit: why descriptors fail</h2>
                                            <div class="cyp-section__rule"></div>
                                        </div>
                    """),
                    mo.md(f"""
                    We are now auditing the **Selected Variant** (`{selected_molecule}`).

                    | Metric | Value |
                    |--------|-------|
                    | **Model Predicted** | {predicted:.2f} |
                    | **Experimental Reality** | {selected_value:.2f} |
                    | **Error** | **{error:.2f}** |

                    Our RandomForest model was trained strictly on 1D/2D global descriptors (MolWt, LogP, TPSA). Because it cannot "see" the 3D topology we just witnessed above, it completely fails to predict the cliff.
                    """),
                    mo.md(
                        f"""
                        **Prediction versus experiment, calculated in pIC50 space**

                        $$\\mathrm{{Prediction\\ error}} = |pIC50_{{predicted}} - pIC50_{{actual}}| = |{predicted:.2f} - {selected_value:.2f}| = {error:.2f}$$
                        $$\\text{{IC50 ratio represented by this gap}} = 10^{{{error:.2f}}} \\approx {implied_ic50_ratio:,.0f}$$

                        The model gives **{predicted:.2f} pIC50** and the assay reports **{selected_value:.2f} pIC50**. That means the model has **{prediction_direction}** than the measured result, with an absolute error of **{error:.2f} pIC50 units**.

                        The fold value is the IC50 ratio corresponding to the logarithmic error; it is not a claim that the model has measured IC50 directly.
                        """
                    ).callout(kind="info"),
                    mo.ui.altair_chart(dumbbell)
                ])
            else:
                prediction_container = mo.md("_Prediction failed - molecule may be missing descriptors_")
    else:
        prediction_container = mo.md("")

    prediction_container
    return


# Cell 18
@app.cell(hide_code=True)
def _(auditor, create_global_scatter, endpoint, mo, top_scaffolds):
    global_chart_container = None

    if endpoint:
        results_df = auditor.get_test_results(endpoint=endpoint)
        global_chart = create_global_scatter(
            results_df,
            endpoint=endpoint,
            cliff_scaffolds=top_scaffolds['scaffold'].tolist(),
            color_cliff_molecules=True
        )

        global_chart_container = mo.vstack([
            mo.Html(f"""
                        <div class="cyp-section">
                            <div class="cyp-section__eyebrow">08 / population-level proof</div>
                            <h2 class="cyp-section__title">Global model performance</h2>
                            <div class="cyp-section__rule"></div>
                        </div>
            """),
            mo.md(f"""
            The scatter plot below shows **all held-out test molecules**.

            Hover over any data point to inspect its 2D chemical structure in real time.
            """),
            global_chart
        ])
    else:
        global_chart_container = mo.md("")

    global_chart_container
    return


# Cell 19
@app.cell(hide_code=True)
def _(mo):
    closing_view = mo.Html("""
        <div class="cyp-section">
            <div class="cyp-section__eyebrow">09 / closing record</div>
            <h2 class="cyp-section__title">What this notebook demonstrates</h2>
            <div class="cyp-section__rule"></div>
        </div>

                <div class="cyp-closing-block">
                    <h3 class="cyp-closing-heading">What this does and demonstrates</h3>
                    <p class="cyp-closing-copy">This notebook turns measured CYP3A4 inhibition data into an inspectable cheminformatics workflow. It ranks activity-cliff candidates, lets readers explore related molecules, and compares experimental activity with a simple descriptor-based model.</p>
                    <ul class="cyp-closing-list">
                        <li>It demonstrates how structurally related molecules can have substantially different measured activities.</li>
                        <li>It connects scaffold ranking, 2D differences, 3D views, and model error in one interactive path.</li>
                        <li>It demonstrates why held-out scaffold evaluation is more informative here than relying only on random splits.</li>
                    </ul>
                </div>

                <div class="cyp-closing-block">
                    <h3 class="cyp-closing-heading">How it helps</h3>
                    <p class="cyp-closing-copy">The explorer helps researchers inspect model blind spots instead of hiding them behind a single aggregate score. It supports hypothesis generation and method education; it is not a clinical, regulatory, or production prediction system.</p>
                </div>

                <div class="cyp-closing-block">
                    <h3 class="cyp-closing-heading">Acknowledgements and project links</h3>
                    <p class="cyp-closing-copy">Built with the following open tools, data sources, and project resources:</p>
                    <div class="cyp-closing-links">
                        <a href="https://github.com/Mohit5Upadhyay/cyp-activity-cliff-explorer-molab">Project repository</a>
                        <a href="https://molab.marimo.io/notebooks">Open the molab notebook workspace</a>
                        <a href="https://marimo.io/pages/events/notebook-competition-3">molab Notebook Competition #3</a>
                        <a href="https://huggingface.co/datasets/openadmet/Octant_CYP_inhibition_reactivity_blog_release">OpenADMET Octant CYP inhibition dataset</a>
                        <a href="https://www.rdkit.org/">RDKit cheminformatics toolkit</a>
                        <a href="https://marimo.io/">marimo reactive notebook framework</a>
                        <a href="https://github.com/koaning/wigglystuff">wigglystuff interactive widgets</a>
                        <a href="https://scikit-learn.org/">scikit-learn model utilities</a>
                    </div>
                </div>

                <div class="cyp-disclosure-wide">
                    <div class="cyp-disclosure-wide__mark">AI</div>
                    <div>
                        <p class="cyp-disclosure-wide__title">AI disclosure</p>
                        <p class="cyp-disclosure-wide__copy">The original writing, notebook structure, and ideas behind the visualizations and interactive experiences came from the author. Claude Sonnet 5 and Gemini 3.1 Pro assisted with refinement, UI composition, debugging. </p>
                    </div>
                </div>
        """)
    closing_view
    return (closing_view,)


if __name__ == "__main__":
    app.run()
