#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division

import sys

T = int(raw_input())

for t in range(1, T + 1):
	N = int(raw_input())
	xs = [int(x) for x in raw_input().split()]
	wrong = 0
	for i in range(len(xs)):
		if xs[i] != i + 1: wrong += 1
	print "Case #%d: %s" % (t, wrong)
