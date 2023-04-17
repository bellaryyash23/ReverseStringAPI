from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/reverse_string/<user_string>', methods=['GET', 'POST'])
def reverse_string(user_string):
    string_to_reverse = user_string
    reversed_string = string_to_reverse[::-1]
    response = make_response(f'<h1>Reversed String is: {reversed_string}</h1>')
    response.headers['Content-Type'] = 'text/html'
    return response


@app.route('/')
@app.route('/reverse_string')
def home():
    response = make_response(
        '<h1>To Reverse String enter the string in following format in url: </h1><br><h1>/reverse_string/<i><u>String '
        'to be Reversed</h1>')
    response.headers['Content-Type'] = 'text/html'
    return response


if __name__ == '__main__':
    app.run(debug=True)
