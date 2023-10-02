import requests
import time


def Take_ID():
    id_number = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")

    ID = id_number.json()[:3]
    return ID


ID = Take_ID()


def show_news(id):
    time.sleep(1)
    response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")
    news = response.json()
    return news


for id in ID:
    news = show_news(id)

    title = news["title"]
    link = news.get("url", "リンクがありません")
    print(f"'title':{title}, 'link'{link}")
