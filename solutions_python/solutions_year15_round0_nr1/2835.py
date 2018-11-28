# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:45:38 2015

@author: Dittaya Wanvarie
"""

with open('A-large.in') as f:
    data = f.readlines()

f = open('output.txt','w')
T = int(data[0])
for c in range(1,T+1):
    line = data[c].rstrip()
    smax, k = line.split()
    smax = int(smax)
    stand = int(k[0])
    add = 0
    for i in range(1,smax+1):
        ki = int(k[i])
        if ki == 0: continue
        if stand < i:
            add += i - stand
            stand = i + ki
        else:
            stand += ki
    print ('Case #',c,': ',add)
    f.write('Case #'+str(c)+': '+str(add)+'\n')
f.flush()
f.close()
