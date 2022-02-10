from flask import Flask, render_template, request
import requests
from datetime import date
from smtplib import SMTP
import os

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
    message = "A random stuff from the internet"
    return render_template("index.html", posts=posts, date=year, image="/assets/img/home-bg.jpg", message=message)


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


@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        name = request.form['contact_name']
        contact_email = request.form['contact_email']
        phone_nr = request.form['contact_phone_number']
        message_tosent = request.form['contact_message']
        email = os.environ.get('EMAIL')
        password = os.environ.get('PASSWORD')
        title = "Message was send succesfully"
        end_message = f"The {name} want to talk \n\n Name: {name} \n Phone Nr: {phone_nr} \n Adress: {contact_email}\n" \
                      f"Want's to talk about: \n {message_tosent}"
        with SMTP("smtp.gmail.com") as smtp:
            smtp.starttls()
            smtp.login(user=email, password=password)
            smtp.sendmail(from_addr=email, to_addrs=email, msg=end_message)

        return render_template('header.html', message=title,image='/assets/img/contact-bg.jpg') + render_template('navigation.html')







if __name__=="__main__":
    app.run(debug=True)