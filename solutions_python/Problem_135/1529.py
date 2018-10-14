#!/usr/bin/env python

T = int(raw_input())
for t in xrange(T):
	row1 = int(raw_input())
	mat1 = []
	for i in xrange(4):
		mat1.append(map(int,raw_input().split()))
	row2 = int(raw_input())
	mat2 = []
	for i in xrange(4):
		mat2.append(map(int,raw_input().split()))
	x = set(mat1[row1-1]).intersection(set(mat2[row2-1]))
	if len(x)==0:
		ans = "Volunteer cheated!"
	elif len(x)==1:
		ans = str(list(x)[0])
	else:
		ans = "Bad magician!"
	print 'Case #%d:'%(t+1),ans


