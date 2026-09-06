"""
CodeAlpha Data Analytics Internship — Task 3: Data Visualization
Dataset : Titanic passenger data (data/titanic.csv)
Author  : Naveed Ali

This script turns the raw dataset into a set of polished, story-driven
visuals (per the task checklist):
- Transform raw data into charts/graphs/dashboard.
- Use Matplotlib & Seaborn to create the visuals.
- Design visuals that clearly reveal insight (direct labels, annotations,
  consistent color story).
- Tie the charts together into one narrative: "Who survived the Titanic,
  and why?"

Run with:  python3 visualize_titanic.py
Outputs  : PNG charts in ./outputs, plus outputs/dashboard.html which
           combines them into a single portfolio-ready page.
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import os

# ---------------------------------------------------------------
# SETUP
# ---------------------------------------------------------------
DATA_PATH = "data/titanic.csv"
OUT_DIR = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid", font_scale=1.05)
PALETTE = {"died": "#B0BEC5", "survived": "#2E8B8B"}
CLASS_PALETTE = "crest"
ACCENT = "#2E8B8B"

df = pd.read_csv(DATA_PATH)
df["Outcome"] = df["Survived"].map({0: "Died", 1: "Survived"})
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1


def annotate_bar_percentages(ax, fmt="{:.0f}%"):
    """Put a percentage label directly above each bar — no legend guessing."""
    for p in ax.patches:
        height = p.get_height()
        if pd.isna(height):
            continue
        ax.annotate(
            fmt.format(height * 100 if height <= 1 else height),
            (p.get_x() + p.get_width() / 2, height),
            ha="center", va="bottom", fontsize=10, fontweight="bold",
            xytext=(0, 3), textcoords="offset points",
        )


# ---------------------------------------------------------------
# CHART 1 — Hero chart: overall survival split (donut)
# ---------------------------------------------------------------
counts = df["Outcome"].value_counts()
fig, ax = plt.subplots(figsize=(6, 6))
wedges, _, autotexts = ax.pie(
    counts, labels=None, autopct="%1.0f%%", startangle=90,
    colors=[PALETTE["died"], PALETTE["survived"]],
    wedgeprops=dict(width=0.42, edgecolor="white"),
    pctdistance=0.8, textprops={"fontsize": 14, "fontweight": "bold", "color": "white"},
)
ax.legend(wedges, counts.index, loc="center", fontsize=13, frameon=False)
ax.set_title("Only 38% of Titanic Passengers Survived", fontsize=15, fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/01_overall_survival.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# CHART 2 — Survival rate by class (with % labels)
# ---------------------------------------------------------------
by_class = df.groupby("Pclass")["Survived"].mean().reset_index()
fig, ax = plt.subplots(figsize=(7, 5))
sns.barplot(x="Pclass", y="Survived", data=by_class, palette=CLASS_PALETTE, ax=ax)
annotate_bar_percentages(ax)
ax.set_title("1st Class Passengers Were 2.5x More Likely to Survive Than 3rd Class",
             fontsize=13, fontweight="bold")
ax.set_xlabel("Passenger Class")
ax.set_ylabel("Survival Rate")
ax.set_xticklabels(["1st Class", "2nd Class", "3rd Class"])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
ax.set_ylim(0, 0.75)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/02_survival_by_class.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# CHART 3 — Survival rate by sex (with % labels)
# ---------------------------------------------------------------
by_sex = df.groupby("Sex")["Survived"].mean().reset_index()
fig, ax = plt.subplots(figsize=(6, 5))
sns.barplot(x="Sex", y="Survived", data=by_sex, palette=["#F4A6A6", "#7FB3D5"], ax=ax)
annotate_bar_percentages(ax)
ax.set_title('"Women and Children First" Held True: Women Survived at 4x the Rate of Men',
             fontsize=12, fontweight="bold")
ax.set_xlabel("")
ax.set_ylabel("Survival Rate")
ax.set_xticklabels(["Female", "Male"])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
ax.set_ylim(0, 1)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/03_survival_by_sex.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# CHART 4 — Class x Sex combined (the strongest single insight)
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="Pclass", y="Survived", hue="Sex", data=df, palette=["#F4A6A6", "#7FB3D5"], ax=ax, errorbar=None)
annotate_bar_percentages(ax)
ax.set_title("Being a Woman Mattered More Than Class — But Both Compounded Survival Odds",
             fontsize=12, fontweight="bold")
ax.set_xlabel("Passenger Class")
ax.set_ylabel("Survival Rate")
ax.set_xticklabels(["1st Class", "2nd Class", "3rd Class"])
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
ax.set_ylim(0, 1.1)
ax.legend(title="Sex")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/04_survival_by_class_and_sex.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# CHART 5 — Age distribution by outcome
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
sns.kdeplot(data=df, x="Age", hue="Outcome", fill=True, common_norm=False,
            palette=[PALETTE["died"], PALETTE["survived"]], alpha=0.55, ax=ax)
ax.axvspan(0, 10, color="gold", alpha=0.15)
ax.text(5, ax.get_ylim()[1] * 0.92, "Children", ha="center", fontsize=10,
        fontweight="bold", color="#8a7000")
ax.set_title("Young Children Had a Visible Survival Edge Over Other Age Groups",
             fontsize=12, fontweight="bold")
ax.set_xlabel("Age")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/05_age_distribution.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# CHART 6 — Fare vs Age scatter, colored by outcome, sized by class
# ---------------------------------------------------------------
size_map = {1: 140, 2: 70, 3: 30}
df["_size"] = df["Pclass"].map(size_map)
fig, ax = plt.subplots(figsize=(8, 5.5))
for outcome, color in zip(["Died", "Survived"], [PALETTE["died"], PALETTE["survived"]]):
    sub = df[df["Outcome"] == outcome]
    ax.scatter(sub["Age"], sub["Fare"], s=sub["_size"], c=color, alpha=0.6,
               label=outcome, edgecolors="white", linewidth=0.4)
ax.set_ylim(0, 300)
ax.set_title("Higher Fares (a Proxy for Class) Cluster With Survival",
             fontsize=12, fontweight="bold")
ax.set_xlabel("Age")
ax.set_ylabel("Fare Paid")
ax.legend(title="Outcome", loc="upper right")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/06_fare_vs_age_scatter.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# CHART 7 — Survival rate by family size
# ---------------------------------------------------------------
by_family = df.groupby("FamilySize")["Survived"].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.lineplot(x="FamilySize", y="Survived", data=by_family, marker="o",
             color=ACCENT, linewidth=2.5, markersize=8, ax=ax)
ax.axvspan(2, 4, color=ACCENT, alpha=0.08)
ax.text(3, 0.05, "Sweet spot:\nfamilies of 2-4", ha="center", fontsize=9,
        color=ACCENT, fontweight="bold")
ax.set_title("Traveling Alone or in a Large Family Both Lowered Survival Odds",
             fontsize=12, fontweight="bold")
ax.set_xlabel("Family Size (Self + Siblings/Spouses + Parents/Children)")
ax.set_ylabel("Survival Rate")
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
ax.set_xticks(sorted(df["FamilySize"].unique()))
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/07_survival_by_family_size.png", dpi=150)
plt.close()

print("All 7 story-driven charts saved to ./outputs")

# ---------------------------------------------------------------
# BUILD A SINGLE-PAGE HTML DASHBOARD THAT TELLS THE FULL STORY
# ---------------------------------------------------------------
cards = [
    ("01_overall_survival.png", "The Baseline",
     "Out of 891 passengers on board, only 38% survived — this is the number every other chart below explains."),
    ("02_survival_by_class.png", "Class Mattered",
     "1st class passengers survived at roughly 63%, more than double the ~24% survival rate in 3rd class — likely tied to cabin location and lifeboat access."),
    ("03_survival_by_sex.png", "Gender Mattered More",
     "Women survived at about 74% versus roughly 19% for men, reflecting the 'women and children first' evacuation protocol."),
    ("04_survival_by_class_and_sex.png", "The Two Factors Compound",
     "A woman in 1st class had the best odds by far; a man in 3rd class had the worst — class and gender stack on top of each other."),
    ("05_age_distribution.png", "Children Had an Edge",
     "The survival-density curve skews younger — children under 10 show a visibly better survival rate than most other age bands."),
    ("06_fare_vs_age_scatter.png", "Fare as a Class Proxy",
     "Higher-fare tickets (bigger dots = higher class) cluster more with survival, reinforcing that wealth and class access shaped outcomes."),
    ("07_survival_by_family_size.png", "The Family-Size Sweet Spot",
     "Solo travelers and very large families (5+) fared worse than small families of 2-4 — small groups could coordinate and board together more easily."),
]

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Titanic Survival — Data Visualization Dashboard</title>
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f7f9fa; color: #23303a; margin: 0; padding: 0 0 60px 0; }
  header { background: linear-gradient(135deg, #1c3d3d, #2E8B8B); color: white; padding: 48px 24px 36px; text-align: center; }
  header h1 { margin: 0 0 8px; font-size: 2rem; }
  header p { margin: 0; opacity: 0.9; font-size: 1.05rem; }
  .container { max-width: 1000px; margin: 0 auto; padding: 32px 20px; }
  .card { background: white; border-radius: 14px; box-shadow: 0 2px 10px rgba(0,0,0,0.06); margin-bottom: 32px; overflow: hidden; }
  .card img { width: 100%; display: block; }
  .card-body { padding: 20px 26px 26px; }
  .card-body h2 { margin: 0 0 8px; font-size: 1.25rem; color: #1c3d3d; }
  .card-body p { margin: 0; line-height: 1.55; color: #445; }
  footer { text-align: center; color: #8a97a0; font-size: 0.85rem; margin-top: 20px; }
</style>
</head>
<body>
<header>
  <h1>🚢 Who Survived the Titanic — and Why?</h1>
  <p>A data story built from 891 passenger records | CodeAlpha Data Analytics Internship — Task 3</p>
</header>
<div class="container">
"""

for img, title, desc in cards:
    html += f"""  <div class="card">
    <img src="{img}" alt="{title}">
    <div class="card-body">
      <h2>{title}</h2>
      <p>{desc}</p>
    </div>
  </div>
"""

html += """</div>
<footer>Built with Python, Pandas, Matplotlib &amp; Seaborn — CodeAlpha Data Analytics Internship</footer>
</body>
</html>
"""

with open("outputs/dashboard.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Dashboard saved to outputs/dashboard.html — open it in a browser to view the full story.")
