# -*- coding: utf-8 -*-
"""exercicio-04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13j5WKsJMNZJTFT2wKwn6UeQJkMcYlDSL
"""

import math

lat1 = float(input("Digite a latitude em grau-decimal do ponto 1: "))
lon1 = float(input("Digite a longitude em grau-decimal do ponto 1: "))

lat2 = float(input("Digite a latitude em grau-decimal do ponto 2: "))
lon2 = float(input("Digite a longitude em grau-decimal do ponto 2: "))

#passando grau decimal para radianos
lat1 = lat1 * math.pi / 180.0
lon1 = lon1 * math.pi / 180.0
lat2 = lat2 * math.pi / 180.0
lon2 = lon2 * math.pi / 180.0

dist12 = 2 * 6371 * math.asin (math.sqrt(math.pow(math.sin((lat2 - lat1) / 2), 2) + 
                                         (math.cos(lat1) * math.cos(lat2) * 
                                         (math.pow(((lon2 - lon1) / 2), 2)))))

print("A distância entre os dois pontos é: ", dist12)