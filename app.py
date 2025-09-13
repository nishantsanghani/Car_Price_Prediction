# ----------------------------------------
# 🚗 Car Price Prediction using Streamlit
# ----------------------------------------

import pandas as pd
import pickle
import streamlit as st
import os

# ----------------------------------------
# App Header
# ----------------------------------------
st.header("🚗 Car Price Prediction ML Model")

# ----------------------------------------
# Load trained ML model (with error handling)
# ----------------------------------------
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)   # ✅ consistent variable name
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# ----------------------------------------
# Load dataset (for dropdown options)
# ----------------------------------------
try:
    cars_data = pd.read_csv("Cardetails.csv")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# Extract brand name from full car name
def get_brand_name(car_name):
    return car_name.split(" ")[0].strip()

cars_data["name"] = cars_data["name"].apply(get_brand_name)

# ----------------------------------------
# User Inputs (UI)
# ----------------------------------------
name = st.selectbox("Select Car Brand", cars_data["name"].unique())
year = st.slider("Car Manufactured Year", 1994, 2024)
km_driven = st.slider("No. of kms Driven", 11, 200000)
fuel = st.selectbox("Fuel type", cars_data["fuel"].unique())
seller_type = st.selectbox("Seller type", cars_data["seller_type"].unique())
transmission = st.selectbox("Transmission type", cars_data["transmission"].unique())
owner = st.selectbox("Owner type", cars_data["owner"].unique())
mileage = st.slider("Car Mileage (km/l)", 10, 40)
engine = st.slider("Engine CC", 700, 5000)
max_power = st.slider("Max Power (bhp)", 0, 200)
seats = st.slider("No of Seats", 5, 10)

# ----------------------------------------
# Prediction Button
# ----------------------------------------
if st.button("Predict"):
    # Create input DataFrame
    input_data_model = pd.DataFrame(
        [[name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
        columns=["name", "year", "km_driven", "fuel", "seller_type", "transmission",
                 "owner", "mileage", "engine", "max_power", "seats"]
    )

    # ----------------------------------------
    # Encoding categorical features
    # ----------------------------------------
    input_data_model["owner"].replace(
        ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'],
        [1, 2, 3, 4, 5],
        inplace=True
    )
    input_data_model["fuel"].replace(
        ['Diesel', 'Petrol', 'LPG', 'CNG'],
        [1, 2, 3, 4],
        inplace=True
    )
    input_data_model["seller_type"].replace(
        ['Individual', 'Dealer', 'Trustmark Dealer'],
        [1, 2, 3],
        inplace=True
    )
    input_data_model["transmission"].replace(
        ['Manual', 'Automatic'],
        [1, 2],
        inplace=True
    )
    input_data_model["name"].replace(
        ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
         'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
         'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
         'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
         'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
        list(range(1, 32)),
        inplace=True
    )

    # ----------------------------------------
    # Prediction
    # ----------------------------------------
    try:
        car_price = model.predict(input_data_model)
        st.success(f"💰 Predicted Car Price: ₹ {car_price[0]:,.2f}")
    except Exception as e:
        st.error(f"❌ Prediction error: {e}")
