T = int(raw_input())
for z in xrange(1,T+1):
    N = map(int, list(raw_input().strip()))
    L = len(N)
    if sorted(N) == N:
        ans = N
    else:
        ans = [9 for i in xrange(L-1)]
        if N[0] > 1:
            ans = [N[0]-1] + ans
        for i in xrange(L-1):
            if sorted(N[:i+1]) == N[:i+1] and N[i+1]-1 >= N[i]:
                ans = N[:i+1] + [N[i+1]-1] + [9 for j in xrange(L-(i+2))]
    print "Case #%d: %s" % (z, ''.join(map(str, ans)))
