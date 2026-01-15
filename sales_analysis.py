import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Remove missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Create total sales column
df['Total Sales'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']

# Save cleaned data
df.to_csv("clean_sales_data.csv", index=False)

# ----------------------------
# Monthly sales analysis
# ----------------------------
monthly_sales = df.groupby('MONTH')['Total Sales'].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.savefig("monthly_sales.png")
plt.show()

# ----------------------------
# Top products analysis
# ----------------------------
product_sales = (
    df.groupby('ITEM DESCRIPTION')['Total Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure()
product_sales.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.savefig("product_sales.png")
plt.show()

print("DONE - files created successfully")
