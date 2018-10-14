#!/usr/bin/env python

import sys

def main():
	with open(sys.argv[1]) as f:
		solve(f)

def solve(f):
	lines = f.readlines()
	T = int(lines[0])
	b = 1
	for i in range(1, T+1):
		N = int(lines[b])
		wires = []
		for l in range(b+1, b+N+1):
			wire = map(int, lines[l].split())
			wires.append(wire)
		b += N+1
		answer = solve_real(wires)
		print "Case #%d: %s" % (i, answer)

def solve_real(wires):
	r = 0
	for i in range(len(wires)):
		for j in range(i+1, len(wires)):
			if wires[i][0] < wires[j][0] and wires[i][1] > wires[j][1]:
				r += 1
			elif wires[i][0] > wires[j][0] and wires[i][1] < wires[j][1]:
				r += 1
	return r

if __name__ == '__main__':
	main()