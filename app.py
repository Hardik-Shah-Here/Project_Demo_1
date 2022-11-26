from pydoc import render_doc
import os
from flask import Flask, render_template, redirect, request, flash, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def sample():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        video = request.files['video']
        if video.filename == '':
            flash('No video selected for uploading')
            return render_template('sample.html', t=title, d=desc, v=video)
        else:
            filename = secure_filename(video.filename)
            video.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('Uploaded Video Filename : ' + filename)
            flash('Video successfully uploaded and displayed below')
            return render_template('sample.html', t=title, d=desc, filename=filename)
    #return render_template('sample.html', t=title, d=desc, v=video)


#@app.route('/products')
#def products():
#    return 'This is a Products Page!'

if __name__ == "__main__":
    app.run(debug=True)