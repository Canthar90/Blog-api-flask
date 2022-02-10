from flask import Flask, render_template
import requests
from datetime import date

app = Flask(__name__)

posts = []

@app.route('/')
def home():
    global posts
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    posts = response.json()
    # print(posts)
    year = date.today()
    # print(year)
    return render_template("index.html", posts=posts, date=year)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<int:index>')
def post(index):
    year = date.today()
    post = posts[index]
    print(post)
    num = index+1
    pictiure = f"""/assets/img/post_image{num}.jpg"""
    return render_template("post.html", post=post, date=year, image=pictiure)


@app.route('/contact')
def contact():
    return render_template("contact.html")



if __name__=="__main__":
    app.run(debug=True)