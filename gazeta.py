import urllib.request
import ssl
import json
import argparse
import codecs
import re

def print_menu(menu: dict):
    print('===========================')
    for option in menu.values():
        print(option)
    while True:
        result = input('Podaj opcje:')
        for key in menu.keys():
            if result == str(key):
                print(f'Wybrałeś opcję {key}')
                print('===========================')
                return key
        else:
            print('Podales zla wartosc!')


def get_from_url(url):
    req = urllib.request.Request(url=url, method='GET')
    with urllib.request.urlopen(req) as f:
        if f.status == 200:
            content = f.read()
            content = codecs.decode(content, encoding='utf-8', errors='ignore')
        else:
            return False
    return content

if __name__ == '__main__':
    content = str(get_from_url("https://www.gazeta.pl/")).replace('\r','').replace('\n', '')

    news_blok_pattern = r'<div class=\"timeline__title\">Najnowsze</div><div class="timeline__list">\s+<div class="timeline__box">(.*)</div>\s+</div>'
    new_block = re.search(news_blok_pattern, content)
    links = new_block.group(1)

    new_pattern = r'<a class=\"timeline__link\" title=\"([^\"]+)\" id=\"LinkArea:BoxOpLink\" href=\"([^\"]+\.html)[^\"]+\">\s+<div class="timeline__linkTime">(\d{1,2}:\d{1,2})</div>'
    news = re.findall(new_pattern, links)


    menu = {}
    link = {}
    c = 0
    MAX_ITEMS =5
    for item in news:
        if c == MAX_ITEMS:
            menu[c +1] = f"{c +1}: Wyjscie"
            break
        else:
            c+=1
            menu[c] = f"{c}: {item[2]}, {item[0]}"
            link[c] = item[1]





    while True:
        option = print_menu(menu)
        if option == MAX_ITEMS +1:
            break
        news_content = get_from_url(link[option])
        description_patern = r'<meta name="Description" content="([A-Za-z0-9łąśćńęó ,-.]+)"/>'
        mesage = re.search(description_patern, news_content)
        print(mesage.group(1))
