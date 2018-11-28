#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#
# searchengines.py
# Search engine switch problem.
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

from itertools import groupby
import sys

sys.setrecursionlimit(3500)

cache = []
searchs = []
nsearchs = 0
engines = []
nengines = 0

cache = {}

def minfor(si, ei):
    global cache
    if (si, ei) in cache:
        return cache[(si, ei)]
    if si == nsearchs:
        return 0
    s = searchs[si]
    c = engines[ei]
    if s != c:
        v = minfor(si + 1, ei)
        cache[(si, ei)] = v
        return v
    else:
        l = [minfor(si, i) for i in xrange(nengines) if i != ei]
        v = min(l) + 1
        cache[(si, ei)] = v
        return v

if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(1, n + 1):
        cache = {}
        engines = []
        searchs = []
        nengines = int(raw_input())
        for a in xrange(nengines):
            engines.append(raw_input())
        nsearchs = int(raw_input())
        for a in xrange(nsearchs):
            searchs.append(raw_input())
        l = [minfor(0, c) for c in xrange(nengines)]
        m = min(l)
        print "Case #%d: %d" % (i, m)
