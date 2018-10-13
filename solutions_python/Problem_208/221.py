import sys
from itertools import accumulate

inf = 1 << 64

def solve():
    T = int(sys.stdin.readline())

    for tc in range(T):
        N, Q = map(int, sys.stdin.readline().split())

        E = []
        S = []

        for i in range(N):
            e, s = map(int, sys.stdin.readline().split())
            E.append(e)
            S.append(s)

        D = []

        for i in range(N - 1):
            line = [int(i) for i in sys.stdin.readline().split()]
            D.append(line[i + 1])
        input()

        input() # U1, V1

        Dac = [0] + list(accumulate(D))

        dp = [[inf]*(N + 1) for i in range(N)]
        dp[0][0] = 0

        for i in range(1, N):
            for j in range(1, i):
                if E[j - 1] >= Dac[i] - Dac[j - 1]:
                    dp[i][j] = dp[i - 1][j] + D[i - 1] / S[j - 1]

            dp[i][i] = min(dp[i - 1][:i]) + D[i - 1] / S[i - 1]

            # print(*dp[i])

        ans = min(dp[N-1])

        print('Case #{}: {}'.format(tc + 1, ans))


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

if __name__ == '__main__':
    solve()