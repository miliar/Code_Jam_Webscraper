#!/usr/bin/env python

from math import sqrt
import sys

def find_fair(lower, upper):
    l_len = len(str(lower))
    u_len = len(str(upper))

    for l in range(l_len, u_len + 1):
        lo = 10**(l-1)
        up = 10**(l) - 1
        for i in find_fair_r(max(lo, lower),
                             min(up, upper)):
            yield i

def find_fair_r(lower, upper):
    assert len(str(lower)) == len(str(upper))
    if len(str(lower)) % 2:
        f = find_fair_odd
    else:
        f = find_fair_even

    for i in f(lower, upper):
        yield i

def find_fair_odd(lower, upper):
    le = len(str(lower))
    lowleft = int(str(lower)[:le/2 + 1])
    uprleft = int(str(upper)[:le/2 + 1])

    for numleft in range(lowleft, uprleft+1):
        numright = ''.join(list(reversed(str(numleft)))[1:])
        num = int(str(numleft)+numright)
        if lower <= num <= upper:
            yield num

def is_fair(num):
    s = str(num)
    l = len(s)
    for i in range((l+ 1) / 2):
        if s[i] != s[-(i+1)]:
            #print s, i, s[i], s[-(i+1)]
            return False
    return True

def find_fair_even(lower, upper):
    le = len(str(lower))
    lowleft = int(str(lower)[:le/2])
    uprleft = int(str(upper)[:le/2])

    for numleft in range(lowleft, uprleft+1):
        numright = ''.join(list(reversed(str(numleft))))
        num = int(str(numleft)+numright)
        if lower <= num <= upper:
            yield num

def main():
    inp = iter(sys.stdin)
    num_cases = int(inp.next())
    for case in range(1, num_cases + 1):
        square_and_fair = 0

        A, B = [ int(a) for a in inp.next().split() ]
        # find all fair numbers between sqrt(A) and sqrt(B)..
        sqrts =  find_fair(int(sqrt(A)),
                           int(sqrt(B)))
        for num in sqrts:
            sqr = num*num
            if A <= sqr <= B and is_fair(sqr):
                square_and_fair += 1

        print "Case #%d: %d" % (case, square_and_fair)

if __name__ == '__main__':
    main()
