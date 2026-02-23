import streamlit as st

# 1. This sets the title of your website
st.title("🎧 QuietHour: Your Sound Guardian")

# 2. This creates a friendly message
st.write("Record the noise that is distracting you, and I will analyze its 'fingerprint'.")

# 3. THE MAGIC LINE: This creates the recorder button automatically
audio_data = st.audio_input("Click the microphone to record")

# 4. This only runs IF you have recorded something
if audio_data:
    # This plays your sound back to you
    st.audio(audio_data)
    
    # This is a 'Mock AI' logic - it simulates what the AI would do
    st.success("Analysis Complete!")
    st.info("AI detected a high-pitched frequency (likely a kettle or whistle).")
    st.warning("Action: Activating 'White Noise' mask to protect your focus.")
    
    # This shows a little balloon celebration for your first app!
    st.balloons()