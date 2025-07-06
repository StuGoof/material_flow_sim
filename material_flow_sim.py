
import streamlit as st

# Title
st.title("Material Flow Simulation")

# Input Section
st.header("Input Parameters")

# Reordered and renamed inputs
dry_meal_feed_rate = st.number_input("Dry Meal Feed Rate (kg/h)", min_value=0.0, value=500.0, step=10.0)
meal_moisture_content = st.number_input("Meal Moisture Content (%)", min_value=0.0, max_value=100.0, value=10.0, step=1.0)

vessel_volume_m3 = st.number_input("Vessel Volume (m³)", min_value=0.1, value=2.0, step=0.1)
bulk_density_g_per_l = st.number_input("Bulk Density (g/L)", min_value=0.0, value=600.0, step=10.0)

liquid_input_1 = st.number_input("Liquid Input 1 (kg/h)", min_value=0.0, value=100.0, step=10.0)
liquid_input_2 = st.number_input("Liquid Input 2 (kg/h)", min_value=0.0, value=50.0, step=10.0)
liquid_input_3 = st.number_input("Liquid Input 3 (kg/h)", min_value=0.0, value=25.0, step=5.0)

material_weight = st.number_input("Material Weight (kg)", min_value=0.0, value=1000.0, step=10.0)

# Calculations
wet_throughput = dry_meal_feed_rate + liquid_input_1 + liquid_input_2 + liquid_input_3

# Avoid division by zero
if wet_throughput > 0:
    retention_time = (material_weight / wet_throughput) * 3600  # seconds
else:
    retention_time = 0.0

# Output Section
st.header("Output Results")
st.metric("Wet Throughput (kg/h)", f"{wet_throughput:.2f}")
st.metric("Retention Time (s)", f"{retention_time:.2f}")
