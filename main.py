import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


#get website in html format#####################################################
response = requests.get(URL)
content_html = response.text

#read website by BeautifulSoup##################################################
soup = BeautifulSoup(content_html, "html.parser")
# print(soup.prettify)

#get list with all  titles#######################################################
web_titles = soup.find_all(name="h3", class_="title")
# print(titles)
# <h3 class="title">5) Pulp Fiction</h3>
title_list = []
for title in web_titles:
    only_title =  title.getText()
    #5) Pulp Fiction
    title_list.append(only_title)
# print(title_list)

#reverse list####################################################################
#method 1
reverse_list = title_list[::-1]
print(reverse_list)

#method 2
# for n in range(end-1,start,stop)# index 
for n in range(len(title_list)-1, -1, -1):
    #print(n)100, 99,98,97
    reverse_list2= title_list[n]
    print(reverse_list2)

#method 3 - reverse() - return changed original list
reverse_list3= title_list.reverse()
print(title_list)

#method 4 - list(reversed(my_list))
reverse_list4 = list(reversed(title_list))
print(reverse_list4)



# #save file######################################################################
with open("movie_list.txt", mode="w", encoding='utf-8') as file:
    #add each line
    for movie in reverse_list:
        file.write(f"{movie}\n")


