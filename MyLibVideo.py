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
        yt = YouTube(url)
        # for stream in yt.streams:
        #     print(stream)
        video = yt.streams.get_highest_resolution()
        video.download('C:/Users/einst/Downloads')
        audio = yt.streams.filter(only_audio=True)[0]
        title = yt.title + '.mp3'
        audio.download('C:/Users/einst/Downloads', filename=title)
        if(video.download('C:/Users/einst/Downloads')):
            success = 'Sucesso ao baixar vídeo'
        else:
            success = 'Falha ao baixar vídeo'
        return render_template('index.html')
    except Exception as error:
        print(error)
app.run()
