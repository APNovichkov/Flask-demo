from random import choice
from flask import Flask, request


app = Flask(__name__)


compliments = ["litty", "dope", "sick", "Wow"]
life_predictions = ["You are going to die", "You will be happy", "Something bad will happen", "Nope, today is not your day",
                    "You are going to find money on the ground", "You are not going to die", "It will be sunny today"]


@app.route("/")
def index():
    return """
    <form action='/compliment'>
        What is your name
        <input type="text" name="username"></input>
        <button type="Submit">Submit</button>
    </form>
    """


@app.route("/compliment")
def give_compliment():
    name = request.args.get("username")
    compliment = choice(compliments)
    return "Hello " + str(name) + ", you are so " + compliment + "!"


if __name__ == "__main__":
    app.run(debug=True)
