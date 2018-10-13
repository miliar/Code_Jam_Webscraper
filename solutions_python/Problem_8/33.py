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

import math

def primes(a, b):
    for n in xrange(a, b + 1):
        ok = True
        for d in xrange(2, int(math.sqrt(n)) + 1):
            if n % d == 0:
                ok = False
                break
        if ok:
            yield n

def primedivisors(m, n):
    for p in primes(m, n):
        if n % p == 0:
            yield p

def nsets(a, b, p):
    sets = [set(primedivisors(p, n)) for n in xrange(a, b + 1)]
    newsets = []
    while True:
        for s in sets:
            found = None
            for i,n in enumerate(newsets):
                for e in s:
                    if e in n:
                        found = n
                        break
                if not found:
                    continue
                else:
                    newsets[i] = newsets[i].union(s)
                    break
            if not found:
                newsets.append(s)
        if sets == newsets:
            return len(sets)
        else:
            sets, newsets = newsets, []
    return len(newsets)

for n in xrange(int(raw_input())):
    a, b, p = [int(e) for e in raw_input().split()]
    print 'Case #%d: %d' % (n + 1, nsets(a, b, p))
