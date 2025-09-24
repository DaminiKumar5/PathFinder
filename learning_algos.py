import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Get the directory of the current script (learning_algos.py)
script_dir = os.path.dirname(__file__)

# Construct the full path to the Excel file
file_path = os.path.join(script_dir, "learning_platform_data.xlsx")

# Check if the file exists before attempting to read
if not os.path.exists(file_path):
    # This will raise a clear error if the file isn't found
    raise FileNotFoundError(f"Excel file not found at: {file_path}")

df = pd.read_excel(file_path)

df['profile'] = (
    df['Highest_Qualification'].astype(str) + " " +
    df['Majors'].astype(str) + " " +
    df['Current_Role'].astype(str) + " " +
    df['Desired_Designation'].astype(str)
)

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df['profile'])

def recommend_courses(user_input, top_n=5):
    print("in recommend_courses")
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)

    df_copy = df.copy()
    df_copy['score'] = similarity[0]
    recommendations = df_copy.sort_values(by='score', ascending=False).head(top_n)

    return recommendations[['Name', 'Highest_Qualification', 'Majors',
                            'Current_Role', 'Desired_Designation', 'score']]
