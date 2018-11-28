#!/usr/bin/python

# python 3

def process(line):
    elems = line.split(" ")
    
    nonbase = []
    opposed = []
    num = int(elems[0])
    i = 1
    while i < num + 1:
        nonbase.append(elems[i])
        i += 1

    num = i + int(elems[i])
    i += 1
    while i < num + 1:
        opposed.append(elems[i])
        i += 1

    ulaz = elems[len(elems) - 1]
    lista = []
    koji = -1
    for u in ulaz:
        koji += 1
        jel = 1
        if len(lista) > 0:
            for nonb in nonbase:
                if (nonb[1] == u and nonb[0] == lista[koji - 1]) or (nonb[0] == u and nonb[1] == lista[koji - 1]):
                    lista[koji - 1] = nonb[2]
                    koji -= 1
                    jel = 0
                    break

        if jel == 1:
            lista.append(u)

        for opp in opposed:
            if opp[0] in lista and opp[1] in lista:
                lista = []
                koji = -1
    
    return lista

# main
cases = int(input())
case = 1
while case <= cases:
    linija = input()
    print("Case #" + str(case) + ": [", end="")
    out = process(linija)
    i = 0
    while i < len(out):
        print(out[i], end="")
        if i != len(out) - 1:
            print(", ", end="")

        i+=1

    print("]")

    case += 1

# vim: set ts=4 sw=4 et:
