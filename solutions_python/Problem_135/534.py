#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(a1, s1, a2, s2):
	y1 = set(s1[a1-1])
	y2 = set(s2[a2-1])
	y3 = set.intersection(y1, y2)

	#print y1, y2

	if(len(y3) == 1):
		return y3.pop()
	elif(len(y3) == 0):
		return "Volunteer cheated!"
	else:
		return "Bad magician!"

if __name__ == "__main__":
	T = int(raw_input())
	s1 = [[0 for i in xrange(4)] for j in xrange(4)]
	s2 = [[0 for i in xrange(4)] for j in xrange(4)]
	for i in xrange(1, T+1):
		a1 = int(raw_input())
		for j in xrange(4):
			s1[j] = map(int, raw_input().split())
		a2 = int(raw_input())
		for j in xrange(4):
			s2[j] = map(int, raw_input().split())
		print "Case #%d:" % i, 
		print solve(a1, s1, a2, s2)