#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2011 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

from common import nt, ni, nl, line


"""
Title
"""

INF = float("inf")

def d_min(vendors):
	d_min = INF
	vendors = iter(vendors)
	b = next(vendors)
	for e in vendors:
		d_min = min(d_min, e-b)
		b = e
	return d_min

def evolve(vendors, dt, D):
	p = -INF
	for i, v in enumerate(vendors):
		if v-dt >= p+D:
			v -= dt
		else:
			v = min(p+D, v+dt)
		p = vendors[i] = v

def minimum(vendors, D):
	t = 0.
	while True:
		d = d_min(vendors)
		if d >= D:
			break
		dt = (D - d)/2.
		t += dt
		evolve(vendors, dt, D)
	return t

T = ni(); nl()
for X in xrange(T):
	print "Case #%s:" % (X+1),
	C, D = ni(), ni(); nl()
	vendors = []
	for _ in xrange(C):
		P, V = ni(), ni(); nl()
		for i in range(V):
			vendors.append(float(P))
	print minimum(vendors, D)
