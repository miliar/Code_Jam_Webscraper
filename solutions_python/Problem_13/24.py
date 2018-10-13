#!/usr/bin/env python

import sys
from array import array

def minchanges(root):
    if nodes[root]==1: return 0
    if gates[root]==2: return M+1
    lc=root*2+1
    rc=root*2+2
    if gates[root]==1:
	# AND
	if changeable[root]==0:
	    return minchanges(lc)+minchanges(rc)
	else:
	    # change to OR
	    return 1+min(minchanges(lc), minchanges(rc))
    # OR
    return min(minchanges(lc), minchanges(rc))

filename=sys.argv[1]
inputfile=file(filename, 'r')
numcases=int(inputfile.readline().strip())
for case in range(1,numcases+1):
    M, V = map(long, inputfile.readline().strip().split())
    nodes = array('B')
    gates = array('B')
    changeable = array('B')
    for m in range((M-1)/2):
	G, C = map(long, inputfile.readline().strip().split())
	nodes.append(0)
	if V==1: gates.append(G)
	else: gates.append(1-G)
	changeable.append(C)
    for m in range((M+1)/2):
	L = long(inputfile.readline().strip())
	if V==1: nodes.append(L)
	else: nodes.append(1-L)
	gates.append(2)
    x=(M-1)/2-1
    while x>=0:
	if gates[x]==1:
	    nodes[x]=min(nodes[x*2+1], nodes[x*2+2])
	else:
	    nodes[x]=max(nodes[x*2+1], nodes[x*2+2])
	x-=1
    minswitches=minchanges(0)
    if minswitches<=M:
	print "Case #%d: %d" % (case, minswitches)
    else:
	print "Case #%d: IMPOSSIBLE" % case
