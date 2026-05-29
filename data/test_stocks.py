
import pytest
from stocks import retrieve_stock_data, retrieve_company_info, retrieve_stocks_financials
import pandas as pd

def test_retrieve_stock_data():
    data  = retrieve_stock_data("AAPL")
    colum_headers_list = data.columns.tolist()
    assert len(colum_headers_list) == 5     
    assert colum_headers_list[0] == (("Close", "AAPL"))
    assert colum_headers_list[1] == ("High", "AAPL")
    assert colum_headers_list == [('Close', 'AAPL'), ('High', 'AAPL'), ('Low', 'AAPL'),('Open', 'AAPL'),('Volume', 'AAPL')]

    data  = retrieve_stock_data("TSLA")
    colum_headers_list = data.columns.tolist()
    assert len(colum_headers_list) == 5     
    assert colum_headers_list[0] == (("Close", "TSLA"))
    assert colum_headers_list[1] == ("High", "TSLA")
    assert colum_headers_list == [('Close', 'TSLA'), ('High', 'TSLA'), ('Low', 'TSLA'),('Open', 'TSLA'),('Volume', 'TSLA')]

    data  = retrieve_stock_data("GOOG")
    colum_headers_list = data.columns.tolist()
    assert len(colum_headers_list) == 5     
    assert colum_headers_list[0] == (("Close", "GOOG"))
    assert colum_headers_list[1] == ("High", "GOOG")
    assert colum_headers_list == [('Close', 'GOOG'), ('High', 'GOOG'), ('Low', 'GOOG'),('Open', 'GOOG'),('Volume', 'GOOG')]


def test_retrieve_company_info():
    info = retrieve_company_info("AAPL")
    assert info["displayName"] == "Apple"
    assert info["state"] == "CA"

    info = retrieve_company_info("TSLA")
    assert info["country"] == "United States"
    assert info["symbol"] == "TSLA"
    assert info["industryDisp"] == "Consumer Electronics" or info["industryDisp"] == "Auto Manufacturers"

def test_retrieve_stocks_financials():
    financials = retrieve_stocks_financials("AAPL")
    latest_expense = financials.iloc[1]
    assert latest_expense > 0
    assert len(financials) == 5  

    financials = retrieve_stocks_financials("TSLA")
    latest_expense = financials.iloc[1]
    assert latest_expense > 0
    assert len(financials) == 5  


    
pytest.main(["-v", "--tb=line", "-rN", __file__])
