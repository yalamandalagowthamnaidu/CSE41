# Database Query and Reasoning

## Overview
This project, **Database Query and Reasoning**, is an intelligent system designed to bridge the gap between natural language inputs and SQL database querying. It empowers users with little to no technical expertise to interact with databases through natural language, generating SQL queries, executing them, and providing detailed reasoning for the results.

## Features
- **Natural Language to SQL Translation**: Converts user-provided natural language queries into accurate SQL commands.
- **Reasoning Module**: Explains how the SQL query was generated and provides context for the results.
- **Dynamic Schema Handling**: Adapts to various database schemas by extracting table structures and column details.
- **CSV Integration**: Allows users to upload datasets in CSV format, which are automatically converted into SQLite databases.
- **User-Friendly Interface**: Built with Streamlit for intuitive interactions, real-time feedback, and visualizations.

## Technology Stack
- **Programming Language**: Python
- **Database**: SQLite
- **Frontend**: Streamlit
- **AI Integration**: Google Gemini AI for natural language processing and reasoning generation
- **Libraries**:
  - `pandas` for data manipulation
  - `sqlite3` for database operations
  - `transformers` for AI-based query generation
  - `python-dotenv` for secure API key management

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/database-query-reasoning.git
   cd database-query-reasoning
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the environment variables:
   - Create a `.env` file in the root directory.
   - Add your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Upload a CSV file through the user interface.
2. View the extracted database schema.
3. Enter a natural language query in the input field.
4. The system generates and executes the corresponding SQL query.
5. View the query results along with detailed reasoning for the output.

## Project Structure
- `app.py`: Main application file for Streamlit.
- `requirements.txt`: List of required Python libraries.
- `.env`: Environment file for storing API keys (not included in the repository).
- `data/`: Directory for storing uploaded datasets.
- `modules/`: Contains modules for handling CSV conversion, query processing, and reasoning.

## Future Enhancements
- **Support for Larger Databases**: Extend compatibility to cloud-based databases like PostgreSQL or MySQL.
- **Multilingual Query Support**: Enable the system to process queries in multiple languages.
- **Enhanced Visualizations**: Add graphical representations for query results and reasoning insights.
- **Advanced Querying Features**: Support for joins, nested queries, and subqueries.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any questions or feedback, feel free to contact:
- **Name**: Yalamandala Gowtham Naidu
- **Email**: [Your Email Address]
- **Affiliation**: Presidency University, Bangalore, Karnataka

