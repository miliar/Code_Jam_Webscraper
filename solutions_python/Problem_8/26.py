import sys
sys.stdin = file('b.in')
sys.stdout = file('b.out','w')
import psyco
q = [None] * 1500000
def isprime(n):
	if n < 10:
		return n in (2,3,5,7)
	if n%2 == 0:
		return False
	try:
		if q[n] is not None:
			return q[n]
	except:
		pass
	i=3
	while i * i <= n:
		if n%i == 0:
			q[n] = False
			return False
		i += 2
	q[n] = True
	return True

def getp(d, x):
	s = x
	while d[x] > 0:
		x = d[x]
	while d[s] > 0:
		ns = d[s]
		d[s] = x
		s = ns
	return x

def merge(d,a,b):
	pa = getp(d,a)
	pb = getp(d,b)
	if pa == pb:
		return
	if abs(d[pa])<abs(pb):
		d[pb] = d[pa]+d[pb]
		d[pa] = pb
	else:
		d[pa] = d[pa]+d[pb]
		d[pb] = pa

def sss():
	cn = int(raw_input())
	for case in xrange(cn):
		a,b,P = [int(x) for x in raw_input().split()]
		d = [-1]*(b-a+1)
		mm = b-a+2
		for p in xrange(P, mm):
			if isprime(p):
				x = a//p*p
				while x < a:
					x += p
				s = x
				while x <= b:
					merge(d,s-a,x-a)
					x += p
		sol = sum(1 for x in d if x < 0)
		print "Case #%d: %d" % (case+1, sol)

psyco.full()
sss()
