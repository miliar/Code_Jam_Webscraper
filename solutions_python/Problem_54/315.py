#!/usr/bin/env python

def gcd(a, b):
	m = a
	while m:
		a = b
		b = m
		m = a % b
	return b

def solve(events):
	events = list(set(events))
	events.sort()
	#print events
	diffs = map(lambda a,b:a-b, events[1:], events[:-1])
	#print diffs
	g = reduce(gcd, diffs)
	return (-events[1]) % g

def solveCase():
	events = [eval(x) for x in raw_input().split(' ')][1:]
	return solve(events)

def outputCase(i):
	print "Case #%d: %s" % (i+1, solveCase())

def main():
	ncase = input()
	for i in xrange(ncase):
		outputCase(i)
	pass

if __name__ == "__main__":
	main()
