from flask import *
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/", prefix="static/", index_file="index.html", autorefresh=True)
@app.route('/', methods=['GET'])
def hello():
  return make_response("Add /static/ to go to our HW2 visualizations.")



if __name__ == "__main__":
  app.run(threaded=True, port=5000)