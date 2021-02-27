import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

messages = []


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/mesages', methods=['GET', 'POST'])
def mesages():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']

        if email and message:
            messages.append({
                'email': email,
                'message': message
            })

            return jsonify({'ok': True, 'message': 'Message created succesfully!'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Oh shit! Something happened! Bad request parameter'}), 400

    if request.method == 'GET':
        if len(messages) > 0:
            return jsonify({'ok': True, 'message': 'Success', 'data': messages})
        else:
            return jsonify({'ok': True, 'message': 'Data message is empty broh!'}), 200

app.run()

