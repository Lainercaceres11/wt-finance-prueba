from requests import Request, Session
#Importamos librerias
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time

#Indicamos la url
url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#Indican desde donde inician hasta donde terminan, ademas de la moneda
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}

#Contiene la api key y la acceptacion de los archivos json
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'e00824f0-6fa2-48d2-a5a3-fee7e5e1468a',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
