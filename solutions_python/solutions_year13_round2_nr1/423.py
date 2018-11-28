import os
import sys


# expand x by the most size
def expand(x):
	return x*2-1

def getMinOps(a,n,s):
	if a == 1:
		return n

	# e[i] is the number of expandings needed to absort s[i]
	e = [0] * (n+1)
	currSize = a
	for i in range(n):
		# compute e[k]
		while currSize <= s[i]:
			currSize = expand(currSize)
			e[i] += 1
		currSize += s[i]
		# print currSize

	
	minOps = n
	sume = 0
	for i in range(n+1):
		minOps = min(minOps, sume + n-i)
		sume += e[i]

	return minOps


f = open(sys.argv[1])
t = int(f.readline())
for k in range(t):

	a,n = [int(x) for x in f.readline().split(' ')]
	s = [int(x) for x in f.readline().split(' ')]
	s.sort()
	# print a, n, s

	minOps = getMinOps(a,n,s)
	print 'Case #'+str(k+1)+': '+str(minOps)

f.close()
