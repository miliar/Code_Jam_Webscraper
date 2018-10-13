#!/bin/python

def sub(l, n, o):
    #import pdb
    #pdb.set_trace()

    l[o] -= n
    if l[o] < 0:
        l[o] += 10
        sub(l, 1, o + 1)

    if len(l) == o + 1 and l[-1] == 0:
        l.pop()

def solve(s):
    l = map(int, list(s))[::-1]
    r = ''

    while l:
        if l != sorted(l, key = lambda x: 0 - x):
            sub(l, l[0] + 1, 0)
        r += str(l.pop(0))
    return r[::-1]

import sys, unittest

class TestSub(unittest.TestCase):

    def test_1(self):
        l = [3, 2, 1]
        sub(l, 4, 0)
        self.assertEqual(l, [9, 1, 1])

    def test_2(self):
        l = [0, 0, 1]
        sub(l, 1, 0)
        self.assertEqual(l, [9, 9])

    def test_3(self):
        l = [0, 1, 1]
        sub(l, 1, 0)
        self.assertEqual(l, [9, 0, 1])

    def test_4(self):
        l = [0, 1]
        sub(l, 1, 0)
        self.assertEqual(l, [9])

if __name__ == '__main__':
    #unittest.main()
    n = int(raw_input())
    for i in xrange(n):
        s = raw_input()
        print 'Case #%d: %s' % (i + 1, solve(s))


