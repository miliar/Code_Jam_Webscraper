from os import sys

def turn(cadena, x, n):
    if(x+n>len(cadena)):raise IndexError
    cadena = cadena[:x] + cadena[x:x+n].replace('-', 'l') + cadena[x+n:]
    cadena = cadena[:x] + cadena[x:x+n].replace('+', '-') + cadena[x+n:]
    cadena = cadena[:x] + cadena[x:x+n].replace('l', '+') + cadena[x+n:]
    return cadena

def revenge(cadena, n):
    cant = 0
    for x in range(len(cadena)):
        if(cadena[x]=='-'):
            cant += 1
            cadena = turn(cadena, x, n)
    return cant


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  entrada = input().split(" ")# read a list of integers, 2 in this case
  try:
      print("Case #{}: {} ".format(i, revenge(entrada[0],int(entrada[1]))))
  except IndexError:
      print("Case #{}: IMPOSSIBLE ".format(i))
