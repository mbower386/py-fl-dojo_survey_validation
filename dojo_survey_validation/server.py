from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from mysqlconnection import connectToMySQL

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/add_survey', methods=["POST"])
def add_pet_to_db():
    mysql = connectToMySQL("survey_db")
    query = "INSERT INTO surveys (name, location, language, comment) VALUES (%(nm)s, %(lo)s, %(la)s, %(cm)s);"
    data = {
        'nm': request.form["username"],
        'lo': request.form["location"],
        'la': request.form["language"],
        'cm': request.form["comment"]
    }
    mysql.query_db(query, data)
    return redirect("/survey", )


@app.route('/survey')
def view_survey():
    # call the function, passing in the name of our db
    mysql = connectToMySQL('survey_db')
    # call the query_db function, pass in the query as a string
    surveys = mysql.query_db('SELECT * FROM survey_db.surveys;')
    print(surveys)
    return render_template("submitted.html", all_surveys=surveys)


if __name__ == "__main__":
    app.run(debug=True)
