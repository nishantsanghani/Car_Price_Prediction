# 🚗 Car Price Prediction using Machine Learning & Streamlit

This project predicts the price of a used car based on various features such as brand, year, kilometers driven, fuel type, transmission, mileage, engine capacity, and more.  
It combines **Machine Learning** for price prediction and an interactive **Streamlit web app** for deployment.

---

## 📁 Project Structure

Car-Price-Prediction/
│── app.py # Streamlit web application
│── Car Price Prediction.ipynb # Jupyter Notebook (model training & EDA)
│── model.pkl # Trained ML model (pickle file)
│── Cardetails.csv # Dataset
│── README.md # Project documentation


---

## 🎯 Objectives

- Build a machine learning model to predict car prices.
- Perform **data cleaning, preprocessing, and feature engineering**.
- Deploy the model using **Streamlit** with an interactive UI.
- Help buyers and sellers estimate fair car prices.

---

## 🛠️ Tech Stack

- **Python** (Pandas, NumPy, Scikit-learn, Pickle)
- **Visualization**: Matplotlib, Seaborn
- **Web App**: Streamlit
- **Dataset**: Car details dataset (`Cardetails.csv`)

---

## 🚀 How to Run the Project

## 1. Clone the Repository

git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction

## 2. Install Dependencies
pip install -r requirements.txt

## 3. Run the Streamlit App
streamlit run app.py

## 4. Open in Browser
The app will be available at:
http://localhost:8501/

🧩 Features of the Web App

- Select Car Brand from dropdown.
- Enter details such as:
    - Manufacturing year
    - Kilometers driven
    - Fuel type
    - Transmission
    - Owner type
    - Mileage, Engine CC, Max Power, Seats
- Get an instant predicted car price.

📊 Workflow

1. Data Preprocessing:
    - Extracted car brand names.
    - Handled categorical variables via encoding.
    - Converted textual values into numerical labels.

2. Model Training:
    - Trained ML model using regression techniques.
    - Saved model as model.pkl.

3. Deployment:
    - Streamlit app (app.py) loads model and takes user input.
    - Predicts price and displays in INR (₹).

Live URL: https://carpriceprediction-system.streamlit.app/
