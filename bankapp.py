import streamlit as st

if "savings_balance" not in st.session_state:
    st.session_state.savings_balance = 200000
if "current_balance" not in st.session_state:
    st.session_state.current_balance = 200000


SAVINGS_WITHDRAWAL_LIMIT = 50000  


def deposit(account_type, amount):
    if account_type == "Savings":
        st.session_state.savings_balance += amount
        st.success(f" {amount} deposited to Savings Account.")
    elif account_type == "Current":
        st.session_state.current_balance += amount
        st.success(f" {amount} deposited to Current Account.")

def withdraw(account_type, amount):
    if account_type == "Savings":
        if amount > SAVINGS_WITHDRAWAL_LIMIT:
            st.warning(f" Exceeds Savings withdrawal limit of ₦{SAVINGS_WITHDRAWAL_LIMIT}.")
            return
        if amount > st.session_state.savings_balance:
            st.error(" Insufficient funds in Savings.")
            return
        st.session_state.savings_balance -= amount
        st.success(f" {amount} withdrawn from Savings Account.")
    elif account_type == "Current":
        if amount > st.session_state.current_balance:
            st.error(" Insufficient funds in Current.")
            return
        st.session_state.current_balance -= amount
        st.success(f" {amount} withdrawn from Current Account.")

st.set_page_config(page_title="Westfago", layout="centered")
st.title("🏦 Westfago Bank App")

tab1, tab2 = st.tabs([" Savings Account", " Current Account"])

with tab1:
    st.subheader("Savings Account")

    st.info(f" Balance: ₦{st.session_state.savings_balance}")
    st.caption(f" Max withdrawal per transaction: ₦{SAVINGS_WITHDRAWAL_LIMIT}")

    action = st.selectbox("Select action", ["Deposit", "Withdraw"])
    amount = st.number_input("Enter amount", min_value=1)

    if st.button("Submit", key="savings_submit"):
        if action == "Deposit":
            deposit("Savings", amount)
        elif action == "Withdraw":
            withdraw("Savings", amount)

with tab2:
    st.subheader("Current Account")

    st.info(f" Balance: ₦{st.session_state.current_balance}")

    action2 = st.selectbox("Select action", ["Deposit", "Withdraw"], key="current_action")
    amount2 = st.number_input("Enter amount", min_value=1, key="current_amount")

    if st.button("Submit", key="current_submit"):
        if action2 == "Deposit":
            deposit("Current", amount2)
        elif action2 == "Withdraw":
            withdraw("Current", amount2)
