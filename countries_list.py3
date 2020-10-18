#There are total 248 countries in this list. LOL I don't know how there are that many.......
import requests

url = "https://api.covid19api.com/countries"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
data = open("countries_list.txt","a")
r = response.json()
for each in r:
	CountryName = each['Country']
	CountryCode = each['ISO2']
	print("CountryName = "+CountryName+"\nCountryCode = "+CountryCode+"\n",file=data)
data.close()