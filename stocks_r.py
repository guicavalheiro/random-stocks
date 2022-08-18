import pandas as pd
import yfinance as yf

import json
import random

from yahoofinancials import YahooFinancials

"""
ABORDAGEM

A cada segunda-feira da semana, terei 100 reais de budget para investir.
Será sorteado 10 ações, onde irei investir 10 reais em cada.

O objetivo é analisar o quão eficiente é uma escolha aleatória comparada com um
fundo de investimentos.

Existirão duas práticas:

Prática A) Não irei vender nenhuma ação, para analisar no fim do ano quanto o dinheiro rendeu.
Prática B) A cada semana que se iniciar, eu vendo as ações da semana anterior, acumulando os lucros/prejuízos.

A análise será feita em cima dos dados da B3/2021

"""

class Carteira:

    def __init__(self):
        
        self.budget_inicial = 100
        self.budget_atual = 0

        self.carteira = {}
        """
        'Ação':{
            dd/mm/aaaa:{
                'quantidade': valor investido / preço
                'valor investido': valor investido
            }
        }
        """

class Acoes:
    def __init__(self):
        f = open('stocks.json')
        self.acoes = json.load(f)
        f.close()
        
"""

Início da semana
    -> Sorteia 10 ações
    -> Compra 10 reais de cada
    -> Armazena as ações compradas e a quantidade comprada
    -> Repete o processo

"""



# for stock in stocks_name['stocks']:

#     try:
#         df = yf.download(stock, start="2021-01-01", end="2021-12-31")
#         print(f"Conseguiu baixar: {stock}")

#     except:
#         print(f"ERRO - Não conseguiu baixar: {stock} - ERRO")