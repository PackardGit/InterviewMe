from flask import Flask, render_template, request, jsonify
import adrian_ai

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['name']
    chat_api = adrian_ai.GptApp()
    response, message = chat_api.predict(user_input, messages)

    if message:
        return jsonify({'response': response})

    return jsonify({'error': 'Missing data!'})


if __name__ == '__main__':
    messages = adrian_ai.configuration_message
    app.run(debug=False, host='0.0.0.0', port=5000)
