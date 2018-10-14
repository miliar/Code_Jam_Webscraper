#!/usr/bin/env python

# Google code jam 2010 : park

import sys
from collections import deque

def simple(r,k,groups):   
    queue = deque(groups)
    total = 0
    for i in range(r):
	fil = 0
	band = []
	while len(queue) > 0 and fil + queue[0] <= k:
	    gr = queue.popleft()
	    fil = fil + gr
	    band.append(gr)
	queue.extend(band)
	total = total + fil
    return total

def result(r,k,groups):
    queue = deque(groups)
    total = 0
    try:
	first = []
	i = 0
	while i < r:
	    fil = 0
	    band = []
	    if first.count(list(queue)) != 0:
		raise NameError('')
	    first.append(list(queue))
	    while len(queue) > 0 and fil + queue[0] <= k:
		gr = queue.popleft()
		fil = fil + gr
		band.append(gr)
	    
	    queue.extend(band)

	    total = total + fil
	    i = i+1
	    
    except NameError:
	z = first.index(list(queue))
	period = i-z
	it = (r-z)/period
	mod = (r-z)%period
	stotal = simple(z,k,groups)
	ptotal = simple(i,k,groups) - stotal
	mtotal = simple(z+mod,k,groups) - stotal

	return stotal + it*ptotal + mtotal

    return total

p = int(sys.stdin.readline())
cases = []
for s in range(1,p+1):
    line = sys.stdin.readline()
    r,_,c = line.partition(' ')
    k,_,n = c.partition(' ')
    r = int(r)
    k = int(k)
    n = int(n)

    line = sys.stdin.readline()
    groups = [0 for i in range(n)]
    for j in range(n):
	groups[j],_,line = line.partition(' ')
	groups[j] = int(groups[j])

    print "Case #" + str(s) + ": " +  str(result(r,k,groups))

