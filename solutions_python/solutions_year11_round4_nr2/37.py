from math import *
inf = open("in.txt", "r")
ouf = open('out.txt','w')

def close_files():
	inf.close
	ouf.close

def precount():
	pass

printcounter = 0
def printstr(a):
	global printcounter
	printcounter +=1
	print >>ouf, 'Case #%d: %s' % (printcounter,a)
	#print >>ouf, 'Case #%d: %.5f %.5f' % (printcounter,a)
	#print >> ouf, st
	#print st
	
def gcd(a,b):
	while a:
		a, b = b % a, a
	return b
	
def lcm(a,b):
	return a * b / gcd(a, b)
#harmony
def solvetest():
	global printcounter
	r, c, d = map(int, inf.readline().split())
	a = []
	for i in xrange(r):
		a.append(map(int, list(inf.readline().strip())))
	k = min(r,c)
	while k >= 3:
		found = 0
		
		for i in xrange(r-k+1):
			for j in xrange(c-k+1):
				mi, mj = 0, 0
				ci, cj = i + float(k-1)/2, j + float(k-1)/2
				for ii in xrange(k):
					for jj in xrange(k):
						mi += (i+ii-ci)*a[i+ii][j+jj]
						mj += (j+jj-cj)*a[i+ii][j+jj]
				mi -= (i+0-ci)*a[i+0][j+0]
				mj -= (j+0-cj)*a[i+0][j+0]
				
				mi -= (i+0-ci)*a[i+0][j+k-1]
				mj -= (j+k-1-cj)*a[i+0][j+k-1]
				
				mi -= (i+k-1-ci)*a[i+k-1][j+0]
				mj -= (j+0-cj)*a[i+k-1][j+0]
				
				mi -= (i+k-1-ci)*a[i+k-1][j+k-1]
				mj -= (j+k-1-cj)*a[i+k-1][j+k-1]
				#print i,j,mi,mj,k
				if mi*mi+mj*mj< 1e-9:
					printstr(str(k))
					return
		k-=1
	printstr("IMPOSSIBLE")

precount()
testnum = int(inf.readline())
for test in xrange(testnum):
	solvetest()
close_files()
