''' 
Pseudo code for the entire UI

import streamlit as st

# Set up the session state
if 'show_feedback' not in st.session_state:
st.session_state.show_feedback = False

# Title for the app
st.title("SMART HR")

# Input fields
goal = st.text_area("Enter your GOAL", height=100)
measure_of_success = st.text_input("Enter your Measure of Success")
start_date = st.date_input("Select start date")
end_date = st.date_input("Select end date")
percentage = st.number_input("Enter the percentage")

# Checkboxes
checked = st.checkbox("Risk assessment")
checked1 = st.checkbox("Resource availability")
checked2 = st.checkbox("Company vision")

# Submit button
if st.button('Submit'):
st.session_state.show_feedback = True

# Conditional display of feedback and smart goal sections
if st.session_state.show_feedback:
st.subheader("Feedback")
feedback = """
The goal is good, but it can be made further better by adding a few points:
1. .....
2. ....
3. .....
Adding this will improve the overall performance.
"""
st.write(feedback)
st.subheader("Smart Goal")
smart_goal_feedback = """
Some smarter goals can be made further better by adding a few points:
1. .....
2. ....
3. .....
Adding this will improve the overall performance.
"""
st.write(smart_goal_feedback)

st.subheader("Please give your feedback:")
col1, col2 = st.columns([1, 1]) # Create two equal-width columns for feedback buttons

with col1:
thumbs_up = st.button("👍", key='thumbs_up_button')

with col2:
thumbs_down = st.button("👎", key='thumbs_down_button')
'''

# Code snippet for UI

import streamlit as st
from datetime import datetime

# Set up the session state
if 'show_feedback' not in st.session_state:
    st.session_state.show_feedback = False
if 'feedback_given' not in st.session_state:
    st.session_state.feedback_given = False
if 'feedback' not in st.session_state:
    st.session_state.feedback = None

# Defining paths for the log files
feedback_log_file = 'feedback_log.txt'

def log_feedback(feedback):
    """Log feedback to a file."""
    with open(feedback_log_file, 'a') as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'{timestamp} - {feedback}\n')

def get_feedback_count():
    """feedback count retrival from the log file."""
    like_count = 0
    dislike_count = 0
    try:
        with open(feedback_log_file, 'r') as file:
            for line in file:
                if 'Thumbs Up' in line:
                    like_count += 1
                elif 'Thumbs Down' in line:
                    dislike_count += 1
    except FileNotFoundError:
        # Log file doesn't exist yet
        pass
    return like_count, dislike_count

st.title("SMART HR")

# Input fields
goal = st.text_area("Enter your GOAL", height=100)
measure_of_success = st.text_input("Enter your Measure of Success")
start_date = st.date_input("Select start date")
end_date = st.date_input("Select end date")
#percentage = st.number_input("Enter the percentage")

Risk_assessment = st.text_area("Enter the Risk assessment", height=100)
Resource_availability = st.text_area("Enter the Resource availability", height=100)
Company_vision = st.text_area("Enter the Company vision", height=100)

# Functions displaying the values entered by the user
def get_input_values():
    return {
        "Goal": goal,
        "Measure of Success": measure_of_success,
        "Start Date": start_date,
        "End Date": end_date,
        #"Percentage": percentage,
        "Risk Assessment": Risk_assessment,
        "Resource Availability": Resource_availability,
        "Company Vision": Company_vision
    }

# Submit button
if st.button('Submit'):
    st.session_state.show_feedback = True

    # Get input values and display them
    input_values = get_input_values()
    st.write("### Entered Information")
    for key, value in input_values.items():
        st.write(f"**{key}:** {value}")

# Display feedback options if feedback is to be shown
if st.session_state.show_feedback and not st.session_state.feedback_given:
    st.write("### Please provide your feedback:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button('👍'):
            st.session_state.feedback = 'Thumbs Up'
            st.session_state.feedback_given = True
            log_feedback(st.session_state.feedback)
    with col2:
        if st.button('👎'):
            st.session_state.feedback = 'Thumbs Down'
            st.session_state.feedback_given = True
            log_feedback(st.session_state.feedback)

# Optionally, you could display the feedback given by the user
if st.session_state.feedback_given:
   st.write(f"### Feedback received: {st.session_state.feedback}")

# Display feedback count
#like_count, dislike_count = get_feedback_count()
#st.write(f"### Feedback Count")
#st.write(f"👍 Thumbs Up: {like_count}")
#st.write(f"👎 Thumbs Down: {dislike_count}")
