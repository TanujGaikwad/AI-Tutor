import streamlit as st
import openai

# Set API key securely
# openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize session state to track view and selection
if 'view' not in st.session_state:
    st.session_state.view = 'topic_selection'
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = None

# List of topics found on average for each grade level
topics = {
    "5th Grade": [
        "Fractions and Decimals",
        "Volume and Measurement",
        "Order of Operations",
        "Graphing on Coordinate Planes",
        "Geometry (Angles, Triangles, Quadrilaterals)",
        "Multiplication & Division",
        "Statistics & Probability"
    ],
    "6th Grade": [
        "Ratios and Proportional Relationships",
        "Integers and Rational Numbers",
        "Algebraic Expressions and Equations",
        "Coordinate Plane and Geometry",
        "Statistics and Probability",
        "Operations with Decimals and Fractions"
    ],
    "7th Grade": [
        "Proportional Relationships",
        "Operations with Rational Numbers",
        "Algebraic Expressions, Equations, & Inequalities",
        "Percentages and Applications",
        "Geometry (Area, Volume, Surface Area)",
        "Statistics and Probability"
    ]
}

# Main app logic
# Placeholder function for LLM question generation
# def generate_question(topic):
#     prompt = f"Generate a multiple-choice math question related to this topic for 5th to 7th graders: {topic}. Provide 4 options labeled A to D."
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=150,
#         temperature=0.7,
#         n=1,
#         stop=None,
#     )
#     return response.choices[0].text.strip()

# Refreshes page to show the main menu of topics
def show_topic_selection():
    st.title("AI Math Tutor")
    grade = st.selectbox("Select your grade level:", list(topics.keys()))
    st.write(f"You selected: {grade}")
    st.header("Math Topics")
    
    for topic in topics[grade]:
        if st.button(topic):
            st.session_state.selected_topic = topic
            st.session_state.view = 'question_page'
            st.rerun()

# Refreshes page to start a question generation session
def show_question_page():
    st.button("← Back to Topic Selection", on_click = go_back)
    st.header(f"Topic: {st.session_state.selected_topic}")
    if st.button("Generate Question"):
        # Placeholder for LLM integration, generates a sample question:
        st.write("Sample multiple-choice question about " + st.session_state.selected_topic)

        # API Call will happen here with context of selected topic and grade level as well as expected answer.
        # Once student answers question, don't empty the area, instead provide feedback and then a button to generate a new question.
        
        # Options would be generated dynamically in production
        st.radio("Choose an answer:", ["A", "B", "C", "D"])

# Change session state to show the topics page
def go_back():
    st.session_state.view = 'topic_selection'
    st.session_state.selected_topic = None

# Display the chosen view
if st.session_state.view == 'topic_selection':
    show_topic_selection()
elif st.session_state.view == 'question_page':
    show_question_page()
