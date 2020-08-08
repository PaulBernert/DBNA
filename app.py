# Import Necessary Libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

@app.route("/clustering")
def clustering():
    return render_template("clustering.html")

@app.route("/methodology/ease-of-doing-business")
def methodology_eodb():
    return render_template("methodology_eodb.html")

@app.route("/methodology/starting-a-business")
def methodology_sab():
    return render_template("methodology_sab.html")

@app.route("/methodology/employing-workers")
def methodology_ew():
    return render_template("methodology_ew.html")

@app.route("/methodology/getting-electricity")
def methodology_ge():
    return render_template("methodology_ge.html")

@app.route("/methodology/paying-taxes")
def methodology_pt():
    return render_template("methodology_pt.html")

@app.route("/methodology/land-space-use")
def methodology_lsu():
    return render_template("methodology_lsu.html")

@app.route("/methodology/resolving-insolvency")
def methodology_re():
    return render_template("methodology_re.html")

if __name__ == "__main__":
    app.run()
