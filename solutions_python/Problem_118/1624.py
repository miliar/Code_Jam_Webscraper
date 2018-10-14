#!/usr/bin/python
import sys

def is_palindrom(num):
	str_num = str(num)
	pjg = len(str_num)
	for x in range(0, pjg/2):
		if str_num[x] != str_num[-(x+1)]:
			return False
	return True

mem = []
for x in range(1, 10000005):
	if is_palindrom(x) and is_palindrom(x*x):
		mem.append(x*x)

t = int(sys.stdin.readline())
for ctr in range(1, t+1):
	a, b = [int(x) for x in sys.stdin.readline().split()]	
	tot = 0
	for m in mem:
		tot = tot+1 if m >= a and m <= b else tot
  	print "Case #{0}: {1}".format(ctr, tot)