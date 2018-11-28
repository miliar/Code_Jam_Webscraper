#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: A.py
# Author: wmg_1001
# mail: wmg_1007@163.com
# Created Time: 2015年04月11日 星期六 20时33分10秒
#########################################################################

T = raw_input()
T = int(T)
for case_T in range(1, T + 1):
	[n, S] = raw_input().split()
	n = int(n)
	[res, tot] = [0, 0]
	for i in range(0, n + 1):
		if S[i] == '0': continue
		if i > res: res = i
		res += int(S[i])
		tot += int(S[i])
	print "Case #%d: %d" % (case_T, res - tot)