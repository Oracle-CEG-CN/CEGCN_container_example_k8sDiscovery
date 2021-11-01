from flask import Flask
#from pyctuator.pyctuator import Pyctuator
#from pyctuator.auth import BasicAuth

app_name = "Example app 1"
app = Flask(app_name)


@app.route("/")
def hello():
    return "Hello World!"

#auth = BasicAuth(os.getenv("sba-username"), os.getenv("sba-password"))
#auth = BasicAuth("user", "pass")
#Pyctuator(
#    app,
#    app_name,
#    app_url="http://192.168.33.11:5000",
#    pyctuator_endpoint_url="http://192.168.33.11:5000/pyctuator",
#    registration_url="http://192.168.33.78:8888/instances",
   # registration_url="http://192.168.33.78:8093/api/applications",
#    registration_auth=auth
#)

app.run(debug=False, host="0.0.0.0", port=5000)
