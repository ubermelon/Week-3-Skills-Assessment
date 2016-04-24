from flask import Flask, render_template, request, session
import jinja2

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def apply():

	return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def response_page():

	fname = request.form.get("fname")
	lname = request.form.get("lname")
	salary = request.form.get("salary")
	position = request.form.get("position")

	return render_template("application-response.html", fname=fname, lname=lname, salary=salary, position=position)

if __name__ == "__main__":
    app.run(debug=True)
