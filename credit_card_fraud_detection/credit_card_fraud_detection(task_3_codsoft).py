# -*- coding: utf-8 -*-
"""Credit Card Fraud Detection(Task-3 CODSOFT).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IVl0KXocqUqJuifUjWI0tn1W3VSsbJHl
"""

#importing the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the datasets
fraudtrain_data = pd.read_csv('fraudTrain.csv')
fraudtest_data = pd.read_csv('fraudTest.csv')

fraudtrain_data = fraudtrain_data[:1000]
fraudtest_data = fraudtest_data[:1000]
print(fraudtrain_data.shape)
print(fraudtest_data.shape)

# Prepare features and target
X = fraudtrain_data.drop(['trans_date_trans_time', 'merchant', 'category', 'first', 'last', 'gender', 'street', 'city', 'state', 'job', 'trans_num', 'dob'], axis=1)
y = fraudtest_data['is_fraud']
print(X.shape)
print(y.shape)
print(fraudtrain_data.shape)
print(fraudtest_data.shape)

# Build and train the Random Forest classifier
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X, y)

# Make predictions from random forests
rf_predictions = rf_classifier.predict(X)

#Evaluating the model
print("Random Forest Accuracy:", accuracy_score(y, rf_predictions))
print("Random Forest Classification Report:")
print(classification_report(y, rf_predictions))
print("Random Forest Confusion Matrix:")
print(confusion_matrix(y, rf_predictions))