#!/bin/sh

fname = 'ttt_large'

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
    
def checktable(t):
	lines = tablelines(t)
	cc = False
	for line in lines:
		if '.' in line:
			cc = True
		else:
			if not ('X' in line):
				return 'O won'
			if not ('O' in line):
				return 'X won'
	if cc:
		return "Game has not completed"
	else:
		return "Draw"
		

def solve():
	inp = tokreader(fname+'.in')
	read = lambda: inp.next()
	readn = lambda x:[read() for i in xrange(x)]
	outp = open(fname+'.out','w')

	N = int(read())
	for i in range(1,N+1):
		table = []
		
		for j in range(4):
			table.append(read())
		res = 'Case #%d: %s\n'%(i,checktable(table))
		print res
		outp.write(res)

	outp.close()
	print 'finished'