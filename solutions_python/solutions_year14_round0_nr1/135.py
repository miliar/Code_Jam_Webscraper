#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# google code jam - c.durr- 2014

# Magic Trick
# https://code.google.com/codejam/contest/2974486/dashboard#s=p0
# compare sets of both rows

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())


def solve(s):
	if len(s)==0:
		return "Volunteer cheated!"
	elif len(s)>1:
		return "Bad magician!"
	else:
		return str(s.pop())

def readRow():
	r = readint()-1
	s = set()
	for i in range(4):
		l = readarray(int)
		if i==r:
			s = set(l)
	return s

for test in range(readint()):
	print "Case #%i:"% (test+1), solve(readRow().intersection(readRow()))