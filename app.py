from flask import Flask, render_template, request
from application.database import db
from sqlalchemy import text
import ollama 

def query_to_string(query_result):

    result = ""
    if query_result:
        for row in query_result:
            result = result + str(row) + "\n"
    else:
        return "No results found."
    
    return result

def get_sql_query(user_input):
    
    prompt = [
        {'role':'system','content':"""

    Given the following database schema:

    **Employees Table**:
    - id (Integer, primary key)
    - name (String, unique, not nullable)
    - department (String, not nullable)
    - salary (Integer, not nullable)
    - hire_date (Date, not nullable)

    **Departments Table**:
    - id (Integer, primary key)
    - name (String, unique, not nullable)
    - manager (String, not nullable)


    Convert the user input into a Sql query using the following scheme. You have to only give sql query as output. No other things. I will directly run the query on the database.

    """},
        {'role':'user','content':f"{user_input}"}

    ]

    response = ollama.chat(model="llama3.2",messages=prompt)

    return response['message']['content']


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db.init_app(app)
app.app_context().push()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":

        user_query = request.form.get('input')

        try:

            sql_query = get_sql_query(user_query)

            print(sql_query)

            sql = text(sql_query)

            result = db.session.execute(sql)

            users_str = query_to_string(result.fetchall())

        except:

            users_str = "Error in processing the query. Try different query."

        return render_template('index.html', text = users_str)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
