import requests
from bs4 import BeautifulSoup
url = "https://realpython.com/python-sql-libraries/"
page = requests.get(url)

print(page)
print(page.status_code)

if page.status_code == 200:
    print("200 status code received")
    content = page.content
    root = BeautifulSoup(content, 'lxml')
    # print(root.prettify())

    children = list(root.children)
    print(children)
