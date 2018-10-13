# -*- coding: utf-8 -*-
import sys
from collections import deque
data = deque(sys.stdin.read().split())
token = data.popleft
T = int(token())

for case in xrange(1, T+1):
	z, b = {},{}
	C = int(token())
	for c in xrange(1, C+1):
		t = token()
		z[tuple(t[:2])]=t[-1]
		z[tuple(t[1::-1])]=t[-1]
	D = int(token())
	for d in xrange(1, D+1):
		t = token()
		b[tuple(t[:2])]=1
		#b[tuple(t[1::-1])]=1
	w = []
	N = int(token())
	for n in list(token()):
		w.append(n)
		if tuple(w[-2:]) in z: w[-2:] = z[tuple(w[-2:])]
		for x in b:
			if x[0] in w and x[1] in w: 
				w=[]
				break
	print "Case #%d: %s" % (case, str(w).replace("'", ''))
		
