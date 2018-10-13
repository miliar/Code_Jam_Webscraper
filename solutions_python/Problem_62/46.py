#!/usr/bin/env python

def solve(t):
    n = int(raw_input())
    wires = []
    for i in xrange(n):
        wires.append(map(lambda x: int(x), raw_input().split()))
    
    wires.sort(lambda x, y: x[0] - y[0])
    ans = 0
    for i in xrange(n):
        l, r = wires[i]
        for j in xrange(i+1, n):
            rl, rr = wires[j]
            if rr < r:
                ans += 1
    
    print 'Case #%d: %d' % (t, ans)

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        solve(case + 1)
    
if __name__ == '__main__':
    main()