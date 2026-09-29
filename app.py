import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json() or {}
    idea = data.get("idea", "").strip()
    genre = data.get("genre", "Adventure")
    characters = data.get("characters", "").strip()

    if not idea:
        return jsonify({"error": "Please enter a story idea."}), 400

    # Demo response. Replace this section with your Gemini API call.
    story = f"""TITLE
{genre} Comic: The Beginning

CHARACTERS
{characters or "Main Hero"}

STORY
Story idea: {idea}

PANELS
1. Scene: The story begins.
   Dialogue: Let's begin the adventure!
   Caption: A new journey starts.

2. Scene: The hero discovers something unusual.
   Dialogue: What is this?
   Caption: A mysterious discovery.

3. Scene: The challenge appears.
   Dialogue: I must solve this!
   Caption: The adventure becomes difficult.

4. Scene: The hero takes action.
   Dialogue: I can do this!
   Caption: Courage changes everything.

5. Scene: The problem is solved.
   Dialogue: We did it!
   Caption: The mystery is finally solved.

6. Scene: A new beginning.
   Dialogue: What comes next?
   Caption: The next adventure awaits."""

    return jsonify({"result": story})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
