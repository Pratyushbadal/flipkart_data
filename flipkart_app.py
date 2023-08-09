import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape_flipkart(search):
    Product_name = []
    Prices = []
    Description = []
    Reviews = []
    Image_urls = []

    page_num = 1
    while True:
        url = f"https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&param=1112&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlJlYWxtZSBzbWFydHBob25lcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=19.productCard.PMU_V2_13&page={page_num}"

        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        products = soup.find_all("div", class_="_1AtVbE")
        if not products:
            break

        for product in products:
            name = product.find("div", class_="_4rR01T")
            if name and name.text.strip() == search:
                price = product.find("div", class_="_30jeq3")
                description = product.find("ul", class_="_1xgFaf")
                review = product.find("div", class_="_3LWZlK")
                image = product.find("img", class_="_396cs4")

                if name:
                    Product_name.append(name.text.strip())
                else:
                    Product_name.append("N/A")

                if price:
                    Prices.append(price.text.strip())
                else:
                    Prices.append("N/A")

                if description:
                    Description.append(description.text.strip())
                else:
                    Description.append("N/A")

                if review:
                    Reviews.append(review.text.strip())
                else:
                    Reviews.append("N/A")

                if image and image.get("src"):
                    Image_urls.append(image.get("src"))
                else:
                    Image_urls.append("N/A")

                return pd.DataFrame.from_dict(
                    {"Product Name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews,
                     "Image URLs": Image_urls})

        page_num += 1

    return pd.DataFrame()


search = input("Enter a mobile device: ")
df = scrape_flipkart(search)

if not df.empty:
    print("\nSearch results for:", search)
    for index, row in df.iterrows():
        print("\n" + "-" * 40)
        for key, value in row.items():
            print(f"{key:<20} {value}")
else:
    print("No device found.")
