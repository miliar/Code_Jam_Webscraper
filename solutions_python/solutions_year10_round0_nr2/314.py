#!/usr/bin/env python

def myabs(a):
	if a < 0:
		return long(-a)
	return long(a)
def myceil(a,b):
	r = long(a)%long(b)
	if r == 0:
		return long(a/b)
	return long((a+b-r)/b)
def mygcd(x,y):
	while x:
		x, y= y%x, x
	return y

#f = open('in.random', 'r')
f = open('B-large.in', 'r')
c = int(f.readline())
count = 0
for line in f:
	count += 1
	if (count > c):
		break
	ti = line.split()
	n = int(ti[0])
	for i in range(1,n+1):
		ti[i] = long(ti[i])
	T,ind = 0,2
	while T == 0:
		T = myabs(ti[1] - ti[ind])
		ind += 1
	for i in range(1,n):
		for j in range(i+1,n+1):
			if ti[i] != ti[j]:
				T = mygcd(T,myabs(ti[i]-ti[j]))
			if T == 1:
				break
	y = T*myceil(ti[1],T) - ti[1]
	print 'Case #' + str(count) + ': '+ str(y)
