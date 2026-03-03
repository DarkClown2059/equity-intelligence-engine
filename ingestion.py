import yfinance as yf
import pandas as pd

def safe_year_index(df):
    try:
        df.index = pd.to_datetime(df.index).year
    except Exception:
        pass
    return df

def get_financials(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)

    income = ticker.financials.T
    balance = ticker.balance_sheet.T
    cashflow = ticker.cashflow.T

    income.sort_index(inplace=True)
    balance.sort_index(inplace=True)
    cashflow.sort_index(inplace=True)

    income = safe_year_index(income)
    balance = safe_year_index(balance)
    cashflow = safe_year_index(cashflow)

    return income, balance, cashflow
