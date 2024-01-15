from Flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

videos = {}

class Video(Resource):
  def get(self, video_id):
    return videos[video_id]
  
  def post(self):
    return {'data': 'Posted'}

api.add_resource(HelloWorld, '/helloworld/<string:name>')

if __name__ == '__main__':
  app.run(debug=True)