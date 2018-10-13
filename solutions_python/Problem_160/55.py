#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import *
#from sets import *
import math
import sys

if __name__ == "__main__":
	t = int(input())
	for caseIdx in range(1,t+1):
		sys.stdout.flush()
		b, n= map(int, input().split(' '))
		mk = [m for m in map(int, input().split(' '))]

		# binary search
		first = 0
		last = 100000*n
		while last - first >1:
			t = math.floor((last+first)/2)
			cutted = 0
			for m in mk:
				cutted = cutted + math.floor(t/m)
			if cutted + b < n:
				first = t
			else:
				last =t

		arr = []
		cutted = 0
		for i, m in enumerate(mk):
			arr.append((last-math.floor(last/m)*m, i+1))
			cutted = cutted + math.floor(last/m)
		arr = sorted(arr, key=lambda pair: (pair[0], -1*pair[1]), reverse=True)
		#print(b, n)
		#print(mk)
		#print(last, cutted, n-cutted)
		#print(arr)
		print("Case #%d: %s" % (caseIdx, arr[n-cutted-1][1]))
