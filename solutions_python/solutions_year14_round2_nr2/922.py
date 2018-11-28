#!/usr/bin/python

#map(float, raw_input().split(" "))

for case in range(1,int(raw_input())+1):          #For all test cases
	A, B, K = map(int, raw_input().split(" "))

	count = 0

	a = 0
	while a < A:
		b = 0
		while b < B:
			if a & b < K:
				count += 1
			b += 1
		a += 1

	print "Case #%d: %d" % (case, count)
