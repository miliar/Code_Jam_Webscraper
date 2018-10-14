from __future__ import division
import sys

def solve(l,llen):
	eat = [l[i-1]-l[i] for i in range(1,llen) if l[i-1]>l[i]]
	eat.append(0)
	m1 = sum(eat)
	k = max(eat)
	m2 = 0
	for i in range(1,llen):
		if(l[i-1]-k<0):
			m2 += l[i-1]
		else:
			m2 += k
	return m1,m2

def main():
	with sys.stdin as inp:
		casos = int(inp.readline())
		for caso in range(casos):
			llen = int(inp.readline())
			l = [int(s) for s in inp.readline().split()]
			m1,m2 = solve(l,llen)
			print('Case #{}: {} {}'.format(caso+1,m1,m2))

main()
