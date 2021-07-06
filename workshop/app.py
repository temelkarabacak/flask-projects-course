from flask import Flask, render_template, redirect, url_for
from flask.helpers import url_for

app = Flask(__name__)

@app.route('/')

def aws():
    return "<h1>Clarusway AWS</h1>"

@app.route('/index')
def index():
    return render_template('index.html', message="Flask dersi")

@app.route('/iletisim')
def iletisim():
    numbers = ["Ankara: 0312 000 00 00", "İstanbul: 0216 000 00 00", "İzmir: 0232 000 00 00"]
    return render_template('iletisim.html', object = numbers)

@app.route('/hata')
def hata():
    return "<h1>Aradığınız sayfa bulunamadı!</h1>"

@app.route('/admin')
def admin():
    return redirect(url_for('hata'))

# @app.route('/<name>')
# def isim(name):
#     isim_format = f"""<!DOCTYPE html>
# <html>
# <head>
#     <title>Greeting Page</title>
# </head>
# <body>
#     <h1>Merhaba, { name }!</h1>
#     <h1>Sayfama hoşgeldin!</h1>
# </body>
# </html>"""
#     return isim_format

@app.route('/<kullanici>')
def uyeol(kullanici):
    return render_template('uyeol.html', kullanici = kullanici)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)