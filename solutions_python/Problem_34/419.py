#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

[L,D,N] = map(int, sys.stdin.readline().split())
words=[]

for i in range(D):
	words.append(sys.stdin.readline().strip())

for case in range(N):
	z = L*[[]]
	for i in range(L):
		z[i] = 26*[False]
	inside=False
	idx=0
	for c in sys.stdin.readline().strip():
		if c=='(':
			inside=True
		elif c==')':
			inside=False
			idx+=1
		else:
			z[idx][ord(c) - ord('a')]=True
			if not inside:
				idx+=1
	assert(idx==L)
	print("Case #", case+1, ": ", len([None for w in words if all(z[i][ord(w[i])-ord('a')] for i in range(L))]), sep="")
