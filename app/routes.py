# import app variable instance in order to run application
# also import necessary flask method
from app import app, db
from flask import render_template, url_for, redirect, flash, json, jsonify, request, session
from app.forms import ImageForm
from app.models import PlaceHolderImage
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from werkzeug.utils import secure_filename
import requests
import base64
import os

# create route for index page, render index.html file
@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    form = ImageForm()
    image = PlaceHolderImage.query.get(1)

    image.image = image.image.decode("utf-8")

    if form.validate_on_submit():

        try:
            data = form.image.data
            filename = secure_filename(data.filename)

            path = os.path.join(
                app.instance_path, 'uploads', filename
            )

            data.save(path)

            str = ""
            with open(path, "rb") as imageFile:
                str = base64.b64encode(imageFile.read())

            if(image):
                image.image = str
            else:
                image = PlaceHolderImage(
                    image = str
                )

            db.session.add(image)
            db.session.commit()

            os.remove(path)

            flash("Image uploaded")
            return redirect(url_for('index'))

        except:
            flash("Sorry your submission did not go through. Try again.")
            return redirect(url_for('index'))

    return render_template('index.html', image=image, form=form)

@app.route('/api/image', methods=['GET'])
def getImage():
    image = PlaceHolderImage.query.get(1)
    image.image = image.image.decode("utf-8")

    return jsonify({"image":image.image})

@app.route('/api/post', methods=['POST', 'GET'])
def setImage():
    image = PlaceHolderImage.query.get(1)

    image.image = image.image.decode("utf-8")

    target=os.path.join(app.instance_path, 'uploads')
    if not os.path.isdir(target):
        os.mkdir(target)

    filename = request.form['filename']
    file = request.files['file']

    filename = secure_filename(filename)

    str = base64.b64encode(file.read())

    if(image):
        image.image = str
    else:
        image = PlaceHolderImage(
            image = str
        )

    db.session.add(image)
    db.session.commit()

    return jsonify({ "image" : image.image.decode("utf-8") })

@app.route('/api/upload', methods=['POST'])
def fileUpload():

    target=os.path.join(app.instance_path, 'uploads')
    if not os.path.isdir(target):
        os.mkdir(target)

    filename = request.form['filename']
    file = request.files['file']

    filename = secure_filename(filename)

    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    response="Whatever you wish too return"
    return response
