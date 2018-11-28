#!/usr/bin/env python
# -*- coding: utf-8 -*-
VERBOSE = 0
def bs(n, k):
    if n == k:
        return (0, 0)
    if n&1:
        pos = n/2
    else:
        pos = n/2 - 1
    ls = pos
    rs = n - pos - 1
    if VERBOSE:
        print("n={}, k={}, ls={}, rs={}".format(
            n, k, ls, rs))
    if k == 1:
        return (max(ls,rs), min(ls,rs))
    k -= 1
    # return bs(max(ls,rs), (k+(k&1))/2)
    lk = (k+(k&1))/2
    if k&1:
        return bs(max(ls,rs), lk)
    else:
        return bs(min(ls,rs), lk)

def test_stalls():
    assert(bs(1, 1) == (0, 0))
    assert(bs(2, 1) == (1, 0))
    assert(bs(3, 1) == (1, 1))
    assert(bs(3, 2) == (0, 0))
    assert(bs(4, 2) == (1, 0))
    assert(bs(5, 2) == (1, 0))
    assert(bs(6, 2) == (1, 1))
    assert(bs(1000, 1000) == (0, 0))
    assert(bs(1000, 1) == (500, 499))
    assert(bs(1000, 999) == (0, 0))
    assert(bs(8, 1) == (4, 3))
    assert(bs(8, 2) == (2, 1))
    assert(bs(8, 3) == (1, 1))
    assert(bs(8, 4) == (1, 0))
    assert(bs(8, 5) == (0, 0))
    assert(bs(8, 6) == (0, 0))
    assert(bs(8, 7) == (0, 0))
    assert(bs(8, 8) == (0, 0))
    assert(bs(9, 1) == (4, 4))
    assert(bs(9, 2) == (2, 1))
    assert(bs(9, 3) == (2, 1))
    assert(bs(9, 4) == (1, 0))
    assert(bs(9, 5) == (1, 0))
    assert(bs(9, 6) == (0, 0))
    assert(bs(9, 7) == (0, 0))
    assert(bs(9, 8) == (0, 0))
    assert(bs(9, 9) == (0, 0))

if __name__ == '__main__':
    T = int(raw_input().strip())
    for case in xrange(T):
        N,K = map(int, raw_input().strip().split())
        minv, maxv = bs(N,K)
        print("Case #{}: {} {}".format(case+1, minv, maxv))

