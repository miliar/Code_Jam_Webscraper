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
		C,F,X = map(float,readn(3))
		
		best = X / 2.0
		ctime = 0
		cfnum = 0
		
		while (ctime < best):
			prodrate = float(cfnum) * F + 2.0
			timeforfinish = X / prodrate
			if (ctime + timeforfinish < best):
				best = ctime + timeforfinish
			timefornext = C / prodrate
			
			ctime += timefornext
			cfnum += 1


		res = 'Case #%d: %.7f\n'%(i,best)
		print res
		outp.write(res)

	outp.close()
	print 'finished'