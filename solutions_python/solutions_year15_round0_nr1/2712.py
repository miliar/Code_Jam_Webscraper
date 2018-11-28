#!/usr/bin/env python3

import sys

ind = []
for line in sys.stdin:
    ind.append(line.rstrip().split(' '))
#print(ind)

limits = int(ind[0][0])

li = 1
for l in ind[1:]:
    smax = int(l[0])
    #print(l[1])
    n = [int(x) for x in l[1]]
    sm = ad = 0
    for i in range(smax+1):
        if sm < i :
            ad += i -sm
            sm = i
        sm += n[i]
    print('Case #'+str(li)+ ':',ad)
    li += 1
