# Financial Analyst Chatbot

A Python-based chatbot that provides financial data analysis, stock information, and answers to common financial questions using real market data and AI-powered responses.

## Features

- 📈 Real-time stock price lookup
- 📊 Historical financial data (2020-2025)
- 💰 Company financial statements (Income, Balance Sheet, Cash Flow)
- 📚 100+ predefined financial Q&A
- 🔍 Market terminology explanations
- 📉 Comparative financial analysis
- ⏳ Time-period specific queries

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/financial-chatbot.git
   cd financial-chatbot
Install required packages:

bash
Copy
pip install yfinance spacy requests beautifulsoup4
Download Spacy language model:

bash
Copy
python -m spacy download en_core_web_sm
(Optional) For AI-powered responses:

Get OpenAI API key from platform.openai.com

Add your key to the client = OpenAI(api_key="YOUR_KEY") line in the code

Usage
bash
Copy
python financial_chatbot.py
Example Queries
Input	Output Type
"Show Microsoft's 2023 balance sheet"	Financial Statements
"What's Tesla's current stock price?"	Real-time Price
"Compare Apple and Amazon market caps"	Comparative Analysis
"Explain short selling"	Definition
"Show NVIDIA's revenue growth 2020-2023"	Historical Trend
Commands
exit - Quit the chatbot

help - Show available command list

Supported Companies
Microsoft (MSFT)

Apple (AAPL)

Tesla (TSLA)

Amazon (AMZN)

Google (GOOGL)

NVIDIA (NVDA)

Troubleshooting
Common Issues
Missing Dependencies:

bash
Copy
pip install -r requirements.txt
Company Not Found:

Use exact company names from supported list

Example: "Microsoft" not "MS Corp"

Data Retrieval Errors:

Check internet connection

Verify date ranges (2020-current year)

API Errors:

For OpenAI issues: verify API key validity

Retry after 1 minute if Yahoo Finance times out

Limitations
Data delayed by 15 minutes for free Yahoo Finance API

Limited to 7 years historical data

Only supports major US-listed tech companies

Financial statements in USD only

Contributing
Fork the repository

Create feature branch:

bash
Copy
git checkout -b feature/new-feature
Commit changes

Push to branch

Open pull request

License
MIT License - See LICENSE file

Note: This tool provides financial information for educational purposes only. Never make investment decisions based solely on automated tools.

Copy

This README includes:

1. Clear installation instructions
2. Usage examples with sample queries
3. Troubleshooting guide for common issues
4. List of supported companies
5. Contribution guidelines
6. License information
7. Important disclaimers

You can customize the following sections as needed:
- Add more companies in "Supported Companies"
- Expand the predefined Q&A list
- Modify license terms
- Add specific contribution guidelines
- Include your contact information