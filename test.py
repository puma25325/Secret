import requests

slug = "will-bitcoin-hit-100k-by-2025"
url = "https://polymarket.com/api/events"

resp = requests.get(url, params={"slug": slug})
resp.raise_for_status()

events = resp.json()

if events:
    event = events[0]
    print(event["title"])
    print(event["id"])
else:
    print("No event found")
