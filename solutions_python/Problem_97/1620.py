#!/usr/bin/env python

def shift(n):
    return n[-1] + n[:-1]

def is_recycled(n, m):
    n = str(n)
    m = str(m)
    shifts = len(n) - 1
    for i in range(shifts):
        n = shift(n)
        if n == m:
            return True
    return False

def main():
    T = int(raw_input().strip())
    for i in range(T):
        recycled = 0
        a, b = [int(a) for a in raw_input().strip().split()]
        for n in range(a, b):
            for m in range(n + 1, b + 1):
                if is_recycled(n, m):
                    recycled += 1
        print "Case #%d: %d" % (i + 1, recycled)

if __name__ == '__main__':
    main()
