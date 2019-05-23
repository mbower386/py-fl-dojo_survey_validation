from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=["POST"])
def process_form():
    print("*" * 50)
    print(request.form)
    print(f"username submitted: {request.form['username']}")
    print(f"location submitted: {request.form['location']}")
    print(f"language submitted: {request.form['language']}")
    print(f"comment submitted: {request.form['comment']}")

    return render_template("submitted.html", 
    name=request.form["username"], location=request.form["location"], language=request.form["language"], comment=request.form["comment"])


if __name__ == "__main__":
    app.run(debug=True)
