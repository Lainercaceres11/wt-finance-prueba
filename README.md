# wt-finance-prueba
Pasos para consumir api
1. Importar librerias 
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
2. Indicar la url
url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
3. Indicar los parametros de la api key 
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}
4. Aceptacion de archivos json y api a utilizar
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'e00824f0-6fa2-48d2-a5a3-fee7e5e1468a',
}

5. Seccion 
session = Session()
session.headers.update(headers)

6. Obtener, leer e imprimir datos de la api key 
try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
  Resultado en formato JSON

![api_key](https://user-images.githubusercontent.com/81586887/171090753-d0ec7773-fa67-4df8-8bcf-26c0bdb15e91.png)

