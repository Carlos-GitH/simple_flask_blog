from flask import Flask, render_template, request
import requests
import smtplib

OWN_EMAIL    = #'YOUR OWN EMAIL ADDRESS'
OWN_PASSWORD = #'YOUR EMAIL ADDRESS PASSWORD'

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/aa8c5caf93bde392d45b'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/blog_<num>')
def post(num):
    blog_url = 'https://api.npoint.io/aa8c5caf93bde392d45b'
    response = requests.get(blog_url)
    all_posts = response.json()
    post = all_posts[int(num)-1]
    return render_template("post.html", post=post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

# @app.route('/form_entry', methods=['post'])
# def form_entry():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#     return render_template("form-entry.html", name=name, email=email, phone=phone, message=message)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(OWN_EMAIL, OWN_PASSWORD)
    connection.sendmail(OWN_EMAIL, 'carlosagcf@outlook.com', email_message)


if __name__ == "__main__":
    app.run(debug=True)