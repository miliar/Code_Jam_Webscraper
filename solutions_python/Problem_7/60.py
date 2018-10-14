#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#
# FILE.py
# DESC
#
# Copyright (c) 2008 Pierre "delroth" Bourdon <root@delroth.is-a-geek.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def combinations(trees):
    return ((a, b, c) for (i,a) in enumerate(trees) for (j,b) in enumerate(trees) for (k,c) in enumerate(trees) if i != j and j != k and i != k)

def validtriangles(trees):
    combs = combinations(trees)
    occ = []
    for t in combs:
        ((x1, y1), (x2, y2), (x3, y3)) = t
        ok = True
        if not ok:
            continue
        if (x1 + x2 + x3) % 3 == 0 and (y1 + y2 + y3) % 3 == 0:
            occ.append(t)
            yield t

for n in xrange(int(raw_input())):
    ntrees, a, b, c, d, x0, y0, m = [int(e) for e in raw_input().split()]
    trees = [(x0, y0)]
    for i in xrange(ntrees - 1):
        x0 = (a * x0 + b) % m
        y0 = (c * y0 + d) % m
        trees.append((x0, y0))
    print 'Case #%d: %d' % (n + 1, len(list(validtriangles(trees))) / 6)
