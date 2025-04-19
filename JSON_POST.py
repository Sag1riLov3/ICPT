import base64
import urllib
import urllib.parse
import requests
import json

API_KEY = "AkzzCCMAYUvCY0uSNvpiMsjs"
SECRET_KEY = "O1FIbOi0OYLDMKlcBDAw9JcXKNmasrU7"


def main():
    url = "https://vop.baidu.com/server_api"
    path = r"C:\Users\22343\Desktop\ICPT\16k.wav"
    # speech 可以通过 get_file_content_as_base64("C:\fakepath\16k.wav",False) 方法获取
    payload = json.dumps({
        "format": "pcm",
        "rate": 16000,
        "channel": 1,
        "cuid": "kKtMmvllbTBTbcGIQqpQsaS6G1KdAVhC",
        "speech": get_file_content_as_base64(path,urlencoded=False),
        "len": 129998,
        "token": get_access_token()
    }, ensure_ascii=False)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload.encode("utf-8"))
    try:
        response_data = response.json()
        if 'result' in response_data:
            result = ''.join(response_data['result'])
            print(f"识别结果字符串: {result}")
        else:
            print("响应中未包含 'result' 字段。")
    except json.JSONDecodeError:
        print("无法将响应内容解析为JSON格式。")

    if result == "北京科技馆。" :
        print("100")

    print(response.text)

def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件Base64编码
    :param path: 文件路径
    :param urlencoded: 是否对Base64编码结果进行URL编码
    :return: Base64编码结果
    """
    with open(path, 'rb') as f:
        content = base64.b64encode(f.read()).decode('utf-8')
    if urlencoded:
        return urllib.parse.quote_plus(content)
    return content

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
