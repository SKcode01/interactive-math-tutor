import streamlit as st
import random
from PIL import Image

# App Title and Custom Header
st.set_page_config(page_title="Interactive Math Tutor", page_icon="📚")
st.title("📚 Interactive Math Tutor")

# Sidebar for User Input
st.sidebar.title("Welcome!")
user_name = st.sidebar.text_input("Enter your name:", placeholder="Type your name...")
if user_name:
    st.sidebar.write(f"👋 Hello, {user_name}! Ready to learn math?")

# Function to Generate Math Problems
def generate_problem():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])
    if operator == "+":
        return num1, num2, operator, num1 + num2
    elif operator == "-":
        return num1, num2, operator, num1 - num2
    elif operator == "*":
        return num1, num2, operator, num1 * num2

# Initialize Session State
if "problem" not in st.session_state:
    st.session_state.problem = generate_problem()
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Display Problem
num1, num2, operator, correct_answer = st.session_state.problem
st.write(f"### Solve this: {num1} {operator} {num2} = ?")

# User Input and Answer Validation
user_answer = st.text_input("Your Answer:", placeholder="Enter your answer here...")

if st.button("Submit"):
    st.session_state.attempts += 1
    if user_answer.isdigit() and int(user_answer) == correct_answer:
        st.success("🎉 Correct!")
        st.session_state.score += 1
        st.session_state.problem = generate_problem()  # Generate a new problem
    else:
        st.error("❌ Incorrect! Try again.")

# Score Display
st.write(f"### Your Score: {st.session_state.score}")
st.write(f"### Total Attempts: {st.session_state.attempts}")

# Add a Fun Image for Motivation
image = Image.open("math_motivation.png")  # Add an image to the same folder as `app.py`
st.image(image, caption="Keep Going! You're doing great!", use_column_width=True)

# Footer
st.write("Enjoy learning math and improving your skills! 🎓")
