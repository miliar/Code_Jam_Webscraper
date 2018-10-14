#!/usr/bin/env python

import sys

def solve(N,case):
    case_split = case.split(" ")
    candies = [int(x) for x in case_split]
   
    # calculate the xor and the sum for all candies
    x = 0
    s = 0
    smallest = 1000000000  
    for c in candies:
        x = x^c
        s += c
        if c<smallest:
            smallest = c 
        

    if x != 0:
        return "NO"

    return s-smallest  

def parse_args():
    f = open(sys.argv[1]) 
    n = int(f.readline().strip())
   
    for i in xrange(1,n+1):
        N = f.readline().strip()
        case = f.readline().strip()
        print "Case #" + str(i)+ ":", solve(N,case)

parse_args()

