import google.generativeai as genai
import streamlit as st  

genai.configure(api_key="Enter_Your_API_Key")

sys_prompt = """You are an advanced AI code reviewer with deep expertise in programming, best practices, and optimization techniques. Your task is to review the given code and provide the following:

Correctness: Identify any logical, syntactical, or runtime errors. Suggest fixes if needed.
Optimization: Suggest ways to improve performance, reduce time complexity, and enhance efficiency."""

st.title("Code Review AI")
userPrompt = st.text_area("Enter your Code:")


gemini = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt)

if st.button("Generate Answer"):
    if userPrompt.strip():  # Check if input is not empty
        response = gemini.generate_content(userPrompt)
        st.write(response.text)  # Ensure text output is displayed
    else:
        st.write("Please enter a valid Data Science query.")
