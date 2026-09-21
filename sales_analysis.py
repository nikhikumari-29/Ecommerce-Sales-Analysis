import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Get the project folder path
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
file_path = BASE_DIR / "data" / "Superstore.csv"

# Load dataset
df = pd.read_csv(file_path)

# Display first 5 rows
print(df.head())

# Display dataset information
df.info()
# Check dataset shape
print("\nDataset Shape:")
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())
# -------------------------------
# DATA CLEANING
# -------------------------------

# Convert date columns to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Check updated data types
print("\nUpdated Data Types:")
print(df.dtypes)

# Create new columns for analysis
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()

# Display first 5 rows after cleaning
print("\nCleaned Dataset:")
print(df.head())
# -------------------------------
# KEY BUSINESS METRICS
# -------------------------------

# Total Sales
total_sales = df["Sales"].sum()

# Total Profit
total_profit = df["Profit"].sum()

# Total Orders
total_orders = df["Order ID"].nunique()

# Total Customers
total_customers = df["Customer ID"].nunique()

# Print business metrics
print("\n--- KEY BUSINESS METRICS ---")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
# -------------------------------
# CATEGORY-WISE ANALYSIS
# -------------------------------

category_sales = df.groupby("Category")[["Sales", "Profit"]].sum().sort_values(
    by="Sales", ascending=False
)

print("\n--- CATEGORY-WISE SALES & PROFIT ---")
print(category_sales)
# -------------------------------
# REGION-WISE ANALYSIS
# -------------------------------

region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values(
    by="Sales", ascending=False
)

print("\n--- REGION-WISE SALES & PROFIT ---")
print(region_analysis)
# -------------------------------
# YEAR-WISE ANALYSIS
# -------------------------------

year_analysis = df.groupby("Year")[["Sales", "Profit"]].sum()

print("\n--- YEAR-WISE SALES & PROFIT ---")
print(year_analysis)
# -------------------------------
# MONTHLY SALES ANALYSIS
# -------------------------------

monthly_sales = df.groupby("Month Name")["Sales"].sum().sort_values(
    ascending=False
)

print("\n--- MONTH-WISE TOTAL SALES ---")
print(monthly_sales)
# -------------------------------
# SUB-CATEGORY ANALYSIS
# -------------------------------

subcategory_analysis = df.groupby("Sub-Category")[["Sales", "Profit"]].sum().sort_values(
    by="Profit", ascending=False
)

print("\n--- SUB-CATEGORY-WISE SALES & PROFIT ---")
print(subcategory_analysis)
# -------------------------------
# DISCOUNT IMPACT ANALYSIS
# -------------------------------

discount_analysis = df.groupby("Discount")[["Sales", "Profit"]].mean()

print("\n--- DISCOUNT VS AVERAGE PROFIT ---")
print(discount_analysis)
# -------------------------------
# TOP 10 PRODUCTS BY SALES
# -------------------------------

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(
    ascending=False
).head(10)

print("\n--- TOP 10 PRODUCTS BY SALES ---")
print(top_products)
# -------------------------------
# VISUALIZATION: CATEGORY SALES
# -------------------------------

category_sales_only = df.groupby("Category")["Sales"].sum().sort_values(
    ascending=False
)

plt.figure(figsize=(8, 5))
category_sales_only.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(BASE_DIR / "images" / "category_sales.png")
plt.show()
# -------------------------------
# VISUALIZATION: YEARLY SALES TREND
# -------------------------------

yearly_sales = df.groupby("Year")["Sales"].sum()

plt.figure(figsize=(8, 5))
plt.plot(yearly_sales.index, yearly_sales.values, marker="o")

plt.title("Year-wise Sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.xticks(yearly_sales.index)

plt.tight_layout()

# Save graph
plt.savefig(BASE_DIR / "images" / "yearly_sales_trend.png")

plt.show()