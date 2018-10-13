# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:57:15 2017

@author: Jorge
"""
import sys
from operator import itemgetter

def printMatrix(m):
    for row in m:
        print ''.join(row)

def solver(dest, horses_info):
    #sorted_velocities = sorted(horses_info, key=itemgetter(1))
    slowest = -1
    speed = dest
    
    for h in horses_info:
        remaining = dest - h[0]
        time = remaining / h[1]
        
        if slowest == -1 or slowest < time:
            slowest = time
    
    speed = round(dest / slowest, 6)
    
    
    return speed

        

n_cases = sys.stdin.readline()

for i in xrange(0,int(n_cases)):
    line = sys.stdin.readline()
    dest = int(line.split(" ")[0])
    n_horses = int(line.split(" ")[1])
    horse_info = []
    for j in xrange(0, n_horses):
        line= sys.stdin.readline()
        line = line.strip()
        aux = line.split(" ")
        horse_info.append([float(aux[0]), float(aux[1])])
    s = solver(dest, horse_info)
    s = '%.6f' % s
    #print "Case #" + str(i) + ": " + str(solver(m))
    print "Case #" + str(i+1) + ": " + str(s) 