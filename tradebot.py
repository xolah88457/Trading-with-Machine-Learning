from lumibot.brokers import Alpaca
from lumibot.backtest import YahooDataBacktesting
from lumibot.strategies.Strategy import Strategy
from lumibot.traders import
from datetime import datetime

API_KEY = "..."
API_SECRET = "..."
BASE_URL = "..."

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

class MLStrat(Strategy):
    def initialize(self, symbol:str="SPY"):
        self.symbol = symbol
        self.sleep_time = "24H"
        self.last_trade = None
        
    def on_trading_iteration(self):
        self.set_universe(["AAPL", "MSFT", "GOOG", "AMZN"])
        self.set_broker(Alpaca(ALPACA_CREDS))
        self.set_trader(MLTrader())
        self.set_backtester(YahooDataBacktesting())

start_date = datetime(2024, 1, 25)
end_date = datetime(2023, 11, 25)

broker = Alpaca(ALPACA_CREDS)

strategy = MLStrat(name="MLStrat", broker=broker, 
                   parameters={"symbol": "SPY"})

strategy.backtest(start_date, end_date,
                  YahooDataBacktesting,
                  parameters={"symbol": "SPY"})
