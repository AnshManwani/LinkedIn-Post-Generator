import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import base64
from PIL import Image
import io

# Options
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

tone_options = [
    "Professional",
    "Friendly",
    "Motivational",
    "Informative",
    "Thought-provoking",
    "Humorous",
]

audience_options = [
    "Recruiters",
    "Tech Community",
    "Entrepreneurs",
    "Students",
    "Designers",
    "Career Advice",
]

def load_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

def main():
    # Load LinkedIn icon
    linkedin_icon = load_base64_image("linkedin.png")

    # Show title with icon using base64 image
    st.markdown(
        f"""
        <h1 style='display: flex; align-items: center; gap: 10px;'>
            🔗 LinkedIn Post Generator
            <img src="{linkedin_icon}" alt="LinkedIn Icon" width="30" height="30">
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Inject CSS to widen dropdowns and prevent text clipping
    st.markdown(
        """
        <style>
        div[role="combobox"] > div {
            min-width: 280px !important;
            max-width: 400px !important;
        }
        .stSelectbox > div > div > div {
            min-width: 280px !important;
            max-width: 400px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Create columns with wider layout for long dropdowns
    col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 3, 3])

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    with col4:
        selected_tone = st.selectbox("Tone", options=tone_options)

    with col5:
        selected_audience = st.selectbox("Audience", options=audience_options)

    if st.button("Generate"):
        post = generate_post(
            selected_length,
            selected_language,
            selected_tag,
            selected_tone,
            selected_audience
        )
        st.markdown(post)  # Render as markdown for better formatting

if __name__ == "__main__":
    main()
