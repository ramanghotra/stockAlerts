import requests
from twilio.rest import Client

# Enter stock ticker followed by stock name here for all stocks you want to receive notifications on
stock_dic = {"TSLA": "Tesla", "AAPL": "Apple", "GME": "Gamestop", "ARKK": "Ark"}
stock_symbols = stock_dic.keys()

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "" # Enter alphavantage api key here
NEWS_API_KEY = "" # Enter newapi key here
TWILIO_SID = "" # Enter twilio SID here
TWILIO_AUTH = "" # Enter twilio key here
VIRTUAL_TWILIO_NUMBER = "+" # Enter twilio number here
VERIFIED_NUMBER = "+" # Enter receiving number here

for symbol in stock_symbols:

    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)

    data = response.json()["Time Series (Daily)"]

    data_list = [value for (key, value) in data.items()]

    yesterday = data_list[0]
    yesterday_close = yesterday["4. close"]

    day_before = data_list[1]
    day_before_close = day_before["4. close"]

    difference = float(yesterday_close) - float(day_before_close)
    if difference > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    diff_percent = (difference / float(yesterday_close)) * 100

    if abs(diff_percent) > 0:
        news_params = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": stock_dic[symbol],
        }
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]

        #### CHANGE NUMBER OF ARTICLES RECEIVED HERE
        three_articles = articles[:1]

        articles_formatted = [
            f"         \n{stock_dic[symbol]}: {up_down} {diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
            for article in
            three_articles]

        client = Client(TWILIO_SID, TWILIO_AUTH)

        for article in articles_formatted:
            message = client.messages.create(
                body=article,
                from_=VIRTUAL_TWILIO_NUMBER,
                to=VERIFIED_NUMBER
            )
