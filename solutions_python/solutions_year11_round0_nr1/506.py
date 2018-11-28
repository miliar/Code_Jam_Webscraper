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
	line = read().split()
	r1 = []
	r2 = []
	t1, t2 = 1, 1
	labels = []
	N = int(line[0])
	ar = line[1:]
	for i in range(N):
		label = ar[2*i]
		labels += [label]
		target = int(ar[2*i+1])
		if label == 'O': 
			r1 += [abs(t1-target)]
			t1 = target
		else:
			r2 += [abs(t2-target)]
			t2 = target
	r1+=[0]
	r2+=[0]
	
	ret = 0
	p1,p2 = 0,0
	for l in labels:
		if l == 'O':
			t = r1[p1]+1
			ret += t
			r2[p2] -= t
			if(r2[p2] < 0): r2[p2] = 0
			p1 += 1
		else:
			t = r2[p2]+1
			ret += t
			r1[p1] -= t
			if(r1[p1] < 0): r1[p1] = 0
			p2 += 1
	wl(TT+1,ret)
	
	
#print(datetime.now()-startTime)

 