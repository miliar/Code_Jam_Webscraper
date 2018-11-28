#! /usr/bin/env python

import sys

if len(sys.argv) < 3:
    exit()

       
filein = sys.argv[1]
fileout = sys.argv[2]

fin = file(filein)
fout = file(fileout,'w')

N = int(fin.readline())

for case in range(N):
    T = int(fin.readline())
    NA, NB = fin.readline().split()
    NA = int(NA)
    NB = int(NB)
    Aarrivals = []
    Adepartures = []
    Barrivals = []
    Bdepartures = []
    for i in range(NA):
        s = fin.readline()
        a,b = s.split()
        x,y = a.split(':')
        leave = int(x)*60+int(y)
        x,y = b.split(':')
        arrive = int(x)*60+int(y)+T
        Aarrivals.append(arrive)
        Adepartures.append(leave)
    for i in range(NB):
        s = fin.readline()
        a,b = s.split()
        x,y = a.split(':')
        leave = int(x)*60+int(y)
        x,y = b.split(':')
        arrive = int(x)*60+int(y)+T
        Barrivals.append(arrive)
        Bdepartures.append(leave)
    Adepartures.sort()
    Aarrivals.sort()
    Bdepartures.sort()
    Barrivals.sort()

    for d in Adepartures:
        for a in Barrivals:
            if a <= d:
                Barrivals.remove(a)
                NA -= 1
                break

    for d in Bdepartures:
        for a in Aarrivals:
            if a <= d:
                Aarrivals.remove(a)
                NB -= 1
                break

    fout.write('Case #%d: %d %d\n' % ((case+1),NA, NB))

fin.close()
fout.close()

