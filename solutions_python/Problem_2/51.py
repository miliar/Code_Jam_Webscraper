from __future__ import with_statement
import math

def readTimes(f):
	d, a = f.readline().strip().split()
	d = int(d[0:2]) * 60 + int(d[3:5])
	a = int(a[0:2]) * 60 + int(a[3:5])
	return (d, a)

def calcMin(list):
	v = m = 0
	for time, type in list:
		if type == "a":
			v += 1
		else:
			v -= 1
			m = min(m, v)
	return m

def processFile(f, outf):
	numCases = int(f.readline())
	for caseNumber in xrange(1, numCases + 1):
		turnaround = int(f.readline())
		na, nb = map(int, f.readline().strip().split())
		
		lista = []
		listb = []
		
		for i in xrange(na):
			d, a = readTimes(f)
			lista.append((d, "d"))
			listb.append((a + turnaround, "a"))
		
		for i in xrange(nb):
			d, a = readTimes(f)
			listb.append((d, "d"))
			lista.append((a + turnaround, "a"))
			
		lista.sort()
		listb.sort()
	
		ma = -calcMin(lista)
		mb = -calcMin(listb)
		s = "Case #" + str(caseNumber) + ": " + str(ma) + " " + str(mb)
		print s
		print >> outf, s

	


input = "B-large"
with open(input + ".in") as f:
	with open(input + ".out", "w") as fout:
		processFile(f, fout)
print "OK!"