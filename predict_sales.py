
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales.csv", parse_dates=['date'])
df_grouped = df.groupby('date')['quantity'].sum().reset_index()
df_grouped['date_ordinal'] = df_grouped['date'].map(lambda x: x.toordinal())

X = df_grouped[['date_ordinal']]
y = df_grouped['quantity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = LinearRegression()
model.fit(X_train, y_train)
df_grouped['prediction'] = model.predict(X)

plt.figure(figsize=(10, 5))
plt.plot(df_grouped['date'], df_grouped['quantity'], label="Réel")
plt.plot(df_grouped['date'], df_grouped['prediction'], label="Prédit", linestyle='--')
plt.title("Prévision des ventes")
plt.xlabel("Date")
plt.ylabel("Quantité vendue")
plt.legend()
plt.tight_layout()
plt.show()
