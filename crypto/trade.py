import binance_config

from binance.client import Client
from binance.enums import *

api_key, secret = binance_config.load_api_keys()
client = Client(api_key, secret)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

# place a test market buy order, to place an actual order use the create_order function
order = client.create_test_order(
    symbol='BNBBTC',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)

# get all symbol prices
prices = client.get_all_tickers()

# withdraw 100 ETH
# check docs for assumptions around withdrawals
from binance.exceptions import BinanceAPIException, BinanceWithdrawException
try:
    result = client.withdraw(
        asset='ETH',
        address='<eth_address>',
        amount=100)
except BinanceAPIException as e:
    print(e)
except BinanceWithdrawException as e:
    print(e)
else:
    print("Success")

# fetch list of withdrawals
withdraws = client.get_withdraw_history()

# fetch list of ETH withdrawals
eth_withdraws = client.get_withdraw_history(asset='ETH')

# get a deposit address for BTC
address = client.get_deposit_address(asset='BTC')

# start aggregated trade websocket for BNBBTC
def process_message(msg):
    print(f"message type: {msg['e']}")
    print(msg)
    # do something

from binance.websockets import BinanceSocketManager
bm = BinanceSocketManager(client)
bm.start_aggtrade_socket('BNBBTC', process_message)
bm.start()

# get historical kline data from any date range

# fetch 1 minute klines for the last day up until now
klines = client.get_historical_klines(
    "BNBBTC",
    Client.KLINE_INTERVAL_1MINUTE,
    "1 day ago UTC")
print(f'1 minute klines: {klines}')

# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines(
    "ETHBTC",
    Client.KLINE_INTERVAL_30MINUTE,
    "1 Dec, 2017",
    "1 Jan, 2018")
print(f'30 minute klines: {klines}')

# fetch weekly klines since it listed
klines = client.get_historical_klines(
    "NEOBTC",
    Client.KLINE_INTERVAL_1WEEK,
    "1 Jan, 2017")
print(f'1 week klines: {klines}')
