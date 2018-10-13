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
	
def reduce(comb, anih, used):
	global invoke
	n = len(invoke)
	if n < 2: return False
	
	x = invoke[n-2]
	y = invoke[n-1]
	if (x,y) in comb:
		z = comb[(x,y)]
		invoke[-2:] = [z]
		used[x] -= 1
		used[y] -= 1
		used[z] += 1
		return True
	elif y in anih:
		used[y] -= 1
		l = anih[y]
		for ch in l:
			if used[ch] > 0:
				invoke = []
				for i in range(26):
					used[chr(ord('A')+i)]=0
				return False
		used[y] += 1
	
	return False
	
T = int(read())
for TT in range(T):
	l = read().split()
	comb = {}
	anih = {}
	pos = 0
	tmp = int(l[0])
	pos += 1
	for i in range(tmp):
		s = l[i+pos]
		comb[(s[0],s[1])]=s[2]
		comb[(s[1],s[0])]=s[2]
	pos += tmp
	tmp = int(l[pos])
	pos+=1
	for i in range(tmp):
		s = l[i+pos]
		if s[0] not in anih: anih[s[0]] = []
		if s[1] not in anih: anih[s[1]] = []
		anih[s[0]]+=s[1]
		anih[s[1]]+=s[0]
	pos += tmp
	s = list(l[pos+1])
	#solve
	used = {}
	for i in range(26):
		used[chr(ord('A')+i)]=0
	invoke = []
	for c in s:
		invoke += [c]
		used[c] += 1
		while reduce(comb, anih, used): pass
	wl(1+TT, '['+', '.join(invoke)+']')

				
				
	
	
#print(datetime.now()-startTime)

 