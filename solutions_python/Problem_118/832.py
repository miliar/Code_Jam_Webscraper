#!/usr/bin/python

import sys
import math

rset = []

def is_pal(s):
	s = str(s)
	l = len(s)
	for i in range(l / 2 + 1):
		if s[i] != s[-i-1]:
			return False
	return True

def cal_digit(s):
	s = str(s)
	l = 0
	for i in s:
		l += int(i) ** 2
	return l

def cal(level, s):
	if len(s) > 0 and s[0] == '0':
		return
	if cal_digit(s) > 9:
		return
	if level == 0:
		if is_pal(s) and cal_digit(s) < 10:
			rset.append(int(s))
		return
	for i in range(4):
		cal(level - 1, s + str(i))

for i in range(1, 9):
	cal(i, '')

T = int(raw_input())
for t in range(1, T+1):
	A, B = sys.stdin.readline().split()
	A, B = math.sqrt(int(A)), math.sqrt(int(B))
	cnt = 0
	for s in rset:
		if s >= A and s <= B:
			cnt = cnt + 1
	print 'Case #%d: %d' % (t, cnt)

