# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
CASES = int(fin.readline())
for case in range(1,CASES+1):
	p = int(fin.readline())
	LINE = []
	M = map(int,fin.readline().split())
	for i in range(0,p):
		LINE.append(map(int,fin.readline().split()))
	deep = len(LINE)
	f = 0
	for i in range(0,len(M)):
		M[i] = deep - M[i]
		if (M[i] > 0):
			f = 1
	q = 0
	if (f == 1):
		for i in range(0,deep):
			flag = 0
			for j in range(0,pow(2,i)):
				t = 0
				for h in range(pow(2,deep-i)*j,pow(2,deep-i)*(j+1)):
					if(M[h] >= 1):
						t = 1
					M[h] -= 1
					if (M[h] > 0):
						flag = 1
				q += t
			if (flag == 0):
				break
	print "Case #%d: %d" % (case,q)
