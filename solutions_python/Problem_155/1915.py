import sys
sys.stdin = open('A-large.in' ,'r')

for asd in xrange(int(raw_input())):
    n,lvls = raw_input().split()
    n = int(n)
    lvls = map(int,list(lvls))
    up = lvls[0]
    ans = 0
    for i in xrange(1,n+1):
        if up<i:
            ans += i-up
            up += i-up
        up+=lvls[i]
    print "Case #%s: %s" %(asd+1,ans)
