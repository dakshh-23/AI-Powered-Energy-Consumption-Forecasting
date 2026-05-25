# train.py
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
import joblib

# Directory creation for data storage
os.makedirs('data', exist_ok=True)

print("⏳ Engineering Enterprise Smart-Grid Telemetry Logs...")
# 1-year sequence hourly data matrix creation
date_range = pd.date_range(start="2025-01-01", end="2026-01-01", freq="h")
df = pd.DataFrame(index=date_range)
df['hour'] = df.index.hour
df['day'] = df.index.dayofweek

# Non-linear energy profiles (Peak industrial cycles + random noise vectors)
base_load = 22.5 
df['Energy'] = base_load + (df['hour'] * 1.4) - (df['day'] * 0.9) + np.random.normal(0, 2.5, len(df))
df.index.name = 'Datetime'
df.to_csv('data/energy.csv')
print("✅ Base Telemetry Matrix persistent at data/energy.csv")

# Feature Vector Splitting
data = pd.read_csv('data/energy.csv', parse_dates=['Datetime'], index_col='Datetime')
X = data[['hour', 'day']]
y = data['Energy']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("🧠 Commencing Multi-Layer Perceptron (MLP) Deep Neural Weight Optimization...")
# High capacity Multi-Layer Perceptron Network Topology
model = MLPRegressor(hidden_layer_sizes=(128, 64), activation='relu', max_iter=600, random_state=42)
model.fit(X_train, y_train)

# Persisting binary weight mapping
joblib.dump(model, 'energy_forecast_model.pkl')
print("💾 Neural Architecture exported successfully as 'energy_forecast_model.pkl'")