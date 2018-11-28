#!/usr/bin/env python
from sys import stdin
T=int(stdin.readline())
for case in range(1,T+1):
	S=set(range(1,17))
	for t in range(2):
		R=int(stdin.readline())
		for r in range(1,5):
			if R==r:
				S&=set(map(int,stdin.readline().split()))
			else:
				stdin.readline()
	t=len(S)
	if t==0:
		S='Volunteer cheated!'
	elif t==1:
		S=S.pop()
	else:
		S='Bad magician!'
	print 'Case #%d:'%case, S
