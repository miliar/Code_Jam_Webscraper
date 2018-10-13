# encoding: utf-8

import sys


T = int(sys.stdin.readline())


for case in xrange(T):
    exist = 0
    need = 0
    _, line = sys.stdin.readline().split(' ')
    for index, a in enumerate(list(line.strip())):
        a = int(a)
        if exist < index:
            d = index - exist
            need += d
            exist += d
        exist += a
    print 'Case #{}: {}'.format(case + 1, need)
