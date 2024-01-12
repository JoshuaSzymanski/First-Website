from portfolio import app
from flask import render_template
import os

picfolder = os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] = picfolder

@app.get('/')
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'gg.jpg')
    return render_template("index.html", user_image = pic1)
