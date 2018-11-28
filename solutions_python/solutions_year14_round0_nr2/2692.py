#!/usr/bin/env python
# -*- coding: utf-8 -*-

T=int(raw_input())

def calc(c,f,x):
	res = 0.0
	rate = 2
	while True:
		t_2buy = c/rate
		t_recover = c/f
		t_go = x/rate
		# print 't_2buy: %f\nt_recover: %f\nt_go: %f\n'%(t_2buy,t_recover,t_go)
		if t_go <= t_2buy + t_recover:
			res+=t_go
			return '{:10.7f}'.format(res)
		rate += f
		res += t_2buy
		# print 'new rate: %f\nnew res: %f\n'%(rate,res)
	return '{:10.7f}'.format(res)

for case in xrange(T):
     c,f,x = map(float,raw_input().split())
     print 'Case #%d:'%(case+1),
     # print 'C= %f F = %f X = %f\n'%(c,f,x)
     print calc(c,f,x)
