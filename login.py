from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
# 定义一个 GET 请求的接口
@app.route('/get_data', methods=['GET'])
def get_data(param1):
    # 获取请求参数
    param = request.args.get('param1')


    # 处理参数并返回响应
    response = {
        'message': 'This is a GET request response',
        'param': param,
    }
    return jsonify(response)


# 定义一个 POST 请求的接口
@app.route('/post_data', methods=['POST'])
def post_data():
    # 获取请求的 JSON 数据
    data = request.get_json()

    if data is None:
        return jsonify({'error': 'No JSON data provided'}), 400

    # 处理数据并返回响应
    response = {
        'message': 'This is a POST request response',
        'received_data': data
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

