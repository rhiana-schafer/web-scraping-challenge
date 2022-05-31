from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

conn = "mongodb://localhost:27017/phone_app"

app.config["MONGO_URI"] = conn
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()    
    return render_template("index.html", mars_data=mars)

@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update_many({}, {"$set": mars_data},upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)