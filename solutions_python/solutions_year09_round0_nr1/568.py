#!/usr/bin/env python

import sys, re
lb = re.compile('\(')
rb = re.compile('\)')
FI=open(sys.argv[1],'r')
line = FI.readline()
words = [int(w) for w in line.split()]
L=words[0]; D=words[1]; N=words[2];
Knowns=[]
for i in xrange(D):
	Knowns.append(FI.readline().rstrip())
for j in xrange(N):
	cand = rb.subn(']',lb.subn('[',FI.readline().rstrip())[0])[0]
	cand = re.compile(cand)
	Matched = 0
	for i in xrange(D):
		if cand.match(Knowns[i]):
			Matched=Matched+1
	print "Case #"+str(j+1)+": "+str(Matched)



