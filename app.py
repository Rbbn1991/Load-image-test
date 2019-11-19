import datetime
import flask
import glob
import pandas as pd
import os
from datetime import date
import cv2
import matplotlib.pyplot as plt

app=flask.Flask("app")

def get_html(page_name):
    html_file=open(page_name+".html")
    content=html_file.read()
    html_file.close()
    return content

@app.route("/")
def index():
    return get_html("index")

@app.route("/uploaded", methods=["POST"])
def capture():
    image_dir=flask.request.args.get("inputFile")
    print(image_dir)
    
    return get_html("uploaded")
