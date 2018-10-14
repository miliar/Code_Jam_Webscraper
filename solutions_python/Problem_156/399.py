nc = int(raw_input())
for cid in range(nc):
    n = int(raw_input())
    a = sorted(map(int, raw_input().split()), reverse=True)
    ans = max(a)+1
    for i in range(1, max(a)+1):
        cnt = i
        for x in a:
            if x - i > 0:
                cnt += (x - 1) / i
        ans = min(ans, cnt)
    print 'Case #%d: %d' % (cid+1, ans)
