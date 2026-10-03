# Wine Quality Assessment — Exploratory Data Analysis (EDA)

An exploratory data analysis project examining the physicochemical properties of red and white wine variants to identify key drivers of perceived wine quality.

---

## 📌 Project Overview

This script merges red and white wine datasets, analyzes the distributions of physicochemical variables, explores relationships between features and wine quality, and exports publication-ready visualizations.

### Key Analysis Highlights
- **Dataset Integration:** Combines red and white wine samples into a unified dataset with wine-type labeling.
- **Visual Analytics:** Generates 9 distinct charts covering feature distributions, type comparisons, and correlation analysis.
- **Automated Export:** Automatically exports all generated figures as high-resolution PNGs (`300 DPI`) into a local directory.

---

## 📊 Generated Visualizations

All plots are automatically saved to the `graphs/` directory:

| Filename | Description |
|---|---|
| `01_wine_type_distribution.png` | Sample count comparison between red and white wines |
| `02_quality_distribution.png` | Distribution of wine quality ratings |
| `03_alcohol_vs_quality.png` | Scatter plot evaluating alcohol content against quality |
| `04_volatile_acidity_vs_quality.png` | Scatter plot evaluating volatile acidity against quality |
| `05_alcohol_by_wine_type.png` | Box plot showing alcohol content across wine types |
| `06_average_quality_by_type.png` | Bar chart comparing mean quality scores by wine type |
| `07_alcohol_distribution.png` | Histogram illustrating global alcohol distribution |
| `08_correlation_matrix.png` | Heatmap depicting correlations across all numeric features |
| `09_quality_by_alcohol_range.png` | Average quality score binned across distinct alcohol brackets |

---

## 📁 Repository Structure

```text
├── Wine_Quality_assesment_EDA_project.py
├── winequality-red.xlsx
├── winequality-white.xlsx
├── graphs/
│   ├── 01_wine_type_distribution.png
│   └── ...
└── README.md
