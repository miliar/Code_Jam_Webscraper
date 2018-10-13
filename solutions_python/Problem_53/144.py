#!/usr/bin/env python

def snapper_chain(n, k):
	return not (k+1)%(2<<(n-1))

def solveCase():
	n, k = [eval(x) for x in raw_input().split(' ')]
	return snapper_chain(n,k) and 'ON' or 'OFF'

def outputCase(i):
	print "Case #%d: %s" % (i+1, solveCase())

def main():
	ncase = input()
	for i in xrange(ncase):
		outputCase(i)
	pass

if __name__ == "__main__":
	main()
