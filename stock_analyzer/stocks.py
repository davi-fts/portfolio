import yfinance as yf
import random


def retrieve_stock_data(ticker, period="1mo", start_date=None,end_date=None):
    arguments = {"tickers" : ticker,
                 "period" : period,
                 "start" : start_date,
                 "end" : end_date
             }
    # Create a dic with arguments that have non-empty values
    arguments = {key: value for key,value in arguments.items() if value}

    # Retrieves stock historical stock price data based on the time defined; defaults to 1 month if no period is set
    data = yf.download(**arguments)

    return data

def retrieve_company_info(ticker):
    # Get company basic inforamation
    company = yf.Ticker(ticker)
    info =  company.info
    return info

def retrieve_stocks_financials(ticker):
    # Get financial data of the company
    company = yf.Ticker(ticker)
    financials = company.financials
    # Get the "Total Exenses" from the financials dataframe
    total_expenses = financials.loc["Total Expenses"]
    return total_expenses

def main():
    period = None
    start_date = None
    end_date = None

    tickers_list = ["TSLA", "AAPL", "GOOG"]
    # Chooses a random ticker from the list
    ticker =  random.choice(tickers_list)
    print(f"Ticker: {ticker}")

    # Get basic information about the company
    company_info = retrieve_company_info(ticker)
    print(f"Country: {company_info['country']}")
    print(f"Recommendation: {company_info['recommendationKey']}")
    print(f"Market capitalization: {company_info['marketCap']}")

    # Ask the user if he/she wants to define a period or a start/end date to analyse historical prices

    chosen_period = input("Choose a period? (Y/N): ").lower().strip()
    if chosen_period == "y":
        period = input("Enter the period (ex: 1d, 3mo, 1y): ")
    else:
        start_end_date = input("Set start and end date? (Y/N): ").lower().strip()
        if start_end_date == "y":
            start_date = input("Enter the start date: (follow the pattern YYYY-MM-DD) ")
            end_date = input("Enter the end date: (follow the pattern YYYY-MM-DD) ")
        else:
                #Defines the default period as 1 month if no specifc period or dates are set
                period = "1mo"

    # Retrieve stock data based on user input
    ticker_data = retrieve_stock_data(ticker, period=period, start_date=start_date,end_date=end_date)
    print(type(ticker_data))
    print (ticker_data)

    # Retrieve and print the company's total expenses
    financials = retrieve_stocks_financials(ticker)
    print("Total expenses: ")
    print(financials)

if __name__ == "__main__":
     main()
     
     
