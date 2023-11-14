from flask import Flask, request, jsonify

from db import db, Post
from schemas import ma, post_schema, posts_schema


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"


db.init_app(app)


ma.init_app(app)


with app.app_context():
    db.create_all()


@app.route('/', methods=["GET"])
def index():
    return jsonify(dict(message="I'm alive !!"))


@app.route('/posts/', methods=["GET"])
def get_posts():
    post = Post.query.all()
    return posts_schema.jsonify(post)


@app.route('/posts/', methods=["POST"])
def create_post():
    post = Post(title=request.json.get('title'),
                description=request.json.get('description'),
                author=request.json.get('author'))
    db.session.add(post)
    db.session.commit()
    return post_schema.jsonify(post), 201


@app.route('/posts/<int:id>/', methods=["GET"])
def get_post(id):
    post = Post.query.get_or_404(id)
    return post_schema.jsonify(post)


@app.route('/posts/<int:id>/', methods=["PUT"])
def edit_post(id):
    post = Post.query.get_or_404(id)
    post.title = request.json.get('title'),
    post.description = request.json.get('description'),
    post.author = request.json.get('author')
    db.session.commit()
    return post_schema.jsonify(post), 200


@app.route('/posts/<int:id>/', methods=["DELETE"])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.commit(post)
    db.session.commit()
    return post_schema.jsonify(post), 200
