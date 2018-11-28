#!/usr/bin/python

import sys

def process(s, engines, num, lis):
    tot = 0
    ind = []
    try:
        while True:
            ind = []
            for eng in engines:
                ind.append(lis.index(eng))
            m = max(ind)
            lis = lis[m:]
            tot += 1
    except ValueError:
        pass
    return tot

def main():
    args = sys.argv[1:]
    f = args[0]
    args = open(f).read().split("\n")
    n, args = int(args[0]), args[1:]
    tot = n
    while n > 0:
        s, args = int(args[0]), args[1:]
        engines, args = args[:s], args[s:]
        num, args = int(args[0]), args[1:]
        lis, args = args[:num], args[num:]
        ans = process(s, engines, num, lis)
        print "Case #%d: %d" % (tot-n+1, ans)
        n -= 1

if __name__ == "__main__":
    sys.exit(main())
