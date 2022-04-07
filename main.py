import requests
import json
import keyring      # or whatever credential manager you fancy

USERNAME = 'USERNAME'
PASSWORD = keyring.get_password('amex_password', USERNAME)
TOKEN = keyring.get_password('amex_token', USERNAME)    # view README for this

cookie = {
    'url': 'https://global.americanexpress.com/myca/logon/us/action/login',
    'payload': f'Logon=Logon&UserID={USERNAME}&Password={PASSWORD}',
    'headers': {
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
    }
}

transactions = {
    'url': 'https://global.americanexpress.com/api/servicing/v1/financials/transactions',
    'querystring': {
        'limit': '1000',
        'offset': '0',
        'start_date': '2021-10-06',
        'end_date': '2022-04-06',
        'extended_details': 'merchant, category',
        'status': 'posted'
    },
    'headers': {
        'account_token': TOKEN
    }
}


with requests.Session() as s:
    # Initial request to set cookies
    s.request('POST', cookie['url'], data=cookie['payload'], headers=cookie['headers'])

    # Main request to retrieve data
    response = s.request('GET', transactions['url'], headers=transactions['headers'], params=transactions['querystring']).json()

    print(json.dumps(response, indent=4))
