import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Load the data model
carbon_footprint_model = pd.read_csv('carbon_footprint_model.csv')

# Define the data entry form
st.title("Carbon Footprint Tracker")
st.header("Enter Your Data")

# Create a form to collect data
data_form = st.form("data_form")
carbon_emissions = data_form.number_input("Carbon Emissions (kg CO2e)", min_value=0, max_value=10000)
energy_consumption = data_form.number_input("Energy Consumption (kWh)", min_value=0, max_value=10000)
distance_traveled = data_form.number_input("Distance Traveled (km)", min_value=0, max_value=10000)
fuel_type = data_form.selectbox("Fuel Type", ["Gasoline", "Diesel", "Electric"])
submit_button = data_form.form_submit_button("Submit")

# Define the carbon footprint calculation function
def calculate_carbon_footprint(carbon_emissions, energy_consumption, distance_traveled, fuel_type):
    # Calculate carbon footprint based on fuel type
    if fuel_type == "Gasoline":
        carbon_footprint = carbon_emissions * 0.85  # conversion factor for gasoline
    elif fuel_type == "Diesel":
        carbon_footprint = carbon_emissions * 0.95  # conversion factor for diesel
    elif fuel_type == "Electric":
        carbon_footprint = energy_consumption * 0.05  # conversion factor for electric vehicles
    else:
        carbon_footprint = 0
    
    # Calculate carbon footprint based on distance traveled
    distance_carbon_footprint = distance_traveled * 0.1
    
    # Calculate total carbon footprint
    total_carbon_footprint = carbon_footprint + distance_carbon_footprint
    
    return total_carbon_footprint

# Calculate the carbon footprint and display the results
if submit_button:
    carbon_footprint = calculate_carbon_footprint(carbon_emissions, energy_consumption, distance_traveled, fuel_type)
    st.write(f"Your carbon footprint is: {carbon_footprint:.2f} kg CO2e")

# Define the visualization function
def visualize_carbon_footprint(carbon_footprint):
    # Create a line chart to visualize the carbon footprint over time
    import matplotlib.pyplot as plt
    
    # Generate some sample data for the chart
    dates = [datetime(2022, 1, 1), datetime(2022, 2, 1), datetime(2022, 3, 1), datetime(2022, 4, 1), datetime(2022, 5, 1)]
    footprints = [carbon_footprint] * len(dates)
    
    # Create the chart
    plt.plot(dates, footprints)
    plt.xlabel("Date")
    plt.ylabel("Carbon Footprint (kg CO2e)")
    plt.title("Carbon Footprint Over Time")
    plt.show()

# Visualize the carbon footprint
if submit_button:
    visualize_carbon_footprint(carbon_footprint)

# Define the reporting function
def generate_report(carbon_footprint):
    # Create a report with the calculated carbon footprint and some additional information
    report = f"Carbon Footprint Report\n\n"
    report += f"Your carbon footprint is: {carbon_footprint:.2f} kg CO2e\n"
    report += f"This is equivalent to {carbon_footprint / 1000:.2f} tons of CO2e.\n"
    report += f"To reduce your carbon footprint by 50%, you can consider the following options:\n"
    report += f"- Use public transportation or walk/bike instead of driving {distance_traveled / 100:.2f} times per week.\n"
    report += f"- Replace your gasoline-powered vehicle with an electric or hybrid vehicle.\n"
    
    return report

# Generate the report and display it
if submit_button:
    report = generate_report(carbon_footprint)
    st.write(report)

# Define the goal setting function
def set_reduction_goal(carbon_footprint):
    # Ask the user to set a reduction goal
    reduction_goal_percentage = st.slider("Set a Reduction Goal (%)", min_value=0, max_value=100)

    # Calculate the reduction goal amount in kg CO2e
    reduction_goal_amount = carbon_footprint * (reduction_goal_percentage / 100)

    return reduction_goal_amount

# Set the reduction goal and display it
if submit_button:
    reduction_goal_amount = set_reduction_goal(carbon_footprint)
    st.write(f"Your reduction goal is: {reduction_goal_amount:.2f} kg CO2e")
