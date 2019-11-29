import json
import os

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/')
def top():
    print('/ start')

    # レスポンスデータの入れ物
    res = dict()

    res['request'] = dict()
    res['request']['url'] = request.url
    res['request']['method'] = request.method

    # リクエストヘッダーからX-Amzn-Trace-Idを取得
    request_headers = dict()
    for header in request.headers:
        request_headers[header[0]] = header[1]
        if header[0].lower() == 'X-Amzn-Trace-Id'.lower():
            trace_id = header[1]
    res['request']['headers'] = request_headers

    # 環境変数から取得
    res['hostname'] = os.uname()[1]
    res['serviceName'] = os.getenv('SERVICE_NAME', 'SimpleService')
    res['backends'] = []
    backend_urls = []
    backend_urls_string = os.getenv('BACKEND_URLS')
    if backend_urls_string:
        backend_urls = backend_urls_string.split(',')

    # バックエンドへリクエストを送る
    for url in backend_urls:
        print(url)
        headers = dict()
        if trace_id:
            headers = {'X-Amzn-Trace-Id': trace_id}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        try:
            content = r.json()
        except json.JSONDecodeError as e:
            content = r.text
            # 100文字のみ
            content = content[:100]
        res['backends'].append({'url': url, 'statusCode': r.status_code, 'content': content})
    print('/ end')
    print(res)
    return jsonify(res)


@app.route('/health')
def health():
    print('/health start')
    print('/health end')
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
