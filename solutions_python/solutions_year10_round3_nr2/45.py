#!/usr/bin/env python

def cal(l, p, c):
    if l * c >= p:
        return 0
        
    q = p / l
    n = 1
    while True:
        if c**n >= q:
            break
        n += 1

    if n != 1:
        n /= 2
    mid = l * c**n

    #print l, p, c, n, mid

    ans1 = max(cal(l, mid, c), cal(mid, p, c)) + 1
    if n % 2 == 1 and mid * 2 < p:
        ans2 = max(cal(l, mid*2, c), cal(mid*2, p, c)) + 1
        ans1 = min(ans1, ans2)
    
    return ans1

def solve(t):
    l, p, c = map(lambda x: int(x), raw_input().split())
    ans = cal(l, p, c)
    
    print 'Case #%d: %d' % (t, ans)

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        solve(case + 1)
    
if __name__ == '__main__':
    main()