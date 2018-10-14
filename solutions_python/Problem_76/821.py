#!/usr/bin/python

T = int(raw_input())

for case in range(1, T+1):
	
	N = int(raw_input())
	C = map(int, raw_input().split())
	ans = 0
	
	accum = 0
	smallest = C[0]
	for candy in C:
		accum = accum ^ candy
		if candy < smallest:
			smallest = candy
	
	if accum != 0:
		ans = 'NO'
	else:
		ans = sum(C) - smallest
	
	print 'Case #' + str(case) + ': ', str(ans)

