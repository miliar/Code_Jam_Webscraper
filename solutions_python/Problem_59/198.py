#!/usr/bin/env python

import sys

dirs = dict()

def train(dirs, item):
	if item not in dirs:
		dirs[item] = 1

def test(dirs, item):
	if item in dirs:
		return 0

	path = ''
	mkdirs = 0
	subs = item.split('/')
	for sub in subs[1:]:
		path += '/' + sub
		if path not in dirs: 
			dirs[path] = 1
			mkdirs += 1

	return mkdirs

t = int(sys.stdin.readline())
for i in range(t):
	dirs.clear()
	params = sys.stdin.readline().split(' ')
	for j in range(int(params[0])):
		train(dirs, sys.stdin.readline().strip())

	mkdirs = 0
	for j in range(int(params[1])):
		mkdirs += test(dirs, sys.stdin.readline().strip())
	
	print "Case #%i: %i" % (i+1, mkdirs)

