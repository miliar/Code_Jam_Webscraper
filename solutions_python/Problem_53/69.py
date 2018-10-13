#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division

import sys

lines = sys.stdin.readlines()

T = int(lines[0])

for t in range(1, T + 1):
	l = lines[t].split()
	N = int(l[0])
	K = int(l[1])
	if (K + 1) % (2 ** N) == 0:
		answer = "ON"
	else:
		answer = "OFF"
	print "Case #%d: %s" % (t, answer)
