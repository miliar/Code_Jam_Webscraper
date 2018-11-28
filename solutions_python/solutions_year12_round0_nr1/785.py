#! /usr/bin/env python3
tr = str.maketrans('yfncilwkbouxmeszvdpjrtgahq', 'acbedgfihkjmlonqpsrutwvyxz')
T = int(input())
for i in range(1, T+1):
	print('Case #%d: %s' % (i, input().translate(tr)))
