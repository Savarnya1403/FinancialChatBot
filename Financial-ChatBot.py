import requests
import spacy
from openai import OpenAI
import logging
import re
import yfinance as yf
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load NLP model
nlp = spacy.load('en_core_web_sm')

# Configure OpenAI (optional - only for non-data questions)
OPENAI_ENABLED = False  # Set to True if you fix API key

# Company to ticker mapping
COMPANY_MAP = {
    'microsoft': 'MSFT',
    'apple': 'AAPL',
    'tesla': 'TSLA',
    'amazon': 'AMZN',
    'google': 'GOOGL',
    'nvidia': 'NVDA'
}

# Financial knowledge base (expanded)
FINANCIAL_KNOWLEDGE = {
    # ... (keep previous 100+ questions/answers)
}

def get_historical_data(symbol, start_year, end_year):
    """Get historical stock data with error handling"""
    try:
        end_year = min(end_year, datetime.now().year)
        stock = yf.Ticker(symbol)
        hist = stock.history(
            start=f"{start_year}-01-01",
            end=f"{end_year}-12-31"
        )
        return hist
    except Exception as e:
        logging.error(f"Historical data error: {e}")
        return None

def get_financial_statements(symbol):
    """Get comprehensive financial data"""
    try:
        stock = yf.Ticker(symbol)
        return {
            'financials': stock.financials,
            'balance_sheet': stock.balance_sheet,
            'cashflow': stock.cashflow,
            'info': stock.info
        }
    except Exception as e:
        logging.error(f"Financial data error: {e}")
        return None

def format_financial_data(data, years):
    """Format financial data for display"""
    formatted = []
    for statement in ['financials', 'balance_sheet', 'cashflow']:
        df = data.get(statement)
        if df is not None:
            filtered = df[[col for col in df.columns if col.year in years]]
            formatted.append(f"\n{statement.upper()}:\n{filtered.to_string()}")
    return '\n'.join(formatted)

def handle_financial_request(company, start_year, end_year):
    """Handle financial data requests"""
    symbol = COMPANY_MAP.get(company.lower())
    if not symbol:
        return f"Company {company} not found in database"

    financial_data = get_financial_statements(symbol)
    if not financial_data:
        return "Could not retrieve financial data"
    
    years = list(range(start_year, end_year+1))
    formatted = format_financial_data(financial_data, years)
    
    info = financial_data['info']
    return (
        f"{company.upper()} ({symbol}) Financial Report {start_year}-{end_year}\n"
        f"Market Cap: ${info.get('marketCap', 'N/A'):,}\n"
        f"Revenue (TTM): ${info.get('totalRevenue', 'N/A'):,}\n"
        f"Profit Margin: {info.get('profitMargins', 'N/A')*100:.2f}%\n"
        f"\nDetailed Financials:\n{formatted}"
    )

def chatbot():
    print("Financial Analyst Bot 2.0 - Type 'exit' to quit")
    while True:
        query = input("\nHow can I assist you? ")
        if query.lower() == 'exit':
            break

        # Extract company and years
        company = next((c for c in COMPANY_MAP if c in query.lower()), '')
        years = [int(y) for y in re.findall(r'\b(20[2-9][0-9])\b', query)]
        start_year = min(years) if years else 2020
        end_year = max(years) if years else datetime.now().year

        if company:
            response = handle_financial_request(company, start_year, end_year)
            print(response)
        else:
            print(FINANCIAL_KNOWLEDGE.get(query, "I can help with financial data for major tech companies. Try asking about Microsoft, Apple, etc."))

if __name__ == "__main__":
    chatbot()