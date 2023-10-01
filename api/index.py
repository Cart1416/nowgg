import importlib
import pip

def install_package(package_name, install_command):
    try:
        importlib.import_module(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        pip.main(['install', install_command])
        print(f"{package_name} has been installed successfully.")
install_package("requests", "requests")
install_package("flask", "flask")
from flask import Flask,request,redirect,Response
import requests
app = Flask(__name__)
SITE_NAME = "https://now.gg"

@app.route("/",methods=['GET','POST'])
def index():
    global SITE_NAME
    if request.method=="GET":
        resp = requests.get(f"{SITE_NAME}")
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=="POST":
        resp = requests.post(f"{SITE_NAME}",data=request.form)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response

@app.route("/<path:path>",methods=["GET","POST"])
def proxy(path):
    global SITE_NAME
    if request.method=="GET":
        resp = requests.get(f"{SITE_NAME}{path}")
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=="POST":
        resp = requests.post(f"{SITE_NAME}{path}",data=request.form)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337)
