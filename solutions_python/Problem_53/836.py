#!/usr/bin/env python

if __name__ == '__main__':
	filestream = open('A-large.in')
	T = int(filestream.readline())
	snappers = []
	for testcase in xrange(T):
		case = filestream.readline()
		parts = case.split(' ')
		N = int(parts[0])
		K = int(parts[1])
		if K&(2**N-1)==2**N-1:
			print 'Case #%d: ON'%(testcase+1)
		else:
			print 'Case #%d: OFF'%(testcase+1)