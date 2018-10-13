def solve(x, s):
    s.sort()
    res = 0
    i, j = 0, len(s)-1
    while i < j:
        if s[i] + s[j] <= x:
            i += 1
            j -= 1
        else:
            j -= 1
        res += 1
    if i == j:
        res += 1
    return res

T = int(raw_input())
for z in xrange(T):
    n, x = map(int,raw_input().split())
    s = map(int, raw_input().split())
    print "Case #%d: %d" % (z+1, solve(x, s))