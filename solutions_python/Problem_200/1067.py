def good(x):
    last = 9;
    while x:
        if x % 10 > last: return False
        last = x % 10
        x /= 10
    return True

T = int(raw_input().strip())
for C in xrange(1, T+1):
    n = int(raw_input().strip())
    ans = 1;
    for i in xrange(1, n+1):
        if good(i): ans = i
    print "Case #%d: %d" % (C, ans)
