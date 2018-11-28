#!/usr/bin/env python
import sys

STR = ['OFF', 'ON']

def compute(n, k):
    res = []
    while k > 0:
        res.append(k % 2)
        k = k / 2
    return sum(res[:n]) == n

def main():
    t = int(sys.stdin.readline())
    for i in range(0, t):
        n, k = sys.stdin.readline().split()
        n = int(n)
        k = int(k)
        print 'Case #%d: %s' % (i + 1, STR[compute(n, k)])
    
if __name__ == '__main__':
  sys.exit(main())
