import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab

##################################################
# Global UI CSS (so it runs on every rerun)
GLOBAL_CSS = """
<style>
/* Entire app background & font */
.stApp {
    background: linear-gradient(135deg, #e8f5e9 0%, #ffffff 100%);
    font-family: 'Poppins', sans-serif;
}

/* Header / titles */
h1, h2, h3 {
    color: #2e7d32;
    font-weight: 600;
}

/* Card look for blocks */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.85);
    border-radius: 12px;
    padding: 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

/* Inputs */
input, textarea, select {
    border: 1px solid #a5d6a7 !important;
    border-radius: 8px !important;
    background-color: #f9fff9 !important;
    color: #1b5e20 !important;
}

/* Buttons */
.stButton button {
    background: linear-gradient(90deg, #388e3c, #66bb6a);
    color: white;
    border-radius: 10px;
    font-weight: 600;
}
.stButton button:hover {
    transform: scale(1.03);
}

/* Expander */
.streamlit-expanderHeader {
    color: #2e7d32 !important;
    font-weight: 600;
}
.streamlit-expanderContent {
    background-color: rgba(230,255,230,0.4);
    border-radius: 8px;
    padding: 10px;
}

/* small spacing fix for tab areas */
.css-1d391kg { padding-top: 8px; }
</style>
"""

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
############################################################


st.title("Expense Tracking System")

tab1, tab2, tab3, tab4 = st.tabs(["Add/Update", "Analytics by Category", "Analytics By Months", "Built by Nishu"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()

with tab4:
    st.markdown("""
        <style>
        .creator-card {
            background: linear-gradient(135deg, #e8f5e9, #ffffff);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            font-family: 'Poppins', sans-serif;
        }
        .creator-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #66bb6a;
            margin-bottom: 15px;
        }
        .creator-name {
            color: #2e7d32;
            font-size: 26px;
            font-weight: 700;
            margin-bottom: 5px;
        }
        .creator-role {
            color: #388e3c;
            font-size: 18px;
            margin-bottom: 15px;
        }
        .creator-desc {
            color: #1b5e20;
            font-size: 15px;
            max-width: 600px;
            margin: 15px auto;
            line-height: 1.7;
            text-align: center;
            letter-spacing: 0.3px;
        }
        </style>

        <div class="creator-card">
            <img src="https://i.postimg.cc/MpVjJr2Q/PROFILE-PHOTO-expense-track.png" class="creator-img" alt="Nishu">
            <div class="creator-name">Nishu kumar</div>
            <div class="creator-role">Developer | Designer | Innovator</div>
            <p class="creator-desc">
                Passionate about crafting intuitive, data-driven web apps that make daily life simpler and smarter.<br>
                This Expense Tracking System was built with Streamlit, FastAPI, love, and a touch of creativity 💚.
            </p>
        </div>
    """, unsafe_allow_html=True)


# BUILT BY NISHU