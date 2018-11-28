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

for i, line in enumerate(sys.stdin.readlines()[1:], 1):
    nums = [int(x) for x in line.split()]
    N, S, p, dancers = nums[0], nums[1], nums[2], nums[3:]
    result = 0
    for d in dancers:
        # normal maximum of triplet
        if d % 3 == 0:
            m = d / 3
        else:
            m = d / 3 + 1

        # maximum using suprising triplet
        if m+1 <= d:
            mm = m+1
        else:
            mm = m

        if m >= p:
            result += 1
        elif S > 0 and mm >= p:
            result += 1
            S -= 1

    print "Case #%d: %d" % (i, result)
            
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
