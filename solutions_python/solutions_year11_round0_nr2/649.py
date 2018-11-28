#!/usr/bin/env python

# Google code jam 2011 : Magicka

import sys

def fpr(l):
    s = '['
    for k in range(len(l)):
        e = l[k]
        if k < len(l)-1:
            s += e+', '
        else:
            s += e
    s += ']'

    return s

def result(comb,opp,invok):
    el_list = []
    while invok != []:
        cur = invok[0]
        invok = invok[1:]
        if el_list != []:
            if el_list[-1]+cur in comb:
                el_list[-1] = comb[el_list[-1]+cur]
                continue
            else:
                fl = False
                for e in el_list:
                    if e+cur in opp:
                        el_list = []
                        fl = True
                        break
                if not fl:
                    el_list.append(cur)
        else:
            el_list.append(cur)

    return fpr(el_list)

p = int(sys.stdin.readline())
for s in range(1,p+1):
    line = sys.stdin.readline()

    # combinations
    c,_,line = line.partition(' ')
    c = int(c)
    comb = {}
    for i in range(c):
        co,_,line = line.partition(' ')
        comb[co[0:2]] = co[2]
        comb[(co[0:2])[::-1]] = co[2]

    # oppositions
    d,_,line = line.partition(' ')
    d = int(d)
    opp = {}
    for i in range(d):
        op,_,line = line.partition(' ')
        opp[op] = 1
        opp[op[::-1]] = 1

    # invok
    n,_,line = line.partition(' ')
    n = int(n)
    invok = []
    for k in range(n):
        invok.append(line[k])

    print("Case #" + str(s) + ": " +  result(comb,opp,invok))

