from re import compile
from sys import stdin

partes = stdin.readline().split(' ')
L = int(partes[0])
D = int(partes[1])
N = int(partes[2])

palabras = ["" for i in range(0, D)]
for i in range(0, D):
    palabras[i] = stdin.readline().replace("\n", "")

for i in range(0, N):
    pattern = stdin.readline().replace("(", "[").replace(")", "]").replace("\n", "")
    total = 0
    m = compile(pattern)
    for j in range(0, D):
        if m.match(palabras[j]) != None:
            total += 1
    print "Case #%d:%2d" % (i+1, total)
