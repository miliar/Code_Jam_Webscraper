#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tidy(any_number):
    if any_number < 10:
        return any_number
    r = 0
    v = any_number
    d = 0
    p = 1
    while v:
        a = v % 10
        v = v / 10
        b = v % 10
        d = d*10 + 9
        # print("r={}, v={}, d={}, a={}, b={}, r={}".format(r,v,d,a,b,r))
        if b > a:
            # adjust digits
            if v:
                v -= 1
            r = d
            p *= 10
            # print("ADJ: v={}, r={}".format(v,r))
            continue
        r += a*p
        p *= 10
    return r

def test_tidy():
    assert(tidy(7) == 7)
    assert(tidy(132) == 129)
    assert(tidy(123) == 123)
    assert(tidy(221) == 199)
    assert(tidy(10) == 9)
    assert(tidy(1000) == 999)
    assert(tidy(111111111111111110) == 99999999999999999)
    assert(tidy(111111101111111110) == 99999999999999999)
    assert(tidy(111111000000000000) == 99999999999999999)
    assert(tidy(111111012345669000) == 99999999999999999)

if __name__ == '__main__':
    T = int(raw_input().strip())
    for case in xrange(T):
        N = int(raw_input().strip())
        print("Case #{}: {}".format(case+1,tidy(N)))

