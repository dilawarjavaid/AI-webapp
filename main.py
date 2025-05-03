from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Gemini API key
genai.configure(api_key='AIzaSyB4AZE1qzlxX-9ieVAXCAJJmM_tkRORUoA')
