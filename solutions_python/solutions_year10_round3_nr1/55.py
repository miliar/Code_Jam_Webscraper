#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

rl = sys.stdin.readline

t = int(rl())

def check(line1, line2) :
	if line1[0] < line2[0] and line1[1] > line2[1] :
		return True
	if line1[0] <= line2[0] and line1[1] > line2[1] :
		return True
	if line1[0] < line2[0] and line1[1] >= line2[1] :
		return True
		
	if line1[0] > line2[0] and line1[1] < line2[1] :
		return True
	if line1[0] >= line2[0] and line1[1] < line2[1] :
		return True
	if line1[0] > line2[0] and line1[1] <= line2[1] :
		return True

for c in xrange(0, t) :
	lines = int(rl())
	
	bias = []
	for line in xrange(0, lines) :
		cur = map(int, rl().split())
		y1 = cur[0]
		y2 = cur[1]		
		bias.append([y1, y2])
	cnt = 0
	for line1 in xrange(0, lines) :
		for line2 in xrange(line1+1, lines) :
			if check(bias[line1], bias[line2]) :
				cnt = cnt + 1
				
	print 'Case #%d: %d' % (c+1, cnt)