import requests

url = "https://api.covid19api.com/summary"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

r = response.json()

TotalDeaths = r['Global']['TotalDeaths']
NewConfirmed = r['Global']['NewConfirmed']
NewRecovered = r['Global']['NewRecovered']
NewDeaths = r['Global']['NewDeaths']
TotalRecovered = r['Global']['TotalRecovered']
TotalConfirmed = r['Global']['TotalConfirmed']
Date = r['Date']
print("COVID CASES AROUND THE WORLD: {} \nTotalCases     = {} \nTotalDeaths    = {} \nTotalRecovered = {} \nTodayCases     = {} \nTodayRecovered = {} \nTodayDeaths    = {}".format(
	Date, TotalConfirmed, TotalDeaths, TotalRecovered, NewConfirmed, NewRecovered, NewDeaths
	)
)
	# "\nTodayRecovered = "+NewRecovered+"\n")

# print(NewConfirmed)