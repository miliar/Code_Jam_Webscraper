#!/usr/bin/env python

import math

inf = open("in.txt", "r")
outf = open("out.txt", "w")

count = int(inf.readline())
j=0

for j in range(1, count + 1):
    print "caso", j
    inf.readline()
    line = inf.readline()[:-1]
    numeros = line.split()
    
    for i in range(0,len(numeros)):
        numeros[i]=int(numeros[i])

    sum = 0
    total = 0
    
    for i in numeros:
        sum = sum ^ i
        total += i
            

    
    if sum == 0:    
        numeros.sort()
        outf.write("Case #" + str(j) + ": " + str(total - numeros[0]) + "\n")
    else:
        outf.write("Case #" + str(j) + ": NO\n")
    print
print "listo si esto es igual a 0, esto =",len(inf.readline())
