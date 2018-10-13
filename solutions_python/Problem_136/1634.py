#!/usr/bin/python
import math

import fileinput 

def intersect(a, b):
     return list(set(a) & set(b))

fi=fileinput.input()
nTestCases=int(fi.readline())

for testNumber in range(1, nTestCases+1):
    cfx= map(float,fi.readline().strip().split(" "))
    c, f, x = cfx[0],cfx[1],cfx[2]
    fact_costs=[0.]*5001
    velocity=2.0
    for i in xrange(1,5001):
        fact_costs[i]=fact_costs[i-1]+c/velocity
        velocity = velocity + f  
    #print("fact costs")
    #print(fact_costs)
    total_costs=[0.]*5001
    velocity=2.0
    for i in xrange(0,5001):
        total_costs[i]=fact_costs[i]+x/velocity
        velocity = velocity + f  
    #print("total costs")
    #print(total_costs)
    result=min(total_costs)
    print("Case #%d: %.7f" % (testNumber, result))




