T = input()
for t in range(T):
    N = input()
    perm = map(lambda x: int(x)-1, raw_input().split())
    cyc = 0
    processed = [False]*1024
    ans = 0.0
    for i in range(N):
        if not processed[i]:
            curr = i
            cyLen = 0
            while True:
                processed[curr] = True
                cyLen += 1
                curr = perm[curr]
                if curr == i:
                    break
            if cyLen > 1:
                ans += cyLen
    print 'Case #%d: %d' % (t+1, ans)