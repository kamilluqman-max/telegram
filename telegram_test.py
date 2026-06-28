import requests

TOKEN = "8891290679:AAES0IK7wGrTPFMwqyc2xaSlwnVJH4wG74w"
CHAT_ID = "6414439003"

message = "📢 Test message from my job bot!"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

print(response.text)
