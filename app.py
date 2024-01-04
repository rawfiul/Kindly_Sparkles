from flask import Flask, flash, redirect, render_template, request
import sqlite3

# Flask initialize
app = Flask(__name__)
# Flask needs a secret key for the flash function to work
app.secret_key='12345'
# Connecting to the app.db to the app.py
con = sqlite3.connect("app.db", check_same_thread = False)
db = con.cursor()
# This makes the fetched row indexable by name
db.row_factory = sqlite3.Row

# Constants
REPORT_LIMIT = 6

# Index Page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # If pair is detected in url, filter according to it
        user_filter = request.args.get("user")
        if user_filter:
            db.execute("SELECT * FROM post WHERE reports <  ? AND user = ?;",(REPORT_LIMIT, user_filter,))
        else:
            # If no user filtering is detected, select all posts from db
            db.execute("SELECT * FROM post WHERE reports <  ?;", (REPORT_LIMIT,))
        all_posts = db.fetchall()
        # Reverse the posts so that newest posts are always on top
        return render_template("index.html", all_posts=reversed(all_posts))

    if request.method == "POST":
        # Flash an error if user entered 0 or too less or too much
        def validate_input(value, min_len, max_len, error_message):
            if not value or not min_len < len(value) < max_len:
                flash(error_message)
                return False
            return True
        # Checks answer before any other field
        user_answer = request.form.get("userAnswer")
        sys_answer = request.form.get("sysAnswer")
        if user_answer != sys_answer:
            flash("Incorrect or missing answer.")
            return redirect("/")
        else:
            title = request.form.get("title")
            content = request.form.get("content")
            image = request.form.get("image")
            user = request.form.get("user")

            input_valid = all([
                validate_input(title, 4, 91, "Please enter a Title of min 5 and max 90 characters."),
                validate_input(content, 14, 1001, "Please enter a story of min 15 and max 1000 characters."),
                validate_input(user, 2, 21, "Please enter a username of min 3 and max 20 characters.")
            ])

            if input_valid:
                if image and not 3 < len(image) < 1001:
                    flash("Please enter a valid URL.")
                    return redirect("/")
                # Update the db with userdata if all checks have passed
                db.execute("INSERT INTO post(user, content, image, title) VALUES (?, ?, ?, ?);", (user, content, image, title))
                con.commit()
        # Redicrect to get so that new post is instantly visible
        return redirect("/")


# Handles the like and report without refreshing the page
@app.route("/action", methods=["POST"])
def action():
    # Gets data from js using fetch()
    data = request.get_json()
    # Make appropriate changes to db
    if data:
        if data["action"] == "like":
            db.execute("UPDATE post SET likes = likes + 1 WHERE id = ?;", (int(data["id"]),))
            con.commit()
            return "Action success"
        if data["action"] == "dislike":
            db.execute("UPDATE post SET likes = likes - 1 WHERE id = ?;", (int(data["id"]),))
            con.commit()
            return "Action success"
        if data["action"] == "report":
            db.execute("UPDATE post SET reports = reports + 1 WHERE id = ?;", (int(data["id"]),))
            con.commit()
            return "Action success"
        if data["action"] == "unreport":
            db.execute("UPDATE post SET reports = reports - 1 WHERE id = ?;", (int(data["id"]),))
            con.commit()
            return "Action success"
    return "Action Error"


# about page
@app.route("/about", methods=["GET"])
def faqs():
    return render_template("about.html")

# Catch all error
@app.errorhandler(Exception)
def handle_error(e):
    # You can log the error or perform other actions here
    return render_template('error.html', error=e), 500