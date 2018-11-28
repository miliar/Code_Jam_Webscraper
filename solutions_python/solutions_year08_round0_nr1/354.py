#!/usr/bin/env python
from sys import argv

f = open(argv[1])
N = int(f.readline())

for i in range(N):
	S = int(f.readline())
	search_engines = []
	for se in range(S): search_engines.append(f.readline()[:-1])

	Q = int(f.readline())
	queries = []
	for qu in range(Q): queries.append(f.readline()[:-1])

	switches = 0
	position = 0
	while(position < Q):
		num_found = 0
		for se in search_engines:
			if se in queries[position:]: num_found += 1
		if num_found < S:
			break
#		print queries[position:]
#		print map(lambda s: queries[position:].index(s), search_engines)
		position += max(map(lambda s: queries[position:].index(s), search_engines))
		switches += 1
	print "Case #%d: %d" % (i+1, switches)



