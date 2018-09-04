# Facebook Page Photo_Scraper

## Useage

* make a file 'config.ini' to the working directory with the following content, replace username and password with your defaults.
* Change OUTPUT to the output folder of your images to be saved, relative to the working directory
```
[DEFAULT]
USERNAME = <username>
SECRET = <password>
OUTPUT = data/

```

* Add page_photo_link to the link of your page's photo directly as given in the sample link, in scrape.py

```

page_photo_link = "https://www.facebook.com/pg/TwinklingDreamsWeddingPlanners/photos/?ref=page_internal"

```
Download the chromedriver for selenium and save it in the directory, find in here https://pypi.org/project/selenium/

To run the script use

```
python3 scrape.py
```
