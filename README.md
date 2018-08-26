# Facebook Page Photo_Scraper

## Useage

* change the username and password variables to your facebook account credentials
* Change dl_path to the output folder of your images to be saved, relative to the working directory
* Add page_photo_link to the link of your page's photo directly as given in the sample link.

```
dl_path = "data/"
username = "user@email.com"
password = "pass"
page_photo_link = "https://www.facebook.com/pg/TwinklingDreamsWeddingPlanners/photos/?ref=page_internal"

```
Download the chromedriver for selenium and save it in the directory, find in here https://pypi.org/project/selenium/

To run the script use

```
python3 scrape.py
```
