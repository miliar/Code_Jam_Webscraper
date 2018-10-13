#!/usr/bin/python

import sys

cases = int(sys.stdin.readline())
for c in range(1, cases+1):
	arr = sys.stdin.readline().split(' ')
	n = int(arr[0])
	m = int(arr[1])

	dirlist = {'':{}}
	while n:
		path = sys.stdin.readline()
		dirs = path.strip().split('/')
		dir_ = dirlist
		for dirname in dirs:
			if dirname in dir_:
				dir_ = dir_[dirname]
			else:
				dir_[dirname] = {}
				dir_ = dir_[dirname]
		n -= 1
	
	cnt = 0
	while m:
		path = sys.stdin.readline()
		dirs = path.strip().split('/')
		dir_ = dirlist
		for dirname in dirs:
			if dirname in dir_:
				dir_ = dir_[dirname]
			else:
				dir_[dirname] = {}
				dir_ = dir_[dirname]
				cnt += 1
		m -= 1
	
	print "Case #%d: %d" % (c, cnt)

