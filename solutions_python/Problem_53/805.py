import sys

def f(N, K):
    return bool(K % (2**N) == (2**N - 1))

def f2(N, K):

    state = [0 for i in range(N)]

    for i in range(K):

        for j in range(N):
            if state[j] == 0:
                break

        for k in range(j + 1):
            state[k] = int(not bool(state[k]))

    return sum(state) == len(state)

T = int(sys.stdin.readline())

for i in range(T):
    N, K = map(int, sys.stdin.readline().split())

    print 'Case #%d: %s' % (i + 1, 'ON' if f(N, K) else 'OFF')
