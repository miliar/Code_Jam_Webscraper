#!/usr/bin/env python2.7

def solve(audience):
    extra = 0
    standing = 0

    for (i, n) in enumerate(audience):
        if standing >= i:
            standing += n
        else:
            missing = i - standing
            extra += missing
            standing += missing
            standing += n

    return extra


def main():
    num_testcases = int(raw_input())
    for ti in xrange(1, num_testcases+1):
        l, audience = raw_input().split()
        assert len(audience) == int(l) + 1
        audience = map(int, audience)
        solution = solve(audience)
        print "Case #%d: %d" % (ti, solution)


if __name__ == "__main__":
    main()

