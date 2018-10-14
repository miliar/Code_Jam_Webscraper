# -*- coding: utf-8 -*-
from math import log10, pow
with open('C-large.in', 'r') as si, open('C-large.out', 'w') as so:
    num = int(si.readline())
    result = ''
    for index in range(num):
        l = map(int, si.readline().split())
        n, m = l[0], l[1]
        xs = set()
        for i in range(n, m + 1):
            dc = int(log10(i))
            prev = i
            mm = int(pow(10, dc + 1))
            h = [i]
            for j in range(dc):
                d = prev / (mm / 10)
                next = 10 * prev - d * (mm - 1)
                if next >= n and next <= m:
                    for k in h:
                        if k < next:
                            xs.add((k, next))
                    h.append(next)
                prev = next
        result = result + 'Case #' + str(index + 1) + ': ' + str(len(xs)) + '\n'
    so.write(result)