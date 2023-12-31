# -*- coding: utf-8 -*-
"""LAI_ESTIMATION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C7k5xSwq_DhazP8j4tbJtQlZ8ZViSShw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("/content/indices_LAI.csv")
data

data.dtypes

data.info()

x = data.drop(["Crop_stage","observed_LAI"],axis=1)
y = data["observed_LAI"]

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# Random Forest Model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100)
model.get_params()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_pred

y_test

model.score(x_train, y_train)

model.score(x_test, y_test)

from sklearn.metrics import confusion_matrix, accuracy_score

np.random.seed(42)
for i in range(5, 100, 5):
  print(f"Trying model with {i} estimators...")
  model = RandomForestRegressor(n_estimators=i).fit(x_train, y_train)
  print(f"model accuracy on test set: {model.score(x_test, y_test) * 100:.2f}%")
  print("")

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

# R^2 (coefficient of determination)
r2 = r2_score(y_test, y_pred)

# RMSE (Root Mean Squared Error)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# MAE (Mean Absolute Error)
mae = mean_absolute_error(y_test, y_pred)

print(f"R^2: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")



from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

data = pd.read_csv("/content/indices_LAI.csv")
x = data.drop(["Crop_stage", "observed_LAI"], axis=1)
y = data["observed_LAI"]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Standardize the features (important for KNN)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Create and train the KNN model
k = 3  # Number of neighbors
knn_model = KNeighborsRegressor(n_neighbors=k)
knn_model.fit(x_train_scaled, y_train)

# Make predictions on the test set
y_pred = knn_model.predict(x_test_scaled)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)

print(f"R^2: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")



from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

data = pd.read_csv("/content/indices_LAI.csv")
x = data.drop(["Crop_stage", "observed_LAI"], axis=1)
y = data["observed_LAI"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Standardize the features (important for SVM)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Create and train the SVM model
svm_model = SVR(kernel='linear')  # You can choose different kernels, e.g., 'linear', 'rbf', 'poly', etc.
svm_model.fit(x_train_scaled, y_train)

# Make predictions on the test set
y_pred = svm_model.predict(x_test_scaled)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)

print(f"R^2: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")



from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load the data
data = pd.read_csv("/content/indices_LAI.csv")
x = data.drop(["Crop_stage", "observed_LAI"], axis=1)
y = data["observed_LAI"]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the XGBoost model
xgb_model = XGBRegressor(n_estimators=35, learning_rate=0.1)  # You can adjust hyperparameters here
xgb_model.fit(x_train, y_train)

# Make predictions on the test set
y_pred = xgb_model.predict(x_test)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)

print(f"R^2: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")

np.random.seed(42)
for i in range(10, 100, 10):
    print(f"Trying model with {i} estimators...")
    xgb_model = XGBRegressor(n_estimators=i, learning_rate=0.1)
    xgb_model.fit(x_train, y_train)
    y_pred = xgb_model.predict(x_test)
    r2 = r2_score(y_test, y_pred)
    print(f"Model R^2 score on test set: {r2:.4f}")
    print("")



import lightgbm as lgb
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load the data
data = pd.read_csv("/content/indices_LAI.csv")
x = data.drop(["Crop_stage", "observed_LAI"], axis=1)
y = data["observed_LAI"]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the LightGBM model
lgb_model = lgb.LGBMRegressor(n_estimators=100, learning_rate=0.1)  # You can adjust hyperparameters here
lgb_model.fit(x_train, y_train)

# Make predictions on the test set
y_pred = lgb_model.predict(x_test)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)

print(f"R^2: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")

# Hyperparameter tuning loop for LightGBM
np.random.seed(42)
for i in range(5, 100, 5):
    print(f"Trying model with {i} estimators...")
    lgb_model = lgb.LGBMRegressor(n_estimators=i, learning_rate=0.1)
    lgb_model.fit(x_train, y_train)
    y_pred = lgb_model.predict(x_test)
    r2 = r2_score(y_test, y_pred)
    print(f"Model R^2 score on test set: {r2:.4f}")
    print("")







