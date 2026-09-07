# CodeAlpha Data Analytics Internship — Task 3: Data Visualization

## 📌 Overview
This project transforms the Titanic passenger dataset into a set of
**polished, story-driven visuals**, following CodeAlpha's Task 3 checklist:
using Matplotlib & Seaborn to design visuals that reveal insight clearly,
and tying them together into a single data story / mini-dashboard.

The whole project answers one question: **"Who survived the Titanic, and
why?"** — walking through class, gender, age, fare, and family size as
contributing factors.

## 🗂 Project Structure
```
CodeAlpha_DataVisualization/
│
├── data/
│   └── titanic.csv                      # Dataset used for the visuals
│
├── outputs/
│   ├── dashboard.html                    # ⭐ Single-page visual story (open in browser)
│   ├── 01_overall_survival.png
│   ├── 02_survival_by_class.png
│   ├── 03_survival_by_sex.png
│   ├── 04_survival_by_class_and_sex.png
│   ├── 05_age_distribution.png
│   ├── 06_fare_vs_age_scatter.png
│   └── 07_survival_by_family_size.png
│
├── visualize_titanic.py                  # Main script (run this)
├── requirements.txt
├── .gitignore
└── README.md
```

## ⭐ View the Dashboard
Open **`outputs/dashboard.html`** in any browser for the full visual story —
each chart is paired with a one-line insight, in narrative order.

## 📊 The Story, Chart by Chart
1. **The Baseline** — only 38% of the 891 passengers survived.
2. **Class Mattered** — 1st class survived at ~63% vs. ~24% in 3rd class.
3. **Gender Mattered More** — women survived at ~74% vs. ~19% for men.
4. **The Two Factors Compound** — a 1st-class woman had by far the best
   odds; a 3rd-class man had the worst.
5. **Children Had an Edge** — survivors skew younger; kids under 10 fared
   noticeably better.
6. **Fare as a Class Proxy** — higher fares (bigger, higher-class dots)
   cluster with survival.
7. **The Family-Size Sweet Spot** — small families (2-4 people) survived
   better than solo travelers or very large families.

## Dashboard Screenshots
<img width="892" height="767" alt="Screenshot 2026-09-07 220655" src="https://github.com/user-attachments/assets/0973d1bd-b702-4f7f-a00a-e3e6e31e10b5" />
<img width="880" height="706" alt="Screenshot 2026-09-07 220637" src="https://github.com/user-attachments/assets/1327715c-2224-4faf-ad03-9d03cce8f9ba" />
<img width="872" height="787" alt="Screenshot 2026-09-07 220608" src="https://github.com/user-attachments/assets/435b7f67-f014-45c0-ac65-f732439674ff" />
<img width="910" height="866" alt="Screenshot 2026-09-07 220549" src="https://github.com/user-attachments/assets/9bda1c4b-96e1-4b29-a04b-907df6c30e16" />



## ⚙️ How to Run This Project Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/<naveedali00>/CodeAlpha_DataVisualization.git
   cd CodeAlpha_DataVisualization
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the visualization script**
   ```bash
   python3 visualize_titanic.py
   ```

5. **View the results**
   - Open `outputs/dashboard.html` in your browser for the full story.
   - Individual PNG charts are also in `outputs/` if you want to embed them
     elsewhere (LinkedIn post, presentation, etc.).

## 🛠 Tools & Libraries Used
- Python 3
- Pandas — data prep and aggregation
- Matplotlib & Seaborn — chart creation
- HTML/CSS — combining the charts into a single-page dashboard

## 🎓 About
This project was completed as **Task 3 (Data Visualization)** for the
[CodeAlpha](https://www.codealpha.tech) Data Analytics Internship. It
builds on the dataset and findings from Task 2 (Exploratory Data Analysis).

## 📄 License
This project is for educational purposes as part of the CodeAlpha internship.
