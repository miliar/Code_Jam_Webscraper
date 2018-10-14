#!/usr/bin/python
'''
2013 qualification round
Problem B. Lawnmower
'''
import sys
from pprint import pprint
debug = '-d' in sys.argv
#fh = sys.stdin
fh = open(sys.argv[1])
cases = int(fh.readline())
for case in range(1, cases+1):
	print 'Case #%i:' % case,
	N, M = [ int(i) for i in fh.readline().split() ]
	# N rows, M columns
	lawn = []
	for i in range(N):
		lawn += [ int(i) for i in fh.readline().split() ]
	if debug:
		print '- %i rows, %i columns' % (N, M)
		for y in range(N):
			print lawn[y*M:(y+1)*M]
	rowmax = [ max(lawn[i*M:(i+1)*M]) for i in range(N) ]
	colmax = [ max(lawn[i::M]) for i in range(M) ]
	if debug:
		print 'rowmax:', rowmax
		print 'colmax:', colmax
	cando = True
	for i in range(len(lawn)):
		if lawn[i] < rowmax[i / M] and lawn[i] < colmax[i % M]:
			cando = False
			if debug:
				print 'Can\'t do lawn[%i]=%i (%i,%i)' % (i, lawn[i], i % M, i / M)
			break
	if cando:
		print 'YES'
	else:
		print 'NO'
	sys.stdout.flush()
