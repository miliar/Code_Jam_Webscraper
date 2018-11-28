#!/usr/bin/env python

T = int(raw_input())
for i in range(T):
	data = raw_input().split()
	C = int(data[0])
	D = int(data[C+1])
	N = int(data[C+D+2])
	combs = dict((x[:2], x[2]) for x in data[1:C+1])
	combs.update(dict((x[1]+x[0], x[2]) for x in data[1:C+1]))
	opp = dict((x, []) for x in ["Q", "W", "E", "R", "A", "S", "D", "F"])
	for x in data[C+2:C+D+2]:
		opp[x[0]].append(x[1])
		opp[x[1]].append(x[0])
	elemlist = []
	for x in data[-1].rstrip():
		elemlist.append(x)
		if ''.join(elemlist[-2:]) in combs.keys():
			elemlist = elemlist[:-2] + [combs[''.join(elemlist[-2:])]]
		else:
			for k in opp[x]:
				if k in elemlist:
					elemlist = []
	print "Case #%d: [%s]" % (i+1, ", ".join(elemlist))
