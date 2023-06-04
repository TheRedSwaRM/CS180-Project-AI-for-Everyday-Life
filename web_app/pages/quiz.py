"""
The following acts as the main page of the web app.
For future additions, Streamlit identifies Markdown text.
"""

# Initial configurations
import streamlit as st
import numpy as np
import pickle
st.set_page_config(initial_sidebar_state="collapsed")

@st.cache_resource
def load_model():
    return pickle.load(open("files/mlp_model.sav", 'rb'))

loaded_model = load_model()

def predict_answers(m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf):
    features = np.array([[m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf]])
    return loaded_model.predict(features)

with st.form("quiz_form"):   
    m_app = st.slider('General Appearance', 1, 5)
    m_speak = st.slider('Manner of Speaking', 1, 5)
    m_phys = st.slider('Physical Condition', 1, 5)
    m_mental = st.slider('Mental Alertness', 1, 5)
    m_conf = st.slider('Self-Confidence', 1, 5)
    m_ideas = st.slider('Ability to Present Ideas', 1, 5)
    m_comm = st.slider('Communication Skills', 1, 5)
    m_perf = st.slider('Student Performance Rating', 1, 5)

    if submitted := st.form_submit_button("Submit"):
        st.markdown("You are:")
        st.write(predict_answers(m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf)[0])