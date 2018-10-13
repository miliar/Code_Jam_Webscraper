#!/usr/bin/env python
import sys

CNS = 'bcdfghjklmnpqrstvwxyz'

def get_sol(name, n):
    lb = 0
    result = 0
    l = len(name)
    for os in xrange(0, len(name)-n+1):
        if all(c in CNS for c in name[os:os+n]):
            result += (1+os-lb) * (l-os-n+1)
            lb = os+1
    return result

def main():
    N = int(sys.stdin.readline())

    for i in xrange(1, N+1):
        name, n = sys.stdin.readline().split()
        print "Case #%d: %d" % (i, get_sol(name, int(n)))

if __name__ == '__main__':
    main()