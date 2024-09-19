# import streamlit as st
# import os
# import google.generativeai as genai
# import speech_recognition as sr
# import pyttsx3

# # Replace with your actual API key
# os.environ["GOOGLE_API_KEY"] = "YOUR API KEY"

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Gemini model
# model = genai.GenerativeModel("gemini-pro")

# def get_gemini_response(question):
#     try:
#         response = model.generate_content(question)
#         return response.text
#     except Exception as e:
#         st.error(f"Error getting Gemini response: {e}")
#         return None

# # Text-to-speech engine
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # Female voice

# # Speech-to-text recognizer
# recognizer = sr.Recognizer()

# def speak(text):
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         st.error(f"Error speaking: {e}")

# def listen():
#     with sr.Microphone() as source:
#         try:
#             st.write("Listening...")
#             audio = recognizer.listen(source)
#             text = recognizer.recognize_google(audio)
#             return text
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't understand that.")
#             return None
#         except sr.RequestError as e:
#             speak("Could not request results from Google Speech Recognition service; {0}".format(e))
#             return None
#         except Exception as e:
#             st.error(f"Error listening: {e}")
#             return None

# st.set_page_config(page_title="AI chatbot")
# st.header("AI Chatbot")

# # Voice input toggle
# voice_input = st.checkbox("Voice Input")

# if voice_input:
#     if st.button("Speak"):
#         user_input = listen()
#         if user_input:
#             response = get_gemini_response(user_input)
#             if response:
#                 speak(response)
#                 st.subheader("Your query:")
#                 st.write(user_input)
#                 st.subheader("AI Response:")
#                 st.write(response)
# else:
#     input = st.text_input("Input:")
#     submit = st.button("Ask the question:")

#     if submit:
#         response = get_gemini_response(input)
#         st.subheader("The response is")
#         st.write(response)
import streamlit as st
import os
import google.generativeai as genai

# Replace with your actual API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyD39ML8eh_7rL-i1ALQTMcfeds-E_GAVag"

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini model
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        st.error(f"Error getting Gemini response: {e}")
        return None

st.set_page_config(page_title="AI chatbot")
st.header("AI Chatbot")

input = st.text_input("Input:")
submit = st.button("Ask the question:")

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)
