#-*- encoding: utf-8 -*-
#!/usr/bin/python

import os, sys, copy, time, itertools

number_map = {}

def solve(line):
    a, b = map(int, line.split())
    values = set()
    subset = set()
    
    x = a
    while x <= b:
        if x % 10000 == 0:
            key = ((x - 1) * 10000, x)
            if (x - 1) * 10000 <= b:
                number_map[key] = subset

            key = (x, (x + 1) * 10000)
            if (x + 1) * 10000 <= b:
                if number_map.has_key(key):
                    values.update(number_map[key])
                    x = (x + 1) * 10000
                    continue

        str_x = str(x)
        for offset in xrange(len(str_x)):
            new = str_x[offset:] + str_x[:offset]
            int_new = int(new)
            if (int_new >= a) and (int_new <= b) and int_new > x and new[0] != '0':
                subset.add((x, new))
                values.add((x, new))

        x += 1

    return len(values)

lines = sys.stdin.read().split('\n')
lines.pop()
lines.pop(0)

case = 0
while lines:
    case += 1
    line = lines.pop(0)

    print 'Case #%d: %s' % (case, solve(line))
