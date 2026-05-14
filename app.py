from flask import Flask, request, jsonify
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pickle

app = Flask(__name__)

# Load model and scaler
kmeans = pickle.load(open("kmeans.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return "Customer Segmentation API is running"





@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    income = float(data["income"])
    spending = float(data["spending"])

    # IMPORTANT: use DataFrame with column names
    X = pd.DataFrame([[income, spending]], columns=["Annual Income (k$)", "Spending Score (1-100)"])

    X_scaled = scaler.transform(X)
    cluster = kmeans.predict(X_scaled)[0]

    return jsonify({"cluster": int(cluster)})


    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)





