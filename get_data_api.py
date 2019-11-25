import requests
import re
import argparse

URL = "http://api.nbp.pl/api/exchangerates/rates/c/{code}/today/"


def get_args():
    my_parser = argparse.ArgumentParser(description="Argument parser for currency code")
    my_parser.add_argument('--code',
                           action='store', type=str, required=True, help='Currency code - 3 letters long string')
    args = my_parser.parse_args()
    code = args.code
    code = str(code).lower()
    if not re.match(r'^[a-z]{3}$',code):
        exit('Currency code is not valid. It has to be 3 letters long. Also please make sure it follows '
             'ISO 4217: https://pl.wikipedia.org/wiki/ISO_4217'
             ' \n')
    return code


def get_ex_rate():
    global URL
    code = get_args()
    r = requests.get(url=URL.format(code=code),headers={'Accept': 'application/json'})
    if r.status_code == 404:
        exit('Invalid currency code or table is not published yet.'
             'Please stick to ISO 4217: https://pl.wikipedia.org/wiki/ISO_4217')
    data = r.json()
    ex_rate_bid = round(data['rates'][0]['bid'], 2)
    ex_rate_ask = round(data['rates'][0]['ask'], 2)
    print(f'1 {code.upper()} bid price is {ex_rate_bid} PLN \n1 {code.upper()} ask price is {ex_rate_ask} '
          f'PLN \n ')


if __name__ == '__main__':
    try:
        get_ex_rate()
    except Exception as e:
        print("type error: " + str(e))
