from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    h1_html_tag = soup.find_all('h1')
    h2_html_tag = soup.find_all('h2')
    for info in h1_html_tag:
        print(info.text)

    for info in h2_html_tag:
        print(info.text)