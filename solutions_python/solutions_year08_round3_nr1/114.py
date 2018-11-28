#!/usr/bin/env python

from sys import exit, argv, stdin

f=open(argv[1])
N=int(f.readline())

for i in range(N):
	P,K,L = map(lambda i: int(i), f.readline().split(' '))
	ans = 0
	freq=map(lambda i: int(i), f.readline().split(' '))
	freq.sort(reverse=True)
	for x in range(len(freq)):
		ans += (x/K+1)*freq[x]
	print "Case #%d: %d" % (i+1, ans)


