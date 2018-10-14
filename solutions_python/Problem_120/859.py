#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import Symbol, solve

cas_n = int(raw_input())

for cas in range(1, cas_n+1):
	r, t = [int(x) for x in raw_input().split(' ')]
	n = Symbol('n')
	f = (2*r + 1 + 2*(n-1))*n - t
	sol = solve(f, n)
	ans1 = sol[0].evalf()
	ans2 = sol[1].evalf()
	ans = max(ans1, ans2)
	if ans < 0:
		asn = 0
	else:
		ans = int(ans)
	print "Case #{}: {}".format(cas, ans)
