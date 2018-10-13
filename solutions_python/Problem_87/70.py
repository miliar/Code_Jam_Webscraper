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
	print >>ouf, 'Case #%d: %.6f' % (printcounter,a)
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
	x, s, r, t, n = map(int, inf.readline().split())
	cur = 0
	a = []
	for i in xrange(n):
		b, e, w = map(int, inf.readline().split())
		if b > cur:
			a.append([0, cur, b])
		a.append([w, b, e])
		cur = e
	if cur != x:
		a.append([0, cur, x])
	
	a.sort()
	time = 0.0
	for i in xrange(len(a)):
		l1 = min(t*(r+a[i][0]), a[i][2]-a[i][1])
		time += float(l1) / (r+a[i][0]) + float(a[i][2]-a[i][1]-l1) / (a[i][0]+s)
		t = t - float(l1) / (r+a[i][0])
	printstr(time)

precount()
testnum = int(inf.readline())
for test in xrange(testnum):
	solvetest()
close_files()
