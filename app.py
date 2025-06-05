from flask import Flask, request, render_template
from models import StoryRequest
from groq_agent import get_generated_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        data = StoryRequest(
            type=request.form["type"],
            tone=request.form["tone"],
            genre=request.form["genre"],
            length=int(request.form["length"]),
            title=request.form.get("title", ""),
            characters=request.form.get("characters", "").split(","),
        )
        output = get_generated_text(data)
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)