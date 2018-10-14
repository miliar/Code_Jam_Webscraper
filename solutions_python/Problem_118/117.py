#!/usr/bin/env python
import bisect
from itertools import chain, combinations
import math
import sys

MAX_DIGITS = 60

def ceil_sqrt(x):
    """smallest integer i such that i**2 >= x"""

    guess = int(math.sqrt(x))
    while 1:
        sq = guess**2
        if (guess-1)**2 < x <= sq:
            return guess
        if sq < x <= (guess+1)**2:
            return guess+1
        guess = (guess + x/guess)/2

def floor_sqrt(x):
    """smallest integer i such that i**2 >= x"""

    guess = int(math.sqrt(x))
    while not guess**2 <= x < (guess+1)**2:
        guess = (guess + x/guess)/2
    return guess

def main():
    roots = set((1, 2, 3))
    for i in xrange(0, MAX_DIGITS-1):
        zeroes = '0'*i
        roots.add(int("1%s1" % zeroes))
        roots.add(int("2%s2" % zeroes))
    for i in xrange(0, (MAX_DIGITS-1)//2):
        zeroes = '0'*i
        roots.add(int("2%s1%s2" % (zeroes, zeroes)))

    for i in xrange(0, (MAX_DIGITS-1)//2):
        for j in xrange(i):
            lst = []
            for k in xrange(i):
                if j == k:
                    lst.append('1')
                else:
                    lst.append('0')
            sub = ''.join(lst)
            rev = ''.join(reversed(lst))
            roots.add(int("1%s2%s1" % (sub, rev)))

    for i in xrange(0, (MAX_DIGITS-1)//2):
        zeroes = "0"*i
        roots.add(int("1%s2%s1" % (zeroes, zeroes)))
        roots.add(int("1%s1%s1" % (zeroes, zeroes)))

        for j in xrange(i):
            lst = []
            for k in xrange(i):
                if j == k:
                    lst.append('1')
                else:
                    lst.append('0')
            sub = ''.join(lst)
            rev = ''.join(reversed(lst))
            roots.add(int("1%s2%s1" % (sub, rev)))

    for i in xrange(0, (MAX_DIGITS-1)//2):
        for comb in chain(
                combinations(xrange(i), 0),
                combinations(xrange(i), 1),
                combinations(xrange(i), 2),
                combinations(xrange(i), 3),):
            comb = set(comb)
            lst = []
            for j in xrange(i):
                if j in comb:
                    lst.append('1')
                else:
                    lst.append('0')
            sub = ''.join(lst)
            rev = ''.join(reversed(lst))
            roots.add(int("1%s%s1" % (sub, rev)))
            roots.add(int("1%s1%s1" % (sub, rev)))
            roots.add(int("1%s0%s1" % (sub, rev)))

    s_roots = sorted(roots)

    assert len(sys.argv) == 3, str(sys.argv)
    in_name = sys.argv[1]
    out_name = sys.argv[2]
    with open(in_name) as f, open(out_name, 'w') as g:
        T = int(f.readline().strip()) # number of cases
        for test_num in xrange(T):
            A, B = map(int, f.readline().strip().split())
            left_root = ceil_sqrt(A)
            right_root = floor_sqrt(B)
            left = bisect.bisect_left(s_roots, left_root)
            right = bisect.bisect_right(s_roots, right_root)

            g.write("Case #%s: %s\n" % (
                test_num+1,
                right-left))
    return 0

if __name__ == "__main__":
    # for i in s:
    #     rt = str(int(math.sqrt(i)))
    #     l = len(rt)
    #     if rt in set('123'):
    #         continue
    #     if rt[0] == '2' and rt[-1] == '2' and all(c == '0' for c in rt[1:-1]):
    #         continue
    #     if l % 2 == 1 and rt[0] == '2' and rt[-1] == '2' and rt[l//2] == '1' and all(c == '0' for c in rt[1:l//2]):
    #         continue

    #     if l % 2 == 1 and rt[l//2] == '2' and all(c in set('012') for c in rt) and rt.count('2') == 1 and rt.count('1') <= 4:
    #         continue
    #     if all(c in set('01') for c in rt) and rt.count('1') <= 9:
    #         continue
    #     print rt, i

    status = main()
    sys.exit(status)

##
# 22, 202, 2002, ...
# 212, 20102, 2001002, ...
# 121, 10201, 11211, 1002001, 1012101, 1102011, ... one or two 1's, with a 2 in the middle
# 1's and 0's, with <= 9 1's
