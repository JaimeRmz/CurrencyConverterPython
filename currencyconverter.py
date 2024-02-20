import requests

CC_API_KEY = "fca_live_18yy8KERD8lPg16CFU6zJq49Nt6JeRyyiX7vxC6r"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={CC_API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(e)
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        print("Failed to fetch data.")
        continue

    if base in data:
        del data[base]

    for ticker, value in data.items():
        print(f"{ticker}: {value}")
