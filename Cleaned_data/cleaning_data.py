import pandas as pd
import string
import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Download required NLTK data files (run once)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Define stopwords set
stop_words = set(stopwords.words('english'))

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    if not isinstance(text, str):
        return ""

    # Lowercase
    text = text.lower()

    # Remove punctuation and special characters using regex
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize by splitting on whitespace
    words = text.split()

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    # Lemmatize each word
    words = [lemmatizer.lemmatize(word) for word in words]

    # Join words back into a single string
    return ' '.join(words)

column_to_clean1 = 'Abstract' 
column_to_clean2 = 'Article Title' 

# Iterate through 5 Excel files
for i in range(1, 6):
    excel_filename = f'dataset-{i}.xls'
    print(f"Processing {excel_filename} ...")

    # Load Excel file
    df = pd.read_excel(excel_filename)

    # Clean the specified columns
    df[column_to_clean1] = df[column_to_clean1].apply(clean_text)
    df[column_to_clean2] = df[column_to_clean2].apply(clean_text)

    # Save to JSON file
    json_filename = f'cleaned-dataset{i}.json'
    df.to_json(json_filename, orient='records')

    print(f"Cleaned data saved to {json_filename}\n")
