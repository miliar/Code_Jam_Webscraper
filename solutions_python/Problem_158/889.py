#!/usr/bin/env python

def possible(X, R, C):
	if ((R*C) % X)>0: # any N-omino works
		return True
	if X > R and X > C: # the | shaped N-omino works
		return True
	m = min(R,C)
	if (X+1)/2 > m: # a L shaped N-omino works
		return True
	if X >= 2*m and m>1: # a t-shaped N-omino works
		return True
	return False

T = int(raw_input())
for case in range(1,T+1):
	X,R,C = (int(i) for i in raw_input().split())
	print('Case #%d: %s' % (case,"RICHARD" if possible(X,R,C) else "GABRIEL"))
