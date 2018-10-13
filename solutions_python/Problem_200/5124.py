#!/usr/bin/python

import sys

def tidy_num():
    n = int(raw_input())

    last = 0

    for i in range(1, n+1):
        if i >= 0 and i <= 9:
            last = i
        else:
            number = str(i)
            cur = 0
            numC = 0
            for j in number:
                if int(j) >= cur:
                    numC = numC + 1
                    cur = int(j)
            if numC == len(number):
                last = i
    return last

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, tidy_num())
