import requests
import re
import argparse

URL = "http://api.nbp.pl/api/exchangerates/rates/c/{code}/today/"


def get_args():
    arguments_parser = argparse.ArgumentParser(description="Argument parser for currency code")
    arguments_parser.add_argument('--code',
                           action='store', type=str, required=True, help='Currency code - 3 letters long string')
    args = arguments_parser.parse_args()
    code = args.code
    code = str(code).lower()
    currency_list = ['usd','aud','cad','eur','huf','chf','gbp','jpy','czk','dkk','nok','sek','xdr']
    if code not in currency_list:
        exit(f'''Currency code is not valid. It has to be 3 letters long. Also please make sure it follows ISO 4217: 
        https://pl.wikipedia.org/wiki/ISO_4217 and is within the list of available currrencies {currency_list}''')
    return code


def get_ex_rate():
    code = get_args()
    r = requests.get(url=URL.format(code=code),headers={'Accept': 'application/json'})
    if r.status_code == 404:
        exit('Invalid currency code or table is not published yet.\n'
             'Please stick to ISO 4217: https://pl.wikipedia.org/wiki/ISO_4217')
    data = r.json()
    round_up = lambda x: round(x,2)
    ex_rate_bid = round_up(data['rates'][0]['bid'])
    ex_rate_ask = round_up(data['rates'][0]['ask'])

    print(f'1 {code.upper()} bid price is {ex_rate_bid} PLN \n1 {code.upper()} ask price is {ex_rate_ask} '
          f'PLN \n ')


if __name__ == '__main__':
    get_ex_rate()