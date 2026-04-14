from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

import gdown
import os

url = "https://drive.google.com/uc?export=download&id=1A88uwlcvt71kjkOxPNIbQ_BVJzm6ktU7"
output = "Brone_model.h5"

if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

model = tf.keras.models.load_model(output)

def preprocess(image):
    image = image.resize((224, 224))  # change if needed
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_path = None

    if request.method == "POST":
        file = request.files["file"]
        if file:
            path = os.path.join("static", file.filename)
            file.save(path)

            img = Image.open(path)
            img = preprocess(img)

            pred = model.predict(img)[0][0]

            if pred > 0.5:
                result = "Fracture Detected"
            else:
                result = "Normal"

            image_path = path

    return render_template("index.html", result=result, image_path=image_path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
