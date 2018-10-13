#!/usr/bin/env python

from __future__ import print_function
import sys

with open(sys.argv[1]) as f:
	for case in range(1, int(f.readline().strip()) + 1):
		colours = map(int, f.readline().strip().split())
		total = colours[0]
		unicorns = {}
		for colour, count in zip('ROYGBV', colours[1:]):
			unicorns[colour] = count
		ordered = [c[0] for c in sorted(unicorns.items(), key=lambda x: x[1], reverse=True) if c[1] > 0]
		if len(ordered) == 1:
			print("Case #%s: IMPOSSIBLE" % case)
			continue
		if unicorns[ordered[0]] > sum([unicorns[c] for c in ordered[1:]]):
			print("Case #%s: IMPOSSIBLE" % case)
			continue
		carry = 0
		height = unicorns[ordered[0]]
		columns = [ordered[0] * height]
		columns += [ordered[1] * unicorns[ordered[1]]]
		if len(columns[1]) < height:
			carry = height - len(columns[1])
			columns[1] += ordered[2] * carry
		if len(ordered) > 2 and unicorns[ordered[2]] > carry:
			columns += [ordered[2] * (unicorns[ordered[2]] - carry)]
			if len(columns[2]) < height:
				columns[2] += ' ' * (height - len(columns[2]))
		answer = ''.join([''.join(r) for r in zip(*columns)]).replace(' ', '')
		print("Case #%s: %s" % (case, answer))