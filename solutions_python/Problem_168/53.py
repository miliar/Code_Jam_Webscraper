#!/bin/sh

#fname = 'A-small-attempt0'
fname = 'A-large'
#fname = 'A-example'

from itertools import *

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

	checkerror = 0

	T = int(read())
	for j in range(1,T+1):
		R,C = map(int,readn(2))
		cells = readn(R)
		
		imposs = False
		
		cnt = 0
		
		for r in range(len(cells)):
			for c in range(len(cells[0])):
				if cells[r][c] != '.':
					upok = False
					for i in range(r-1,-1,-1):
						if cells[i][c] != '.':
							upok = True			

					downok = False
					for i in range(r+1,R):
						if cells[i][c] != '.':
							downok = True
							
					leftok = False
					for i in range(c-1,-1,-1):
						if cells[r][i] != '.':
							leftok = True				

					rightok = False
					for i in range(c+1,C):
						if cells[r][i] != '.':
							rightok = True				

					ok = ((upok and (cells[r][c] == '^')) or (downok and (cells[r][c] == 'v')) or
						   (leftok and (cells[r][c] == '<')) or (rightok and (cells[r][c] == '>')))
					
#					print r,c,upok,downok,leftok,rightok,ok	
					
					if not ok:
						if (not upok) and (not downok) and (not rightok) and (not leftok):
							imposs = True
						else:
							cnt += 1
					

		if imposs:
			res = 'Case #%d: IMPOSSIBLE\n'%(j)
		else:
			res = 'Case #%d: %d\n'%(j,cnt)
		print res
		outp.write(res)
		

	outp.close()
	print 'finished'
