#!/usr/bin/env python
# -*- coding: utf-8 -*-

def run_case():
	ret = 0

	l = raw_input()

	a = raw_input().split(' ')
	b = raw_input().split(' ')
	A = []
	B = []
	for x in a:
		A.append(int(x))
	for x in b:
		B.append(int(x))
	A.sort()
	B.sort()
	B.reverse()
	#print a
	#print b

	for x, y in zip(A, B):
		#print x, y
		ret += int(x) * int(y)
	return ret

# Program starts here
cases = []

N = int(raw_input())

for x in range(N):
	cases.append(run_case())

i = 1
for x in cases:
	print "Case #%i: %i" % (i, x)
	i = i + 1

