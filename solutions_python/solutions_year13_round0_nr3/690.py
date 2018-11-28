def isP(n):
    n = str(n)
    return all([n[i] == n[-(i+1)] for i in range(0, len(n))])


a = []
for i in xrange(1, 10**7):
    if isP(i) and isP(i*i):
        a.append(i*i)

tests = int(raw_input())
for r in range(1,tests+1):
    print "Case #%d:" % r,
    L,R= (int(x) for x in raw_input().strip().split())
    res =0
    for x in a:
        if L <= x <= R:
            res += 1
    print res
