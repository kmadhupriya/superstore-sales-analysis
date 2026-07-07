import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv', encoding='latin1')

# 1. Sales by Category
print("SALES BY CATEGORY:")
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))
print()

# 2. Sales by Region
print("SALES BY REGION:")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))
print()

# 3. Sales by Segment (Consumer/Corporate/Home Office)
print("SALES BY SEGMENT:")
print(df.groupby('Segment')['Sales'].sum().sort_values(ascending=False))
print()

# 4. Top 5 States by Sales
print("TOP 5 STATES BY SALES:")
print(df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(5))
print()

# 5. Top 10 Products by Sales
print("TOP 10 PRODUCTS BY SALES:")
print(df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10))
print()

# 6. Sales trend over time (year-wise)
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Year'] = df['Order Date'].dt.year
print("SALES BY YEAR:")
print(df.groupby('Year')['Sales'].sum())
print()

# 7. Chart - Sales by Region
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
region_sales.plot(kind='bar', title='Total Sales by Region', color='coral')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('sales_by_region.png')
print("Chart saved as sales_by_region.png")
