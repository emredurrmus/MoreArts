from flask import Flask, render_template, request


from AI import *


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/movie", methods=["GET", "POST"])
def movie():
    question1answer = None
    question2answer = None
    question3answer = None
    question4answer = None
    ai_question = None
    ai_answer = None

    if request.method == "POST":
        question1answer = request.form.get("question1")
        question2answer = request.form.get("question2")
        question3answer = request.form.get("question3")
        question4answer = request.form.get("question4")
        ai_question = movie_question_maker(question1answer, question2answer, question3answer, question4answer)
        ai_answer = ask_ai(ai_question)

    return render_template("movie.html", ai_answer=ai_answer)


@app.route("/tvseries", methods=["GET", "POST"])
def tvseries():
    question1answer = None
    question2answer = None
    question3answer = None
    question4answer = None
    ai_question = None
    ai_answer = None

    if request.method == "POST":
        question1answer = request.form.get("question1")
        question2answer = request.form.get("question2")
        question3answer = request.form.get("question3")
        question4answer = request.form.get("question4")
        ai_question = tvseries_question_maker(question1answer, question2answer, question3answer, question4answer)
        ai_answer = ask_ai(ai_question)

    return render_template("tvseries.html", ai_answer=ai_answer)

@app.route("/music", methods=["GET", "POST"])
def music():
    question1answer = None
    question2answer = None
    question3answer = None
    question4answer = None
    ai_question = None
    ai_answer = None

    if request.method == "POST":
        question1answer = request.form.get("question1")
        question2answer = request.form.get("question2")
        question3answer = request.form.get("question3")
        question4answer = request.form.get("question4")
        ai_question = music_question_maker(question1answer, question2answer, question3answer, question4answer)
        ai_answer = ask_ai(ai_question)

    return render_template("music.html", ai_answer=ai_answer)


if __name__ == "__main__":
    app.run(debug=True)
