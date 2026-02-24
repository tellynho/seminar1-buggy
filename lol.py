from flask import Flask, request
from tld import get_tld
from dns import resolve
import requests
app = Flask(__name__)

BLACKLIST = ['127.0.0.1', '0.0.0.0']

@app.route('/')
def vuln():
    if 'url' in request.args:
        try:
            url = request.args['url']
            info = get_tld(url, as_object=True)
            if resolve(info.parsed_url[1]) not in BLACKLIST:
                return requests.get(url).text
            else:
                return 'blacklisted'
        except:
            return 'bad url'
    else:
        return 'supply url to GET `url`'