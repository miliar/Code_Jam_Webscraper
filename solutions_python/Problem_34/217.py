#!/usr/bin/python

import re
import sys

input = sys.stdin
wordlen, numwords, numcases = map(int, input.readline().strip().split(" "))

# Load words and cases
# No harm in loading these; only 5000 cases max.
words = [ input.readline().strip() for _ in range(numwords) ]
cases = [ input.readline().strip() for x in range(numcases) ]

id = 0
for case in cases:
	id += 1
	# Construct a regular expression for every case.
	r = "^" + case.replace("(", "[").replace(')', ']') + "$"
	r = re.compile(r)
	n = 0
	for w in words:
		if r.match(w):
			n += 1
	print "Case #%d: %d" % (id, n)
