#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  pancakes.py
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def main():
    fi = open('B-large.in', 'r')
    fo = open('pancakes_large_output.txt', 'w')
    test = int(fi.readline())
    for cases in range(1, test+1):
        n = int(fi.readline())
        l = list(map(int, fi.readline().split()))
        res = max(l)
        # highest stack
        h = 1
        while (h < res):
            h += 1
            # time needed to split each stack
            cnt = sum([int((x-1)/h) for x in l])
            res = min(res, h + cnt)
        fo.write('Case #%d: %d\n' % (cases, res))
    fi.close()
    fo.close()
    return 0

if __name__ == '__main__':
    main()

