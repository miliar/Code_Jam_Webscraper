import bisect
import math

def test():
	N,K = map(int,raw_input().strip().split(' '))
	l = [N]
	for i in xrange(K-1):
		n = max(l)
		c = l.count(n)
		if K<=c:
			break
		l = list(filter(lambda a: a!=n, l))
		n-=1
		l+=[int(math.ceil(n/2.0))]*c
		l+=[int(math.floor(n/2.0))]*c
		K-=c

	last = max(l)-1
	print int(math.ceil(last/2.0)), int(math.floor(last/2.0))

T = input()

for i in xrange(T):
	print "Case #"+str(i+1)+":",
	test()