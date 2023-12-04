import requests
from bs4 import BeautifulSoup

# url = "https://www.wizardingworld.com/discover/books"

# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
# }

# req = requests.get(url, headers=headers)

# src = req.text

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# находим все на звания книг и ссылки на них
all_books_links = soup.find_all(class_="ProductCard_link__z-ZoA")

for link in all_books_links:
    link_text = link.text  # название книги
    link_href = link.get("href")  # ccылка на книгу

    print(f"{link_text.strip()}: {link_href}")
