import requests

address = input("Enter your country code from the given list(Countries_list.txt) : ")

url = "https://api.covid19api.com/summary"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

r = response.json()

for each in r['Countries']:
	if each['CountryCode'] == address:
		country = each['Country']
		TotalDeaths = each['TotalDeaths']
		NewConfirmed = each['NewConfirmed']
		NewRecovered = each['NewRecovered']
		NewDeaths = each['NewDeaths']
		TotalRecovered = each['TotalRecovered']
		TotalConfirmed = each['TotalConfirmed']
		print("COVID CASES IN {} : \nTotalCases     = {} \nTotalDeaths    = {} \nTotalRecovered = {} \nTodayCases     = {} \nTodayRecovered = {} \nTodayDeaths    = {}".format(
				country, TotalConfirmed, TotalDeaths, TotalRecovered, NewConfirmed, NewRecovered, NewDeaths
			)
		)

