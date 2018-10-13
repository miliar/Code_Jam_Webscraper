#!/usr/bin/python
'''
2019 qualification round
Problem C. Fair and Square

Uses a number format of
prefix, middle
where middle is None (represents the empty string) or a integer from 0 to 9
prefix is the first half of digits, excluding the middle digit if there is one
'''
import sys
from math import *
#from pprint import pprint
debug = '-d' in sys.argv
#fh = sys.stdin
fh = open(sys.argv[1])

def splitnum(nn):
	if debug:
		print 'splitnum(%s)' % `nn`
	s = str(nn)
	digits = len(s)
	if digits == 1:
		p = None
		m = int(s)
	elif digits % 2:
		# odd number of digits
		p = int(s[:digits/2])
		m = int(s[digis/2])
	else:
		# even number of digits
		p = int(s[:digits/2])
		m = None
	return [p, m]

def digits(n):
	return int(log10(n)) + 1

def inc(n):
	if debug:
		print 'inc(%s)' % `n`
	p, m = n
	if m != None: # we have a middle digit
		n[1] += 1
		if m != 9:
			return
		if not p:
			n[0] = 1
			n[1] = None
			return
		# m has gone from 9 to 0 so increment p:
	if digits(p+1) == digits(p):
		n[0] += 1
		return
	# number of digits has changed
	if m == None:
		m[0] = 10 ** (digits(p) - 1)
		m[1] = 0
	else:
		m[0] = p + 1
		m[1] = None

def tonum(n):
	if debug:
		print 'tonum(%s)' % n
	p, m = n
	if p:
		s = str(p)
	else:
		s = ''
	#if debug:
	#	print 's=%s, m=%s' % (`s`, `m`)
	m = '%01i' % m if m != None else ''
	return int('%s%s%s' % (s, m, s[::-1]))

def ispal(n):
	s = str(n)
	return s == s[::-1]

cases = int(fh.readline())
for case in range(1, cases+1):
	print 'Case #%i:' % case,
	startsq, endsq = fh.readline().split()
	start = int(ceil(sqrt(int(startsq))))
	end = int(sqrt(int(endsq)))
	if debug:
		print startsq, 'to', endsq, '=>', start, 'to', end
	n = splitnum(start)
	while tonum(n) < start:
		inc(n)
	count = 0
	while True:
		nn = tonum(n)
		if nn > end:
			break
		assert ispal(nn)
		if ispal(nn**2):
			count += 1
			if debug:
				print 'found', nn, nn**2
		inc(n)
	print count
	sys.stdout.flush()
