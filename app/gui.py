import streamlit as st

def run_app():
    st.set_page_config(page_title="Mini Fitness Coach 🏋️‍♂️", layout="centered")

    st.title("🏋️‍♂️ Mini Fitness Coach")
    st.write("Welcome to your personal fitness assistant!")

    name = st.text_input("What's your name?")
    goal = st.selectbox(
        "What’s your workout goal today?",
        ["Build muscle 💪", "Burn fat 🔥", "Improve endurance 🏃‍♂️", "Just stay active 😎"]
    )
    duration = st.slider("How long do you want to train? (minutes)", 5, 120, 30)

    if st.button("Start Workout"):
        if name:
            st.success(f"Great, {name}! Let's start your {goal.lower()} workout for {duration} minutes! 💪")
        else:
            st.warning("Please enter your name first!")

# This makes Streamlit run it automatically
if __name__ == "__main__":
    run_app()