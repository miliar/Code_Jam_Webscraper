#!/usr/bin/env python
import sys

def solve(ne, lines):
	engines = lines[:ne]
	queries = lines[ne:]

	# Coalace into longest runs
	runs = []
	for e in engines:
		n = 0
		ln = 0
		for q in queries:
			if e == q:
				if n > ln:
					runs.append((e, ln, n - 1))
				ln = n + 1
			n += 1
		if n != ln:
			runs.append((e, ln, n - 1))

	# Find minimum spanning tree
	key = lambda x: x[1]
	runs.sort(key=key)
	key = lambda x: x[2]
	runs.sort(key=key, reverse=True)

	end = len(queries)
	best = end + 1
	i = 0
	p = -1
	changes = 0
	while p < end - 1:
		if runs[i][1] <= p + 1 and runs[i][2] > p:
			p = runs[i][2]
			changes += 1
			i = 0
		else:
			i+=1
	if changes == 0:
		changes = 1
	return changes - 1

def main():
	s = sys.stdin

	n = int(s.readline().strip())
	for i in range(n):
		e = int(s.readline().strip())
		input = []
		for j in range(e):
			input.append(s.readline().strip())
		q = int(s.readline().strip())
		for j in range(q):
			input.append(s.readline().strip())
		print "Case #%i: %i" % (i + 1, solve(e, input))

if __name__ == "__main__":
	main()
