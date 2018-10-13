#! /usr/bin/python
import sys

def sum_alt(seq):
    def add_alt(x,y): return x^y
    return reduce(add_alt, seq, 0)

cases = int(sys.stdin.readline()[:-1])
actual_case = 0

while actual_case < cases:
    # reading and so
    actual_case += 1

    #nacteni 1 cisla
    n = int(sys.stdin.readline()[:-1])
    
    line = sys.stdin.readline()[:-1].split()
    candies = map(int,line)

    if (sum_alt(candies) <> 0):
        print "Case #%d: NO" %(actual_case)
    else:
	print "Case #%d: %d" %(actual_case,sum(candies)-min(candies))

