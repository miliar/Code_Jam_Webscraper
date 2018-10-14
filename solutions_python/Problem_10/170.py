#!/usr/bin/env python


import sys

def min_presses(places, keys, occurences) :
	o = list(occurences)
	o.sort()
	o.reverse()
	result = 0
	i = 0
	s = len(o)
	idx = 1
	while i < s :
		result += reduce(int.__add__, o[i:i + keys]) * idx
		idx += 1
		i += keys
	return result


test_cnt = int(sys.stdin.readline())

for i in xrange(test_cnt) :
	places, keys, letters = tuple([int(x) for x in sys.stdin.readline().split()])
	occurences = [int(x) for x in sys.stdin.readline().split()]
	if keys * places < letters :
		print 'Case #%d: Impossible' % i+1
	else :
		print 'Case #%d: %d' % (i+1, min_presses(places, keys, occurences))

