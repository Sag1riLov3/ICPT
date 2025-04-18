import requests
import json


def main():
    api_key = 'AkzzCCMAYUvCY0uSNvpiMsjs'
    secret_key = 'O1FIbOi0OYLDMKlcBDAw9JcXKNmasrU7'
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'
    url = f"{token_url}?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    try:
        response_data = response.json()
        if 'access_token' in response_data:
            access_token = ''.join(response_data['access_token'])
            print(f"access_token: {access_token}")
        else:
            print("响应中未包含 'access_token' 字段。")
    except json.JSONDecodeError:
        print("无法将响应内容解析为JSON格式。")

    print(response.text)


if __name__ == '__main__':
    main()


