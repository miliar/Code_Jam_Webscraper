import sys
cases = int(sys.stdin.readline())
for case in range(1, cases+1):
    n, counts = sys.stdin.readline().split(' ')
    ct = 0
    ans = 0
    for s in range(int(n) + 1):
        if ct < s:
            ans += s - ct
            ct = s
        ct += int(counts[s])
    print "Case #%d: %d" % (case, ans)
