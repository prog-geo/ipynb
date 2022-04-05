# -*- coding: utf-8 -*-
"""exercicio-04

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/188RUT7UoLHHe2WNa7rphkB0xvNC6A9gH
"""

R = 6373.0

lat1 = math.radians(-26.901004)
lon1 = math.radians(-48.673679)
lat2 = math.radians(-27.596861)
lon2 = math.radians(-48.452317)

dlon = lon2 - lon1

dlat = lat2 - lat1

a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
distance = R * c

print("lat1:" , lat1)
print("lon1:" , lon1)
print("lat2:" , lat2)
print("lon2:" , lon2)
print(distance)