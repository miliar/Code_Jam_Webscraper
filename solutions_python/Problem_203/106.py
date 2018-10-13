#!/usr/bin/env python3

def parse():
	r, c = map(int, input().split())
	g = []
	for _ in range(r):
		g.append(list(input()))
	return g

def solve(g):
	r, c = len(g), len(g[0])
	l = list(map(lambda s: [x for x in s if x!='?'], g))
	for i, s in enumerate(g):
		if l[i]:
			k = 0
			for j in range(c):
				if s[j]=='?': s[j] = l[i][k]
				else:
					if k+1 < len(l[i]): k += 1
	k = -1
	f = -1
	for i in range(r):
		if '?' not in g[i]:
			k = i
			if f == -1: f = i
		else:
			if k != -1: g[i] = g[k]
	for i in range(r):
		if '?' in g[i]: g[i] = g[f]
	return g

def main():
	for i in range(int(input())):
		g = parse()
		g = solve(g)
		print('Case #{}:'.format(i+1))
		for r in g:
			print(''.join(r))

if __name__ == '__main__': main()