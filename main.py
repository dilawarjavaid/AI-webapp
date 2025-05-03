from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Gemini API key
genai.configure(api_key='AIzaSyB4AZE1qzlxX-9ieVAXCAJJmM_tkRORUoA')

model = genai.GenerativeModel('gemini-2.0-flash-exp')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    if not user_input:
        return jsonify({'error': 'Empty message'}), 400
    response = model.generate_content(user_input)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)