#!/usr/bin/env python
from sys import stdin
import math

# limit in terms of digits
def isPS(pp):
	pp = str(pp)
	return pp == pp[::-1]

def genPS(limit = 1e15):
	pno = { 1, 4, 9 }
	ctrs = list("0123456789") + ['']
	c = True
	cnt = len(pno)
	i = 1
	while c:
		c = False
		curr = str(i)
		crev = curr[::-1]
		for ctr in ctrs:
			cno = int(curr + ctr + crev)
			cno = cno * cno
			if cno <= limit:
				c = True
				if isPS(cno):
					pno.add(cno)
					cnt += 1
		i += 1
# 	print(i)
# 	print sorted(pno)
# 	print(cnt)
	return sorted(pno)

def main(): 
	TC = int(stdin.readline().strip())
	pno = genPS(1e16)
	for t in range(TC):
		(A, B) = stdin.readline().strip().split()
		A, B = int(A), int(B)
		print "Case #{0}: {1}".format(t+1, sum([1 for i in pno if A <= i and i <= B]))

main()
