import streamlit as st
import pandas as pd
import os

# Define the path for the subjects data file
DATA_DIR = "data"
SUBJECTS_FILE = os.path.join(DATA_DIR, "subjects.csv")


def ensure_data_file_exists():
    """Create the data directory and subjects.csv if they don't exist."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(SUBJECTS_FILE):
        pd.DataFrame(columns=["subject_name", "description"]).to_csv(
            SUBJECTS_FILE, index=False
        )


def load_subjects():
    """Load subjects from the CSV file."""
    ensure_data_file_exists()
    return pd.read_csv(SUBJECTS_FILE)


st.set_page_config(page_title="Add Subjects", page_icon="📚")

st.title("📚 Manage Subjects")

subjects_df = load_subjects()

st.header("Current Subjects")
if subjects_df.empty:
    st.info("No subjects have been added yet.")
else:
    st.dataframe(subjects_df, use_container_width=True)

st.header("Add a New Subject")
with st.form("add_subject_form", clear_on_submit=True):
    subject_name = st.text_input("Subject Name")
    subject_description = st.text_area("Description (Optional)")
    submitted = st.form_submit_button("Add Subject")

    if submitted:
        if not subject_name:
            st.error("Subject name cannot be empty.")
        elif subject_name in subjects_df["subject_name"].values:
            st.warning(f"Subject '{subject_name}' already exists.")
        else:
            new_subject = pd.DataFrame([{"subject_name": subject_name, "description": subject_description}])
            updated_subjects = pd.concat([subjects_df, new_subject], ignore_index=True)
            updated_subjects.to_csv(SUBJECTS_FILE, index=False)
            st.success(f"Successfully added subject: {subject_name}")
            st.rerun()