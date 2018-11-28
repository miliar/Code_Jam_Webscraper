wel = "welcome to code jam"
L = len(wel)
N = int(raw_input())
for k in xrange(N):
    a = [0]*(L+1)
    a[0] = 1
    str = raw_input()
    for i in xrange(len(str)):
        for j in xrange(L, 0, -1):
            if wel[j-1] == str[i]:
                a[j] = (a[j] + a[j-1])%10000

    res = ''
    p, t = 1000, a[L]
    while p > 0:
        res += chr(ord('0') + t/p)
        t %= p
        p /= 10
    print "Case #%d: %s" % (k+1, res)