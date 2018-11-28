#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division

import sys

T = int(raw_input())

for t in range(1, T + 1):
	N = int(raw_input())
	cs = [int(x) for x in raw_input().split()]
	xored = 0
	for c in cs:
		xored = xored ^ c
	if xored == 0:
		print "Case #%d: %s" % (t, sum(cs) - min(cs))
	else:
		print "Case #%d: NO" % t
