from flask import Flask, render_template, request, jsonify, redirect, url_for
import tensorflow as tf
import keras
import numpy as np
import os
from PIL import Image
from keras.preprocessing import image

app = Flask(__name__)

# Folder where the photos will be uploaded
UPLOAD_FOLDER = 'image_store'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model
human_model = keras.models.load_model('static/models/human_classifier_model.h5')
object_model = keras.models.load_model('static/models/ai_model.h5')

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the home page
@app.route('/services')
def services():
    return render_template('service.html')

# Route for the service page
@app.route('/why')
def why():
    return render_template('why.html')

# Route for the team page
@app.route('/team')
def team():
    return render_template('team.html')

# Route for the human model page
@app.route('/human')
def human():
    return render_template('human_model_page.html', result=None)

# Route for the object model page
@app.route('/object')
def object():
    return render_template('object_model_page.html', result=None)

# Logic which processes an uploaded image and returns a result to the route below
@app.route('/upload_human', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        IMAGE_SIZE_HUMAN = (128, 128)

        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Create an Image Object from an Image
        img = Image.open(filename)

        # Make the uploaded image have the desired size
        resized_im = img.resize(IMAGE_SIZE_HUMAN)

        # Convert the image to a NumPy array
        img_array = image.img_to_array(resized_im)

        # Expand the dimensions to match the input shape expected by the model
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction using the model
        prediction = human_model.predict(img_array)
        print(prediction[0][0])
        result = "AI-generated" if prediction[0][0] < 0.5 else "Real"

        response = render_template('human_model_page.html', result=result)
        
        return response

@app.route('/upload_object', methods=['POST'])
def upload_object_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        IMAGE_SIZE_OBJECT = (256, 256)

        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Create an Image Object from an Image
        img = Image.open(filename)

        # Make the uploaded image have the desired size
        resized_im = img.resize(IMAGE_SIZE_OBJECT)

        # Convert the image to a NumPy array
        img_array = image.img_to_array(resized_im)

        # Expand the dimensions to match the input shape expected by the model
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction using the model
        prediction = object_model.predict(img_array)
        result = "AI-generated" if prediction[0][0] < 0.5 else "Real"

        response = render_template('object_model_page.html', result=result)
        return response

if __name__ == '__main__':
    app.run()
