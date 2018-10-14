#!/usr/bin/python3

from sys import stdin

def can_win_round_good(W, L):
	return L != 0

def can_win_round_bad(W, L):
	return W == 0

def check_good(we, n, mask):
	W = we
	L = 2 ** n - 1 - W
	for i in range(n):
		if can_win_round_good(W, L):
			if mask[i] == '0':
				return True
			else:
				L -= 1
				if W % 2 == 0:
					W //= 2
					L //= 2
				else:
					W = W // 2 + 1
					L = L // 2
		else:
			if mask[i] == '1':
				return False
			else:
				W -= 1
				if W >= L:
					W -= L
					W //= 2
				else:
					W = 0
	return True

def check_bad(we, n, mask):
	W = we
	L = 2 ** n - 1 - W
	for i in range(n):
		# print('bad', 'we = ' + str(we), 'mask = ' + mask, i, W, L, sep = ', ')
		if W == 0:
			if mask[i] == '0':
				return True
			else:
				L -= 1
				L //= 2
		else:
			if mask[i] == '1':
				return False
			else:
				W -= 1
				L = L // 2 + L % 2
				W = W // 2
	return True

def find(n, mask, f):
	l = -1
	r = (2 ** n)
	while r - l > 1:
		m = (l + r) // 2
		if f(m, n, mask):
			l = m
		else:
			r = m
	return l

def solve(tn):
	n, p = map(int, stdin.readline().split())
	mask = list(map(lambda x: '0' * (n - len(x)) + x, [bin(2 ** n - p)[2:]]))[0]
	l = -1
	r = (2 ** n) - 1
	print('Case #%d: %d %d' % (tn + 1, find(n, mask, check_bad),find(n, mask, check_good) ))

t = int(stdin.readline())
for i in range(t):
	solve(i)
