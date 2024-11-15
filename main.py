import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

#print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.title)

#title_list=[]
#title_index=[]
title_text_list=[]

title_tag_list = soup.find_all(class_="listicleItem_listicle-item__title__BfenH")

for title_tag in reversed(title_tag_list):
    title_text_list.append(title_tag.getText())
    #title = title_tag.getText().split(" ",1)
    #title_list.append(title[1])
    #title_index.append(int(title[0].replace(")","")))

#print(title_list)
#print(title_index)
print(title_text_list)
#h3.listicleItem_listicle-item__title__BfenH:nth-child(3)

#div.listicle_listicle__item__CJna4:nth-child(2) > h3:nth-child(2)