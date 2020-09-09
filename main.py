import requests
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/get_posts', methods=["POST"])
def url():
    url = request.form.get('msg')
    text_file = open("latest_post.txt", "wt")
    write_file = text_file.write(url)
    text_file.close()

    return jsonify({'result': url, 'msg': 'success'})
def get_latest_posts():
  print('Getting')
  resp = requests.get('https://www.instagram.com/dieweltentdecker/?__a=1')
  data = resp.text
  print(data)
  
if __name__ == "__main__":
    # the server will start
    #app.run()
    get_latest_posts()