import json
from time import sleep

import requests

URL_ALL = 'https://economia.awesomeapi.com.br/all'
URL_MOEDA = 'https://economia.awesomeapi.com.br/all'


def parsing(moeda):
    try:
        resposta = requests.get('{}/{}'.format(URL_MOEDA, moeda))
        if resposta:
            texto = resposta.text
            if texto:
                conversao = json.loads(texto)
                return conversao
    except:
        print('erro')


def mostrar_moeda(moeda):

    try:
        dict = parsing(moeda)
        if dict:
            chave = dict[moeda]
            code = chave['code']
            codein = chave['codein']
            name = chave['name']
            bid = chave['bid']
            ask = chave['ask']
            high = chave['high']
            low = chave['low']
            varbid = chave['varBid']
            print('## MOEDA: {} - {} / {}  ##'.format(code, codein, name))
            print('## BID: {} # ASK: {} ##'.format(bid, ask))
            print('## HIGH: {} # LOW: {} ##'.format(high, low))
            print('## varBid:  -0.02  ##'.format(varbid))
    except Exception as e:
        print(e)


if __name__ == '__main__':

    try:
         moeda = input('Digite uma moeda para fazer cotação: ')
         while moeda:
             print(mostrar_moeda(moeda))
             for contagem in range(0, 5):
                sleep(5)
             print(mostrar_moeda(moeda))
    except Exception as e:
        print(e)

