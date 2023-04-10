from time import sleep
from typing import Optional

import requests
from config import CONFIG

url = f'{CONFIG.tg_api_url}{CONFIG.tg_token}'


def get_updates(offset: int = 0) -> Optional[list[dict]]:
    return requests.get(f'{url}/getUpdates', params={'offset': offset}).json()['result']


def run() -> None:
    try:
        with open('last_update.txt', 'r') as file:
            last_update_id = int(file.read())
    except FileNotFoundError as e:
        last_update_id = 0
    while True:
        if updates := get_updates(last_update_id):
            for update in updates:
                update_id = update['update_id']
                if update_id > last_update_id:
                    last_update_id = update_id
                    with open('last_update.txt', 'w') as file:
                        file.write(str(last_update_id))
                        message = update['message']
                        chat_id = message['chat']['id']
                        text = message['text']
                        requests.get(f'{url}/sendMessage', params={'chat_id': chat_id, 'text': text})
        sleep(1)


if __name__ == '__main__':
    # print(requests.get(f"{url}/getUpdates").json())
    run()
