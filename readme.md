# Multi-Platform Weather Alert

This project is a Multi-Platform Weather Alert bot that fetches weather data from the CWA Open Data API and sends notifications to Slack, Telegram, and Line Notify channels. The bot is configurable, allowing you to enable or disable notifications for each platform.

## Features

- Fetches weather alerts from the CWA Open Data API.
- Sends notifications to Slack, Telegram, discord, and Line Notify channels.
- Easily configurable to enable or disable notifications for each platform.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your local machine.
- Required Python packages: `requests`, `slack_sdk`.
- API tokens and channel IDs for Slack, Telegram, and Line Notify.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tbdavid2019/multi-platform-weather-alert.git
    cd multi-platform-weather-alert
    ```

2. Install the required Python packages:

    ```bash
    pip install requests slack_sdk
    ```

## Configuration

1. Open the `Weather_Alert_Bot.py` file in a text editor.
2. Replace the following placeholders with your actual tokens and IDs:

    ```python
    slack_token = 'your Slack OAuth Token'
    channel_name = '#your-channel'
    telegram_bot_token = 'your Telegram Bot API Token'
    telegram_chat_id = 'your Telegram Chat ID'
    line_notify_token = 'your Line Notify Token'
    discord_webhook_url = 'your discord webhook'
    ```

3. Set the `enable_slack_bot`, `enable_telegram_bot`, and `enable_line_notify` variables to `True` or `False` to enable or disable notifications for each platform:

    ```python
    enable_slack_bot = True
    enable_telegram_bot = True
    enable_line_notify = True
    enable_discord_notify = True
    ```

## Usage

1. Run the bot using the following command:

    ```bash
    python3 Weather_Alert_Bot.py
    ```

2. The bot will fetch weather alerts for Kaohsiung City and send notifications to the enabled platforms.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## Contact

If you have any questions, feel free to reach out:

- GitHub: [tbdavid2019](https://github.com/tbdavid2019)

---

# 多平台天氣警報

本專案是一個多平台天氣警報機器人，它從 CWA 開放數據 API 獲取天氣數據，並將通知發送到 Slack、Telegram 和 Line Notify 頻道。此機器人支持配置，您可以選擇啟用或禁用每個平台的通知功能。

## 功能

- 從 CWA 開放數據 API 獲取天氣警報。
- 將通知發送到 Slack、Telegram 和 Line Notify 頻道。
- 可以輕鬆配置以啟用或禁用每個平台的通知。

## 先決條件

在開始之前，請確保您已滿足以下要求：

- 在您的本地機器上安裝 Python 3.x。
- 所需的 Python 套件：`requests`、`slack_sdk`。
- Slack、Telegram 和 Line Notify 的 API Token 及頻道 ID。

## 安裝

1. 克隆此儲存庫：

    ```bash
    git clone https://github.com/tbdavid2019/multi-platform-weather-alert.git
    cd multi-platform-weather-alert
    ```

2. 安裝所需的 Python 套件：

    ```bash
    pip install requests slack_sdk
    ```

## 配置

1. 使用文本編輯器打開 `Weather_Alert_Bot.py` 文件。
2. 將以下佔位符替換為您的實際 Token 和 ID：

    ```python
    slack_token = '您的 Slack OAuth Token'
    channel_name = '#您的頻道'
    telegram_bot_token = '您的 Telegram Bot API Token'
    telegram_chat_id = '您的 Telegram 頻道 ID'
    line_notify_token = '您的 Line Notify Token'
    discord_webhook_url = '你的 discord webhook'
    ```

3. 設置 `enable_slack_bot`、`enable_telegram_bot` 和 `enable_line_notify` 變量為 `True` 或 `False` 以啟用或禁用每個平台的通知：

    ```python
    enable_slack_bot = True
    enable_telegram_bot = True
    enable_line_notify = True
    enable_discord_notify = True
    ```

## 使用方法

1. 使用以下命令運行機器人：

    ```bash
    python3 Weather_Alert_Bot.py
    ```

2. 機器人將獲取高雄市的天氣警報，並將通知發送到啟用的平臺。

## 許可證

此專案已獲 MIT 許可證。請參閱 [LICENSE](LICENSE) 文件了解更多詳情。

## 貢獻

歡迎貢獻！請提出 issue 或提交 pull request。

## 聯繫方式

如有任何問題，請隨時聯繫：

- GitHub: [tbdavid2019](https://github.com/tbdavid2019)
