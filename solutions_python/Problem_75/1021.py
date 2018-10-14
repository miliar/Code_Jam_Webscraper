#!/usr/bin/python

import sys

def solve(combine, oppose, base):
	out = []
	for i in range(len(base)):
		if len(out) > 0 and base[i] + out[-1] in combine:
			out[-1] = combine[base[i]+out[-1]]
		elif base[i] in oppose and oppose[base[i]] in out:
			out = []
		else:
			out.append(base[i])
	return out



T = int(sys.stdin.readline())
lines = sys.stdin.readlines()

for t in range(T):
	parts = lines[t].split()
	p = 0
	C = int(parts[0])
	combine = {}
	oppose = {}
	for c in range(C):
		comb = parts[c+1]
		combine[comb[0]+comb[1]] = comb[2]
		combine[comb[1]+comb[0]] = comb[2]
	p += 1 + C
	D = int(parts[p])
	for d in range(D):
		opp = parts[p+d+1]
		oppose[opp[0]] = opp[1]
		oppose[opp[1]] = opp[0]
	p += 1 + D
	N = int(parts[p])
	b = parts[p+1:][0]
	base = [b[x] for x in range(len(b))]
	sol = solve(combine, oppose, base)
	print "Case #" + str(t+1) + ": [" + ', '.join(sol) + "]"
