# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 23:33:21 2017

@author: ASUS
"""

FILENAME = 'A-large.in'

def steed(d, n, horses):
    timelist = []
    for i in range(n):
        pos = int(horses[i][0])
        spd = int(horses[i][1])
        time = (d - pos)/spd
        timelist.append(time)
    maxtime = max(timelist)
    return d/maxtime

fr = open(FILENAME, 'r')
fw = open('outputAl.txt', 'w')

t = fr.readline()
t = int(t.strip())

for i in range(t):
    
    case = fr.readline().split()
    n = int(case[1])
    horses = []
    
    for j  in range(n):
        
        horses.append(fr.readline().strip().split())
    
    d = int(case[0])
    
    k = steed(d, n, horses)
    
    fw.write("Case #{}: {}\n".format(i+1, k))

fr.close()
fw.close()