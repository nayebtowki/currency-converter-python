import requests

API_KEY= "fca_live_xaoui4IaKg9Z55FmN88BKbvGmWLPxfBONEpbOzkw"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "GBP","AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(f"Error: {e}")
        print("Unable to retrieve rates. Please check your input or try again.")
        return None

while True:
    base = input("Enter Base Currency (e.g. GBP) (q for quit): ").upper()
    
    if base == "Q":
        break
    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticket, value in data.items():
        print(f"{ticket} : {value:.2f}")