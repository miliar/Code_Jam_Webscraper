T = int(raw_input())
for t in xrange(1, T+1):
    s, k = raw_input().split()
    s, k = map(lambda x: 1 if x == "+" else 0, list(s)), int(k)
    cnt = 0
    for i in xrange(len(s)-k+1):
        if s[i] == 0:
            cnt += 1
            for j in xrange(i, i+k):
                s[j] = 1-s[j]
    if sum(s) == len(s):
        ans = str(cnt)
    else:
        ans = "IMPOSSIBLE"
    print "Case #%d: %s" % (t, ans)
