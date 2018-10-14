#!/usr/bin/env python

import math

inf = open("in.txt", "r")
outf = open("out.txt", "w")

count = int(inf.readline())
j=0

for j in range(1, count + 1):
    print "caso", j
    
    line = inf.readline()[:-1].split()
    
    comb=[]
    oppos=[]
    
    for i in range(1, int(line[0]) +1):
        comb.append(list(line[i]))
        
    for i in range(0, int(line[len(comb) + 1])):
        oppos.append(list(line[len(comb) + 2 + i]))
  
    string = line[len(comb) + len(oppos) + 3]
    invkL=[]
    print "str:",string
    element = string [0]
    string = string[1:]
    invkL.append(element)
    
    print "comb:", str(comb)
    print "opp:", str(oppos)
    print "invkL=", str(invkL)
    for i in range(0, len(string)):
        element = string [0]
        string = string[1:]
        invkL.append(element)
        
        combinado = False
        
        for combinador in comb:

            if combinador[:2] == invkL[-2:] or combinador[1::-1] == invkL[-2:]:

                invkL=invkL[:-2]
                invkL.append(combinador[2])
                combinado = True
                break
                
        if not combinado:

            for opuesto in oppos:
                print opuesto[1::-1]
                print invkL[-2:]
                print opuesto[1::-1] == invkL[-2:]
                try:
                    invkL.index(opuesto[0])
                    invkL.index(opuesto[1])
                    invkL=[]
                    break
                except ValueError:
                    pass

        print "invkL=", str(invkL)
    outf.write("Case #" + str(j) + ": [") 
    
    for op in range(0, len(invkL)):
        outf.write(invkL[op])
        if  op <> len(invkL) - 1:
            outf.write(", ")
    
    outf.write("]\n")

    print
print "listo si esto es igual a 0, esto =",len(inf.readline())
