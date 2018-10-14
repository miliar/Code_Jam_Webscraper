#! /usr/bin/env python
#################################################################################
#     File Name           :     Problem B. Infinite House of Pancakes.py
#     Created By          :     xiaodi
#     Creation Date       :     [2015-04-12 07:48]
#     Last Modified       :     [2015-04-12 07:48]
#     Description         :      
#################################################################################

T = int(raw_input())
for t in xrange(T):
	minutes = 0
	D = int(raw_input())
	P = map(int, raw_input().split())
	minutes = max(P)
	for x in xrange(1,max(P)):
		minutes2 = x;
		for xx in P:
			if xx > x:
				if xx % x == 0:
					minutes2 = minutes2 + xx/x -1;
				else:
					minutes2 = minutes2 + xx/x;
		minutes = min(minutes, minutes2)
	print "Case #%d:" % (t+1), minutes