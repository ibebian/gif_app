import json
import requests
from flask import Flask, render_template, request

GIF_ENDPT = "http://api.giphy.com/v1/gifs/search"

QS = {
    'q': None,
    'api_key': 'dc6zaTOxFJmzC',
    'limit': 1,
    'offset': 0
}

app = Flask(__name__)

@app.route('/giphy')
def search_page():
    print "#################### page rendered"
    return render_template('gif.html')


@app.route('/giphy/search')
def show_gif():
    print "################ this function hit"

    QS['q'] = request.args.get('kw')

    response = requests.get(GIF_ENDPT, params=QS)

    payload = json.loads(response.content)
    url = payload['data'][0]['images']['downsized_large']['url']

    return render_template('gif_result.html', url=url)


if __name__ == "__main__":
    app.debug = True
    app.run()