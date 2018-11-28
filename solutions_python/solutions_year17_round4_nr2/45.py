#!/usr/bin/env python3

def parse():
	n, c, m = map(int, input().split())
	tc = [[] for _ in range(c)]
	tp = [[] for _ in range(n)]
	for _ in range(m):
		p, b = map(int, input().split())
		tc[b-1].append(p-1)
		tp[p-1].append(b-1)
	return tc, tp

def solve(tc, tp):
	rc = max(len(l) for l in tc)
	lenp = [len(l) for l in tp]
	sump = [len(l) for l in tp]
	for i in range(1,len(sump)):
		sump[i] += sump[i-1]
	rp = max(x//(i+1) + (x%(i+1)!=0) for i, x in enumerate(sump))
	r = max(rc, rp)
	s = 0
	f = 0
	for p, x in enumerate(lenp):
		if x<=r:
			f += r-x
		else:
			k = x-r
			s += k
			f -= k
	return r, s

def main():
	for i in range(int(input())):
		tc, tp = parse()
		r, s = solve(tc, tp)
		print('Case #{}: {} {}'.format(i+1, r, s))

if __name__ == '__main__': main()