#!/usr/bin/python

import sys

T = int(sys.stdin.readline().strip())

cards_1 = [[],[],[],[]]
cards_2 = [[],[],[],[]]

for i in range(1,T+1):
	
	row_1 = int(sys.stdin.readline().strip())
	cards_1[0] = sys.stdin.readline().strip().split()
	cards_1[1] = sys.stdin.readline().strip().split()
	cards_1[2] = sys.stdin.readline().strip().split()
	cards_1[3] = sys.stdin.readline().strip().split()
	
	row_2 = int(sys.stdin.readline().strip())
	cards_2[0] = sys.stdin.readline().strip().split()
	cards_2[1] = sys.stdin.readline().strip().split()
	cards_2[2] = sys.stdin.readline().strip().split()
	cards_2[3] = sys.stdin.readline().strip().split()
	
	intersect = []
	for n in cards_1[row_1-1]:
		if n in cards_2[row_2-1]:
			intersect.append(n)
	
	if len(intersect)==0: print "Case #%s: Volunteer cheated!" % i
	if len(intersect)>1: print "Case #%s: Bad magician!" % i
	if len(intersect)==1: print "Case #%s: %s" % (i, intersect[0])
