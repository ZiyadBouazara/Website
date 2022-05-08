from flask import Blueprint

views = Blueprint('views', __name__)  # This is how we define a blueprint


@views.route('/')
def home():
    return "<h1>Test</h1>"
