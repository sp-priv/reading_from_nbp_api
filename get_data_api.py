from pandas.io.json import json_normalize
import requests


def get_currency():
    code = input("Type currency that you would like to to exchange rate for (3 characters) \n")
    code = code.lower()
    return code


def get_ex_rate():
    code = get_currency()
    table = 'a'
    # code = 'chf'
    URL = "http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/?format=json".format(table=table,code=code)
    r = requests.get(url = URL)
    data = r.json()
    rates = json_normalize(data['rates'])
    ex_rate = rates['mid'][0]
    print(f'1 {code.upper()} equals {ex_rate} in PLN')
    return ex_rate


if __name__ == '__main__':
    get_ex_rate() 