#!/usr/bin/python

# google code jam - c.durr - 2010

# Snapper Chain

# Is the N-bit of K 1 or 0 ?

import sys

T = int(raw_input())
for t in range(T):
    N, K = map(int, raw_input().split())

    a = ["OFF","ON"][ (((K&((1<<N)-1))+1)>>N)&1 ]

    print "Case #%i:"%(t+1), a
    
