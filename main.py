from flask import Flask, render_template
import requests


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

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)