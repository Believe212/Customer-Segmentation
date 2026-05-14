# Customer Segmentation

A Machine Learning-powered Flask API that predicts customer clusters based on **Annual Income** and **Spending Score** using a trained **K-Means Clustering model**.

---

## Synent Technologies Internship Project

synent-task<task 3>-<Customer Segmentation>-<Believe Nosakhare>
```

## Project Overview

This project uses **unsupervised machine learning (K-Means clustering)** to segment customers into different behavioral groups based on:

- Annual Income (k$)
- Spending Score (1–100)

The API accepts customer data through a POST request and returns the predicted customer cluster.

---

## Features

- REST API built with Flask
- Predicts customer cluster instantly
- Uses trained K-Means model
- Data preprocessing with StandardScaler
- JSON response output

---

## Project Structure

```bash
customer-segmentation/
│
├── app.py
├── kmeans.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- Pickle

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/customer-segmentation-api.git
cd customer-segmentation-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the API

Start the Flask server:

```bash
python app.py
```

Server runs on:

```bash
http://127.0.0.1:5000
```

---

## Example Test with Postman

### URL

```bash
POST http://127.0.0.1:5000/predict
```

### JSON Body

```json
{
  "income": 60,
  "spending": 75
}
```

### Result

```json
{
  "cluster": 1
}
```

---

## Future Improvements

- Add customer segment labels
- Deploy to Render or Heroku
- Add frontend dashboard
- Visualize customer clusters

---

## Author

**Believe Nosakhare**
---

## License

This project is open-source and available under the MIT License.
