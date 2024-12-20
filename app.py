import streamlit as st
import random

# App Title
st.title("Interactive Math Tutor")

# Greeting the User
st.sidebar.title("Welcome!")
user_name = st.sidebar.text_input("Enter your name:", placeholder="Type your name...")
if user_name:
    st.sidebar.write(f"Hello, {user_name}! 🎉")

# Generate Math Problem
def generate_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2, num1 + num2

# Initialize Session State
if "problem" not in st.session_state:
    st.session_state.problem = generate_problem()
if "score" not in st.session_state:
    st.session_state.score = 0

# Display the Problem
num1, num2, correct_answer = st.session_state.problem
st.write(f"**Solve this:** {num1} + {num2} = ?")

# User Input
user_answer = st.text_input("Your Answer:", placeholder="Enter your answer here...")

# Submit Button
if st.button("Submit"):
    if user_answer.isdigit() and int(user_answer) == correct_answer:
        st.success("🎉 Correct!")
        st.session_state.score += 1  # Increment score
        st.session_state.problem = generate_problem()  # Generate a new problem
    else:
        st.error("❌ Wrong! Try again.")

# Display Score
st.write(f"**Your Score:** {st.session_state.score}")

# Footer
st.write("Enjoy learning math!")
