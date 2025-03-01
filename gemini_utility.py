import os

import google.generativeai as genai
from dotenv import load_dotenv

# load the environment variables
load_dotenv()

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure API key
genai.configure(api_key=GOOGLE_API_KEY)

def load_gemini_model():
    model = genai.GenerativeModel('gemini-1.5-flash')
    return model