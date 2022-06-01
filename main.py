from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

post_list = []

blog_url = "https://api.npoint.io/5798ea950963d77a5d85"
response = requests.get(blog_url)
blog_posts = response.json()

for x in blog_posts:
    post_obj = Post(x["id"], x["title"], x["subtitle"], x["body"])
    post_list.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html", all_posts=blog_posts)

@app.route("/post/<int:id>")
def show_post(id):
    ind = id - 1 #id 1 = post 0, 1 difference
    display_post = post_list[ind]
    return render_template("post.html", post=display_post)


if __name__ == "__main__":
    app.run(debug=True)
