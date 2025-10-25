import requests
from bs4 import BeautifulSoup
import csv

# NDL Search APIから書籍情報を取得（タイトル・出版社・出版年のみ）
def get_ndl_books_api(person_name, max_pages=2):
    base_url = "https://iss.ndl.go.jp/api/opensearch"
    results = []

    for page in range(1, max_pages + 1):
        params = {
            "any": person_name,
            "cnt": 20,
            "page": page
        }
        res = requests.get(base_url, params=params)
        soup = BeautifulSoup(res.content, "xml")

        items = soup.find_all("item")
        for item in items:
            title = item.find("title").text if item.find("title") else "不明"
            publisher = item.find("dc:publisher").text if item.find("dc:publisher") else "不明"
            date = item.find("dc:date").text if item.find("dc:date") else "不明"

            results.append({
                "タイトル": title,
                "出版社": publisher,
                "出版年": date
            })

    return results

# CSVファイルに保存
def save_books_to_csv(books, filename="books.csv"):
    fieldnames = ["タイトル", "出版社", "出版年"]
    with open(filename, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            writer.writerow(book)

# 実行例
if __name__ == "__main__":
    person_name = "久生十蘭"  # 任意の人物名に変更可能
    books = get_ndl_books_api(person_name, max_pages=3)
    save_books_to_csv(books)
    print(f"{len(books)} 件の書籍情報を books.csv に保存しました。")