#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Scott Patterson
# asp742@gmail.com
#

import sys
from itertools import cycle

def min_scalar(v1, v2):
    v1.sort()
    v2.sort()

    return sum(x*y for x, y in zip(v1, v2[::-1]))

def main():
    file = sys.argv[1]
    data = (lines.strip() for lines in open(file))

    ncase = int(data.next())
    for case in range(ncase):
        nelem = int(data.next())

        v1 = [int(x) for x in data.next().strip().split()]
        v2 = [int(x) for x in data.next().strip().split()]

        print 'Case #%d: %d' % (case + 1, min_scalar(v1,v2))


if __name__ == '__main__':
    main()
