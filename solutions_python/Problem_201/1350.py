import bisect
import math

def code():
	N,K = map(int,raw_input().strip().split(' '))
	dictionary = {N:1}
	for i in xrange(K-1):
		n = max(dictionary.keys(), key=int)
		m = dictionary.pop(n,None)
		if K<=m:
			dictionary[n]=m
			break
		n-=1
		n1 = int(math.ceil(n/2.0))
		if n1 in dictionary:
			dictionary[n1]+=m
		else:
			dictionary[n1]=m
		n1 = int(math.floor(n/2.0))
		if n1 in dictionary:
			dictionary[n1]+=m
		else:
			dictionary[n1]=m
		K-=m

	last = max(dictionary.keys(), key=int)-1
	print int(math.ceil(last/2.0)), int(math.floor(last/2.0))

T = input()

for i in xrange(T):
	print "Case #"+str(i+1)+":",
	code()
