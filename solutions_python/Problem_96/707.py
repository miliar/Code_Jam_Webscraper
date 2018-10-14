# -*- coding: utf-8 -*-
from math import floor
with open('B-large.in', 'r') as si, open('B-large.out', 'w') as so:
    num = int(si.readline())
    result = ''
    for i in range(num):
        l = map(int, si.readline().split())
        n, s, p, ss = l[0], l[1], l[2], l[3:]
        count = 0
        for x in ss:
            r = floor((x - p) / 2)
            if r < 0 or r < p - 2: continue
            if r == p - 2:
                if s <= 0: continue
                s = s - 1
            count = count + 1
        result = result + 'Case #' + str(i+1) + ': ' + str(count) + '\n'
    print result
    so.write(result)