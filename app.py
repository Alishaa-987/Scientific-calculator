import streamlit as st
import math
import numpy as np

# --- Custom CSS ---
def local_css():
    st.markdown("""
    <style>
    /* Container styling */
    .main {
        background-color: #f0f2f6;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 12px;
    }

    .stButton>button:hover {
        background-color: white; 
        color: black; 
        border: 2px solid #4CAF50;
    }

    /* Result styling */
    .result {
        font-size: 24px;
        color: #333333;
        font-weight: bold;
    }

    /* Title styling */
    .title {
        color: #4CAF50;
        font-family: 'Arial';
        font-size: 36px;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Input styling */
    .input-field {
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- Title ---
st.markdown("<h1 class='title'>🧮 Scientific Calculator</h1>", unsafe_allow_html=True)

# --- Inputs ---
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter the first number", value=0.0, key="num1")
with col2:
    num2 = st.number_input("Enter the second number", value=0.0, key="num2")

# --- Operation Selection ---
operations = ["Add", "Subtract", "Multiply", "Divide", "Exponent", "Logarithm", "Sine", "Cosine", "Tangent", "Factorial"]
operation = st.selectbox("Select operation", operations)

# --- Perform Calculation ---
result = None

def calculate():
    global result
    try:
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        elif operation == "Exponent":
            result = math.pow(num1, num2)
        elif operation == "Logarithm":
            if num1 > 0 and num2 > 0:
                result = math.log(num1, num2)
            else:
                result = "Error: Invalid input for logarithm"
        elif operation == "Sine":
            result = math.sin(math.radians(num1))
        elif operation == "Cosine":
            result = math.cos(math.radians(num1))
        elif operation == "Tangent":
            result = math.tan(math.radians(num1))
        elif operation == "Factorial":
            if num1 >= 0 and float(num1).is_integer():
                result = math.factorial(int(num1))
            else:
                result = "Error: Factorial is only defined for non-negative integers"
    except Exception as e:
        result = f"Error: {str(e)}"

# --- Button with Styling ---
if st.button("Calculate"):
    calculate()

# --- Display Result ---
if result is not None:
    st.markdown(f"<p class='result'>Result: {result}</p>", unsafe_allow_html=True)
