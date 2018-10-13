#!/bin/sh

fname = 'B-large'

def tokreader(filename):
	for line in open(filename):
		for item in line.strip().split():
			yield item

def readn(n):
    r = []
    for i in xrange(n):
        r.append(read)
    return r

def solve():
	inp = tokreader(fname+'.in')
	read = lambda: inp.next()
	readn = lambda x:[read() for i in xrange(x)]
	outp = open(fname+'.out','w')

	N = int(read())
	for i in range(1,N+1):
		D = int(read())
		P = map(int,readn(D))

		ms = max(P)

		best = 1000
		for eattime in range(1,ms+1):
			st = 0
			for p in P:
				if p > eattime:
					cst = (p - 1) / eattime
					st += cst
			if st + eattime < best:
				best = st + eattime
				print i,st,eattime

		res = 'Case #%d: %d\n'%(i,best)
		print res
		outp.write(res)

	outp.close()
	print 'finished'