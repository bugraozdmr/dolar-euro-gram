from bs4 import BeautifulSoup
import requests

url = "https://www.doviz.com/"
header = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
}

respond = requests.get(url,headers=header)
html = respond.content

soup = BeautifulSoup(html,"html.parser")

deger = soup.find("div",{"class":"table table-narrow"}).find_all("td",{"class":"text-bold"})
para = []

a = 0
for i in deger:
    if i.text.startswith("%"):
        continue
    #1.değer dolar 2.değer euro
    para.append(i.text)
    a += 1
    if a == 2:
        break
#para[0] dolar      para[1] euro

gram_altın = soup.find("div",{"class":"item"}).find("span",{"class":"value"}).text


print("1 dolar {} TL\n1 euro {} TL\n1 gram altın {} TL".format(para[0],para[1],gram_altın))

