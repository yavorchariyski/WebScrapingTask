# Web Scraping with Selenium and BeautifulSoup

## Project Overview ##
This project is a web scraper that retrieves product information from a given URL and stores the data in a JSON file. The project is built using Python and makes use of the Selenium and BeautifulSoup libraries.

### Requirements ###
* Python 3.x
* Selenium
* BeautifulSoup4
* json
  
### Installation ###
* You can install the requirements by running the following command:
```shell
pip install -r requirements.txt
```
### Usage ###
The project is run using the main.py file. The product information is retrieved from the URL specified in the resources.py file. The scraped information includes the product name, price, color, and a list of sizes.<br/><br/>
The product information is stored in the data/product.json file.

### Configuration ###
The configuration for the project is stored in the <b><u>resources.py</u></b> file. The following information can be configured:

* <b>PRODUCT_URL</b>: The URL for the product page to be scraped
* <b>NAME_SELECTOR</b>: The CSS selector for the product name
* <b>PRICE_SELECTOR</b>: The CSS selector for the product price
* <b>COLOR_SELECTOR</b>: The CSS selector for the product color
* <b>SIZE_SELECTORS</b>: The CSS selector for the product sizes
* <b>IMPLICIT_WAIT</b>: The implicit wait time in seconds for the WebDriver to wait for the page to load before proceeding with the scraping.

### Project Structure ###
The project has the following file structure:

* <b>main.py</b>: The main file that runs the scraper
* <b>resources.py</b>: The configuration file for the project
* <b>requirements.txt</b>: The file containing the list of required packages and their versions
* <b>data/</b> :The directory containing the <b>product.json</b> file that stores the scraped product information

### Output ###
The output of the script will be saved in a file named <i><b>'product.json'</b></i> located in the <i><b>'data'</b></i> directory. This file will contain the following information about the product being scraped:
* Name /as string/
* Price /as double/
* Color /as string/
* Sizes /as array/

Output example:
```json
{
    "name": "MIDI SATIN SKIRT",
    "price": 29.99,
    "color": "RED",
    "sizes": ["XS", "S", "M", "L", "XL"]
}
```
Note that if any of the information is not present on the product page, the corresponding value in the JSON file will be set to <b><i>'None'</i></b>.

### Note ###
* Make sure that you have the correct URL to scrape.
* The information extracted may change over time, so make sure to verify the accuracy of the information extracted.