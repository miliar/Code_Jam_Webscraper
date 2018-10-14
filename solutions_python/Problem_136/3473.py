#!/usr/bin/env python
# -*- coding: utf-8 -*-

def compute(c,f,x):
	v1 = 2.
	t1 = 0.
	u1 = t1 + x/v1
	tf1 = c/v1

	while True:
		v2 = v1 + f	# moc produkcyjna fabryki
		t2 = t1 + tf1
		u2 = t2 + x/v2
		tf2 = c/v2

		if u2 > u1: return u1
		if abs(u2-u1) < 0.0000001: return u1

		v1=v2
		t1=t2
		u1=u2
		tf1=tf2



def testcase(tc):
	global cnt
	cnt=0
	c,f,x = map(float, raw_input().split(' '))
	ans = "%.7f" % (compute(c,f,x))
	print "Case #%d: %s" % (tc, ans)

if __name__ == "__main__":
	t = int(raw_input())
	for i in range(t):
		testcase(i+1)

