import itertools

tcou = int(raw_input())

for ti in range(tcou):
    n, p = [int(x) for x in raw_input().split()]
    g = [int(x) for x in raw_input().split()]
    num = [0 for _ in range(p)]
    for x in g:
        num[x%p] += 1
    num[0] = 0
    ans = len(g)
    for x in range(1, p):
        if p-x!=x:
            cou = min(num[x], num[p-x])
        else:
            cou = num[x]//2
        ans -= cou
        num[x] -= cou
        num[p-x] -= cou
    for x in range(1, p):
        if num[x]>=p+p:
            ans -= ((num[x]-p)//p)*(p-1)
            num[x] -= ((num[x]-p)//p)*p
    r = []
    for x in range(1, p):
        for t in range(num[x]):
            r.append(x)
    best = len(r)
    for perm in itertools.permutations(r):
        s = 0
        cou = 0
        for x in perm:
            if s!=0:
                cou += 1
            s = (s+x)%p
        best = min(best, cou)
    print 'Case #{}: {}'.format(ti+1, ans-best)
