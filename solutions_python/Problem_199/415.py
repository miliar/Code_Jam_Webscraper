T = input()
d = {'+': '-', '-': '+'}
for x in range(1, T + 1):
    S, K = raw_input().split(' ')
    S = list(S)
    K = int(K)
    n = len(S)

    delta = 0
    ans = 'IMPOSSIBLE'
    t = [0 for i in xrange(3 * n)]
    ansCount = 0
    for i in xrange(n):
        delta += t[i]
        if delta % 2 == 1:
            S[i] = d[S[i]]
        if S[i] == '-':
            if K > 1:
                delta += 1
                t[i + K] = -1
            if i < n - K + 1:
                ansCount += 1
                S[i] = '+'
    if S.count('-') == 0:
        ans = ansCount
    print 'Case #%d: %s' % (x, str(ans))


