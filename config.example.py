# Configuration Example

# Server
HOST = '0.0.0.0'
PORT = 5000
DEBUG = False

# Database
DATABASE_PATH = 'trading_bot.db'

# Trading
AUTO_TRADING = True
TRADING_INTERVAL = 180  # seconds
COINS = ['BTC', 'ETH', 'SOL', 'BNB', 'XRP', 'DOGE']

# Market Data
MARKET_API_CACHE = 5  # seconds
MARKET_API_URL = 'https://api.coingecko.com/api/v3'

# Refresh Rates (frontend)
MARKET_REFRESH = 5000  # ms
PORTFOLIO_REFRESH = 10000  # ms
TRADE_FEE_RATE = 0.001  # 交易费率：0.1%（双向收费）

