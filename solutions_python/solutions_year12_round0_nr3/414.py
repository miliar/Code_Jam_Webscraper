#!/usr/bin/env python
# -*- coding:utf-8 -*-

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, raw_input().split())

dd = set()

def dp():
	n = 1
	m = 2000000
	for ll in xrange(n, m+1):
		v = str(ll)
		for i in xrange(1, len(v)):
			new_value = int(v[i:] + v[:i])
			if n <= new_value <= m and new_value > ll and (ll, new_value) not in dd:
				dd.add((ll, new_value))

def doit(n, m):
	ans = 0
	for v1, v2 in dd:
		if n <= v1 <= m and n <= v2 <= m: ans += 1
	return ans

if __name__ == '__main__':
    dp()
    C = readint()
    for c in xrange(1, C+1):
		n, m = readlinearray(int)
		ans = doit(n, m)
		print 'Case #%d: %s' % (c, ans)
