t = input()
for _t in xrange(t):
    t -= 1
    n, s = raw_input().split()
    n = int(n)
    sigma = 0
    ans = 0;
    for i in xrange(n + 1):
        #print sigma, i
        if sigma >= i:
            sigma += int(s[i])
        else:
            ans += i - sigma
            sigma = i + int(s[i])
    print 'Case #' + str(_t + 1) + ':', ans
