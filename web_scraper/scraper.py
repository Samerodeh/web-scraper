import json
import requests
from bs4 import BeautifulSoup 

url = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser').find(id = "bodyContent").find_all('a', title = 'Wikipedia:Citation needed')
    return len (soup)

def get_citations_needed_report(url):
    page = requests.get(url)
    text = BeautifulSoup(page.content, 'html.parser').find(id = "bodyContent").find_all('p')
    get_citations = []

    for p in text:
        if p.find('a', title = 'Wikipedia:Citation needed'):
            text = p.text
            count_citation = text.count("[citation needed]")
            i = 0
            while i < count_citation:
                division = text.split("[citation needed]")
                dictionary_of_citation = {"paragraph": division[0], "text": p.text}
                text = text.replace(division[0], "")
                text = text.replace("[citation needed]", "")
                get_citations.append(dictionary_of_citation)
                i += 1

    json_file = json.dumps(get_citations, indent = 4)
    with open('scraper.json', 'w') as f:
        f.write(json_file)

    results  = ""
    for i in get_citations:
        results  += (f"- Citation needed :-\n\n {i['paragraph']} \n\n")
    return results 

if __name__ == "__main__":
    print (f"\n - Citation needed number :-\n\n {get_citations_needed_count(url)}\n ")
    print(get_citations_needed_report(url))