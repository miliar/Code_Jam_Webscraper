import math
import sys

c = int(sys.stdin.readline())
for x in range(0, c):
	i = sys.stdin.readline().split()
	r,k,n = map(int, i)

	i = sys.stdin.readline().split()
	g = map(int, i)

	pos = 0
	tot = 0
	for i in range(0, r):
		nb = 0
		t = 0
		while nb < k:
			if t == n:
				break
			elif k-nb >= g[pos]:
				nb += g[pos]
				pos = (pos+1)%n
			else:
				break
			t=t+1
		tot += nb

	print "Case #"+str(x+1)+":", tot
