# -*- coding: utf-8 -*-


T = int(raw_input())

for t in range(1,1+T):
	
	N = int(raw_input())
	nums = [int(w) for w in raw_input().split()]
	wrong = 0
	for i,n in enumerate(nums):
		if n!=i+1:
			wrong += 1
	
	print "Case #{x}: {y}".format(x=t,y=float(wrong))










