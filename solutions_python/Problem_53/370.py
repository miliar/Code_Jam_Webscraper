#!/usr/bin/python

def snap_it(n, k):
    return ((k+1) % 2**n == 0)

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        n, k = [int(s) for s in raw_input().split()]
        is_on = snap_it(n, k)
        print 'Case #%d: %s' % (i+1, 'ON' if is_on else 'OFF')
