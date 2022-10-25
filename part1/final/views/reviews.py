from flask import request
from flask_restx import Resource, Namespace

from models import Review
from setup_db import db

review_ns = Namespace("reviews")


@review_ns.route('/')
class RewiewView(Resource):
    def get(self):
        review = Review.query.all()
        res = []
        for book in review:
            sm_d = book.__dict__
            del sm_d['_sa_instance_state']
            res.append(book.__dict__)
        return res, 200

    def post(self):
        data = request.json
        new_book = Review(**data)

        db.session.add(new_book)
        db.session.commit()
        return "", 201


@review_ns.route('/<int:rid>')
class RewiewView(Resource):
    def get(self, rid):
        book = Review.query.get(rid)
        result = book.__dict__
        del result['_sa_instance_state']
        return result, 200

    def put(self, rid):
        review = Review.query.get(rid)
        req_json = request.json
        review.user = req_json.get("user")
        review.rating = req_json.get("rating")
        review.book_id = req_json.get("book_id")
        db.session.add(review)
        db.session.commit()
        return "", 204

    def delete(self, rid):
        review = Review.query.get(rid)

        db.session.delete(review)
        db.session.commit()
        return "", 204