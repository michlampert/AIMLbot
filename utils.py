import requests
from bs4 import BeautifulSoup

def make_ul(l):
    result = ""

    if not l: return "*jak narazie to pusto tutaj ;)*"
    for li in l:
        result += "> " + str(li) + "€"

    return result

def get_info(about):
    URL = "https://www.google.com/search?q=info"+"+".join(about.split(" "))
    # print(URL)
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"}

    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    # print(soup.prettify())
    try:
        raport = soup.find_all("div", class_="uqZISe")[0].find_all("span", class_="fYyStc")[0].get_text().strip()
    except:
        raport = "Nie wiem"
    # print(raport)
    return raport

def get_weather(city):
    URL = "https://www.google.com/search?q=pogoda+"+"+".join(city.split(" "))
    # print(URL)
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"}

    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    # print(soup.prettify())
    try:
        temp = soup.find_all("span", class_="qXLe6d epoveb")[0].find_all("span", class_="fYyStc")[0].get_text().strip()
        clouds = soup.find_all("span", class_="qXLe6d F9iS2e")[0].find_all("span", class_="fYyStc")[2].get_text().strip()
        raport = temp + " | " + clouds
    except:
        raport = "Nie wiem"
    # print(raport)
    return raport

def add_task(list, task):
    list += [task]

def delete_task(list, task):
    if task in list: list.remove(task)

def reset(list):
    import copy
    l2 = copy.copy(list)
    for task in l2: delete_task(list, task)

# print(get_info("barack obama"))
# get_weather("wodzislaw slaski")