#! /usr/bin/env python

import sys

filein = sys.argv[1]
fileout = sys.argv[2]
fin = file(filein)
fout = file(fileout,'w')

T = int(fin.readline())

for i in range(1,T+1):
    t = int(fin.readline())
    v1 = fin.readline().split()
    v2 = fin.readline().split()
    for j in range(len(v1)):
        v1[j] = int(v1[j])
        v2[j] = int(v2[j])
    v1.sort()
    v2.sort()
    v2.reverse()
    sum = 0
    for m in range(len(v1)):
        sum += v1[m]*v2[m]

    fout.write('Case #%d: %d\n'%(i,sum))

fin.close()
fout.close()
