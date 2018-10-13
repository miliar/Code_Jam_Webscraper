T = int(raw_input().strip())
for C in xrange(T):
    n = int(raw_input().strip())
    nao = sorted(map(float, raw_input().strip().split()))
    ken = sorted(map(float, raw_input().strip().split()))
    i = 0
    ans1, ans2 = 0, 0
    for s in nao:
        if s > ken[i]:
            ans1 += 1
            i += 1

    i = n - 1
    for s in reversed(nao):
        if s > ken[i]:
            ans2 += 1
        else:
            i -= 1
    print "Case #%d: %d %d" % (C + 1, ans1, ans2)
