#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Created by Izidor Matušov <izidor.matusov@gmail.com>
#            on 14.04.2012

import sys
import multiprocessing

def find_y(l):
    A, B = l
    result = 0
    for n in xrange(A, B+1):
        s = str(n)
        used = set()
        for l in xrange(len(s)):
            m = int(s[-l:] + s[:len(s)-l])
            if A <= n < m <= B and m not in used:
                used.add(m)
                result += 1
    return result

inp = [[int(x) for x in line.split()] for line in sys.stdin.readlines()[1:]]

cpus = 2*multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=cpus)
for case, y in enumerate(pool.map(find_y, inp), 1):
    print "Case #%d: %d" % (case, y)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
