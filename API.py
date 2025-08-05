import os
from dotenv import load_dotenv

load_dotenv()

API_KEYS = {
    "newsKey": os.getenv("NEWS_API_KEY")
}
