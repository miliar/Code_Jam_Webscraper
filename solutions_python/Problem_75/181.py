#!/usr/bin/python

T = int(raw_input())
for t in xrange(T):
	data = raw_input().split()
	n = int(data[0])
	C = data[1 : n + 1]
	data = data[n + 1 : ]
	m = int(data[0])
	D = data[1 : m + 1]
	data = data[m + 1 : ]
	s = data[1]
	mapping = {}
	Dr = map(lambda x: x[1] + x[0], D)
	conflicts = set(D + Dr)
	for item in C:
		mapping[item[0], item[1]] = item[2]
		mapping[item[1], item[0]] = item[2]
	r = []
	for c in s:
		if len(r) == 0:
			r.append(c)
			continue
		if (r[-1], c) in mapping:
			c = mapping[r[-1], c]
			r.pop()
			r.append(c)
			continue
		if len(set(map(lambda x: x + c, r)).intersection(conflicts)) > 0:
			r = []
			continue
		r.append(c)
	print "Case #%d: %s" % (t + 1, str(r).replace("'", ""))
