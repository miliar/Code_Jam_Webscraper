#!/usr/bin/python

import sys

def store_cards():
	arrange = []
	for i in xrange(4):
		arrange.append(map(int,sys.stdin.readline().strip().split()))
	return arrange

T = int(sys.stdin.readline().strip())
for i in xrange(T):
	row1 = int(sys.stdin.readline().strip()) - 1
	arrange1 = store_cards()
	row2 = int(sys.stdin.readline().strip()) - 1
	arrange2 = store_cards()
	count = 0
	for x in arrange1[row1]:
		for y in arrange2[row2]:
			if x == y:
				count = count + 1
				card = x
	if count == 1:	result = card
	elif count > 1: result = "Bad magician!"
	else: result = "Volunteer cheated!"
	print "Case #%d: %s" %(i+1,str(result))
		
