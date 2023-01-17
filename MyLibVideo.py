from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/downloadVideo', methods=['POST',])
def downloadVídeo():
    url = request.form['url']
    yt = YouTube(url)
    for stream in yt.streams:
        print(stream)
    video = yt.streams.get_highest_resolution()
    video.download('C:/Users/einst/Downloads')

app.run()
