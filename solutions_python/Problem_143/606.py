#!/usr/bin/python3
from sys import argv

with open(argv[1]) as inp, open(argv[2], 'w') as out:
    cases = int(inp.readline())
    for case in range(cases):
        (a, b, k) = (int(x) for x in inp.readline().split())
        result = 0
        for x in range(a):
            for y in range(b):
                if (x & y) < k:
                    result += 1

        out.write('Case #%d: %d\n' % ((case + 1), result))
