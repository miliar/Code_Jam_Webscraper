#!/usr/bin/env python

class streamreader:
	def __init__(_, s): _.t = (t for t in s.read().split())
	def __div__(_, t): return (t)(_.t.next())

def solve(N, inherits):
	# supers = {}
	# for i in xrange(1, N + 1):
	# 	supers[i] = []
	# for i in xrange(1, N + 1):
	# 	for j in inherits[i - 1]:
	# 		supers[j].append(i)

	found = set()
	superclasses = {}

	def find_superclasses(i):
		if i not in found:
			classes = set()
			for parent in inherits[i - 1]:
				ps = find_superclasses(parent)
				if not classes.isdisjoint(ps):
					raise 'diagonal'
				classes.update(ps)
			classes.add(i)
			superclasses[i] = classes
			found.add(i)
		return superclasses[i]

	try:
		for i in xrange(1, N + 1):
			find_superclasses(i)
	except:
		return 'Yes'

	return 'No'


import sys
reader = streamreader(sys.stdin)
T = reader/int
for t in xrange(1, T + 1):
	N = reader/int
	inherits = []
	for _ in xrange(N):
		M = reader/int
		inherits.append([reader/int for __ in xrange(M)])
	print 'Case #%d: ' % t, solve(N, inherits)