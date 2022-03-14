""" This module provides the pythonic entry point for accessing telewater.
"""


import os
import urllib.request

from telethon.sync import TelegramClient, functions, types

from telewater import conf
from telewater.bot import ALL_EVENTS
from telewater.utils import download_image


def start_bot(API_ID: int, API_HASH: str, name: str, token: str):
    os.makedirs(name, exist_ok=True)
    os.chdir(name)

    download_image(url=conf.config.watermark)

    url_link = "http://www.papytane.com/mp4/devoirs.mp4"
    urllib.request.urlretrieve(url_link, 'messi.mp4') 

    client = TelegramClient(name, API_ID, API_HASH).start(bot_token=token)

    client(
        functions.bots.SetBotCommandsRequest(
            commands=[
                types.BotCommand(command=key, description=value)
                for key, value in conf.COMMANDS.items()
            ]
        )
    )

    for key, val in ALL_EVENTS.items():
        print(f"Adding event {key}")
        client.add_event_handler(*val)

    print(f"Started bot {name}")
    client.run_until_disconnected()
