# web-scraping-challenge

In this challenge, I utilize powerful Chromedriver and the BeautifulSoup Python module to scrape several websites about Mars. I store the scraped data into a local MongoDB database and display the data with the Flask Python module.


First portion of scraped data is the most recent news title and teaser summary from the mars.nasa.gob website.

Second portion of scraped data is from the jpl.nasa.gov website for a featured image of mars. This image periodically changes roughly every hour, so results may vary if you try to rerun my scripts.

I used the pandas Python module to import the tables from space-facts.com/mars/ and clean up the data to be displayed on my flask app.

Final portion of scraped data is from https://astrogeology.usgs.gov. Utilizing the chromedriver to click on specific hypertext links to grab high resolution images of each of Mars' hemispheres and their title.


To run this code, clone this repository to your machine. Make sure you have all modules in both app.py and scrape_mars.py files. In the scrape_mars.py file, line 8, replace my filepath to the filepath of your chromedriver.exe (Windows).

The MongoDB server is the general local server when you install MongoDB. If you want to connect to another server, please modify line 9 in the app.py file to your desired MongoDB server.

Once you have your chromedriver pathed and your MongoDB server connected, run the command "python app.py" in your terminal while in the directory of your local repository and click the local host port that is displayed on your terminal to open the HTML file. 

There will be no data displayed on the landing page until you hit the button "Grab some data!". This button will initiate the webscraping. Sit back, take a sip of a cold one, and enjoy the scraping at work!

when the scraping is completed, the chromedriver will close and the data will now be on the landing page!




