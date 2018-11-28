from math import pi
from itertools import combinations

# file = open("A-small-attempt0.in", "r")
# t = int(file.readline().strip("\n"))
t = int(input().strip())
# file_out = open("output.out", "w")

risultato = ""
for m in range(t):        
    pancake = dict()
    lista_pancake = []
    # n, k = [int(x) for x in file.readline().strip("\n").split(" ")]
    n, k = [int(x) for x in input().strip().split(" ")]
    for i in range(n):
        # r, h = [int(x) for x in file.readline().strip("\n").split(" ")]
        r, h = [int(x) for x in input().strip().split(" ")]
        pancake["r"] = r
        pancake["a_lat"] = 2 * r * pi * h
        pancake["a_sup"] = r ** 2 * pi
        lista_pancake.append(dict(pancake))
    lista_pancake = sorted(lista_pancake, key=lambda k: (-k["r"], -k["a_lat"]))
    massimo = 0
    for combinazione in combinations(lista_pancake, k):
        somma = combinazione[0]["a_sup"]
        for pancake in combinazione: somma += pancake["a_lat"]
        if somma > massimo: massimo = somma
    risultato += "Case #" + str(m + 1) + ": " + str(massimo) + ("\n" if m != t - 1 else "")
        
print(risultato)
# file_out.write(risultato)
# file_out.close()
