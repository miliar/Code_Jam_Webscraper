#!/usr/bin/python
# Python 2.6.5
# Google Code Jam 2011: Problem B (Magicka)

import sys

T = int(sys.stdin.readline())
for case in xrange(1,T+1):
	line = sys.stdin.readline().split()
	comb = {}
	opp = {}
	ptr = 1
	for cstring in line[1:1+int(line[0])]:
		comb[cstring[:2]] = cstring[2]
		comb[cstring[1::-1]] = cstring[2]
		ptr += 1
	D = int(line[ptr])
	ptr += 1
	for dstr in line[ptr:ptr+D]:
		opp.setdefault(dstr[0], []).append(dstr[1])
		opp.setdefault(dstr[1], []).append(dstr[0])
		ptr += 1
	N = int(line[ptr])
	ptr += 1
	elist = []
	for el in line[ptr]:
		#print elist, el
		if len(elist) > 0 and (elist[-1]+el) in comb:
			elist[-1] = comb[elist[-1]+el]
		elif el in opp:
			for d in opp[el]:
				if d in elist:
					elist = []
					break
			else:
				elist.append(el)
		else:
			elist.append(el)
	print "Case #{0}: [{1}]".format(case, ', '.join(elist))
