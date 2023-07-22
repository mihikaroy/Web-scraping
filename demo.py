import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_product_listings(num_pages=20):
    base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
    params = {
        "k": "bags",
        "crid": "2M096C61O4MLT",
        "qid": "1653308124",
        "sprefix": "ba%2Caps%2C283",
        "ref": "sr_pg_",
    }

    all_products = []

    for page in range(1, num_pages + 1):
        params["page"] = page
        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("div", {"data-component-type": "s-search-result"})

        for product in products:
            product_data = {}
            all_products.append(product_data)
        time.sleep(2)

    return all_products
def scrape_additional_info(all_products):
    for product in all_products:
        url = product["product_url"]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        time.sleep(2)
def export_to_csv(all_products, output_file="amazon_products.csv"):
    df = pd.DataFrame(all_products)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    all_products = scrape_product_listings(num_pages=20)
    scrape_additional_info(all_products)
    export_to_csv(all_products)



