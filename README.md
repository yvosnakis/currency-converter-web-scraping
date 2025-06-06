# Real-Time Currency Converter using Web Scraping

This is a Python-based desktop application for real-time currency conversion, developed as part of my dissertation project. It scrapes live exchange rate data from [x-rates.com](https://www.x-rates.com) and provides users with an intuitive interface to convert between multiple currencies. This application offers an alternative to paid APIs, making it ideal for personal or educational use.

## Features

- Real-time exchange rates retrieved via web scraping.
- Graphical user interface (GUI) built with PySide6 and/or PyQt6.
- Multiple currency support, with country flags and dropdown menus.
- Error handling for user input and connection issues.
- Comparison with a static rate version (more in my dissertation).

## Technologies Used

- Python
- PySide6 / PyQt6 – GUI development
- BeautifulSoup – Web scraping
- Requests – HTTP requests
- Qt Designer – UI design

## Getting Started

### Prerequisites

Ensure you have Python 3 installed, along with the required libraries:

```bash
pip install PySide6 PyQt6 beautifulsoup4 requests
```

### Running the Application

To run the real-time currency converter:

```bash
python main.py
```

This will launch the application window. Input the amount, select source and target currencies, and click "Get Exchange Rate" to view the result.


## Legal and Ethical Use

This project uses web scraping for educational purposes only. Please review the terms of service of any scraped websites and ensure compliance. The x-rates.com data was used under fair use assumptions for non-commercial academic research.

## Background

This application was developed for the dissertation:
> Comparative Analysis of Web Scraping Techniques for Real-Time Exchange Rates in Currency Conversion Applications

The research explores the advantages and limitations of web scraping versus static data methods and APIs in financial contexts.

## Future Enhancements

- Replace web scraping with an API for improved reliability
- Support more currencies
- Add historical data charts
- Handle website layout changes dynamically

## License

This project is for academic and personal use only. Redistribution or commercial use is not permitted without consent.
