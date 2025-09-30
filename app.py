import streamlit as st

# Initialize session state to track view and selection
if 'view' not in st.session_state:
    st.session_state.view = 'topic_selection'
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = None

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

def show_question_page():
    st.button("← Back to Topic Selection", on_click=go_back)
    st.header(f"Topic: {st.session_state.selected_topic}")
    if st.button("Generate Question"):
        # Placeholder for LLM integration, generates a sample question below:
        st.write("Sample multiple-choice question about " + st.session_state.selected_topic)
        # Options would be generated dynamically in production
        st.radio("Choose an answer:", ["A", "B", "C", "D"])
    st.text_input("Your response:")

def go_back():
    st.session_state.view = 'topic_selection'
    st.session_state.selected_topic = None

# Display the correct view
if st.session_state.view == 'topic_selection':
    show_topic_selection()
elif st.session_state.view == 'question_page':
    show_question_page()
