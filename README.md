# Stock Text Alerts
Python script that will text you change in price close of user chosen stocks and will also send news articles.

In order to run script fill in missing portion at the top of the script:


  STOCK_API_KEY = "" # Enter alphavantage api key here
  
  
  NEWS_API_KEY = "" # Enter newsapi key here
  
  
  TWILIO_SID = "" # Enter twilio SID here
  
  
  TWILIO_AUTH = "" # Enter twilio key here
  
  
  VIRTUAL_TWILIO_NUMBER = "+" # Enter twilio number here
  
  
  VERIFIED_NUMBER = "+" # Enter receiving number here
  
  Update stock_dic with stocks you wish to receive updates about. (Format: tickersymbol:company name)
  
  Once done, run script.




Created using newsapi, alphavantage stock api, and twilio
