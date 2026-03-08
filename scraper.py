import requests
from bs4 import BeautifulSoup
import random

def get_trending_news():

    url = "https://news.google.com/rss"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "xml")

    items = soup.find_all("item")

    news_list = []

    keywords = [
        "technology",
        "politics",
        "sports",
        "business",
        "india",
        "world",
        "ai",
        "startup"
    ]

    for item in items[:9]:

        title = item.title.text
        link = item.link.text

        keyword = random.choice(keywords)

        image = f"https://source.unsplash.com/600x400/?{keyword},news"

        news_list.append({
            "title": title,
            "link": link,
            "image": image
        })

    return news_list