#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request
import argparse

SEARCH_URL = 'https://www.etymonline.com/search?q='
AGENT = {'User-Agent': "Magic Browser"}


def soup_search(query_url: str, search_term: str):
    # post request to search URL, return beautiful soup parsed object
    url = query_url + search_term
    req = urllib.request.Request(url, headers=AGENT)
    response = urllib.request.urlopen(req)
    html = response.read()
    return BeautifulSoup(html, 'html.parser')


def first_result_print(search_page):
    print("{}\n".format(search_page.find("div", class_="searchList__pageCount--2jQdB").get_text()))
    print(search_page.find("section", class_="word__defination--2q7ZH undefined").get_text().replace('\n', '\n\n'))


def main():
    parser = argparse.ArgumentParser(prog='etym.py', usage='%(prog)s word')
    parser.add_argument('word', help="The word you wish to look up")
    args = parser.parse_args()
    results = soup_search(SEARCH_URL, args.word)
    first_result_print(results)


if __name__ == '__main__':
    main()
