#!/usr/bin/env python3

from math import ceil, floor

def parse():
	n, p = map(int, input().split())
	r = list(map(int, input().split()))
	q = []
	for _ in range(n):
		q.append(list(map(int, input().split())))
	return r, q

def serv(s, p):
	q = p/s
	l = ceil(q/1.1)
	h = floor(q/0.9)
	return (l, h)

def valid(s):
	l, h = 0, float('inf')
	for sl, sh in s:
		l, h = max(l, sl), min(h, sh)
	return l <= h

def solve(r, q):
	p = []
	for i, l in enumerate(q):
		p.append(sorted(map(lambda x: serv(r[i], x), l)))
	n, m = len(p), len(p[0])
	k = [0]*n
	s = 0
	while True:
		if any(x >= m for x in k): break
		l = [x[k[i]] for i, x in enumerate(p)]
		if valid(l):
			s += 1
			for i in range(n): k[i] += 1
		else:
			i, _ = min(enumerate(l), key=lambda x: x[1][1])
			k[i] += 1
	return s

def main():
	for i in range(int(input())):
		r, q = parse()
		s = solve(r, q)
		print('Case #{}: {}'.format(i+1, s))

if __name__ == '__main__': main()