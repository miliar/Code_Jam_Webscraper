def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

c = int(raw_input())
for case in range(1, c+1):
    n, pd, pg = map(int,raw_input().split())
    base = 100 / gcd(pd, 100)
    if base <= n and not (pd<100 and pg==100) and not (pd>0 and pg==0):
        print "Case #%d: Possible" % case
    else:
        print "Case #%d: Broken" % case
