#!/usr/bin/python

# python 3

def simulate(popis):
    trenutno = "";
# position
    o_p = 1
    b_p = 1
# koraci
    o_k = 0
    b_k = 0

    out = 0
    for korak in popis:
        if trenutno != korak[0]:
            trenutno = korak[0]

            if trenutno == "O":
                o_k = 0
                pomak = abs(int(korak[1:]) - o_p)
                b_k -= pomak
                if b_k < 0:
                    o_k = abs(b_k) + 1
                    out += abs(b_k) + 1
                    b_k = 0
                else:
                    o_k = 1
                    out += 1
                o_p = int(korak[1:])
            else:
                b_k = 0
                pomak = abs(int(korak[1:]) - b_p)
                o_k -= pomak
                if o_k < 0:
                    b_k = abs(o_k) + 1
                    out += abs(o_k) + 1
                    o_k = 0
                else:
                    b_k = 1
                    out += 1
                b_p = int(korak[1:])
        else:
            if trenutno == "O":
                pomak = abs(int(korak[1:]) - o_p) + 1
                o_k += pomak
                out += pomak
                o_p = int(korak[1:])
            else:
                pomak = abs(int(korak[1:]) - b_p) + 1
                b_k += pomak
                out += pomak
                b_p = int(korak[1:])

    return out


def process(line):
    elems = line.split(" ")
    num = int(elems[0])

    popis = []
    i = 1
    while i < len(elems):
        popis.append(elems[i] + elems[i + 1])
        i += 2

    return simulate(popis)

cases = int(input())
case = 1
while case <= cases:
    linija = input()
    print("Case #" + str(case) + ": " + str(process(linija)))
    case += 1

# vim: set ts=4 sw=4 et:
