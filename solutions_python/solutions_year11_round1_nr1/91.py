#! /usr/bin/python
import sys

def main():
    t = input()
    for i in xrange(1, t + 1):
        print 'Case #%d:' % i,
        n, pd, pg = map(int, raw_input().split())
        print 'Possible' if solve(n, pd, pg) else 'Broken'

def solve(n, pd, pg):
    # pd / 100 = wd / d
    # pg / 100 = wg / g
    # d = n + x
    # g = d + y
    # wg = wd + wy
    # pd * d = wd * 100
    # pg * (d + y) = (wd + wy) * 100
    if pg == 100: return pd == 100
    if pg ==   0: return pd ==   0
    if n >= 100: return True
    for d in xrange(1, n + 1):
        if (pd * d) % 100 == 0:
            return True
    return False

if __name__ == '__main__':
    sys.exit(main())
