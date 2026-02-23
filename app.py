import streamlit as st
import numpy as np
import time

# 1. Page Config
st.set_page_config(page_title="QuietHour Ultimate", page_icon="🎧", layout="wide")

# 2. Advanced Styling
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: white; }
    .stMetric { background-color: #1a1d24; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 QuietHour Pro")
st.caption("AI-Powered Focused Environment | Building AI Course Project")
st.divider()

# 3. Layout: Two Columns
left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.write("### ⏺️ Capture Environment")
    audio_data = st.audio_input("Initialize Listener")
    
    if audio_data:
        st.audio(audio_data)
        st.success("Noise Pattern Captured")
        
        # Simulated Waveform Visual
        st.write("Analyzing Signature...")
        chart_placeholder = st.empty()
        for i in range(20):
            chart_placeholder.line_chart(np.random.randn(15, 1))
            time.sleep(0.05)
        st.info("AI Detection: **Low-Frequency Construction Rumble**")

with right_col:
    st.write("### 🛡️ Acoustic Shield")
    st.write("If distraction is detected, activate the masking shield below:")
    
    # 4. THE MASKING BUTTON
    if st.button("🔊 Activate Rainfall Shield"):
        st.toast("Shield Active: 450Hz Masking Frequency Injected")
        # High quality rain sound from the internet
        rain_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" # Using a sample mp3 for demonstration
        st.audio("https://www.zapsplat.com/wp-content/uploads/2015/sound-effects-one/rain_moderate_loop.mp3", autoplay=True)
        st.write("🌧️ **Playing: Heavy Rain Masking**")

    # 5. Metrics Dashboard
    st.divider()
    m_col1, m_col2 = st.columns(2)
    m_col1.metric("Noise Floor", "-38 dB", "Normal")
    m_col2.metric("Focus Score", "94%", "+5%")

st.divider()
st.caption("© 2026 QuietHour AI. Built with Streamlit & Python.")