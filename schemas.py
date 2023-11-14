from flask_marshmallow import Marshmallow


ma = Marshmallow()


class PostSchema(ma.Schema):
    class Meta:
        fields = ("title", "author", "description")


post_schema = PostSchema()


posts_schema = PostSchema(many=True)
