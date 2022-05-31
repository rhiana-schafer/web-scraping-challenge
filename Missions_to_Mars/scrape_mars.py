from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    #setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    scraped_data={}

    #setting up base urls
    news_url = 'https://redplanetscience.com/'
    space_url = 'https://spaceimages-mars.com/'
    facts_url = 'https://galaxyfacts-mars.com/'
    hemi_url = 'https://marshemispheres.com/'

    #NASA Mars News
    browser.visit(news_url)
    time.sleep(1)
    html=browser.html
    soup=bs(html, 'html.parser')

    latest = soup.find_all('div', class_='list_text')[0]
    news_title=latest.find('div', class_='content_title').text
    news_p=latest.find('div', class_='article_teaser_body').text
    
    browser.quit()

    # JPL Mars Space Images—Featured Image
    browser.visit(space_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    image_area = soup.find_all('div', class_='floating_text_area')[0]
    featured_image_url=space_url+image_area.a['href']
    featured_image_url
    browser.quit()


    # Mars Facts
    df=pd.read_html(facts_url, header=0,index_col=0)[0]
    html_table = df.to_html()
    html_table = html_table.replace('\n', '')
    html_table

    #  Mars Hemispheres
    #browser.visit(hemi_url)
    #time.sleep(1)
    #html = browser.html
    #soup = bs(html, 'html.parser')
    #article_list = soup.find_all('div', class_='item')
    #hemisphere_image_urls = []
    #for article in article_list:
    #    hemi = {}
    #    hemi['title'] = article.h3.text.replace(' Enhanced','') 
    #    hemi['img_url'] = hemi_url+article.img['src']
    #    hemisphere_image_urls.append(hemi)
    #hemisphere_image_urls
    #browser.quit()

    # Build our dictionary from our scraped data

    scraped_data['news_title'] = news_title
    scraped_data['news_p'] = news_p
    #scraped_data['featured_image_url'] = featured_image_url
    scraped_data['html_table'] = html_table
    #scraped_data['hemisphere_image_urls'] = hemisphere_image_urls


    return scraped_data
