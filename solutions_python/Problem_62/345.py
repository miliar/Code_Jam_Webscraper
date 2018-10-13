#!/usr/bin/env python

# Google code jam 2010 : wires

import sys

def inter(a,b):
    if b[1] >= b[0]:
	if a[0] <= a[1]:
	    return (a[0] < b[0] and a[1] > b[1]) or (a[0] > b[0] and a[1] < b[1])
	else:
	    return a[0] > b[0] and a[1] < b[1]
    else:
	if a[0] <= a[1]:
	    return a[0] < b[0] and a[1] < b[1]
	else:
	    return (a[0] > b[0] and a[1] < b[1]) or (a[0] < b[0] and a[1] > b[1])

def result(wires,n):
    count = 0
    for j in range(n):
	for k in range(j):
	    p = wires[j]
	    q = wires[k]
	    if p != q and (inter(p,q) or inter(q,p)):
		count += 1
    return count

p = int(sys.stdin.readline())
cases = []
for s in range(1,p+1):
    line = sys.stdin.readline()
    N = int(line)

    wires = [[0,0] for i in range(N)]
    for j in range(N):
	line = sys.stdin.readline()
	p,_,q = line.partition(' ')
	wires[j] = [int(p),int(q)]

    print "Case #" + str(s) + ": " +  str(result(wires,N))

