#! /usr/bin/env python3
T = int(input())
for i in range(T):
	fields = input().split()
	C = int(fields[0])
	comb = {}
	for f in fields[1:1+C]:
		comb[frozenset(f[:2])] = f[2]
	D = int(fields[1+C])
	opp = set()
	for f in fields[2+C:2+C+D]:
		opp.add(frozenset(f))
	els = []
	for e in fields[3+C+D]:
		if not els:
			els = [e]
		else:
			fset = frozenset((els[-1], e))
			if fset in comb:
				els[-1] = comb[fset]
			elif any(frozenset((e, f)) in opp for f in els):
				els = []
			else:
				els.append(e)
	print('Case #%d: [%s]' % (i+1, ', '.join(els)))