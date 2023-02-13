# Import the required libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import resources

# Create Chrome options to run in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# Create a new instance of Chrome WebDriver
try:
    browser = webdriver.Chrome(options=options)
except Exception as e:
    print("An error occurred while creating the WebDriver:", e)
    browser.quit()

# Navigate to the URL
try:
    browser.get(resources.PRODUCT_URL)
except Exception as e:
    print("An error occurred while navigating to the URL:", e)
    browser.quit()

# Wait for the page to fully load
try:
    browser.implicitly_wait(resources.IMPLICIT_WAIT)
except Exception as e:
    print("An error occurred while waiting for the page to load:", e)
    browser.quit()

# Parse the HTML using BeautifulSoup
try:
    soup = BeautifulSoup(browser.page_source, "html.parser")
except Exception as e:
    print("An error occurred while parsing the HTML:", e)
    browser.quit()


# Select the elements from the page using CSS selectors
try:
    name_element = soup.select_one(resources.NAME_SELECTOR)
    if name_element:
        name_element = name_element.text
    price_element = soup.select_one(resources.PRICE_SELECTOR)
    if price_element:
        price_element = float(price_element.text.replace('£', '').strip())
    color_element = soup.select_one(resources.COLOR_SELECTOR)
    if color_element:
        color_element = color_element.text
    size_elements = soup.select(resources.SIZE_SELECTORS)
except Exception as e:
    print("An error occurred while selecting elements from the page:", e)
    browser.quit()

# Create a dictionary to store the product data
product_data = {
    # Store the name of the product if it was found
    'name': name_element if name_element else None,
    # Store the price of the product if it was found
    'price': price_element if price_element else None,
    # Store the color of the product if it was found
    'color': color_element if color_element else None,
    # Store the list of sizes if any were found
    'sizes': [size_element.text for size_element in size_elements] if size_elements else None
}

# Write the product data to a JSON file
try:
    with open('data/product.json', 'w') as file:
        json.dump(product_data, file)
except Exception as e:
    print("An error occurred while writing the product data to a JSON file:", e)

# Close the WebDriver
browser.quit()
