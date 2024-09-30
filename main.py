from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def    greet():
  if request.method == "POST":
    name = request.form.get("name")
    return render_template("index.html", greeting="Hola " + name + "!")
  return render_template("index.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)