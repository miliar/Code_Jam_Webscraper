# -*- coding: utf-8 -*-

from __future__ import division
import math
from collections import defaultdict as dd

T = int(raw_input())

for case in xrange(1,T+1):
	
	X,S,R,t,N = map(int, raw_input().split())
	
	ways = [map(int,raw_input().split()) for i in xrange(N)]
	
	dsp = dd(int)	# distance for speed.  key:speed, value:dist
	for way in ways:
		d = way[1] - way[0]
		dsp[way[2]] += d
	wsum = sum(dsp.values())
	left = X-wsum
	dsp[0] += left
	
	tt = 0
	for boost,dist in sorted(dsp.iteritems(), key=lambda kv: kv[0]):
		maxtrun = dist / (R+boost)
		trun = min(t,maxtrun)
		drun = trun * (R+boost)
		dwalk = dist - drun
		twalk = dwalk / (S+boost)
		tt += trun + twalk
		t -= trun
	
	
	print 'Case #{x}: {y}'.format(x=case, y=tt)




























































