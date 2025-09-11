import streamlit as st
import pickle

import nltk
from nltk.corpus import stopwords # stopwords don’t carry significant meaning, e.g: a, the, is, in, of, and etc
from nltk.stem.porter import PorterStemmer # stemming is the process of reducing a word to its root form
import string

# Text cleaning function
def transform_text(text):
  text=text.lower() #convert in lower case

  text=nltk.word_tokenize(text) #tokenization of words


  #remove special characters, stopwords and punctuation

  y=[] #store cleaned characters
  for i in text:
    if i.isalnum(): #checks whether the character i is alphanumeric — meaning: Letters (A–Z, a–z),Digits (0–9)
      if i not in stopwords.words('english') and i not in string.punctuation: #check for stopwords and punctuation
        y.append(i)

  text=y[:]
  y.clear()

  ps= PorterStemmer()
  for i in text:
    y.append(ps.stem(i))

  return " ".join(y) #return as string



# Load the trained model and vectorizer
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# Streamlit App
st.title("📧 Email/SMS Spam Detector")

st.markdown("""
    This app detects whether an email or SMS message is **Spam** or **Not Spam (Ham)**.
    Simply enter your message and click **Predict** to check instantly.
    """)
st.markdown("---")

user_input = st.text_area("Enter your message:")

if st.button('Predict'):
    if user_input.strip() != "":
        trans=transform_text(user_input)
        vect=vectorizer.transform([trans])
        pred=model.predict(vect)[0]

        if pred==1:
            st.error("This looks like SPAM!")
        else:
            st.success("This looks like HAM (Not Spam).")

    else:
        st.warning("Please enter a message.")
