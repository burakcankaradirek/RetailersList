# RetailersList  

This project is a **web scraper** that extracts retailer names and addresses from the web site.  
It uses **Selenium** and **BeautifulSoup** to collect data and saves it as a CSV file.  

---

## Features  
✅ Extracts retailer information (**Name, Street Address, City, State, ZIP Code**)  
✅ Uses **Selenium** to load the webpage dynamically  
✅ Parses HTML with **BeautifulSoup** for efficient data extraction  
✅ Saves the extracted data to a CSV file (`retailers.csv`)  

---

## Requirements  

Ensure you have the following installed before running the script:  

- Python 3.x  
- Google Chrome browser  
- ChromeDriver (compatible with your Chrome version)  
- Required Python libraries:  

  ```bash
  pip install selenium beautifulsoup4 pandas

---

## Example Output (`retailers.csv`)

| Name           | Street Address | City    | State | ZIP   |
|----------------|----------------|---------|-------|-------|
| Healthy Market | 123 Main St    | Denver  | CO    | 80202 |
| Organic World  | 456 Green Ave  | Austin  | TX    | 73301 |

---

## Learn More

To learn more about this app, you can check out my Medium blog [here](https://medium.com/@burakcankaradirek/web-scraping-with-selenium-and-beautifulsoup-cd5647fe5b57).
