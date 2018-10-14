#!/usr/bin/python

import sys
import math	
from datetime import datetime

startTime = datetime.now()
sys.setrecursionlimit(20000)

def readn(n):
	return [raw_input() for i in range(n)]
def read():
	return raw_input()
def readints():
	return map(int, read().split())
def wl(n, o):
	print("Case #{0}: {1}".format(n, str(o)))
	
	
T = int(read())
for TT in range(T):
	N = int(read())
	cand = readints()
	bs = 0
	s = 0
	m = 100000000000
	for c in cand:
		if c < m: m = c
		s += c
		bs ^= c
	if bs != 0: wl(TT+1, "NO")
	else: wl(TT+1, s-m)
	
	
	
#print(datetime.now()-startTime)

 