def g(l, k):
    s = '+' * l
    d = {}
    d[s] = 0
    Q = [s,]
    while len(Q):
        cs = Q[0]
        Q = Q[1:]
        for i in range(0, l-k+1):
            _s = ''
            for j in xrange(l):
                if j >= i and j < i+k:
                    _s += '-' if cs[j] == '+' else '+'
                else:
                    _s += cs[j]
            if not d.has_key(_s):
                d[_s] = d[cs] + 1
                Q.append(_s)
    return d


# g(3, 1)

T = input()
for _ in xrange(T):
    S,K = raw_input().split(' ')
    K = int(K)
    L = len(S)
    d = g(L, K)
    ret = "IMPOSSIBLE"
    if d.has_key(S):
        ret = d[S]
    print "Case #%s: %s" % (_+1, ret)
