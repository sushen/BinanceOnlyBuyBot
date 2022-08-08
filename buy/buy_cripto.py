# import time
from pprint import pprint

from main.all_variable import Variable

from api_callling.api_calling import APICall

# from error_handleing.round import PriceRound

from email_option.sending_mail import MailSender


class BuyCripto:
    def round_symbol_price(self, currency):

        avg_price = APICall.client.get_avg_price(symbol=currency)
        amount_of_usd = Variable.DOLLAR
        round_with_usd = float(amount_of_usd) / float(avg_price['price'])

        if round_with_usd >= 10:
            dollar_convert = round(round_with_usd)
            print(f"{dollar_convert} is bigger than 10")
        elif round_with_usd >= 1:
            dollar_convert = round(round_with_usd, 2)
            print(f"{dollar_convert} is bigger than 1")
        elif round_with_usd < 0.006:
            str_currency = str(round_with_usd)
            currency = str_currency[:7]
            dollar_convert = float(currency)
            print(f"{dollar_convert} is smaller than 0.0006")
        elif round_with_usd < 0.6:
            print(round_with_usd)
            dollar_convert = round(round_with_usd, 2)
            print(f"{dollar_convert} is smaller than 0.6")
        elif round_with_usd < 1:
            dollar_convert = round(round_with_usd, 4)
            print(f"{dollar_convert} is smaller than 1")
        elif round_with_usd < .005:
            dollar_convert = round(round_with_usd, 5)
            print(f"{dollar_convert} is smaller than 0.005")

        print(dollar_convert)
        # print(input("_____:"))
        return dollar_convert

    def coin_buy(self, symbol):
        qty = self.round_symbol_price(symbol)
        order = APICall.client.order_market_buy(
            symbol=symbol,
            quantity=qty,
        )
        # try:
        #     order = APICall.client.order_market_buy(
        #         symbol=currency_symbol,
        #         quantity=qty,
        #     )
        # except:
        #     print("Exception IN ")
        #     time.sleep(2)
        #     qty = PriceRound.buy_error_round(self, currency_symbol)
        #     order = APICall.client.order_market_buy(
        #         symbol=currency_symbol,
        #         quantity=qty,
        #     )

        self.order_buying_price = float(order['fills'][0]['price'])
        receiver_mail = Variable.MAIL
        sender = MailSender()

        email_subject = f"We Buy {self.order_buying_price} coin"
        email_body = f"{order}"

        sender.send_mail(receiver_mail, email_subject, email_body)
        print(f'{email_subject}\n\n {email_body}')
        pprint(order)


# currency_symbol = 'SLPBUSD'
# Buy().coin_buy(currency_symbol)


