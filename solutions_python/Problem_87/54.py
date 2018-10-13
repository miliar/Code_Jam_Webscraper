#!/usr/bin/env python
from sys import stdin, stderr
T=int(stdin.readline())
for case in range(1, T+1):
	X, S, R, T, N=map(int, stdin.readline().split())
	B,E,W=[0.0],[],[0.0]
	for n in range(N):
		b,e,w=map(float, stdin.readline().split())
		E.append(b)
		B.append(b)
		E.append(e)
		W.append(w)
		B.append(e)
		W.append(0.0)
	E.append(X)
	O=0
	while W:
		s=W.index(min(W))
		b,e,w=B.pop(s),E.pop(s),W.pop(s)
		t=(e-b)/(w+R)
		if t<T:
			T-=t
		else:
			t=(e-b-T*(w+R))/(w+S)+T
			T=0
		O+=t
	print "Case #%d:"%case, O
