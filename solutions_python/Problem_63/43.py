# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
CASES = int(fin.readline())
#print CASES
for case in range(1,CASES+1):
	LPC = map(int,fin.readline().split())
	L=LPC[0]
	P=LPC[1]
	C=LPC[2]
	COUNT = 0
	Q = P*1.0/L
	RES = 0
	while Q > 1:
		Q/=C
		COUNT+=1
	while COUNT > 1:
		COUNT/=2.0
		RES += 1
	print "Case #%d: %d" % (case,RES)
