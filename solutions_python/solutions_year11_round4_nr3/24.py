#!/usr/bin/python

name = 'C-small'
maxN = 1000

prime = [True]*(maxN+1)
prime[0] = prime[1] = False
for i in xrange(2, maxN+1):
	for j in xrange(2*i,maxN+1,i):
		prime[j] = False

def solve(N):
	if N == 1: return 0
	min = 0
	max = 1
	for i in xrange(N+1):
		if not prime[i]: continue
		p = i
		e = 1
		while True:
			p *= i
			if p > N: break
			e += 1
		min += 1
		max += e
	return max-min

fin = open(name+'.in')
fout = open(name+'.out', 'w')

T = int(fin.readline().strip())
for i in xrange(T):
	res = solve(int(fin.readline().strip()))
	fout.write('Case #%s: %s\n' % (i+1, res))

fin.close()
fout.close()
