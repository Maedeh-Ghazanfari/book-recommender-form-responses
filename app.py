import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="your information")

st.title("📚 Quick Book Recommender")

# Shortened form
name = st.text_input("Your Name or Nickname (optional):")

genres = st.multiselect(
    "What genres do you enjoy?",
    ["Fantasy", "Science Fiction", "Romance", "Mystery", "Thriller", "Historical",
     "Non-Fiction", "Self-Help", "Horror", "Biography", "Young Adult", "Classics"]
)

books_loved = st.text_area("Tell us a few books you've loved recently:")

mood_request = st.text_area("What kind of book are you in the mood for right now?")

style = st.multiselect(
    "Preferred storytelling style (optional):",
    ["Fast-paced", "Descriptive", "Dialogue-heavy", "Character-driven", "Action-driven"]
)

submit = st.button("Submit")

if submit:
    entry = {
        "timestamp": datetime.now(),
        "name": name,
        "genres": ", ".join(genres),
        "books_loved": books_loved,
        "mood_request": mood_request,
        "style": ", ".join(style)
    }

    try:
        df = pd.read_csv("user_data.csv")
        df = df.append(entry, ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([entry])

    df.to_csv("user_data.csv", index=False)
    st.success("✅ Thanks! We’ve saved your preferences.")
