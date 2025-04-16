import pickle
from flask import Flask, jsonify, request
from sklearn.feature_extraction import DictVectorizer

app = Flask('lead_scoring_model')

# Load the model and vectorizer
with open('lead-model.bin', 'rb') as f_out:
    dv, model = pickle.load(f_out)

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    # Check if the JSON body was received
    if not customer:
        return jsonify({'error': 'No customer data provided'}), 400

    # Transform the customer dictionary
    customer_data = dv.transform([customer])
    prediction = model.predict(customer_data)[0]
    probability = model.predict_proba(customer_data)[0][1]

    result = {
        'prediction': int(prediction),
        'probability': float(probability)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
