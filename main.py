from bs4 import BeautifulSoup
import requests
import re
import csv
from itertools import zip_longest

url =  "https://www.dell.com/en-us/shop/deals/business-deals/business-laptop-deals"
    
laptop_names_dataset = []
laptops_prices_dataset = []
laptop_specs_dataset = []
laptops_imgs_dataset = []
response = requests.get(url) 
src = response.content
# print(src)
soup = BeautifulSoup(src,"lxml")
laptop_len = soup.find_all("div",{"class":"ps-system-title-container ps-title-container"})


laptop_names = soup.find_all("div",{"class":"ps-system-title-container ps-title-container"})

laptop_price = soup.find_all("div",{"class":"ps-dell-price ps-simplified"})

laptop_specs_first = soup.find_all("li",{"class":"variant-specs-column variant-specs-first-column"})

laptop_specs_second = soup.find_all("li",{"class":"variant-specs-column variant-specs-second-column"})

laptop_allSpecs = soup.find_all("div",{"class":"iconography-feature-specs"})

laptop_img = soup.find_all("div",{"class":"ps-image ps-product-image-with-high-resolution"})


def get_laptop_name(laptopnames):
    
    for i in range(len(laptop_len)):
        lap_name = laptopnames[i].find("a").text.strip()
        laptop_names_dataset.append(lap_name)

def get_laptop_prices(price):
    for i in range(len(laptop_len)):
        lap_price = price[i].find_all("span")
        laptops_prices_dataset.append(lap_price)



def get_laptop_specs(spec):
    specs_section = soup.find('section', class_='ps-show-hide')
    specs = []
    for spec_container in specs_section.find_all('div', class_='short-specs ps-dds-svg-icon-container'):
        spec_name = spec_container.find('span', class_='svg-icon').next_sibling.strip()
        specs.append(f"{spec_name}")
        laptop_specs_dataset.append(specs)

def get_laptop_image(url):
    for i in range(len(laptop_len)):
        lap_img = url[i].find("img")
        img_src = lap_img.get('src')
        laptops_imgs_dataset.append(img_src)

get_laptop_prices(laptop_price)
get_laptop_name(laptop_names)
get_laptop_specs(laptop_allSpecs)
get_laptop_image(laptop_img)

file_list = [laptop_names_dataset, laptops_prices_dataset,laptop_specs_dataset,laptops_imgs_dataset]
exported_ = zip_longest(*file_list)


with open('laptops_dataset.csv', 'w', newline='', encoding='utf-8') as f:
    wr = csv.writer(f)
    wr.writerow(["Name","Price", "Specs","Images"])
    wr.writerows(exported_)

# print(laptops_imgs_dataset)






