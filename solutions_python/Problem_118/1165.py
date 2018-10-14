#!/usr/bin/python

import sys

def getE(s):
	p1 = int(s)
	p2 = int(s[::-1])
	num = p1 * 10 ** len(s) + p2;
	return num * num;
	
def getO(s, m):
	p1 = int(s)
	p2 = int(s[::-1])
	l = len(s)
	num = p1 * 10 ** (l + 1) + int(m) * 10 ** l + p2;
	return num * num

def getRes(lim):
	res = 0
	if 1 * 1 <= lim:
		res += 1
	if 2 * 2 <= lim:
		res += 1
	if 3 * 3 <= lim:
		res += 1
	for i in range(1, 27):
		L = 2 ** (i - 1)
		R = 2 ** i - 1
		l = L
		r = R
		ok = l - 1
		while l <= r:
			m = (l + r) / 2
			if getE(bin(m).replace("0b", "")) <= lim:
				ok = m
				l = m + 1
			else:
				r = m - 1
		res += ok - L + 1
		if ok < R:
			break
		if getE(str(2 * 10 ** (i - 1))) <= lim:
			res += 1
		else:
			break
	for i in range(1, 27):
		L = 2 ** (i - 1)
		R = 2 ** i - 1
		l = L
		r = R
		ok = l - 1
		while l <= r:
			m = (l + r) / 2
			if getO(bin(m).replace("0b", ""), '2') <= lim:
				ok = m
				l = m + 1
			else:
				r = m - 1
		res += (ok - L + 1) * 3
		if ok < R:
			s = bin(ok + 1).replace("0b", "")
			if getO(s, '2') <= lim:
				res += 3
			elif getO(s, '1') <= lim:
				res += 2
			elif getO(s, '0') <= lim:
				res += 1
			break
		s = str(2 * 10 ** (i - 1))
		if getO(s, '1') <= lim:
			res += 2
		elif getO(s, '0') <= lim:
			res += 1
	return res

def main():
	fin = open('input.txt', 'r')
	fout = open('output.txt', 'w')
	t = int(fin.readline())
	for tc in range(t):
		nums = fin.readline().split(' ')
		fout.write('Case #' + str(tc + 1) + ': ' + str(getRes(int(nums[1])) - getRes(int(nums[0]) - 1)) + '\n')
	fin.close()
	fout.close()

if __name__ == '__main__':
    main()
