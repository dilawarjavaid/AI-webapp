This is a simple web-based chatbot built with Flask, HTML/CSS (Bootstrap), jQuery, and Google's Gemini API. It allows users to interact with Google's Gemini LLM through a clean and responsive web interface.

🚀 Features
Chat interface with user-friendly styling

Asynchronous communication using AJAX

Markdown support using Showdown.js

Real-time responses from Google's Gemini 2.0 Flash model

🛠️ Technologies Used
Flask (Python Web Framework)

Gemini API (Google Generative AI)

HTML, CSS (Bootstrap 5), JavaScript (jQuery)

Showdown.js (Markdown to HTML converter)

🧰 Installation & Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/gemini-chatbot-flask.git
cd gemini-chatbot-flask
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
requirements.txt should include:

nginx
Copy
Edit
Flask
google-generativeai
3. Set Your Gemini API Key
Replace this line in your Python script:

python
Copy
Edit
genai.configure(api_key='YOUR_API_KEY')
with your actual API key from Google AI Studio.

🔐 Warning: Never expose your API key in production. Use environment variables for security.

4. Run the Application
bash
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:5000

📁 Project Structure
php
Copy
Edit
├── app.py                 # Main Flask app
├── templates/
│   └── index.html         # Frontend HTML file
├── static/                # (Optional) For any custom CSS/JS
├── requirements.txt       # Python dependencies
└── README.md              # This file
🧪 Sample Usage
Type a message like "Tell me a joke" and hit Send

The bot responds using the Gemini 2.0 Flash model

Markdown formatting is supported in responses

🧩 Notes
Make sure you’re using the right model name: 'gemini-2.0-flash-exp'

This app currently doesn't handle conversations (no chat history tracking)

For production, consider hiding API keys and using HTTPS
