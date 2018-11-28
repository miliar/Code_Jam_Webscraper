#!/usr/bin/python

n = int(raw_input())
for i in xrange(1, n+1):
	s = int(raw_input())
	dict = {}
	for j in xrange(s):
		dict[raw_input()] = 0
	q = int(raw_input())
	result = 0
	count = 0
	for j in xrange(q):
		query = raw_input()
		if dict.has_key(query) and dict[query] == result:
			dict[query] = dict[query] + 1
			count = count + 1
			if count == len(dict):
				count = 1
				result = result + 1
				dict[query] = dict[query] + 1
	print "Case #%d: %d" % (i, result)
