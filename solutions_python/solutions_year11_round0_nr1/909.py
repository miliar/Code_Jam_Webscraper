#!/usr/bin/env python

import sys

filename = sys.argv[1]
f = open(filename, 'r')
T = int(f.readline())

fout = open("output", 'w') 

for i in range(T):
    l = f.readline().split()
    N = int(l[0])
    Bl = []
    Ol = []
    for j in range(N):
        if l[j*2+1]=='B':
            Bl.append((j, int(l[j*2+2])))
        else:
            Ol.append((j, int(l[j*2+2])))
    
    t = 0
    Bp = Op = 1
    bp = op = 0
    for j in range(N):
        if len(Bl)>=0 and bp<len(Bl) and Bl[bp][0]==j:
            x = Bl[bp][1]
            y = Ol[op][1] if len(Ol)>=0 and op<len(Ol) else Op
            bp += 1
            d = abs(x-Bp)
            Bp = x
            t += d + 1
            if (y > Op): Op = min(Op+d+1, y)
            elif (y < Op): Op = max(Op-d-1, y)
        elif len(Ol)>=0 and op<len(Ol) and Ol[op][0]==j:
            x = Ol[op][1]
            y = Bl[bp][1] if len(Bl)>=0 and bp<len(Bl) else Bp
            op += 1
            d = abs(x-Op)
            Op = x
            t += d + 1
            if (y > Bp): Bp = min(Bp+d+1, y)
            elif (y < Bp): Bp = max(Bp-d-1, y)
        else: print "something wrong!"
        
    fout.write("Case #" + str(i+1) + ": " + str(t) + "\n")

fout.close()
