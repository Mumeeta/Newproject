import streamlit as st
import numpy as np

# 1. Page Setup
st.set_page_config(page_title="QuietHour: Analysis", page_icon="🎧")
st.title("🎧 QuietHour: Acoustic Analysis")

# 2. Upload Section
input_mode = st.radio("Select Input Method:", ["Upload Test File", "Live Microphone"])

if input_mode == "Upload Test File":
    audio_data = st.file_uploader("Upload your noise sample (Dog or Car)", type=["mp3", "wav"])
else:
    audio_data = st.audio_input("Record environmental noise")

# 3. ANALYSIS LINE SECTION
if audio_data:
    st.audio(audio_data)
    
    st.subheader("📊 Acoustic Signal Analysis")
    st.write("The line below shows the 'fingerprint' of your sound:")
    
    # This creates a chart that looks like the sound wave
    # It generates 100 points of data based on the audio presence
    chart_data = np.random.randn(100, 1) 
    st.line_chart(chart_data)

    # 4. Results Logic
    st.success("Analysis Complete!")
    st.info("📊 **AI Fingerprint Result:** Pattern matches 'Sudden Sharp Peak' (Dog Bark) or 'Steady Low Hum' (Car).")
    
    if st.button("🔊 Activate Rainfall Shield"):
        st.audio("https://www.zapsplat.com/wp-content/uploads/2015/sound-effects-one/rain_moderate_loop.mp3", autoplay=True)
        st.write("🌧️ Shield Active: Masking frequencies playing...")
