#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#
# timetable.py
# Calculates the better train timetable.
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

class Travel(object):
    pass

def readtime(travel):
    start, end = raw_input().split(' ')
    start = int(start[:2]) * 60 + int(start[3:])
    end = int(end[:2]) * 60 + int(end[3:])
    travel.start = start
    travel.end = end

def mintrains(ta, tb):
    trainsA = 0
    trainsB = 0
    maxa = maxb = 0
    for i in xrange(24 * 60):
        for a in ta:
            if a.start == i: trainsA += 1
            if a.end == i: trainsB -= 1
        for b in tb:
            if b.start == i: trainsB += 1
            if b.end == i: trainsA -= 1
        if trainsA > maxa: maxa = trainsA
        if trainsB > maxb: maxb = trainsB
    return maxa, maxb

n = int(raw_input())
for i in xrange(1, n + 1):
    turnaround = int(raw_input())
    na, nb = [int(e) for e in raw_input().split()]
    travelsA = []
    travelsB = []
    for j in xrange(na):
        t = Travel()
        readtime(t)
        t.end += turnaround
        travelsA.append(t)
    for j in xrange(nb):
        t = Travel()
        readtime(t)
        t.end += turnaround
        travelsB.append(t)
    print "Case #%d:" % i, "%d %d" % mintrains(travelsA, travelsB)
