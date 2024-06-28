from bs4 import BeautifulSoup
import requests
import re

url =  "https://www.dell.com/en-us/shop/dell-laptops/scr/laptops"
    
laptop_names_dataset = []
laptops_prices_dataset = []
laptop_specs = []

response = requests.get(url) 
src = response.content
# print(src)
soup = BeautifulSoup(src,"lxml")
laptop_len = soup.find_all("div",{"class":"ps-variant-title-container"})


laptop_names = soup.find_all("div",{"class":"ps-variant-title-container"})

laptop_price = soup.find_all("div",{"class":"ps-variant-price"})

laptop_specs_first = soup.find_all("li",{"class":"variant-specs-column variant-specs-first-column"})

laptop_specs_second = soup.find_all("li",{"class":"variant-specs-column variant-specs-second-column"})


def get_laptop_name(laptopnames):
    
    for i in range(len(laptop_len)):
        lap_name = laptopnames[i].find("a").text.strip()
        laptop_names_dataset.append(lap_name)

def get_laptop_prices(price):
    for i in range(len(laptop_len)):
        lap_price = price[i].find("span").text.strip()
        laptops_prices_dataset.append(lap_price)

def get_laptop_specs(specs1,spec2):
    for i in range(7):
        lap_specs = specs1[i].find_all("div",{"spec-value"}).text.strip()
        lable_specs = specs1[i].find_all("div",{"spec-label"}).text.strip()
        # lap_specs2 = spec2[i].find("div",{"spec-value"})
        # lable_specs2 = spec2[i].find("div",{"spec-lable"})
        laptop_specs.append(f"{lable_specs} : {lap_specs}")
        # laptop_specs.append(f"{lap_specs2} : {lable_specs2}")
        laptop_specs.append("-----")

# def get_laptop_specs(specs1,spec2):
#     lap_specs = specs1[0].find("div",{"spec-value"}).text.strip()
#     lable_specs = specs1[0].find("div",{"spec-label"}).text.strip()
#     lap_specs2 = spec2[0].find("div",{"spec-value"})
#     lable_specs2 = spec2[0].find("div",{"spec-lable"})
#     laptop_specs.append(f"{lable_specs} : {lap_specs}")
#     laptop_specs.append(f"{lap_specs2} : {lable_specs2}")
#     laptop_specs.append("-----")


# get_laptop_prices(laptop_price)
# get_laptop_name(laptop_names)
get_laptop_specs(laptop_specs_first,laptop_specs_second)
print(laptop_specs)




