#!/usr/bin/env python

n = int(raw_input())

rep = {'z':'q','q':'z','a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

for i in xrange(n):
	line = raw_input()
	r = []
	for j in xrange(len(line)):
		r.append(rep.get(line[j],' '))
	res = ''.join(r)
	print "Case #%d: %s" % (i+1, res)

