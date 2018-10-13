#!/usr/bin/env python
import sys

N = int(sys.stdin.readline().split()[0])

for n in range(N):
	sw=0

	S = int(sys.stdin.readline().split()[0])
	Sset = set()
	for s in range(S):
		Sset.add(sys.stdin.readline())

	Q = int(sys.stdin.readline().split()[0])
	Qrys=[]
	for q in range(Q):
		Qrys.append(sys.stdin.readline())
		
	UsedSet = set()
	for q in Qrys:
		UsedSet.add(q)
		if len( Sset.difference(UsedSet) ) == 0:  # |Sset \ (UsedSet + {q})| == 0
			UsedSet.clear()
			UsedSet.add(q)
			sw+=1

	print "Case #"+str(n+1)+": "+str(sw)
