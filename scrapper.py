import requests
import os

TOKEN = os.getenv("8891290679:AAES0IK7wGrTPFMwqyc2xaSlwnVJH4wG74w")
CHAT_ID = os.getenv("6414439003")

def send_telegram(title, url):
    message = f"""📢 New Job Alert

{title}

Apply Here:
{url}
"""

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=30
    )
