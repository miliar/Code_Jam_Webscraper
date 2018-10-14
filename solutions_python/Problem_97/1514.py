#! /usr/bin/env python
import sys

# known naive algorithm, guaranteed to fail the large input,
# but I don't have much time


def main():
    n = int(raw_input())
    for i in xrange(1, n + 1):
        a, b = map(int, raw_input().split())
        print 'Case #%d:' % i,
        print solve(a, b)


def solve(a, b):
    l = len(str(a))
    count = 0
    for n in xrange(a, b):
        sn = str(n)
        found = set()
        for i in xrange(1, l):
            sm = sn[i:] + sn[:i]
            if sn < sm and int(sm) <= b:
                found.add(sm)
        count += len(found)
    return count


if __name__ == '__main__':
    sys.exit(main())
