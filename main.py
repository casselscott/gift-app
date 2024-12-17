import streamlit as st
import openai
from PIL import Image
import os
from dotenv import load_dotenv



def add_custom_css():
     st.markdown(
        """
        <style>
        /* Full-width background color */
        .stApp {
            background-color: black;
            background-size: cover;
            background-position: center;
        }

        /* Full-width header image styling */
        .full-width-image {
            width: 100%;
            height: auto;
        }

        /* Sidebar background color */
        .css-1lcbmhc { /* Class for sidebar container */
            background-color: #111;
            color: dark;
        }

        /* Text colors for sidebar and app */
        .css-1lcbmhc, .css-1v3fvcr { /* Sidebar and main container text */
            color: black;
        }

        /* Inputs and buttons styling */
        textarea, input, button {
            background-color: #333;
            color: white;
            border: 1px solid #555;
        }

        /* Heading colors */
        h1, h2, h3, h4, h5, h6 {
            color: white;
        }


        /* Footer styling */
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #111;
            color: white;
            text-align: left;
            padding: 10px 0;
            font-size: 14px;
        }

        /* Add spacing between elements */
        .spacer {
            height: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )



# Load environment variables from .env file
load_dotenv()

# Access the secret key
secret_key = os.getenv('OPENAI_KEY')


def add_footer():
    st.markdown(
        """
        <div class="footer">
            © 2024 Merry Christmas and a Happy New Year!!!| Created with ❤️ by Soft Tech Group
        </div>
        """,
        unsafe_allow_html=True
    )
# Streamlit app
def main():
    # Apply custom CSS
    add_custom_css()
    
    st.title("The Season of Joy and Love!!!")

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    
    st.video("images/christmas.mp4")

    # Sidebar for customization


    st.sidebar.title("")
    st.sidebar.image("images/tree.jpeg")
    temperature = st.sidebar.slider(
        "Temperature", 0.0, 1.0, 0.7, step=0.1,
        help="Controls the randomness of the model's responses."
    )
    max_tokens = st.sidebar.slider(
        "Max Tokens", 50, 300, 150, step=10,
        help="Controls the length of the response."
    )
    prompt = st.text_area(":", placeholder="Find the Perfect Gift...")

    # Submit button
    if st.button("Generate Ideas"):
        if prompt.strip() == "":
            st.warning("Please Suggest a Christmas Gift.")
        else:
            with st.spinner("Generating response..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=temperature,
                        max_tokens=max_tokens
                    )
                    st.success("Response Generated!")
                    st.text_area("Personalised Gifts Suggestions:", response["choices"][0]["message"]["content"], height=200)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

          # Add the footer
    add_footer()

if __name__ == "__main__":
    main()
