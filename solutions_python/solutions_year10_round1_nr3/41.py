import sys
import operator

sys.setrecursionlimit(2000)

M = 1000001
ra = {1:(1,1), 2:(2,3), 3:(2,0)}
start=4
for n in range(3,M):
	nmax = ra[n][0]+n-1
	ra[n]=(ra[n][0],nmax)
	for k in range(start, nmax+1):
		ra[k]=(n,0)
	start = nmax+1

def readn(f, n):
	return [f.readline().rstrip('\n') for i in range(n)]

fileName = "C-small-attempt0"	
f = open(fileName+".in", 'r')

test = int(f.readline())

def solve(A1, A2, B1, B2):
	s = 0
	for a in range (A1, A2+1):
		ran = ra[a]
		if B1 > ran[1]: continue
		if B2 < ran[0]: continue
		sta = min(ran[1],B2)

		end = max(ran[0], B1)

		s += (-end+sta+1)
	return (A2-A1+1)*(B2-B1+1) - s

for ii in range(test):
	(A1, A2, B1, B2) = map(int, f.readline().split())
	print("Case #{0}: {1}".format(ii+1, solve(A1, A2, B1, B2)))