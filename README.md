# Web Scraping with Selenium and BeautifulSoup

## Project Overview ##
This project uses Selenium and BeautifulSoup to scrape information from a website and save it as a JSON file.

### Requirements ###
* Python 3.9 or higher
* Selenium
* BeautifulSoup4
* json
  
### Installation ###
* You can install the requirements by running the following command:
```shell
pip install -r requirements.txt
```

* Run 
```shell
main.py
```
The script will navigate to a URL, wait for the page to fully load, and then parse the HTML using BeautifulSoup. The information is then extracted and saved as a JSON file in the <b>data</b> folder.

### Output ###

```json
{
    "name": "MIDI SATIN SKIRT",
    "price": 29.99,
    "color": "RED",
    "sizes": ["XS", "S", "M", "L", "XL"]
}
```

### Note ###
* Make sure that you have the correct URL to scrape.
* The information extracted may change over time, so make sure to verify the accuracy of the information extracted.