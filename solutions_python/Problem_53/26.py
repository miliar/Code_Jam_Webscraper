import sys
import operator

def readn(f, n):
	return [f.readline().rstrip('\n') for i in range(n)]
	
f = open("A-large.in", 'r')

test = int(f.readline())

def check(N,K):
	return (((K+1) >> N) << N) == K+1

for tt in range(test):
	(N,K) = map(int,f.readline().split())
	if check(N,K): print("Case #{0}: {1}".format(tt+1, "ON" ))
	else: print("Case #{0}: {1}".format(tt+1, "OFF" ))