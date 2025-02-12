# Chat Assistant for Database

This project implements an AI chatbot that allows users to interact with a SQLite database using natural language queries. The chatbot converts user input into SQL statements, executes them, and returns formatted responses, making data retrieval accessible without requiring SQL knowledge.

## Problem Statement

Build an AI chatbot that will accept natural language queries from users, convert them into SQL statements, execute them on a provided SQLite database, and return clear, formatted responses. The chatbot should enable seamless interaction with the database without requiring users to have SQL knowledge, making data retrieval more accessible and efficient.

## Features

- Natural language query processing
- SQL query generation from user input
- Execution of SQL queries on a SQLite database
- User-friendly response formatting

## Technologies Used

- Python: Primary programming language
- Flask: Web application framework
- Flask-SQLAlchemy: Database interactions with SQLite
- Ollama: Advanced language model integration
- Meta Llama 3.2: Multilingual large language model for query processing

## Database Schema

The project uses a sample database with two tables:

### Employees Table

| Column    | Type    |
|-----------|---------|
| ID        | Integer |
| Name      | Text    |
| Department| Text    |
| Salary    | Integer |
| Hire_Date | Date    |

### Departments Table

| Column  | Type    |
|---------|---------|
| ID      | Integer |
| Name    | Text    |
| Manager | Text    |

## Chatbot Functionality

- Understanding user's natural language queries
- Translating queries to SQL
- Executing SQL queries against the database
- Presenting results in a user-friendly format

## Setup and Installation

1. Clone the repository
2. Install required dependencies:
   pip install flask flask-sqlalchemy ollama
4. Install Ollama following the instructions at: https://ollama.ai/download
5. Pull and run the Llama 3.2 model:
   ollama pull llama3.2
   ollama run llama3.2
5. Run the Flask application:
6. Access the chatbot interface at `http://127.0.0.1:5000`

## Usage

Users can interact with the chatbot by entering natural language queries. Example queries include:

- Show me all employees in the [department] department.
- Who is the manager of the [department] department?
- List all employees hired after [date].
- What is the total salary expense for the [department] department?

## Challenges and Limitations

- Handling complex and ambiguous queries
- Ensuring accurate and efficient database interactions
- High computational resource requirements for efficient processing

## Future Improvements

- Expand the range of supported query types
- Implement more advanced natural language processing techniques
- Optimize performance for larger databases

## About Meta Llama 3.2

The Meta Llama 3.2 collection of multilingual large language models is a collection of pre-trained and instruction-tuned generative models in 1B and 3B sizes. The Llama 3.2 instruction-tuned text only models are optimized for multilingual dialogue use cases, including agentic retrieval and summarization tasks.

