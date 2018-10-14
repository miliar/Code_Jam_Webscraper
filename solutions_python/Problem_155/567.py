#!/bin/env python

# google code jam 2015 problem 1

def solve(s):
    n = 0 # people needed
    t = int(s[0]) # total number of people with shyness level i-1
    for i in range(1, len(s)):
	 si = int(s[i])
	 if t < i:
	     n += i - t
	     t = i
	 t += si
    return n

tests = int(raw_input())
for k in range(tests):
    n, s = raw_input().split()
    #n = int(n)
    x = solve(s)
    print "Case #%d: %d" % (k+1, x)
    #print n, s, len(s) - n - 1
