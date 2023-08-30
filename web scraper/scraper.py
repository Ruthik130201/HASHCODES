import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.tutorialspoint.com/tutorialslibrary.htm')

print("The status code is ", res.status_code)
print("\n")

soup_data = BeautifulSoup(res.text, 'html.parser')

print(soup_data.title)
print(soup_data.find_all('h4'))

#print(soup_data.get_text())

#Get classes of any element in the HTML page
#print(soup_data.find('p')['class'])

# Get first element in the HTML page
#print(soup_data.find('p') )
