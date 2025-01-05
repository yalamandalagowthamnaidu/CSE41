from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import pandas as pd
from transformers import pipeline
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide query response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to fetch the schema of the table
def get_table_schema(db_file, table_name):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        schema = cursor.fetchall()
        return [(col[1], col[2]) for col in schema]  # Returns column names and types
    except Exception as e:
        print(f"An error occurred while fetching the schema: {e}")
        return []
    finally:
        if 'connection' in locals():
            connection.close()

# Function to convert CSV to SQLite3 database
def csv_to_sqlite(csv_file, db_file, table_name):
    try:
        df = pd.read_csv(csv_file)
        connection = sqlite3.connect(db_file)
        df.to_sql(table_name, connection, if_exists='replace', index=False)
        print(f"Data successfully loaded into table '{table_name}' in the database '{db_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'connection' in locals():
            connection.close()

# Function to execute queries on SQLite3 database
def execute_query(db_file, query):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            results = cursor.fetchall()
            return results
        else:
            connection.commit()
            print("Query executed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'connection' in locals():
            connection.close()

# Function to provide reasoning for the query and results using Gemini
def provide_reasoning(question, sql_query, results):
    prompt = f"""
    You are an AI assistant skilled in SQL and reasoning. Explain the following:
    - The natural language question: '{question}'
    - The SQL query: '{sql_query}'
    - The results obtained: {results if results else 'No results found'}
    Provide a detailed reasoning for the generated query and its output.
    """
    reasoning_response = get_gemini_response(question, [prompt])
    return reasoning_response

# Streamlit App
st.set_page_config(page_title="SQL Query & Reasoning Tool")
st.header("SQL Query and Reasoning")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload your dataset (CSV format):", type=["csv"])
database_file = "user_data.db"
table_name = "uploaded_table"

if uploaded_file:
    csv_to_sqlite(uploaded_file, database_file, table_name)
    st.success(f"File uploaded and data loaded into table '{table_name}'.")

# Fetch and display schema
table_schema = get_table_schema(database_file, table_name)
st.subheader("Table Schema:")
st.write(pd.DataFrame(table_schema, columns=["Column Name", "Data Type"]))

# Enhanced prompt for Gemini model
prompt = [
    f"""
    You are an expert in converting English questions to SQL query!
    The SQL database has a table named '{table_name}' with the following schema:
    {', '.join([f'{col[0]} ({col[1]})' for col in table_schema])}.
    Generate an SQL query based on the input question.
    Ensure the query references the table '{table_name}' and infers column names based on the schema.
    Avoid extra formatting such as ''' or the word SQL explicitly.
    """
]

# Input for natural language question
question = st.text_input("Enter your query in natural language:")
submit = st.button("Generate Query and Execute")

if submit and question:
    sql_query = get_gemini_response(question, prompt)
    st.write(f"Generated SQL Query: {sql_query}")

    # Execute the query
    results = execute_query(database_file, sql_query)

    # Display results
    if results:
        st.subheader("Query Results:")
        st.write(pd.DataFrame(results))
    else:
        st.warning("No results found for the query.")

    # Provide reasoning
    reasoning = provide_reasoning(question, sql_query, results)
    st.subheader("Reasoning:")
    st.write(reasoning)
