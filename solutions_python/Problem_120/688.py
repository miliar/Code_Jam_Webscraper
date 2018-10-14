#!/usr/bin/env python
#-*- coding: utf-8 -*-

ans = []
with open('input.txt', 'r') as f:
    n = int(f.readline())
    for i in xrange(n):
        r, t = map(int, f.readline().split(' '))
        count = 0
        print r, t
        while True:
            t -= (2 * r + 1)
            if t < 0:
                break
            count += 1
            r += 2

        #print count
        ans.append("Case #{0}: {1}".format(i+1, count))

with open('output.txt', 'w') as fout:
    fout.write('\n'.join(ans))

        

