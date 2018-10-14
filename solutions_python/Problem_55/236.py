#!/usr/bin/env python

def solve(case):
    ans = 0
    R, k, N = map(lambda x: int(x), raw_input().split())
    g = map(lambda x: int(x), raw_input().split())

    for i in xrange(R):
        remain = k
        s = 0
        for j in xrange(len(g)):
            if remain >= g[j]:
                remain = remain - g[j]
            else:
                s = j
                break
        
        ans = ans + (k - remain)
        g = g[s:] + g[:s]
        
    print 'Case #%d: %d' % (case + 1, ans)

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        solve(case)
    
if __name__ == '__main__':
    main()