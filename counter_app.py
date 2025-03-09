from flask import Flask, render_template
import os

app = Flask(__name__)

# Counter file
counter_file = "counter.txt"

# Ensure the counter file exists
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

@app.route("/")
def index():
    with open(counter_file, "r") as f:
        count = int(f.read())
    return render_template("index.html", count=count)

@app.route("/click")
def click():
    with open(counter_file, "r") as f:
        count = int(f.read()) + 1
    with open(counter_file, "w") as f:
        f.write(str(count))
    return str(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
