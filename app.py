#library imports
import os

#Flask imports
from flask import Flask, request
from flask.ext.restful import Api, Resource, reqparse

# import neural net and constuct
from neural_net import NeuralNet

class NeuralResource(Resource):

  def get(self,timedate):
    "Get results from a particular neural network"
    
    try:
      result = neuralNet.result(timedate)
    except Exception as error:
      return str(error), 500

    return result

class NeuralResources(Resource):

  def post(self):
    "Run a new neural network"

    data = request.get_json()
    
    try:
      timedate = neuralNet.run(data)
    except Exception as error:
      return str(error), 500

    return timedate

  def get(self):
    "Return a list of neural networks"

    return ['one','two']

neuralNet = NeuralNet()

#Find static path from relative path
currentPath = os.getcwd()
basePath = os.path.split(currentPath)[0]
staticPath = os.path.join(basePath,'SamProject','client')
print(staticPath)

#Define static folder path
app = Flask(__name__, static_folder=staticPath, static_url_path='')
api = Api(app)

@app.route('/')
def index():
  "Index file to run the front end components through angular JS"

  print(os.getcwd(),staticPath)
  return app.send_static_file('index.html')

if __name__ == '__main__':

  # Add api resources
  api.add_resource(NeuralResource, '/results/<string:timedate>')
  api.add_resource(NeuralResources, '/results')

  #Run Server on port 0.0.0.0
  app.run(host='0.0.0.0', port=80, debug=True)