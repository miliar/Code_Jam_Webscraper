#!/usr/bin/env python

import itertools

file = open("C-small-attempt1.in")

numcases = int(file.readline().rstrip())
cases = file.read().split("\n")
cases = map(lambda i: cases[i],filter(lambda i: i%2 == 1,range(len(cases))))
for index, case in enumerate(cases):
    case = case.split()
    cases[index] = map(int, case)

def patrick(candylist):
    rezultat = 0
    for candy in candylist: rezultat ^= candy
    return rezultat
    
def sean(candylist):
    rezultat = 0
    for candy in candylist: rezultat += candy
    return rezultat

def shift(l, n):
    return l[n:] + l[:n]

final = ""
for indextop, case in enumerate(cases):
    rezultati = []
    tempcase = []
    for i in range(len(case)):
        tempcase.append(shift(case,i))
        
    for perm in tempcase:
        for index in range(len(perm)):
            if index != 0:
                if patrick(perm[:index]) == patrick(perm[index:]):
                    rezultati.append((perm, index))
    
    if len(rezultati) == 0:
        final += "Case #"+str(indextop+1)+": NO\n"
    else:
        candylist = []                
        for rezultat in rezultati:
            candylist.append(rezultat[0][rezultat[1]:])
            candylist.append(rezultat[0][:rezultat[1]])
        
        rez = map(sean, candylist)
        final += "Case #"+str(indextop+1)+": "+str(max(rez))+"\n"
    
file = open("candyrezultat.txt", "w")
file.write(final.rstrip())