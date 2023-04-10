import os

from dotenv import load_dotenv


class Config:
    tg_api_url: str = f"https://api.telegram.org/bot"
    tg_token: str
    open_ai_token: str
    
    def __init__(self):
        load_dotenv()
        self.tg_token = os.getenv("TG_TOKEN")
        self.open_ai_token = os.getenv("OPEN_AI_KEY")


CONFIG = Config()
