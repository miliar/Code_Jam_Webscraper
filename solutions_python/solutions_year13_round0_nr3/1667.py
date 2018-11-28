

from sys import stdin
from math import sqrt, ceil, floor
from collections import defaultdict

def is_p(x):
	for y in range(len(x)/2):
		if x[y] != x[len(x)-y-1]: return False
	return True

def f(a,b):
	l = []
	a = long(ceil(sqrt(a)))
	b = long(floor(sqrt(b)))
	c = 0
	for x in range(a, b+1):
		if is_p(str(x)) and is_p(str(x*x)):
			#print x, x*x
			c += 1
			l.append(x*x)
	return l 

def r():
	a = 1
	b = 1 
	while True:
		cur = 0
		#print 'range start: ', a,b
		while cur == 0:
			cur = f(a,b)
			b += 1
		print "found ", a,b, b-1, int(sqrt(b-1))
		a = b + 1
		b = a



def g(x):
	s = len(str(x))
	if s == 1: return 3 
	if s == 2: return 2
	pp = 3
	p = 2
	cur = 0
	for x in range(3,s+1):
		if x % 2 != 0:
			cur = p + pp
		else:
			cur = p - pp
		pp = p
		p = cur
	return cur
		

if __name__ == '__main__':
	T = int(stdin.readline())
	#l = f(1,10**14)
	l = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L]
	for t in range(1, T+1):
		a,b = stdin.readline().strip().split()
		a,b = long(a), long(b)
		c = 0
		for x in l:
			if x >= a and x <= b: 
				c += 1
		print "Case #" + str(t)+': ' + str(c)
	
	 
