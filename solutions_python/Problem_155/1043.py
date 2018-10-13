T = int(raw_input())
for t in xrange(T):
    _, s = raw_input().split()
    ans = 0
    cnt = 0
    for i in xrange(len(s)):
        while cnt < i:
            cnt += 1
            ans += 1
        cnt += int(s[i])
    print "Case #{}: {}".format(t+1, ans)
