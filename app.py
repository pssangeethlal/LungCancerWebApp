from flask import Flask, render_template, request, url_for, redirect,flash
# from keras.models import load_model
# from keras.preprocessing import image
# import tensorflow as tf
# import numpy as np
from werkzeug.utils import secure_filename
#model = load_model('best_model_1.hdf5')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
app = Flask(__name__)
app.secret_key = "mahnofman"
@app.route('/')
def home():
    return render_template('index.html')
'''
@app.route('/', methods=["POST","GET"])
def predict():
    if request.method == 'POST':
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect('prediction')
        file = request.files['imagefile']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect('prediction')
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename)
            img_path = "./static/images/"+file.filename
            file.save(img_path)
            test_image = image.load_img(img_path,target_size = (227,227))
            test_image = image.img_to_array(test_image)
            test_image = np.array([test_image], dtype=np.float16) / 255.0
            prediction = model.predict(test_image)
            categories = ["Cancerous","Non cancerous"]
            string = categories[np.argmax(prediction)]
            print("predvalue...........---------",np.max(prediction))
            return render_template('index.html',scrollToAnchor="detection-sec", file=string, filename=filename)
        else:
                flash('Allowed image types are -> png, jpg, jpeg')
                return redirect('prediction')
   ''' 
@app.route('/prediction')
def pred_page():
    return render_template('index.html',scrollToAnchor="detection-sec")
@app.route('/load_imag/<filename>')
def load_imag(filename):
    
    return redirect(url_for('static', filename='images/' + filename), code=301)

if __name__ == "__main__":
    app.run(debug=True)