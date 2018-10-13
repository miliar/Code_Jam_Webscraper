# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 02:28:14 2015

@author: leello
"""

def twpod(x, y):
	table = {
	('1', '1'):'1',
	('1', 'i'): 'i',
	('1', 'j'): 'j',
	('1', 'k'): 'k',

	('i', '1'): 'i',
	('i', 'i'): '-1',
	('i', 'j' ): 'k',
	('i', 'k' ): '-j',

	('j', '1' ): 'j',
	('j', 'i' ): '-k',
	('j', 'j' ): '-1',
	('j', 'k' ): 'i',

	('k', '1' ): 'k',
	('k', 'i' ): 'j',
	('k', 'j' ): '-i',
	('k', 'k' ): '-1'
	}
	if '-' in x:
		if '-' in y:
			return table[(x[1], y[1])]
		else:
			if '-' in table[(x[1], y)]:
				return table[(x[1], y)][1]
			else:
				return '-'+table[(x[1], y)]
	if '-' in y:
		if '-' in table[(x, y[1])]:
			return table[(x, y[1])][1]
		else:
			return table[(x, y[1])]
	return table[(x, y)]

def mult(s):
	ans = s[0]
	for k in range(1, len(s)):
		ans = twpod(ans, s[k])
	return ans

def find(ls, c, m, dat):
	i = m
	prod = dat
	while prod!= c:
		if i >= len(ls):
			return -1, prod
		prod = twpod(prod, ls[i])
		i += 1
	return i, prod


T = int(input())
for i in range(1, T+1):
	L, X = map(int,input().split())
	S = str(input()) * X
	ans = "NO"
	if mult(S) == '-1' and L > 1:
		mi, mj = 1,1
		di = S[0]
		while mi <= len(S) - 2 and ans=="NO":
			ti, di = find(S, 'i', mi, di)
			if ti == -1:
				break

			dj = S[ti]
			while mj <= len(S) - mi - 1:
				tj, dj = find(S[ti:], 'j', mj, dj)
				if tj == -1:
					break
				if tj + ti >= len(S):
					break
				if mult(S[tj+ti:]) == 'k':
					ans = 'YES'
					break
				mj += 1
			mi += 1
	print("Case #{0}: {1}".format(i, ans))