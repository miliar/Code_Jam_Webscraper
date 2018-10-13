#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division

import sys

T = int(raw_input())

for t in range(1, T + 1):
	xs = raw_input().split()
	C = int(xs[0])
	cs = xs[1:1+C]
	D = int(xs[1+C])
	ds = xs[2+C:2+C+D]
	ns = xs[3+C+D]

	combines = {}
	for c in cs:
		combines[c[:2]] = c[2]
		combines["".join(reversed(c[:2]))] = c[2]

	opposes = {}
	for d in ds:
		opposes[d[:2]] = True
		opposes["".join(reversed(d[:2]))] = True

	# print "", combines
	# print "", opposes

	output = ""
	for n in ns:
		output += n
		while combines.get(output[-2:]):
			output = output[:-2] + combines[output[-2:]]
		blankit = False
		for x in output:
			if opposes.get(x + output[-1]):
				blankit = True
		if blankit: output = ""
		# print n, output
	# print
	print "Case #%d: [%s]" % (t, ", ".join(output))
