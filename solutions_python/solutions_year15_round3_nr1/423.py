__author__ = 'sanjay'

import sys, math

def find_max(r, c, w):
    return int(r * math.ceil((c / float(w))) + w - 1)

test = int(sys.stdin.readline())

for i in range(test):
    r, c, w = map(int, sys.stdin.readline().split())

    print 'Case #%d: %d' % (i + 1, find_max(r, c, w))