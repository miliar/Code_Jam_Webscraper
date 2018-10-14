#-*- encoding: utf-8 -*-

import sys, re

def pattern(test_case):
    return re.compile(test_case.replace('(', '[').replace(')', ']'))

def how_many(p, words):
    matched = filter(lambda x: x is not None, (p.match(word) for word in words))
    return len(matched)

if __name__ == '__main__':
    L, D, N = (int(x) for x in sys.stdin.readline().strip().split())
    words = [sys.stdin.readline().strip() for x in xrange(D)]
    test_cases = [sys.stdin.readline().strip() for x in xrange(N)]

    line_n = 1
    for case in test_cases:
        p = pattern(case)
        print 'Case #%d: %d' % (line_n, how_many(p, words))
        line_n += 1
