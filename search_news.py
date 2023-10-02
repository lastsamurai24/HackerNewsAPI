import requests
import time
id_number = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")

ID = id_number.json()[:5]

for id in ID:
    time.sleep(1)
    response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")
    news = response.json()
   
    title = news['title']
    link = news['url']
    print(f"'title':{title},'link'{link}")
