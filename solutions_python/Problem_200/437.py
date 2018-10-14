#!/usr/bin/env python3

def parse():
	n = int(input())
	return n

def solve(n):
	s = list(map(int, str(n)))
	i, k = len(s)-2, len(s)
	while i >= 0:
		if s[i] > s[i+1]:
			s[i] -= 1
			k = i+1
		i -= 1
	return int(''.join(map(str, s[:k])) + '9'*(len(s)-k))

def main():
	for i in range(int(input())):
		n = parse()
		r = solve(n)
		print('Case #{}: {}'.format(i+1, r))

if __name__ == '__main__': main()