def lastTidy(n):
    ll = map(int, list(str(n)))
    for itr in xrange(len(ll)-1, 0, -1):
        if ll[itr] < ll[itr-1]:
            ll[itr] = 9
            ll[itr-1] -= 1
            for j in xrange(itr+1, len(ll)):
                if ll[j] < ll[j-1]:
                    ll[j] = 9

    return int("".join(map(str, ll)))


T = input()
for t in xrange(T):
    res = lastTidy(input())
    print 'Case #%d: %d' % (t+1, res)