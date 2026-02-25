import yfinance as yf
.\Scripts\activate
# 台股代碼需加上 .TW (上市) 或 .TWO (上
stock_id = "2330.TW"
tsmc = yf.Ticker(stock_id)

# 取得最新一筆交易資料
data = tsmc.history(period="1d")
latest_price = data['Close'].iloc[-1]

print(f"台積電 (2330) 最新收盤價: {latest_price}")
