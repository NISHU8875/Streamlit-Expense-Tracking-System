## improved code 
import streamlit as st
from datetime import datetime
import requests


API_URL = "http://localhost:8000"


def add_update_tab():

    ##################################################################

    # Header Banner
    st.markdown("""
        <div style="
            background: linear-gradient(90deg, #2e7d32, #66bb6a);
            padding: 20px 30px;
            border-radius: 15px;
            text-align: center;
            color: white;
            margin-bottom: 25px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
            font-family: 'Poppins', sans-serif;
        ">
            <h2 style="margin-bottom:5px;">💰 Add or Update Your Daily Expenses</h2>
            <p style="font-size:15px; opacity:0.9;">
                Spend Smart. Save Better. Live Freely.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Continuing with rest of my form and logic here
    ########################################

    st.header("Expense Tracking System")

    # ---- Date input ----
    selected_date = st.date_input(
        "Enter Date",
        datetime(2024, 8, 1),
        label_visibility="collapsed",
        key="selected_date"
    )
    selected_date_str = selected_date.isoformat()

    #  Fetching existing expenses for this date 
    try:
        resp = requests.get(f"{API_URL}/expenses/{selected_date_str}", timeout=5)
        if resp.status_code == 200:
            existing_expenses = resp.json() or []
        else:
            existing_expenses = []
            st.warning(f"No expenses found or bad status ({resp.status_code}).")
    except requests.RequestException as e:
        existing_expenses = []
        st.error(f"Error fetching data: {e}")

    # Now Syncing row count with fetched data 
    if "last_date" not in st.session_state or st.session_state.last_date != selected_date_str:
        st.session_state.num_expenses = len(existing_expenses) if existing_expenses else 5
        st.session_state.last_date = selected_date_str

    #  Letting the user choose number of expense rows (1–100) 
    num_expenses = st.number_input(
        "Number of expenses to add/update",
        min_value=1,
        max_value=100,
        step=1,
        key="num_expenses",
    )
    num_expenses = int(num_expenses)

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    # Expense form
    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns([2, 2, 4])
        with col1:
            st.markdown("**Amount**")
        with col2:
            st.markdown("**Category**")
        with col3:
            st.markdown("**Notes**")

        expenses = []
        for i in range(num_expenses):
            if i < len(existing_expenses):
                exp = existing_expenses[i]
                amount = exp.get("amount", 0.0)
                category = exp.get("category", "Shopping")
                notes = exp.get("notes", "")
            else:
                amount, category, notes = 0.0, "Shopping", ""

            c1, c2, c3 = st.columns([2, 2, 4])
            with c1:
                amount_input = st.number_input(
                    label=f"Amount {i+1}",
                    min_value=0.0,
                    step=1.0,
                    value=amount,
                    key=f"amount_{i}_{selected_date_str}",
                    label_visibility="collapsed",
                )
            with c2:
                category_input = st.selectbox(
                    label=f"Category {i+1}",
                    options=categories,
                    index=categories.index(category),
                    key=f"category_{i}_{selected_date_str}",
                    label_visibility="collapsed",
                )
            with c3:
                notes_input = st.text_input(
                    label=f"Notes {i+1}",
                    value=notes,
                    key=f"notes_{i}_{selected_date_str}",
                    label_visibility="collapsed",
                )

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input.strip(),
            })

        submit = st.form_submit_button("Submit")

        if submit:
            filtered_expenses = [e for e in expenses if e["amount"] > 0]

            if not filtered_expenses:
                st.warning("Please enter at least one valid expense (amount > 0).")
                return

            try:
                post_resp = requests.post(
                    f"{API_URL}/expenses/{selected_date_str}",
                    json=filtered_expenses,
                    timeout=5,
                )
                if post_resp.status_code in (200, 201):
                    st.success("✅ Expenses updated successfully!")
                    total = sum(e["amount"] for e in filtered_expenses)
                    st.info(f"Saved {len(filtered_expenses)} entries — Total ₹{total:.2f}")
                    # st.session_state.num_expenses = len(filtered_expenses)
                    st.session_state["num_expenses_count"] = len(filtered_expenses)
                    st.rerun()
                else:
                    st.error(f"❌ Failed to update expenses (status {post_resp.status_code})")
            except requests.RequestException as e:
                st.error(f"Network error: {e}")

    #  Viewing existing server data 
    with st.expander(f"View existing data for {selected_date_str}"):
        if existing_expenses:
            st.table(existing_expenses)
        else:
            st.write("No expenses found for this date.")
