#! /usr/bin/python2.7

def prev_tidy(n):
#     print n
    s_n = str(n)
    for i in xrange(1, len(s_n)):
        if ord(s_n[i - 1]) > ord(s_n[i]):
            return prev_tidy(int(s_n[:i]) * (10 ** (len(s_n) - i)) - 1)
    return n
def is_tidy(n):
    s_n = str(n)
    return all(ord(s_n[i - 1]) <= ord(s_n[i]) for i in xrange(1, len(s_n)))

import sys
f = sys.stdin
#f = open("q2_example.in")
T = int(f.readline())
for i in xrange(1, T + 1):
    N = int(f.readline())
    print "Case #%d: %d" % (i, prev_tidy(N))