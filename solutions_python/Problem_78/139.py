#!/usr/bin/env python

import sys

filename = sys.argv[1]
fin = open(filename, 'r')
T = int(fin.readline())

fout = open("output", 'w') 

factors = [1, 2, 4, 5, 10, 20, 25, 50, 100]

for i in range(T):
    l = fin.readline().split()
    N = int(l[0])
    Pd = int(l[1])
    Pg = int(l[2])

    if ((Pg==0)and(Pd!=0)) or ((Pg==100)and(Pd!=100)):
        fout.write("Case #" + str(i+1) + ": " + "Broken\n")
        continue     
    
    D = 0
    for f in factors:
        if f>N: break
        if ((f*Pd)%100)==0:
            D = f
            break
    if D==0:
        fout.write("Case #" + str(i+1) + ": " + "Broken\n")
        continue  

    G = 0
    for f in factors:
        if ((f*Pg)%100)==0:
            G = f
            break
    if G==0:
        fout.write("Case #" + str(i+1) + ": " + "Broken\n")
        continue  

    fout.write("Case #" + str(i+1) + ": " + "Possible\n")
        
    
