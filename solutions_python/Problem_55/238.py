# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
CASES = int(fin.readline())
for case in range(1,CASES+1):
	RKN = map(int,fin.readline().split())
	r = RKN[0]
	k = RKN[1]
	n = RKN[2]
	code = map(int, fin.readline().split())
	t = 0
	index = 0
	now = 0
	p = [(0,0) for x in range(0,n)]
	total = 0
	earn = 0
	
	for i in range(0,r):
		now = 0
		t = 0
		while(t+code[(index)%n] <= k and now <n):
			t = t +code[index]
			index = index + 1
			index = index % n
			now = now + 1
		earn = earn + t
	print "Case #%d: %d" % (case,earn)
    
