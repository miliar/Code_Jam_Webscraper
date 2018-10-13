#!/bin/sh

fname = 'lawn_large'

def tokreader(filename):
	for line in open(filename):
		for item in line.strip().split():
			yield item

def readn(n):
    r = []
    for i in xrange(n):
        r.append(read)
    return r
    
def tablelines(t):
	r = []
	for k in range(4):
		r.append([t[k][i] for i in range(4)])
	for k in range(4):
		r.append([t[i][k] for i in range(4)])
	r.append([t[i][i] for i in range(4)])
	r.append([t[3-i][i] for i in range(4)])
	return r
    
def checktable(b,n,m):
	rowmin = [min(r) for r in b]
	rowmax = [max(r) for r in b]
	cols = [[b[k][i] for k in range(n)] for i in range(m)]
	colmin = [min(c) for c in cols]
	colmax = [max(c) for c in cols]
	for i in range(n):
		for j in range(m):
			if not ((b[i][j]==rowmax[i]) or (b[i][j]==colmax[j])):
				return "NO"
	return "YES"

def solve():
	inp = tokreader(fname+'.in')
	read = lambda: inp.next()
	readn = lambda x:[read() for i in xrange(x)]
	outp = open(fname+'.out','w')

	T = int(read())
	for i in range(1,T+1):
		n,m = map(int,readn(2))
		b = []
		for j in range(n):
			r = []
			for k in range(m):
				r.append(int(read()))
			b.append(r)
			
		print b
		res = 'Case #%d: %s\n'%(i,checktable(b,n,m))
		print res
		outp.write(res)

	outp.close()
	print 'finished'