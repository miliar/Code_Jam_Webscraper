#!/usr/bin/env python
# -*- coding:utf-8 -*-

RICHARD = "RICHARD"
GABRIEL = "GABRIEL"

def solve(x, r, c):
    if (r*c) % x != 0:
        return RICHARD
    if x >= 8:
        return RICHARD
    if x == 2:
        return GABRIEL

    if (r*c)/x <= x/2:
        return RICHARD
    if r < (x-1)/2+1 or c < (x-1)/2+1:
        return RICHARD
    if r < x and c < x:
        return RICHARD

    return GABRIEL


def main():
    # test case num
    t_num = int(raw_input())

    for t in xrange(t_num):
        # X R C
        x, r, c = map(lambda x:int(x), raw_input().split())

        winner = solve(x, r, c)
        print "Case #{}: {}".format(t+1, winner)


if __name__ == "__main__":
    main()
