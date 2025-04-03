import pandas as pd

def load_currency_data(file_path):
    # Load the currency data
    return pd.read_csv(file_path, encoding="latin1")

def convert_currency(amount, currency_code, currency_df):
    # Find the exchange rate for the given currency code
    row = currency_df[currency_df["code"] == currency_code]
    if not row.empty:
        rate = row.iloc[0]["rate"]
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

def main():
    file_path = "C:\\Users\\theda\\Laboratory-Activity-4B-Set-and-Dictionary\\currency.csv"
    currency_df = load_currency_data(file_path)
    
    # User input
    amount = float(input("How much dollar do you have? "))
    currency_code = input("What currency do you want to have? ").upper()
    
    converted_amount = convert_currency(amount, currency_code, currency_df)
    
    if converted_amount is not None:
        print(f"\nDollar: {amount} USD")
        print(f"{currency_df[currency_df['code'] == currency_code]['name'].values[0]}: {converted_amount}")
    else:
        print("Invalid currency code. Please check and try again.")

if __name__ == "__main__":
    main()