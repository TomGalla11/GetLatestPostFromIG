import requests
from flask import Flask, request, jsonify

@app.route('/api/get_posts', methods=["POST"])
def url():
    url = request.form.get('msg')
    text_file = open("latest_post.txt", "wt")
    write_file = text_file.write(url)
    text_file.close()

    return jsonify({'result': url, 'msg': 'success'})
def get_latest_posts():
  print('Getting')
  