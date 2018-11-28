#!/usr/bin/env python

# Google code jam 2014

import sys

'''
while (x - c)/alpha >= x/(alpha+f):
    n_farms += 1
    alpha += f
'''

def result(c, f, x):
    alpha = 2.0
    n_farms = 0

    # find out how many farms to buy
    n_farms = int((f*x-2*c)/(f*c))

    # sum everything
    t = 0
    alpha = 2.0
    for k in range(n_farms):
        t += c/alpha
        alpha += f
    t += x/alpha

    return str(t)
    
p = int(sys.stdin.readline())
for q in range(1,p+1):

    line = sys.stdin.readline()
    c,_,line = line.partition(' ')
    f,_,line = line.partition(' ')
    x,_,line = line.partition(' ')

    c = float(c)
    f = float(f)
    x = float(x)

    print("Case #" + str(q) + ": " +  result(c, f, x))

