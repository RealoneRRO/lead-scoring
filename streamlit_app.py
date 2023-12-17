import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data for demonstration
data = {'Feature_1': [1, 2, 3, 4, 5],
        'Feature_2': [2, 3, 4, 5, 6],
        'Label': [0, 0, 1, 1, 1]}

df = pd.DataFrame(data)

# Assume 'Feature_1' and 'Feature_2' are your features, and 'Label' is the target variable
X = df[['Feature_1', 'Feature_2']]
y = df['Label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Streamlit app
st.title("Logistic Regression Streamlit App")

# Sidebar with user input
st.sidebar.header("User Input")

feature_1 = st.sidebar.slider("Feature 1", float(X['Feature_1'].min()), float(X['Feature_1'].max()))
feature_2 = st.sidebar.slider("Feature 2", float(X['Feature_2'].min()), float(X['Feature_2'].max()))

# Make predictions
prediction = model.predict([[feature_1, feature_2]])

# Display prediction
st.write("Prediction:", prediction)

# Display the trained model's accuracy on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.write("Model Accuracy on Test Set:", accuracy)
