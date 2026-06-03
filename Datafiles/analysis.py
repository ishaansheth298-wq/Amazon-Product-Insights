import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("amazon.csv")

# Clean Rating Column
data["rating"] = pd.to_numeric(data["rating"], errors="coerce")
data = data.dropna(subset=["rating"])

print("=" * 50)
print("TOP RATED PRODUCTS")
print("=" * 50)

top_products = data.sort_values(
    by="rating",
    ascending=False
)

print(top_products[["product_name", "rating"]].head(10))

print("\n")

print("=" * 50)
print("HIGHEST DISCOUNTS")
print("=" * 50)

top_discount = data.sort_values(
    by="discount_percentage",
    ascending=False
)

print(
    top_discount[
        ["product_name", "discount_percentage"]
    ].head(10)
)

print("\n")

print("=" * 50)
print("CATEGORY ANALYSIS")
print("=" * 50)

category_rating = (
    data.groupby("category")["rating"]
    .mean()
    .sort_values(ascending=False)
)

print(category_rating.head(10))

# Visualization
top_categories = category_rating.head(10)

top_categories.plot(kind="bar")

plt.title("Top 10 Categories by Average Rating")
plt.ylabel("Average Rating")

plt.show()
