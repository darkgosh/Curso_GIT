#Conetor test

import requests
from bs4 import BeautifulSoup

# URL de la página web de Binance con información sobre criptomonedas
url = "https://www.binance.com/es/markets"

# Realizar una petición GET a la URL
res = requests.get(url)

# Verificar si la petición es exitosa
# Esta linea solo es para generar cambio en GIT
if res.status_code == 200:
  # Parsear el contenido de la página web con BeautifulSoup
  soup = BeautifulSoup(res.content, "html.parser")

  # Extraer los datos de precios en tiempo real de las 4 criptomonedas
  prices = {}
  for crypto in ["Bitcoin", "Ethereum", "Ripple", "Litecoin"]:
    crypto_price = soup.find("td", string=crypto).find_next("td").text
    prices[crypto] = crypto_price

  # Imprimir los precios en tiempo real de las 4 criptomonedas
  print(prices)
else:
  # En caso de una petición no exitosa, imprimir un mensaje de error
  print("No se pudo recopilar los datos en tiempo real")
