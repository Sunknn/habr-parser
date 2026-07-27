import requests
from bs4 import BeautifulSoup

url = "https://habr.com/ru/articles/top/daily/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Новая строка — ищем все статьи по классу контейнера
articles = soup.find_all("article", class_="tm-articles-list__item")

for i, article in enumerate(articles, 1):
    title_tag = article.find("a", class_="tm-title__link")
    title = title_tag.text.strip() if title_tag else "Без названия"

    views_tag = article.find("span", class_="tm-icon-counter__value")
    views = views_tag.text.strip() if views_tag else "0"

    print(f"{i}. {title} | Просмотры: {views}")