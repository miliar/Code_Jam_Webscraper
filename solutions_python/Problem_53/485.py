#!/usr/bin/env python

# Google code jam 2010 : snapper

import sys

def snap(snappers):
    for k in range(len(snappers)):
	if not snappers[k]:
	    snappers[k] = True
	    break
	else:
	    snappers[k] = False
    return snappers
    

def result(n,k):
    snappers = [False for i in range(n)]
    for j in range(k):
	snappers = snap(snappers)
    flag = True
    for light in snappers:
	flag = flag & light
    if flag: 
	return "ON" 
    else:
	return "OFF"

n = int(sys.stdin.readline())
cases = []
k = 0
for line in sys.stdin:
    k = k+1
    a,_,c = line.partition(' ')
    a = int(a)
    c = int(c)
    print "Case #" + str(k) + ": " +  result(a,c)

