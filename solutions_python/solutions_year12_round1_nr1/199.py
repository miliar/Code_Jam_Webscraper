#!/usr/bin/python -OO
'''
Google codejam template
'''
import sys
#fh = sys.stdin
fh = open(sys.argv[1])

cases = int(fh.readline())

debug = 0
for case in range(1, cases+1):
	print 'Case #%i:' % case,
	a, b = [ int(i) for i in fh.readline().split() ]
	# a = typed characters
	# b = total characters in password
	p = [ float(i) for i in fh.readline().split() ]
	assert a == len(p) 
	avgbest = 100
	# just press enter, then enter full password
	avgbest = 2 + b
	# press backspace then finish password:
	pright = 1.0
	for keep in range(a+1):
		if keep > 0:
			pright *= p[keep-1]
		pwrong = 1 - pright
		avg = pright * ((a-keep) + (b-keep)+1) \
		   + pwrong * ((a-keep) + (b-keep) + b + 2)
		if avg < avgbest:
			avgbest = avg
	print avgbest
