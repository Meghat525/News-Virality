from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import newspaper
from newspaper import Article
import nltk
driver = webdriver.Chrome("C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")
news_links=[] #List to store links of news
headings=[] #list to store headings of news
articles=[] #List to store text of the news
shares=[] #List to number of shares
keywords=[]
publish_dates=[]


#Collecting data of latest news
driver.get("https://www.indiatimes.com/")

content = driver.page_source
soup = BeautifulSoup(content)


for news_link in soup.find_all('a',href=True,attrs={'caption'}):
    news_links.append(news_link.get('href'))


for link in news_links:
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content)
    #If the article does not contain the share count
    if soup.find_all('div',attrs={'class':'share share-top'})==[]:
        shares.append("0")
    else:
        for share in soup.find_all('div',attrs={'class':'share share-top'}):
            shares.append(share.text)
    article = Article(link)
    article.download()
    article.parse()
    article.nlp()
    headings.append(article.title)
    publish_dates.append(article.publish_date)
    articles.append(article.text)




#Collecting data of old news

news_archive_links=[]
for i in range(1,101):
    new_link="https://www.indiatimes.com/seoarchive/news/pg-1"
    new_link=new_link[:-1]+str(i)
    driver.get(new_link)
    content = driver.page_source
    soup = BeautifulSoup(content)
    for news_link in soup.find_all('a',href=True,attrs={'caption'}):
            news_archive_links.append(news_link.get('href'))

    
for link in news_archive_links:
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content)
    #If the article does not contain the share count
    if soup.find_all('div',attrs={'class':'share share-top'})==[]:
        shares.append("0")
    else:
        for share in soup.find_all('div',attrs={'class':'share share-top'}):
            shares.append(share.text)
    article = Article(link)
    article.download()
    article.parse()
    article.nlp()
    headings.append(article.title)
    publish_dates.append(article.publish_date)
    articles.append(article.text)



data=pd.DataFrame({"Heading":headings,"Article":articles,"Publish_Date":publish_dates,"Shares":shares})
data.to_csv("news_dataset.csv", encoding='utf-8', index=False)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
