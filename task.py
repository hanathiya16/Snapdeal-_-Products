=========================================================
TASK 1: PRICE vs DISCOUNT (Scatter + 2D Histogram)
 =========================================================
import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, linregress
from dataclasses import dataclass
from typing import Dict, List

random.seed(123)

price = [math.exp(random.gauss(5.5, 0.6)) for _ in range(1000)]
discount = [
    max(0, min(50, 20 - 0.003 * p + random.gauss(0, 2)))
    for p in price
]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].scatter(price, discount, alpha=0.5)
axes[0].set_title("Price vs Discount")
axes[0].set_xlabel("Price")
axes[0].set_ylabel("Discount (%)")

axes[1].hist2d(price, discount, bins=40)
plt.colorbar(axes[1].collections[0], ax=axes[1])
axes[1].set_title("Discount Density")

plt.tight_layout()
plt.show()


 =========================================================
TASK 2: STYLED DATAFRAME (DISCOUNT & RATING)
 =========================================================
df_style = pd.DataFrame([
    {"Product": "A", "Price": 10.0, "Discount": 0.60, "Rating": 4.2},
    {"Product": "B", "Price": 15.0, "Discount": 0.05, "Rating": 2.7},
    {"Product": "C", "Price": 20.0, "Discount": 0.20, "Rating": 2.9},
])

def discount_style(v):
    if v > 0.5:
        return "background-color: green; color: white"
    if v < 0.1:
        return "background-color: red; color: white"
    return ""

def rating_style(v):
    if v < 3:
        return "background-color: orange; color: white"
    return ""

styled_df = (
    df_style.style
    .applymap(discount_style, subset=["Discount"])
    .applymap(rating_style, subset=["Rating"])
    .format({"Price": "${:.2f}", "Discount": "{:.0%}"})
)

print("\nStyled DataFrame created (works in Jupyter Notebook)")


 =========================================================
 TASK 3: PRICE vs RATING (BUBBLE + CORRELATION)
 =========================================================
np.random.seed(0)

df = pd.DataFrame({
    "subcategory": np.random.choice([f"subcat_{i}" for i in range(1, 21)], 1000),
    "price": np.random.lognormal(3.0, 0.8, 1000),
    "rating": np.clip(np.random.normal(4.0, 0.6, 1000), 1, 5)
})

grp = df.groupby("subcategory").agg(
    avg_price=("price", "mean"),
    avg_rating=("rating", "mean"),
    count=("rating", "size"),
    sd_rating=("rating", "std")
).reset_index()

sns.scatterplot(
    data=grp, x="avg_price", y="avg_rating",
    size="count", hue="count", sizes=(40, 400),
    palette="viridis"
)

plt.xscale("log")
plt.title("Average Price vs Rating")
plt.show()

pr, _ = pearsonr(np.log(grp["avg_price"]), grp["avg_rating"])
sr, _ = spearmanr(grp["avg_price"], grp["avg_rating"])
print(f"Pearson: {pr:.3f}, Spearman: {sr:.3f}")


 =========================================================
TASK 4: DISCOUNT vs RATING ANALYSIS
 =========================================================
np.random.seed(42)

df2 = pd.DataFrame({
    "Discount": np.random.uniform(0, 50, 1000)
})
df2["Rating"] = np.clip(3 + 0.01 * df2["Discount"] + np.random.normal(0, 1, 1000), 1, 5)

corr, p = pearsonr(df2["Discount"], df2["Rating"])
print(f"Correlation: {corr:.3f}, P-value: {p:.3f}")

plt.scatter(df2["Discount"], df2["Rating"], alpha=0.4)
plt.xlabel("Discount (%)")
plt.ylabel("Rating")
plt.title("Rating vs Discount")
plt.show()


 =========================================================
TASK 5: DISCOUNT TREND OVER TIME
 =========================================================
dates = pd.date_range("2025-01-01", periods=90)
df_time = pd.DataFrame({
    "date": dates,
    "discount": np.random.uniform(5, 30, 90)
})

daily_avg = df_time.groupby("date")["discount"].mean().reset_index()

plt.plot(daily_avg["date"], daily_avg["discount"])
plt.title("Discount Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Discount (%)")
plt.show()


 =========================================================
TASK 6: KPI ANALYSIS & BUSINESS INSIGHTS
 =========================================================
@dataclass
class KPIMetrics:
    average_price: float = 950
    average_discount: float = 40
    average_rating: float = 3.8

    def __post_init__(self):
        self.effective_price = self.average_price * (1 - self.average_discount / 100)

class KPIAnalyzer:
    def __init__(self, kpis: KPIMetrics):
        self.kpis = kpis

    def run(self):
        print("\n" + "=" * 60)
        print("E-COMMERCE KPI ANALYSIS")
        print("=" * 60)

        loss = self.kpis.average_price - self.kpis.effective_price
        print(f"Price          : ${self.kpis.average_price}")
        print(f"Discount       : {self.kpis.average_discount}%")
        print(f"Effective Price: ${self.kpis.effective_price}")
        print(f"Loss / Unit    : ${loss}")

        rating_pct = (self.kpis.average_rating / 5) * 100
        print(f"Rating         : {self.kpis.average_rating} ({rating_pct:.1f}%)")

        print("\nRecommendations:")
        print("1. Reduce discount to 25–30%")
        print("2. Improve quality & delivery")
        print("3. Use targeted discounts")

kpis = KPIMetrics()
KPIAnalyzer(kpis).run()