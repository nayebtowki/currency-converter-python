# 💱 Currency Converter (Python CLI)

A simple command-line currency converter built with Python and the [FreeCurrencyAPI](https://freecurrencyapi.com/).  
This tool fetches real-time exchange rates and allows users to convert from a base currency to multiple target currencies using live data.

---

## 📌 Features

- 🔁 Converts from a base currency to multiple target currencies
- 🧾 Only allows these supported currencies: `USD`, `CAD`, `EUR`, `GBP`, `AUD`, `CNY`
- 📡 Uses FreeCurrencyAPI to fetch live exchange rates
- 🔁 Keeps running until the user quits (`q`)
- 🧠 Good practice for API integration, input validation, and Python scripting

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Install the required dependency:
   ```bash
   pip install requests
3. Run the script:
    python main.py
## 💬 Supported Currencies

Only the following base currencies are allowed:
USD, CAD, EUR, GBP, AUD, CNY
If a user enters a currency not in this list, the program will ask again

## 🧪 Example Output
$ python main.py
Enter Base Currency ['USD', 'CAD', 'EUR', 'GBP', 'AUD', 'CNY'] (q to quit): gb

Exchange Rates for 1 GBP:
``` USD : 1.3720053960
CAD : 1.8769310161
EUR : 1.1696896705
AUD : 2.0994154649
CNY : 9.8406693244

Enter Base Currency ['USD', 'CAD', 'EUR', 'GBP', 'AUD', 'CNY'] (q to quit): q

## Technologies Used
- Python 3
- requests library
- FreeCurrencyAPI
