import sys,re,fractions

nCases = int(sys.stdin.readline())
for _ in range(1,nCases+1):
    n, pd, pg = map(int, sys.stdin.readline().split())
    d = 100/fractions.gcd(pd,100)
    if (pd > 0 and pg == 0) or (pd < 100 and pg == 100):
        res = 'Broken'
    elif d <= n:
        res = 'Possible'
    else:
        res = 'Broken'
    print 'Case #%d: %s'% (_, res)
