def all_powered(chain, N):
    return chain == (2**N - 1)

def solve(N, K):
    x = 2**N
    last_chain = K % x
    return all_powered(last_chain, N)

if __name__ == '__main__':
    T = input()
    for i in xrange(T):
        N, K = [int(x) for x in raw_input().split()]
        on = solve(N, K)
        print 'Case #%d: %s' % (i + 1, 'ON' if on else 'OFF')
