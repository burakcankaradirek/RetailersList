from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Open the browser with Selenium
driver = webdriver.Chrome()
driver.get("https://www.naturalfoodretailers.com/retailer-directory")

# Wait until the page is fully loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mix")))

# Get the HTML content of the page
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the browser
driver.quit()

# Extract retailer information
retailers = soup.find_all('div', class_='mix')

data = []
for retailer in retailers:
    name_tag = retailer.find('h3')
    if name_tag:
        name = name_tag.text.strip()

        # Find address details
        location_details = retailer.find('div', class_='location-details')
        if location_details:
            address_lines = location_details.find_all('div')

            # Get the street address
            street = address_lines[0].text.strip() if len(address_lines) > 0 else ''

            # Parse city, state, and ZIP code
            city, state, zip_code = '', '', ''
            if len(address_lines) > 1:
                city_state_zip = address_lines[1].text.strip()
                parts = city_state_zip.split(',')

                if len(parts) == 2:
                    city = parts[0].strip()
                    state_zip = parts[1].strip().split()
                    state = state_zip[0] if len(state_zip) > 0 else ''
                    zip_code = state_zip[1] if len(state_zip) > 1 else ''
        else:
            street, city, state, zip_code = '', '', '', ''

        # Append extracted data
        data.append([name, street, city, state, zip_code])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Name', 'Street Address', 'City', 'State', 'ZIP'])

# Save to CSV
with open("retailers.csv", mode="w", encoding="utf-8", newline="") as file:
    df.to_csv(file, index=False)

print("retailers.csv file created.")
