
import tkinter as tk
from tkinter import messagebox
import subprocess

def run_analysis():
    subprocess.run(["python", "analysis/explore_data.py"])

def run_prediction():
    subprocess.run(["python", "ml/predict_sales.py"])

app = tk.Tk()
app.title("Outil d'analyse des ventes")

tk.Label(app, text="Analyse et Prévision des ventes", font=("Arial", 16)).pack(pady=10)
tk.Button(app, text="🔍 Analyse des ventes", command=run_analysis, width=30).pack(pady=5)
tk.Button(app, text="📈 Prévision IA", command=run_prediction, width=30).pack(pady=5)

app.mainloop()
