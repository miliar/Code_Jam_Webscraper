#!/usr/bin/python

import math

def main():
	with open("C-large-1.in") as f:
		T = int(f.readline().strip())

		for Tcur in range(1, T+1):
			(a, b) = [int(x) for x in f.readline().strip().split()]
			#print "Finding FAS between %d, %d"  % (a, b)
			print "Case #%d: %s" % (Tcur, foo(a, b))
		f.close()

def foo(a, b):
	return len( squaresOfFairsBetween(a, b) ) 

def squaresOfFairsBetween(a, b):
	res = list()

	if a <= 1 and b >= 1:
		res.append(1)
	if a <= 4 and b >= 4:
		res.append(4)
	
	if a <= 9:
		a = 9
	
	sa = hardNextFair(int(math.sqrt(a))-1)
	sb = int(math.sqrt(b))
	sa2 = pow(sa, 2)

	found = 0
	zz = []

	while sa <= sb:
		#print "%s is fair." % (sa)
		sa2 = pow(sa, 2)
		if sa2 >= a and isFair(sa2):
			res.append(sa2)
			found = 1
			#print "%d^2 = %d" % (sa, sa2)

		if not found:
			sa = hardNextFair(sa)
		else:
			zz = [int(x) for x in list(str(sa))]
			sa = nextFair(zz)
	
	return res

def isFair(n):
	s = str(n)
	d = len(s)
	return all( s[i] == s[d-1-i] for i in range(d / 2) )

def hardNextFair(n):
	n += 1
	while not isFair(n):
		n += 1
	return n

def nextFair(zz):
	d = len(zz)
	dl = (d+1)/2

	base3Inc(zz, dl - 1)
	d = len(zz)

	# Copy to the right side
	for i in range(d/2):
		zz[d-1-i] = zz[i]
	
	ls = ''.join(map(str, zz))
	return int(ls)

def base3Inc(zz, i):
	if i < 0:
		zz.insert(0, 1)
	else:
		zz[i] += 1
		if zz[i] > 2:
			zz[i] = 0
			base3Inc(zz, i-1)

if __name__=="__main__":
	main()
