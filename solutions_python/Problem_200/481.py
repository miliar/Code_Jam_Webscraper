T = int(raw_input())
for t in xrange(1, T+1):
    n = list(reversed(raw_input()))
    ans = n[0]
    for c in n[1:]:
        if c <= ans[0]:
            ans = c + ans
        else:
            ans = str(int(c)-1) + "9"*len(ans)
    print "Case #%d: %d" % (t, int(ans))
