import streamlit as st

st.set_page_config(
    page_title="Mobile Network Comparison",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Mobile Network Comparison Tool")

st.write("Welcome to Mobile Network Comparison Tool!")

st.success("Application is running successfully.")
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Mobile Network Comparison Tool",
    page_icon="📡",
    layout="wide"
)

# Network Data
networks = {
    "GSM": {"Data Rate": 0.014, "Latency": 500},
    "GPRS": {"Data Rate": 0.114, "Latency": 300},
    "WCDMA": {"Data Rate": 2, "Latency": 100},
    "LTE": {"Data Rate": 100, "Latency": 40},
    "WiMAX": {"Data Rate": 70, "Latency": 50}
}

# Header
st.title("📡 Mobile Network Comparison Tool")
st.caption("Interactive Telecommunication Network Analysis System")
st.divider()

# Sidebar
st.sidebar.header("⚙️ Network Configuration")

selected_network = st.sidebar.selectbox(
    "Select Network",
    list(networks.keys())
)

signal_strength = st.sidebar.slider(
    "Signal Strength (%)",
    min_value=10,
    max_value=100,
    value=75,
    step=5
)

# Selected Network Data
data_rate = networks[selected_network]["Data Rate"]
latency = networks[selected_network]["Latency"]

signal_factor = signal_strength / 100

effective_speed = data_rate * signal_factor
effective_latency = latency + (100 - signal_strength) * 2

packet_loss = (100 - signal_strength) * 0.1

# Dashboard Metrics
st.subheader("📊 Network Performance Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Selected Network",
    selected_network
)

col2.metric(
    "Data Rate",
    f"{effective_speed:.2f} Mbps"
)

col3.metric(
    "Latency",
    f"{effective_latency:.0f} ms"
)

col4.metric(
    "Packet Loss",
    f"{packet_loss:.1f}%"
)

st.divider()

# Network Comparison Table
st.subheader("📋 Network Comparison")

df = pd.DataFrame(networks).T
df.index.name = "Network"
df = df.reset_index()

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# Graphs
st.subheader("📈 Performance Analysis")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        df,
        x="Network",
        y="Data Rate",
        color="Network",
        title="Data Rate Comparison (Mbps)"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:
    fig2 = px.bar(
        df,
        x="Network",
        y="Latency",
        color="Network",
        title="Latency Comparison (ms)"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

# Signal Analysis
st.subheader("📶 Signal Strength Analysis")

st.progress(signal_strength / 100)

if signal_strength >= 80:
    st.success("Strong Signal")
elif signal_strength >= 50:
    st.warning("Moderate Signal")
else:
    st.error("Weak Signal")

# Recommendation
st.subheader("💡 Network Recommendation")

best_network = max(
    networks,
    key=lambda x: networks[x]["Data Rate"]
)

st.success(
    f"Recommended Network: {best_network}"
)

st.info(
    "LTE provides the highest data rate "
    "among the networks in this comparison."
)

# Footer
st.divider()

st.caption(
    "Educational Simulation | "
    "Diploma Electronics & Telecommunication"
)
