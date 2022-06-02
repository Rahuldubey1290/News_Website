from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    api_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=ef413c606a7a4fabbd4522f8a0dd00bb"
    r = requests.get(api_url).json()

    act_dict = {
        'articles': r['articles']
    }
    return render_template('/index.html', act_dict=act_dict)


if __name__ == '__main__':
    app.run(debug=True)
