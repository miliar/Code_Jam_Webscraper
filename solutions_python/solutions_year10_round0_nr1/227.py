#!/usr/bin/env python

def solve(case):
    ans = 'OFF'
    n, k = map(lambda x: int(x), raw_input().split())

    real = k % 2 ** n
    if bin(real) == bin(2**n - 1):
        ans = 'ON'
    
    print 'Case #%d: %s' % (case + 1, ans)

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        solve(case)
    
if __name__ == '__main__':
    main()