intrare = open("B-small-attempt.in", "r")
out = open("Output.txt", "w")

T = int(intrare.readline())#Numarul de cazuri
for caz in range(1, T+1):
    abk = intrare.readline()[:-1]
    abk = [int(x) for x in abk.split(' ')]
    a, b, k = abk
    p = []
    for x in range(a):
        for y in range(b):
            p.append(x&y)
    pFiltrat = []
    for element in p:
        if element < k:
            pFiltrat.append(element)
    #print(len(pFiltrat))
    raspuns = "Case #" + str(caz) + ": " + str(len(pFiltrat))+"\n"
    out.write(raspuns)
