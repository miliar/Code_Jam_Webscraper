#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline())
for t in xrange(T):
	N = int(sys.stdin.readline())
	naomi = sorted([float(x) for x in sys.stdin.readline().split()])
	ken = sorted([float(x) for x in sys.stdin.readline().split()])
	#print "N:", N
	#print "Naomi:", naomi
	#print "Ken:", ken

	klookup = {}
	for i,k in enumerate(ken):
		klookup[ k ] = i
	index, nidx = 0, 0
	while index < len(ken):
		es = [k for k in ken[index:] if k > naomi[nidx]]
		if len(es) == 0:
			nidx = max(nidx, 0)
			break
		elem = es[0]
		#print "[1] elem:", elem
		index = klookup[elem]+1
		nidx += 1

	naomi, ken = ken, naomi

	klookup = {}
	for i,k in enumerate(ken):
		klookup[ k ] = i
	index, kidx = 0, 0
	while index < len(ken):
		es = [k for k in ken[index:] if k > naomi[kidx]]
		if len(es) == 0:
			kidx = max(kidx, 0)
			break
		elem = es[0]
		#print "[2] elem:", elem
		index = klookup[elem]+1
		kidx += 1

	print "Case #%d: %d %d"%(t+1,kidx,N-nidx)
