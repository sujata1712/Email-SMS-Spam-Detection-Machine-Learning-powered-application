# Email-SMS-Spam-Detection-Machine-Learning-powered-application
This is a Machine Learning–powered application that detects whether a given Email or SMS message is Spam or Not Spam (Ham).
The project includes both the model training pipeline (Jupyter Notebook) and a Streamlit web app for real-time predictions.

----
# Features
- Preprocessing: Tokenization, Stopword Removal, Punctuation Removal, Stemming
- Feature Extraction: TF-IDF Vectorization
- Classification using Machine Learning models (final model saved as spam_model.pkl)
- Easy-to-use Streamlit Web App for instant spam detection
- Modular code with clear training (.ipynb) and deployment (.py) files
  
---
# Project Structure

├── app.py                     # Streamlit app for live spam detection  
├── Email_Spam_Detection.ipynb # Jupyter Notebook (data preprocessing, training, evaluation)  
├── spam_model.pkl             # Saved trained ML model  
├── vectorizer.pkl             # Saved TF-IDF vectorizer  
├── requirements.txt           # Python dependencies  
├── README.md                  # Project documentation  

---
# Model Training

- Open Email_Spam_Detection.ipynb in Jupyter Notebook.
- The notebook covers:
        - Data Preprocessing
        - Feature Extraction (TF-IDF)
        - Model Training (Random Forest, Naïve Bayes, etc.)
        - Model Evaluation & Selection
        - Saving the trained model (spam_model.pkl) and vectorizer (vectorizer.pkl)

---
# Running the Streamlit App
Run the following command inside the project directory:

```bash
streamlit run app.py

  
