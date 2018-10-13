def solve():
    s, k = raw_input().split()
    k = int(k)
    s = [x == '+' for x in s]
    ans = 0
    for i in xrange(len(s) - k + 1):
        if s[i]:
            continue
        ans += 1
        for j in xrange(k):
            s[i+j] = not s[i+j]
    if all(s):
        print ans
    else:
        print "IMPOSSIBLE"

T = int(raw_input())
for i in xrange(T):
    print "Case #%d:" % (i + 1),
    solve()
