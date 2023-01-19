from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/downloadVideo', methods=['POST',])
def downloadVídeo():
    try:
        url = request.form['url']
        formato = request.form['formato']
        yt = YouTube(url)
        if(formato == 'mp3'):
            audio = yt.streams.filter(only_audio=True)[0]
            title = yt.title + '.mp3'
            audio.download('C:/Users/einst/Downloads', filename=title)
        else:
            video = yt.streams.get_highest_resolution()
            video.download('C:/Users/einst/Downloads')

        return render_template('index.html')
    except Exception as error:
        print(error)
app.run()
