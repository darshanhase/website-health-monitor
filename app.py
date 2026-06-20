from flask import Flask, request, render_template, redirect, url_for
import requests, time
import database

app = Flask(__name__)

# Home page: form to enter website URL
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # request.form gets data from HTML form input
        url = request.form["url"]

        try:
            start = time.time()
            response = requests.get(url, timeout=5)
            latency = round((time.time() - start) * 1000, 2)  # ms
            status = response.status_code
        except Exception as e:
            latency = None
            status = f"Error: {e}"

        # Save result into SQLite
        database.insert_result(url, status, latency)

        # Show current result
        return render_template("index.html", result={"url": url, "status": status, "latency": latency})

    return render_template("index.html", result=None)

# History page: show all past checks
@app.route("/history")
def history():
    results = database.get_all_results()
    return render_template("history.html", results=results)

if __name__ == "__main__":
    database.init_db()
    app.run(debug=True)
