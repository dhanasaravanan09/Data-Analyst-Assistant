import streamlit as st
import pandas as pd

# Load dataset
data = pd.read_csv("Superstore.csv", encoding="latin1")

# Title
st.title("🤖 Data Analyst Assistant")
st.write("Ask questions about your sales dataset.")

# ---------------- FILTERS ----------------

st.sidebar.subheader("Filters")

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(data["Region"].unique().tolist())
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(data["Category"].unique().tolist())
)

if selected_region != "All":
    data = data[data["Region"] == selected_region]

if selected_category != "All":
    data = data[data["Category"] == selected_category]

# ---------------- DASHBOARD ----------------

st.subheader("📊 Sales Dashboard")

total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
total_orders = data["Order ID"].nunique()
total_quantity = data["Quantity"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"₹{total_sales:,.2f}")
col2.metric("Total Profit", f"₹{total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Total Quantity", f"{total_quantity:,}")

# ---------------- DATASET ----------------

with st.expander("📋 View Dataset"):
    st.dataframe(data)

# ---------------- BOT ----------------

st.subheader("🤖 Ask the Data Analyst Assistant")

question = st.text_input(
    "Ask your question:",
    placeholder="Example: Which category has the highest sales?"
)

if question:

    question = question.lower().strip()

    # Total Sales
    if "total sales" in question or "total revenue" in question:
        total_sales = data["Sales"].sum()
        st.success(f"Total sales: ₹{total_sales:,.2f}")

    # Total Profit
    elif "total profit" in question:
        total_profit = data["Profit"].sum()
        st.success(f"Total profit: ₹{total_profit:,.2f}")

    # Total Quantity
    elif "total quantity" in question:
        total_quantity = data["Quantity"].sum()
        st.success(f"Total quantity sold: {total_quantity:,} units")

    # Number of Orders
    elif "how many orders" in question or "number of orders" in question:
        orders = data["Order ID"].nunique()
        st.success(f"Total orders: {orders:,}")

    # Highest Sales Category
    elif "category" in question and "sales" in question:
        category_sales = data.groupby("Category")["Sales"].sum()
        category = category_sales.idxmax()
        sales = category_sales.max()

        st.success(
            f"{category} has the highest sales: ₹{sales:,.2f}"
        )

    # Highest Sales Region
    elif "region" in question and "sales" in question:
        region_sales = data.groupby("Region")["Sales"].sum()
        region = region_sales.idxmax()
        sales = region_sales.max()

        st.success(
            f"{region} has the highest sales: ₹{sales:,.2f}"
        )

    # Highest Profit State
    elif "state" in question and "profit" in question:
        state_profit = data.groupby("State")["Profit"].sum()
        state = state_profit.idxmax()
        profit = state_profit.max()

        st.success(
            f"{state} has the highest profit: ₹{profit:,.2f}"
        )

    # Best Selling Product
    elif "product" in question and (
        "most" in question
        or "best" in question
        or "highest" in question
    ):
        product_quantity = data.groupby("Product Name")["Quantity"].sum()
        product = product_quantity.idxmax()
        quantity = product_quantity.max()

        st.success(
            f"The best-selling product is {product} "
            f"with {quantity:,} units sold."
        )

    # Average Discount
    elif "average discount" in question:
        average_discount = data["Discount"].mean()

        st.success(
            f"Average discount: {average_discount:.2%}"
        )

    # Average Profit
    elif "average profit" in question:
        average_profit = data["Profit"].mean()

        st.success(
            f"Average profit per order: ₹{average_profit:,.2f}"
        )

    # Unknown Question
    else:
        st.warning(
            "Sorry, I don't understand that question yet."
        )