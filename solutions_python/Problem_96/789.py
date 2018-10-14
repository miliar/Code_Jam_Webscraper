#! /usr/bin/env python

normal = {}
surprise = {}

def add_if_better(group, total, score):
	if total not in group:
		group[total] = 0
	group[total] = max(group[total], score)

for x in range(11):
	for y in range(11):
		for z in range(11):
			if any([abs(m) > 2 for m in x-y, y-z, x-z]):
				continue

			score = max(x,y,z)
			total = x+y+z
			if any([abs(m) == 2 for m in x-y, y-z, x-z]):
				add_if_better(surprise, total, score)
			else:
				add_if_better(normal, total, score)
for i in range(31):
	if i in surprise and i in normal:
		if normal[i] >= surprise[i]:
			del surprise[i]

def best(scores, p, S):
	if not scores:
		return 0
	possible = []
	x, rest = scores[0], scores[1:]
	if x in surprise and S:
		b = best(rest, p, S-1)
		if surprise[x] >= p:
			b += 1
		possible.append(b)
	b = best(rest, p, S)
	if normal[x] >= p:
		b += 1
	possible.append(b)
	return max(possible)

def main(args):
	with open(args[1]) as inp:
		cases = int(inp.readline())
		for i in range(cases):
			line = [int(x) for x in inp.readline().strip().split()]
			N, S, p, scores = line[0], line[1], line[2], line[3:]
			print "Case #%d: %d" % (i+1, best(scores, p, S))

if __name__ == '__main__':
	import sys
	main(sys.argv)