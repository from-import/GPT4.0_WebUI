import g4f
from flask import Flask, request, render_template


app = Flask(__name__)

def chatgpt4(content):
    response = g4f.ChatCompletion.create(
        model= 	g4f.models.default,
        messages=[{"role": "user", "content": content}],
        proxy="http://127.0.0.1:7890",
        timeout=120, # in secs
    )
    return response

@app.route('/process', methods=['POST'])
def process_input():
    if request.method == 'POST':
        input_data = request.data.decode('utf-8')
        output_data = chatgpt4(input_data)
        return output_data

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)