# import requests
# from bs4 import BeautifulSoup
# import json
# import os

# # Replace '<your_url>' with the actual URL you want to scrape
# url = 'https://www.nike.com/w/jordan-1-shoes-4fokyzy7ok'

# # Send a GET request to the URL
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find elements based on the specified classes
#     link_overlay = soup.find('a', class_='product-card__link-overlay')

#     # Check if the link_overlay is found
#     if link_overlay:
#         # Extract information from the linked page
#         linked_page_url = link_overlay['href']
#         linked_page_response = requests.get(linked_page_url)

#         if linked_page_response.status_code == 200:
#             linked_page_soup = BeautifulSoup(linked_page_response.text, 'html.parser')

#             # Extract h1, h2, div, and picture elements with specified classes
#             h1_element = linked_page_soup.find('h1', class_='pdp_product_title')
#             h2_element = linked_page_soup.find('h2', class_='headline-5 pb1-sm d-sm-ib')
#             div_element = linked_page_soup.find('div', class_='product-price css-11s12ax is--current-price css-tpaepq')
#             picture_element = linked_page_soup.find('picture')

#             # Create a dictionary to store the extracted information
#             data = {}
#             if h1_element:
#                 data['h1'] = h1_element.text.strip()
#             if h2_element:
#                 data['h2'] = h2_element.text.strip()
#             if div_element:
#                 data['div'] = div_element.text.strip()
#             if picture_element:
#                 source_element = picture_element.find('source')
#                 if source_element:
#                     srcset_attribute = source_element.get('srcset')
#                     data['picture_srcset'] = srcset_attribute
#                 else:
#                     print("No 'source' element found in 'picture'")
#             else:
#                 print("No 'picture' element found on the linked page")

#             # Save the data to a JSON file
#             json_filename = 'extracted_data.json'
#             with open(json_filename, 'w') as json_file:
#                 json.dump(data, json_file, indent=2)

#             # Print the absolute path of the JSON file
#             json_path = os.path.abspath(json_filename)
#             print(f'Data successfully extracted and saved to: {json_path}')
#         else:
#             print(f'Failed to retrieve linked page ({linked_page_response.status_code})')
#     else:
#         print('Link overlay not found on the main page')
# else:
#     print(f'Failed to retrieve the main page ({response.status_code})')

import requests 
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest


url  = "https://wuzzuf.net/search/jobs/?q=flutter+developer&a=navbl"
request = requests.get(url)
src = request.content

soup = BeautifulSoup(src , "lxml")
