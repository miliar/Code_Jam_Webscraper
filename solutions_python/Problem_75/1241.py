#!/usr/bin/python

import sys

def comboCheck(r, c):
	rl = len(r)
	if rl < 2:
		return r
	combo = r[rl-1]+r[rl-2]
	if c.has_key(combo):
		r.pop()
		r.pop()
		r.append(c[combo])
	return r

def checkClear(r, d):
	for i in range(len(d)):
		if d[i][0] in r:
			if d[i][1] in r:
				return list()
	return r

lines = sys.stdin.readlines();

T = int(lines[0])
for t in range(T):
	l = lines[t+1]

	C = int(l[0])
	l = l[2:]
	c = dict()
	for i in range(C):
		k1 = l[:2]
		k2 = l[1]+l[0]
		v = l[2:3]
		c[k1] = v
		c[k2] = v
		l = l[4:]

	D = int(l[0])
	l = l[2:]
	d = list()
	for i in range(D):
		v = l[:2]
		l = l[3:]
		d.append(v)

	N = int(l[0])
	l = l[2:].strip()
	
	r = list()
	for i in range(len(l)):
		r.append(l[i])
		r = comboCheck(r,c)
		r = checkClear(r, d)
	
	print "Case #"+str(t+1)+": "+str(r).replace('\'','')
	#print "Case #"+str(t)+": " + r
