import math
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
	print >>ouf, 'Case #%d: ' % (printcounter)
	for i in a:
		print >>ouf, '%.6f' % (i)
	#print >>ouf, 'Case #%d: %.5f %.5f' % (printcounter,a)
	#print >> ouf, st
	#print st

def solvetest():
	n = int(inf.readline())
	a = []
	for i in xrange(n):
		a.append(list(inf.readline().strip()))
	wp = []
	for i in xrange(n):
		wp.append([0.0,0.0])
		#c = 0
		for j in a[i]:
			if j != '.':
				wp[i][1] += 1
				wp[i][0] += int(j)
	# wp counted
	owp = [];
	for  i in xrange(n):
		owp.append(0.0)
		c = 0
		for j in xrange(n):
			if a[i][j] == '.' or wp[j][1] == 1:
				continue
			owp[i] += (wp[j][0] - int(a[j][i])) / (wp[j][1] - 1)
			c+=1
		if c != 0:
			owp[i] /= c
	oowp = []
	for i in xrange(n):
		oowp.append(0.0)
		c = 0
		for j in xrange(n):
			if a[i][j] == '.':
				continue
			oowp[i] += owp[j]
			c += 1
		if c != 0:
			oowp[i] /= c
	rpi = []
	for i in xrange(n):
		rpi.append(0.25 * wp[i][0]/wp[i][1] + 0.5 * owp[i] + 0.25 * oowp[i])
	printstr(rpi)
	
precount()
testnum = int(inf.readline())
for test in xrange(testnum):
	solvetest()
close_files()
