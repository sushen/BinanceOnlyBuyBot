import os
import time

from binance.client import Client

from email_option.sending_mail import MailSender
from main.all_variable import Variable

gmail = Variable.MAIL
receiver_mail = gmail
message = f'Check you heruku for get exception .'

api_key = os.environ.get('binance_api_key')
api_secret = os.environ.get('binance_api_secret')


class APICall:
    client = Client(api_key, api_secret)



