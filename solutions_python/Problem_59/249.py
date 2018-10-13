#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline())

for cc in range(1, T+1):
	new = []
	old = ['/']
	N, M = [int(s) for s in sys.stdin.readline().split()]
	for i in range(0, N):
		s = sys.stdin.readline()
		j = 0
		while j != -1:
			j = s.find('/', j+1)
			if not s[:j] in old:
				old.append(s[:j])

	for i in range(0, M):
		s = sys.stdin.readline()
		j = 0
		while j != -1:
			j = s.find('/', j+1)
			if not s[:j] in old and not s[:j] in new:
				new.append(s[:j])
	
	print "Case #%d: %d"%(cc, len(new))

