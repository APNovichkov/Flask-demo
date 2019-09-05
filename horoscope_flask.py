from flask import Flask, request
from random import sample


app = Flask(__name__)

predictions = ["You are going to collapse", "You will be happy", "Something bad will happen", "Nope, today is not your day",
               "You are going to find money on the ground", "You are not going to die", "It will be sunny today",
               "It will rain today", "You will lose all your money", "Someone will help you today"]


@app.route('/')
def index():
    return """
    <form action='/compliment'>
        <p>
            What is your name?
            <input type="text" name="name"/>
        </p>
        <p>
            <input type="checkbox" name="show_predictions"/>
            Show Horoscope
        </p>
        <p>
            How many horoscope predictions?
            <select name="num_predictions">
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
            </select>
        </p>
        <input type="submit">
    </form>
    """


@app.route('/compliment')
def get_compliment():
    name = request.args.get('name')
    num_predictions = int(request.args.get('num_predictions'))
    show_predictions = request.args.get('show_predictions')
    horocope_prediction = ', '.join(sample(predictions, num_predictions))

    if show_predictions:
        return f'Hello there, {name}! {horocope_prediction}!'
    else:
        return f'Hello there, {name}! You are not ready for the Horoscope yet!'


if __name__ == "__main__":
    app.run(debug=True)
