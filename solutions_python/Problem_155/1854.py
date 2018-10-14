#!/usr/bin/env python

import sys, os

def solve(Smax, audience ) :
	'''
	Find necessary # of people to get the standing ovation
	'''

	Smax = int(Smax)
	people = []
	for a in audience :
		people.append( int(a) )

	if Smax+1 != len(people) :
		print >>sys.stderr, "Error! Smax (%d) does not agree with length of audience (%d)" %(Smax, len(people))
		sys.exit(-1)

	ntotal = 0 #number of people in standing.
	nneed = 0 #number of people to invite to make the standing ovation

	for i, n in enumerate(people) :
		if i <= ntotal :
			ntotal += n
			#print 'OK', i, n, ntotal, nneed
		else :
			nneed += i-ntotal
			ntotal += i-ntotal+n
			#print 'Adding', i, n, ntotal, nneed

	return nneed

if __name__ == '__main__' :

	fn = sys.argv[1]
	fp = open( fn )

	T = int(fp.readline().strip())

	for i in xrange(1, T+1) :
		Smax, audience = fp.readline().split()
		print "Case #%d: %d"%( i, solve(Smax, audience) )
