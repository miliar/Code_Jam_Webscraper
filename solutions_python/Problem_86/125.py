#!/usr/bin/python

import sys
import math	
import Queue
from datetime import datetime

startTime = datetime.now()
sys.setrecursionlimit(20000)

def readn(n):
	return [raw_input().strip() for i in range(n)]
def read():
	return raw_input().strip()
def readints():
	return map(int, read().split())
def readint():
	return readints()[0]
def wl(n, o):
	print("Case #{0}: {1}".format(n, o))
	
def solve(N,L,H,A):
	for f in range(L,H+1):
		ok = True
		for note in A:
			if note % f != 0 and f % note != 0:
				ok = False
				break
		if ok: return f
	return "NO"
	
T = readint()
for TT in range(T):
	N,L,H = readints()
	A = readints()
	wl(TT+1, solve(N,L,H,A))
	
	
	
	
#print(datetime.now()-startTime)