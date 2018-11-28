#!/usr/bin/python



def readfile():
    nrs = []
    with open('bath.in', 'r') as f:
        f.readline()
        for line in f:
			n, k = map(int, line.split())
			nrs.append((n, k))
    return nrs


def solve(n ,k):
	from math import log
	lower = 2**(int(log(k, 2)))
	upper = 2**(int(log(k, 2))+1) - 1
	if upper >= n:
		return 0, 0
	left = n-lower+1
	left -= (upper - lower + 1)
	stalls = left / (upper - lower + 1)
	remainder = left - (stalls * (upper - lower + 1))
	sol1 = stalls / 2
	if k - lower + 1 <= remainder:
		if stalls % 2 == 1:
			return sol1 + 1, sol1 + 1
		else:
			return sol1 + 1, sol1
	if stalls % 2 == 1:
		return sol1 + 1, sol1
	return sol1, sol1


nrs = readfile()
with open('bath.out', 'w') as f:
    for i, bath in enumerate(nrs):
        sol = solve(bath[0], bath[1])
        newline = '\n' if i < len(nrs)-1 else ''
        f.write('Case #%d: %d %d%s' % (i+1, sol[0], sol[1], newline))	
