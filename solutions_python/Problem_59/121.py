#!/usr/bin/python

import sys, os



def mkdir(root, path, n):
	p = path.split("/")[1:]
	cd = root
	for i in p:
		if i not in cd:
			n += 1
			cd[i] = {}
		cd = cd[i]
	return n

cases = int(sys.stdin.readline())

for case in xrange(cases):
#for case in [0]:
	_nm = map(int, sys.stdin.readline().split() )
	n = _nm[0]
	m = _nm[1]
	
	root = {}
	
	for i in xrange(n):
		path = sys.stdin.readline().strip()
		mkdir(root, path, 0)
	
	dirs = 0
	
	for i in xrange(m):
		path = sys.stdin.readline().strip()
		dirs = mkdir(root, path, dirs)
	
	print "Case #{0}: {1}".format( case + 1, dirs)
	
	
