#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: B.py
# Author: wmg_1001
# mail: wmg_1007@163.com
# Created Time: 2015年04月11日 星期六 21时11分26秒
#########################################################################

T = raw_input()
T = int(T)
for case_T in range(1, T + 1):
	n = raw_input()
	n = int(n)
	f = [int(i) for i in raw_input().split()]
	max_H = 0
	for i in range(n): max_H = max(max_H, f[i])
	res = max_H
	for H in range(1, max_H + 1):
		t_res = H
		for i in range(n):
			if f[i] > H: t_res += (f[i] - H - 1) / H + 1
		res = min(res, t_res)
	print "Case #%d: %d" % (case_T, res)
