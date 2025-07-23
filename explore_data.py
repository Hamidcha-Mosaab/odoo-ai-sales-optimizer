
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/sales.csv", parse_dates=['date'])
print(df.head())

daily_sales = df.groupby('date')['quantity'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=daily_sales, x='date', y='quantity')
plt.title("Ventes quotidiennes")
plt.xlabel("Date")
plt.ylabel("Quantité vendue")
plt.tight_layout()
plt.show()
