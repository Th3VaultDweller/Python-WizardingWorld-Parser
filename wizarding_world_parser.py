import json

import requests
from bs4 import BeautifulSoup

# url = "https://www.wizardingworld.com/discover/books"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

# req = requests.get(url, headers=headers)

# src = req.text

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# # находим все на звания книг и ссылки на них
# all_books_links = soup.find_all(class_="ProductCard_link__z-ZoA")

# all_books_links_dict = {}
# for i, link in enumerate(all_books_links):
#     link_text = link.text  # название книги
#     link_href = link.get("href")  # ccылка на книгу
#     print(i)  # нумерация книг начинается с нуля
#     print(f"{link_text.strip()}: {link_href}")

#     # ключ - название книги, значение - ссылка на книгу
#     all_books_links_dict[link_text.strip()] = link_href

# # сохраняем полученные названия и ссылки в словарь.json
# # indent=4 - необходимый отступ
# # ensure_ascii=False не экранирует символы и помогает в работе с кириллицей
# with open("all_books_links_dict.json", "w") as file:
#     json.dump(all_books_links_dict, file, indent=4, ensure_ascii=False)

with open("all_books_links_dict.json") as file:
    all_books = json.load(file)

iteration_count = int(len(all_books)) - 1
count = 0
for book_name, book_href in all_books.items():
    if count == 0:
        rep = [",", ", ", "-", "'", ":", " "]
        for item in rep:
            if item in book_name:
                book_name = book_name.replace(item, "_")

        req = requests.get(url=book_href, headers=headers)
        src = req.text

        with open(f"data/{count}_{book_name}.html", "w") as file:
            file.write(src)

        # with open(f"data/{count}_{book_name}.html") as file:
        #     src = file.read()

        # soup = BeautifulSoup(src, "lxml")

        # # собираем аннотации книг
        # book_annotation = soup.find(
        #     "div", class_="ArticleGambit_default__3mOC- ArticleGambit_left__qElyK"
        # )
        # print(book_annotation)

        count += 1

        print(f"# Итерация {count}. {book_name} записан...")

        iteration_count = iteration_count - 1

        if iteration_count == 0:
            print(f"Работа завершена.")
            break

        print(f"Осталось итераций: {iteration_count}")
