import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import joblib


dataset = pd.read_csv("algae_dataset.csv")


def clean_data(df):
    if df.isnull().sum().any():
        df.fillna(df.mean(), inplace=True)
    return df

dataset = clean_data(dataset)


label_encoder = LabelEncoder()
dataset['best_algae'] = label_encoder.fit_transform(dataset['best_algae'])


X = dataset.drop(columns=['best_algae'])
y = dataset['best_algae']


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=label_encoder.classes_))


joblib.dump(model, "algae_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
joblib.dump(scaler, "scaler.pkl")
print("Model, scaler, and label encoder saved.")
