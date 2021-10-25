import csv
import requests
import json

from unicodedata import normalize

LIMIT = 50
URL = f'https://api.strelka.institute/api/ru/magazine/feed?format=news&limit={LIMIT}'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
}
HOST = 'https://strelkamag.com/news/'
TAGS = ['Москва', 'Барселона', 'Ижевск']


def get_html(url: str) -> object:
    r = requests.get(url, headers=HEADERS)
    return r


def get_content(content: dict):
    result = []

    for item in content['feed']:
        for tag in item['tags']:
            if tag['name'] in TAGS:
                result.append(
                    {
                        'id': item['id'],
                        'title': normalize(
                            'NFKC',
                            item['title']
                        ),
                        'date': item['publishedAt'][:10],
                        'url': HOST + item['slug']
                    }
                )
    return result


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['id', 'Заголовок', 'Дата', 'Ссылка'])
        for item in items:
            writer.writerow([item['id'], item['title'], item['date'], item['url']])


if __name__ == '__main__':
    html = get_html(URL)
    if html.status_code == 200:
        news = get_content(json.loads(html.text))
    else:
        print('Error')
    save_file(news, 'news.csv')
