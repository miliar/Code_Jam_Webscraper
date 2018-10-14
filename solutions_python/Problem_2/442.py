#!/usr/bin/env python

import sys

def addtime(a, b):
	cmin = (a[1] + b[1]) % 60
	chour = (a[0] + b[0] + ((a[1] + b[1]) / 60)) % 24
	
	return (chour, cmin)
	
def timetoint(t):
	return t[0] * 100 + t[1]
	
def inttotime(i):
	tmin = i % 100
	thour = i / 100
	
	return (thour, tmin)
	
def calc(atob, btoa, t):
	
	reqA = []
	reqB = []
	avlA = []
	avlB = []
	
	requiredA = 0
	requiredB = 0
	
	for i in atob:
		reqA.append(i[0])
		avlB.append(timetoint(addtime(inttotime(i[1]), (0,t))))
		
	for i in btoa:
		reqB.append(i[0])
		avlA.append(timetoint(addtime(inttotime(i[1]), (0,t))))
		
	reqA.sort()
	reqB.sort()
	avlA.sort()
	avlB.sort()
	avlA.reverse()
	avlB.reverse()
	
	for i in reqA:
		if avlA and avlA[-1] <= i:
			avlA.pop()
		else:
			requiredA = requiredA+1
			
	for i in reqB:
		if avlB and avlB[-1] <= i:
			avlB.pop()
		else:
			requiredB = requiredB+1
			
	return(requiredA, requiredB)
	
if __name__ == '__main__':
	
	inp = open(sys.argv[1])
	op = open(sys.argv[2], 'w')
	
	cases = int(inp.readline()[:-1])
	
	for i in range(1, cases + 1):
		t = int(inp.readline()[:-1])
		s = inp.readline()[:-1]
		tl = s.split()
		trains_from_A = int(tl[0])
		trains_from_B = int(tl[1])
		atob = []
		btoa = []
		
		for j in range(1, trains_from_A+1):
			line = inp.readline()[:-1]
			times = line.split()
			time_dep = times[0].split(':')
			time_arr = times[1].split(':')
			
			atob.append((timetoint((int(time_dep[0]), int(time_dep[1]))), timetoint((int(time_arr[0]), int(time_arr[1])))))
			
		for k in range(1, trains_from_B +1):
			line = inp.readline()[:-1]
			times = line.split()
			time_dep = times[0].split(':')
			time_arr = times[1].split(':')
			
			btoa.append((timetoint((int(time_dep[0]), int(time_dep[1]))), timetoint((int(time_arr[0]), int(time_arr[1])))))
			
		print atob
		print btoa
		ans = calc(atob, btoa, t)
		print ans
		op.write('Case #%s: %s %s\n' %(i, ans[0], ans[1]))
		
	inp.close()
	op.close()
