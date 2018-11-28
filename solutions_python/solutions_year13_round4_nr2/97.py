#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#========================================================================
#   FileName: B.py
#     Author: YIMMON
#      Email: yimmon.zhuang@gmail.com
#   HomePage: http://qr.ae/8DMzu
# LastChange: 2013-06-01 23:26:23
#========================================================================
import sys, math

def get_p1(p):
	ret = 0
	while p > 1:
		ret += 1
		p >>= 1
	return ret

def f1(p):
	pp = 1
	while pp <= p:
		if pp == p:
			return 1
		pp <<= 1
	return 0 

def get_p2(p):
	pp = 1
	cnt = 0
	while pp <= p:
		pp <<= 1
		cnt += 1
	cnt -= 1
	ret = 0
	while cnt >= 0 and ((1<<cnt) & p) != 0:
		ret += 1
		cnt -= 1
	return ret

T = sys.stdin.readline().split()[0]
T = int(T)

for cas in range(T):
	line = sys.stdin.readline().split()
	n = int(line[0])
	p = int(line[1])
	p1 = get_p1(p)
	q = n-p1
	ans2 = (1<<n) - (1<<q)

	if p <= (1<<(n-1)) or f1(p) == 1:
		p2 = 0
	else:
		p2 = get_p2(p-1)
	q = min((1<<n), (1<<(p2+1))-1)
	ans1 = q-1
	if p == (1<<n):
		ans1 = (1<<n)-1
	if p == ((1<<n)-1):
		ans1 = (1<<n)-2

	print "Case #" + str(cas+1) + ": " + str(ans1) + " " + str(ans2)

