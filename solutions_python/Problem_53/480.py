def solve(N, K):
    states = [0] * N
    power = 0

    for i in xrange(K):
#        print power
#        print ' '.join(map(str, states))
#
        for i in xrange(power + 1):
            if i >= N:
                break
            states[i] = 1 - states[i]

        power = 0
        for i, p in enumerate(states):
            if not p:
                break
            power = i + 1

    ans = N <= power
#    print N, power, states, ans
    return ans

#def solve(N, K):
#    N -= 1
#
#    r = bin(K)[:1:-1]
#    l = len(r)
#
#    state = 0
#    if N < l:
#        state = int(r[N])
#
#    return state

#def solve(N, K):
#    n = 1<<(N-1)
#    return (K // n) % 2

#for n in xrange(1, 30):
#    for k in xrange(0, 30):
#        print 'n=%d' % n, 'k=%d' % k
#        exp = (k // 2**(n-1)) % 2
#        ans = solve(n, k)
#        assert exp == ans, 'n=%d k=%d e=%d a=%d' % (n, k, exp, ans)
#
#raise SystemExit

T = int(raw_input())

for case in xrange(1, T + 1):
    N, K = map(int, raw_input().split())
    state = solve(N, K)

    answer = ('OFF', 'ON')[state]

    print 'Case #%d: %s' % (case, answer)

