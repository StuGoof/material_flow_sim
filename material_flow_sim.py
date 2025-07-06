
import streamlit as st
import matplotlib.pyplot as plt

# Title
st.title("Material Flow Simulation")

# Sidebar inputs
st.sidebar.header("Input Parameters")

feed_rate_kgph = st.sidebar.slider("Feed Rate (kg/h)", min_value=100, max_value=10000, value=1000, step=100)
vessel_volume_m3 = st.sidebar.slider("Vessel Volume (m³)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
bulk_density_gl = st.sidebar.slider("Bulk Density (g/L)", min_value=100, max_value=2000, value=800, step=50)
moisture_content_pct = st.sidebar.slider("Moisture Content (%)", min_value=0, max_value=100, value=10, step=1)
water_input_kgph = st.sidebar.slider("Water Input (kg/h)", min_value=0, max_value=5000, value=500, step=100)

# Convert units
bulk_density_kgm3 = bulk_density_gl / 1000 * 1000  # g/L to kg/m³
total_input_kgph = feed_rate_kgph + water_input_kgph  # total mass input
material_volume_m3 = feed_rate_kgph / bulk_density_kgm3  # volume of dry material
total_volume_m3 = material_volume_m3 + (water_input_kgph / 1000)  # water assumed to have density 1000 kg/m³

# Filling degree
filling_degree_pct = min((total_volume_m3 / vessel_volume_m3) * 100, 100)

# Material weight including moisture
material_weight_kg = feed_rate_kgph * (1 + moisture_content_pct / 100)

# Retention time in seconds
if total_input_kgph > 0:
    retention_time_sec = (material_weight_kg / total_input_kgph) * 3600
else:
    retention_time_sec = 0

# Display results
st.subheader("Simulation Results")
st.metric("Filling Degree (%)", f"{filling_degree_pct:.1f}")
st.metric("Material Weight (kg)", f"{material_weight_kg:.1f}")
st.metric("Retention Time (s)", f"{retention_time_sec:.1f}")

# Visualization
st.subheader("Vessel Fill Level")
fig, ax = plt.subplots(figsize=(4, 6))
ax.barh(["Vessel"], [filling_degree_pct], color="skyblue")
ax.set_xlim(0, 100)
ax.set_xlabel("Filling Degree (%)")
st.pyplot(fig)
