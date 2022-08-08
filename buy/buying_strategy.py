import sys

from buy.buy_cripto import BuyCripto

from api_callling.api_calling import APICall

from main.all_variable import Variable

from real_time_data.real_time_data import RealTimeData


class BuyingStrategy(RealTimeData, BuyCripto):

    def buying_condition(self, symbol):
        avg_price = APICall.client.get_avg_price(symbol=symbol)
        finding_price = float(avg_price['price'])
        Buying_condition = True
        lowest_price = []
        while Buying_condition:
            self.streamKline(currency=symbol.lower(), interval="1m")
            current_price = float(RealTimeData.append_currency[-1])
            if len(lowest_price) == 0:
                lowest_price.append(current_price)
            if current_price < lowest_price[-1]:
                lowest_price.append(current_price)
            lowest_price_main =float(lowest_price[-1])
            decrease_price_with_stop_loss = float(lowest_price_main) + (
                    float(lowest_price_main) * Variable.BUYING_STOP_LOSS)
            total_find = Variable.DOLLAR / finding_price
            total_current = Variable.DOLLAR / current_price
            total_buying_point = Variable.DOLLAR / decrease_price_with_stop_loss
            print("------------------------------------")
            print(f"|   Try to Buy {symbol} Currency   |")
            print("------------------------------------")
            print(f"{finding_price} & Total {total_find} FINDING PRICE")
            print(f"{current_price} & Total {total_current} CURRENT PRICE")
            print(f"{lowest_price_main} & Total {Variable.DOLLAR/lowest_price_main} DOWN PRICE")
            print(f"\n{decrease_price_with_stop_loss} & Total {total_buying_point} BUYING POINT\n")
            if decrease_price_with_stop_loss <= current_price:
                self.coin_buy(symbol=symbol)
                print(input("Buy Done :"))
                Buying_condition = False


currency_symbol = Variable.CRIPTO_SYMBOL
BuyingStrategy().buying_condition(currency_symbol)

