#!/usr/bin/python
def timeToMin(s):
	a = map(int,s.split(":"))
	return a[0]*60+a[1]
	
	
fin = open("b.in","r")
fout = open("b.out","w")

n = int(fin.readline())

LEN = 1440

for i in range(n):
	
	t = int(fin.readline())
	na, nb = map(int, fin.readline().split())
	
	
	a = [0]*(LEN+t)
	b = [0]*(LEN+t)
	
	for j in range(na):
		t1, t2 = map(timeToMin, fin.readline().split())
		t2 += t
		a[t1] -= 1
		b[t2] += 1
	
	for j in range(nb):
		t1, t2 = map(timeToMin, fin.readline().split())
		t2 += t
		b[t1] -= 1
		a[t2] += 1
		
	at = 0
	s = 0
	for k in a:
		s += k
		if s < 0:
			at -= s
			s = 0
		
	bt = 0
	s = 0
	for k in b:
		s += k
		if s < 0:
			bt -= s
			s = 0
	
	print >> fout, "Case #%d: %d %d" % (i+1, at, bt)
	print "Case #%d: %d %d" % (i+1, at, bt)
		