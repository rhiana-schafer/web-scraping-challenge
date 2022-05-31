# web-scraping-challenge

This project was completed as a part of the Data Science and Visualization Bootcamp at Northwestern University (https://bootcamp.northwestern.edu/data/)

## Project Intro/Objective
The purpose of this project is twofold:
<ol>
  <li> To scrape the web for data about Mars </li>
  <li> To then display that data in a webpage that can be easily updated with a new scrape </li>
 </ol>

### Methods Used
* Web Scraping
* Database Building
* Web Page Creation

### Technologies
* Jupyter Notebook
* Beautiful Soup
* Python
* Pandas
* Requests/Splinter
* MongoDB
* Flask
* HTML

### Files: All within Missions_to_Mars folder
* mission_to_mars.ipynb - jupyter notebook file containing code for scraping data sources
* scrape_mars.py - python script that is just a conversion from the above jupyter notebook
* app.py - runs flask app to display website
* templates:
  *  index.html - website shell/template

### Data Sources
<ul>
<li>Latest news about mars was scraped from: https://redplanetscience.com/</li>
<li>A featured image of mars was scraped from: https://spaceimages-mars.com/</li>
<li>Facts about the planet (such as diameter, mass, etc) were scraped from:  https://galaxyfacts-mars.com/</li>
<li>High res images for each hemisphere were scraped from: https://marshemispheres.com/</li>
</ul>
