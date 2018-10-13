def rev(s):
    l = len(s)
    ans = ""
    for i in range(l - 1, -1, -1):
        ans += s[i]
    return ans
sq = [0] * 1001
for i in xrange(100):
    if i * i < 1000:
        st = str(i)
        rst = rev(st)
        ssq = str(i * i)
        rssq = rev(ssq)
        if st == rst and ssq == rssq:
            sq[i * i] = 1
d = [0 for i in xrange(1001)]
for i in range(1001):
    if sq[i] == 1:
        d[i] = d[i - 1] + 1
    else:
        d[i] = d[i - 1]
T = input()
for kase in xrange(T):
    A, B = map(int,raw_input().split())
    id = kase + 1
    ans = d[B] - d[A - 1]
    print "Case #" + str(id) + ":", ans   