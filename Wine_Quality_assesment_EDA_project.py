import pandas as pd
import matplotlib.pyplot as plt
import os
# Load data
red = pd.read_excel("winequality-red.xlsx")
white = pd.read_excel("winequality-white.xlsx")
# Add wine type
red["wine_type"] = "Red"
white["wine_type"] = "White"
# Combine datasets
wine = pd.concat([red, white], ignore_index=True)
# Create graphs folder
os.makedirs("graphs", exist_ok=True)
# 1. Wine Type Distribution
wine_type_count = wine["wine_type"].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(wine_type_count.index, wine_type_count.values)
plt.title("Wine Type Distribution")
plt.xlabel("Wine Type")
plt.ylabel("Number of Samples")
plt.tight_layout()
plt.savefig("graphs/01_wine_type_distribution.png", dpi=300)
plt.show()
# 2. Wine Quality Distribution
quality_count = wine["quality"].value_counts().sort_index()
plt.figure(figsize=(8, 5))
plt.bar(quality_count.index.astype(str), quality_count.values)
plt.title("Wine Quality Distribution")
plt.xlabel("Quality Score")
plt.ylabel("Number of Samples")
plt.tight_layout()
plt.savefig("graphs/02_quality_distribution.png", dpi=300)
plt.show()
# 3. Alcohol vs Quality
plt.figure(figsize=(8, 5))
plt.scatter(wine["alcohol"], wine["quality"], alpha=0.25, s=12)
plt.title("Alcohol vs Wine Quality")
plt.xlabel("Alcohol")
plt.ylabel("Quality")
plt.tight_layout()
plt.savefig("graphs/03_alcohol_vs_quality.png", dpi=300)
plt.show()
# 4. Volatile Acidity vs Quality
plt.figure(figsize=(8, 5))
plt.scatter(wine["volatile acidity"], wine["quality"], alpha=0.25, s=12)
plt.title("Volatile Acidity vs Wine Quality")
plt.xlabel("Volatile Acidity")
plt.ylabel("Quality")
plt.tight_layout()
plt.savefig("graphs/04_volatile_acidity_vs_quality.png", dpi=300)
plt.show()
# 5. Alcohol Distribution by Wine Type
plt.figure(figsize=(8, 5))
plt.boxplot(
    [red["alcohol"].dropna(), white["alcohol"].dropna()],
    tick_labels=["Red", "White"]
)
plt.title("Alcohol Distribution by Wine Type")
plt.xlabel("Wine Type")
plt.ylabel("Alcohol")
plt.tight_layout()
plt.savefig("graphs/05_alcohol_by_wine_type.png", dpi=300)
plt.show()
# 6. Average Quality by Wine Type
average_quality = wine.groupby("wine_type")["quality"].mean()
plt.figure(figsize=(8, 5))
plt.bar(average_quality.index, average_quality.values)
plt.title("Average Quality by Wine Type")
plt.xlabel("Wine Type")
plt.ylabel("Average Quality")
plt.tight_layout()
plt.savefig("graphs/06_average_quality_by_type.png", dpi=300)
plt.show()
# 7. Alcohol Distribution
plt.figure(figsize=(8, 5))
plt.hist(wine["alcohol"], bins=30)
plt.title("Alcohol Distribution")
plt.xlabel("Alcohol")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("graphs/07_alcohol_distribution.png", dpi=300)
plt.show()
# 8. Correlation Matrix
correlation = wine.drop(columns=["wine_type"]).corr(numeric_only=True)
plt.figure(figsize=(10, 8))
plt.imshow(correlation, aspect="auto")
plt.colorbar(label="Correlation")
plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=70,
    ha="right"
)
plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)
plt.title("Correlation Matrix of Wine Variables")
plt.tight_layout()
plt.savefig("graphs/08_correlation_matrix.png", dpi=300)
plt.show()
# 9. Quality by Alcohol Range
wine["alcohol_group"] = pd.cut(
    wine["alcohol"],
    bins=[0, 9, 10, 11, 12, 13, 15],
    labels=["£9", "9–10", "10–11", "11–12", "12–13", "13–15"],
    include_lowest=True
)
average_quality_alcohol = wine.groupby(
    "alcohol_group",
    observed=False
)["quality"].mean()
plt.figure(figsize=(9, 5))
plt.bar(
    average_quality_alcohol.index.astype(str),
    average_quality_alcohol.values
)
plt.title("Average Quality by Alcohol Range")
plt.xlabel("Alcohol Range")
plt.ylabel("Average Quality")
plt.tight_layout()
plt.savefig("graphs/09_quality_by_alcohol_range.png", dpi=300)
plt.show()
# Summary
print("Total observations:", len(wine))
print("Red wine observations:", len(red))
print("White wine observations:", len(white))
print("Number of features:", len(wine.columns) - 2)
print("Target variable: quality")
print("Missing values:", wine.isna().sum().sum())
print("\nAverage Quality:")
print(wine.groupby("wine_type")["quality"].mean())
print("\nQuality Distribution:")
print(wine["quality"].value_counts().sort_index())