import requests
import datetime

global_url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?convert=INR'

request = requests.get(global_url, headers={'X-CMC_PRO_API_KEY': 'Your_API_Key'})
results = request.json()
# print(json.dumps(result, sort_keys=True, indent=4))

active_cryptocurrencies = results['data']['active_cryptocurrencies']
active_market_pairs = results['data']['active_market_pairs']
btc_dominance = results['data']['btc_dominance']
last_updated = results['data']['last_updated']
global_cap = results['data']['quote']['INR']['total_market_cap']
global_volume = results['data']['quote']['INR']['total_volume_24h']

active_cryptocurrencies_string = '{:,}'.format(active_cryptocurrencies)
active_market_pairs_string = '{:,}'.format(active_market_pairs)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)
last_updated_string = datetime.datetime.strptime(last_updated, "%Y-%m-%dT%H:%M:%S.%fZ")

print()
print('The are currently ' + active_cryptocurrencies_string + ' active cryptocurrencies and ' + active_market_pairs_string + ' active market pairs.')
print('The global cap of all cryptos is ' + global_cap_string + ' and the 24h volume is ' + global_volume_string + '.')
print('Bitcoin\'s total percentage of the global cap is ' + str(btc_dominance) + '%.')
print('This information was last updated on ' + str(last_updated_string) + '.')
