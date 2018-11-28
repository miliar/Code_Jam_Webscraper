#!/usr/bin/env python3

def parse():
	s, k = input().split()
	return list(s), int(k)

def solve(s, k):
	n, i, r = len(s), 0, 0
	while i < n:
		if s[i] == '-':
			if i+k > n: return 'IMPOSSIBLE'
			for j in range(i, i+k):
				s[j] = '+' if s[j] == '-' else '-'
			r += 1
		i += 1
	return r

def main():
	for i in range(int(input())):
		s, k = parse()
		r = solve(s, k)
		print('Case #{}: {}'.format(i+1, r))

if __name__ == '__main__': main()