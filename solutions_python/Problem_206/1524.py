# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 07:00:45 2017

@author: Bert
"""

# 1 ≤ N ≤ 2.
#Large dataset
#
#1 ≤ N ≤ 1000.

def handle_case(D, N, horses):
    #small is no 0,G, V
    #when does the latest horse arrive
    #then use that time

    arrivals = [(D-p)/v for p,v in horses]
    arrival = max(arrivals)
    speed = D/arrival
    return speed
   


def read_case(ifh,ofh,x):
    D, N = list(map(int,ifh.readline().split()))
    horse = []
    for i in range(N):
        K, S = list(map(int,ifh.readline().split()))
        horse.append((K, S))
        
    solution = handle_case(D, N, horse)
    o = "Case #{}: {}".format(x+1,solution)
    print (o)
    ofh.write(o)
    ofh.write("\n")
    
  
#with open("A-small.in") as fh, open("output-small.txt","w") as op:
with open("A-large.in") as fh, open("Aoutput-large.txt","w") as op:
#with open("Atest.txt") as fh, open("output-test.txt","w") as op:
    cases = int(fh.readline())
    for x in range(cases):
        read_case(fh,op,x)