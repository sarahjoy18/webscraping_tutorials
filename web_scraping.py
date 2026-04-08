from bs4 import BeautifulSoup
from selenium import webdriver

dr = webdriver.Chrome()
url = 'https://www.datacamp.com/tutorial'
dr.get(url)
doc = BeautifulSoup(dr.page_source,"html.parser")
# print(doc.prettify())

title_tag = doc.find('title')
print('reading '+title_tag.text+'...')
for tutorial in doc.find_all('h2',class_='css-1yr1rb9'):
    print('--------------------------------------------------------')
    print(tutorial.text)
    desc_tag = tutorial.parent.parent.find('div',class_='css-aa366q')
    print(desc_tag.text)

#Below is for webscraping static html only
# with open("index.html") as file:
#     doc = BeautifulSoup(file, 'html.parser')
#     print("reading the file...")
#
# title_tag = doc.find('title')
# headings_tags = doc.find_all('h1')
#
# print(title_tag.text)
#
# for heading in headings_tags:
#     print(heading.text)
#
# answer = input("If you want to check further, type 'more' to continue: ")
# if answer == 'more':
#     section_tags = doc.find_all('h2')
#     for section in section_tags:
#         print(section.text)
#         for content in doc.find_all('p'):
#             print(content.text)

