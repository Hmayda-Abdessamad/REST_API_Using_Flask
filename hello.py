from flask import Flask
from flask_restplus import Api, Resource

app = Flask("My Hello World Application")
api = Api(app)

# Define a namespace for your API
ns = api.namespace('hello', description='Hello World Operations')

@ns.route("/")
class HelloWorld(Resource):
    def get(self):
        """Returns a Hello World message"""
        return "Hello World!"

# Generate the Swagger JSON file
@api.documentation
def custom_ui():
    return {
        'swagger': '2.0',
        'info': {
            'title': 'Hello World API',
            'description': 'Sample API for Hello World',
            'version': '1.0',
        },
    }

if __name__ == "__main__":
    app.run(debug=True)
