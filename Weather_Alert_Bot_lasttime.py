import requests
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack, Telegram, 和 Line Notify 配置
slack_token = '你的 Slack OAuth Token'
channel_name = '#your-channel'  # Slack的頻道
telegram_bot_token = '你的 Telegram Bot API Token'
telegram_chat_id = '你的頻道 ID' # Telegram的頻道
line_notify_token = '你的 Line Notify Token'
discord_webhook_url = '你的 discord webhook'


# 啟用/停用機器人選項
enable_slack_bot = True
enable_telegram_bot = True
enable_line_notify = True
enable_discord_notify = True


# CWA API URL
cwa_api_url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/W-C0033-001'
params = {
    'Authorization': '填入你的 CWA的token',  #要去這裏申請 https://opendata.cwa.gov.tw/about/application/general
    'format': 'JSON',
    'locationName': '高雄市',   #可以改其他縣市 台北市 台中市
    'phenomena': '大雨,豪雨,大豪雨,超大豪雨,陸上強風'
}

# 存儲上一次的警報信息的文件路徑
last_hazard_file = 'last_hazard_info.json'

# 初始化 last_hazard_info 變數
last_hazard_info = None

def load_last_hazard_info():
    try:
        with open(last_hazard_file, 'r') as file:
            content = file.read().strip()
            if content:
                return json.loads(content)
            else:
                return None
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print(f"Warning: {last_hazard_file} is not a valid JSON file.")
        return None

def save_last_hazard_info(hazard_info):
    with open(last_hazard_file, 'w') as file:
        json.dump(hazard_info, file)

def fetch_weather_alert():
    response = requests.get(cwa_api_url, params=params)
    return response.json()

def send_notifications(weather_info):
    # 發送到 Slack
    if enable_slack_bot:
        client = WebClient(token=slack_token)
        try:
            response = client.chat_postMessage(
                channel=channel_name,
                text=weather_info
            )
        except SlackApiError as e:
            print(f"Error sending message to Slack: {e.response['error']}")

    # 發送到 Telegram
    if enable_telegram_bot:
        telegram_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
        telegram_params = {
            'chat_id': telegram_chat_id,
            'text': weather_info
        }
        response = requests.get(telegram_url, params=telegram_params)
        if response.status_code != 200:
            print(f"Error sending message to Telegram: {response.status_code}, {response.text}")

    # 發送到 Line Notify
    if enable_line_notify:
        line_notify_url = 'https://notify-api.line.me/api/notify'
        line_notify_headers = {
            'Authorization': f'Bearer {line_notify_token}'
        }
        line_notify_data = {
            'message': weather_info
        }
        response = requests.post(line_notify_url, headers=line_notify_headers, data=line_notify_data)
        if response.status_code != 200:
            print(f"Error sending message to Line Notify: {response.status_code}, {response.text}")

    # 發送到 Discord
    if enable_discord_notify:
        discord_data = {
            'content': weather_info
        }
        response = requests.post(discord_webhook_url, json=discord_data)
        if response.status_code != 204:
            print(f"Error sending message to Discord: {response.status_code}, {response.text}")

# 主程序
data = fetch_weather_alert()

try:
    hazards = data['records']['location'][0]['hazardConditions']['hazards']
    if hazards:
        hazard_info = hazards[0]
        language = hazard_info['info']['language']
        phenomena = hazard_info['info']['phenomena']
        significance = hazard_info['info']['significance']
        start_time = hazard_info['validTime']['startTime']
        end_time = hazard_info['validTime']['endTime']
        
        weather_info = (f"高雄市的天氣狀況\n"
                        f"現象：{phenomena}\n"
                        f"意義：{significance}\n"
                        f"開始時間：{start_time}\n"
                        f"結束時間：{end_time}")

        last_hazard_info = load_last_hazard_info()

        if weather_info != last_hazard_info:
            send_notifications(weather_info)
            save_last_hazard_info(weather_info)

    # 如果這次訊息無警報，且上次有警報，則清空檔案內容
    elif last_hazard_info:
        save_last_hazard_info(None)

except KeyError as e:
    print(f"無法取得天氣資訊，出現 KeyError: {e}")
