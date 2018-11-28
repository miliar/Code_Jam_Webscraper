#!/usr/bin/python3

t = int(input())
for c in range(t):
	n, k = map(int, input().strip().split())
	print('Case #%d: %s' % (c + 1, 'ON' if 2**n-1 == k & (2**n-1) else 'OFF'))
