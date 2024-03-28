from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

# Replace with your actual API key
API_KEY = "AIzaSyBH4ASza_0YKfxeeOvyb8ZqOYHaOuDHoWM"

@app.route("/api/ai-function", methods=["POST"])
def ai_function():
  data = request.get_json()
  if data and "input" in data and data["api_key"] == API_KEY:
    # Process user input using your AI logic (replace with actual functionality)
    output = utils.process_ai_request(data["input"])
    return jsonify({"output": output})
  else:
    return jsonify({"error": "Invalid request"}), 401

if __name__ == "__main__":
  app.run(debug=True)
