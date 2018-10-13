#!/usr/bin/env pypy
import sys, os
# Cases
t = int(sys.stdin.readline())

for i in xrange(t):
	data = list()
	for j in xrange(4):
		data.append(sys.stdin.readline().rstrip('\n'))
	sys.stdin.readline()
	result = 'Draw'
	for j in xrange(4):
		if '.' in data[j]:
			result = 'Game has not completed'
	# check lines
	for j in xrange(4):
		markset = set(data[j]) - set('T')
		if ('.' not in markset) and len(markset) == 1:
			result = list(markset)[0] + ' won'
	for j in xrange(4):
		markset = set(map(lambda x: x[j], data)) - set('T')
		if ('.' not in markset) and len(markset) == 1:
			result = list(markset)[0] + ' won'
	markset = set([data[j][j] for j in xrange(4)]) - set('T')
	if ('.' not in markset) and len(markset) == 1:
		result = list(markset)[0] + ' won'
	markset = set([data[j][3-j] for j in xrange(4)]) - set('T')
	if ('.' not in markset) and len(markset) == 1:
		result = list(markset)[0] + ' won'
	print "Case #%d: %s" % (i+1, result)
