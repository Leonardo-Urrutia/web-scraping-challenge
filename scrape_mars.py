# Importing modules for script
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "../chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars_data = {}
    # URL to Nasa's Mars news page
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Grabbing first news chunk of html to grab title and p txt
    first_news_results = soup.find("li", class_="slide")
    content_title = first_news_results.find("div", class_="content_title").text
    first_article_p_txt = first_news_results.find("div", class_="article_teaser_body").text

    mars_data["title"] = content_title
    mars_data["summary"] = first_article_p_txt

    # Storing url to page to grab the featured image and base url to concat to src of img
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    mars_url = 'https://www.jpl.nasa.gov'
    browser.visit(featured_image_url)
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Grabbing container html of image
    featured_image_container = soup.find("div", class_="carousel_container")
    featured_img_half_link = featured_image_container.find("a", class_="button fancybox")["data-fancybox-href"]
    full_img_url = f'{mars_url}{featured_img_half_link}'

    mars_data["featured_img"] = full_img_url

    # URLS for beautiful images of hemispheres
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemi_base_url = "https://astrogeology.usgs.gov"
    hemisphere_image_urls = [] # Empty list created to store dictionaries of each hemisphere
    browser.visit(hemi_url)
    time.sleep(1)

    # Goes through each hemisphere and grabbing image links and title
    # 1
    browser.links.find_by_partial_text('Cerberus').click()
    html = browser.html
    soup = bs(html, "html.parser")

    cerb_img = soup.find("img", class_="wide-image")["src"]
    hemi_base_url = "https://astrogeology.usgs.gov"
    full_cerb_img = f"{hemi_base_url}{cerb_img}"

    text_container = soup.find("section", class_="block metadata")
    hemi_title = text_container.find("h2", class_="title").text

    hemi_dict = {"title": hemi_title, "img_url": full_cerb_img}
    hemisphere_image_urls.append(hemi_dict)
    browser.visit(hemi_url)

    # 2
    browser.links.find_by_partial_text('Schiaparelli').click()
    html = browser.html
    soup = bs(html, "html.parser")
    schia_img = soup.find("img", class_="wide-image")["src"]
    full_schia_img = f"{hemi_base_url}{schia_img}"

    text_container = soup.find("section", class_="block metadata")
    hemi_title = text_container.find("h2", class_="title").text

    hemi_dict = {"title": hemi_title, "img_url": full_schia_img}
    hemisphere_image_urls.append(hemi_dict)
    browser.visit(hemi_url)

    # 3 
    browser.links.find_by_partial_text('Syrtis Major').click()
    html = browser.html
    soup = bs(html, "html.parser")
    syrtis_img = soup.find("img", class_="wide-image")["src"]
    full_syrtis_img = f"{hemi_base_url}{syrtis_img}"

    text_container = soup.find("section", class_="block metadata")
    hemi_title = text_container.find("h2", class_="title").text


    hemi_dict = {"title": hemi_title, "img_url": full_syrtis_img}
    hemisphere_image_urls.append(hemi_dict)
    browser.visit(hemi_url)

    #4 
    browser.links.find_by_partial_text('Valles Marineris').click()
    html = browser.html
    soup = bs(html, "html.parser")
    valles_img = soup.find("img", class_="wide-image")["src"]
    full_valles_img = f"{hemi_base_url}{valles_img}"

    text_container = soup.find("section", class_="block metadata")
    hemi_title = text_container.find("h2", class_="title").text


    hemi_dict = {"title": hemi_title, "img_url": full_valles_img}
    hemisphere_image_urls.append(hemi_dict)

    mars_data["hemi"] = hemisphere_image_urls

    browser.quit()


    return mars_data
