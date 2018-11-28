import sys

def solve():
    T = int(sys.stdin.readline())

    for tc in range(T):
        S, K = sys.stdin.readline().split()
        S = [1 if ch == '+' else 0 for ch in S]

        K = int(K)
        N = len(S)

        cnt = 0

        for i in range(N - K + 1):
            if S[i] == 0:
                S[i:i + K] = [i ^ 1 for i in S[i:i + K]]
                cnt += 1
                # print(*S, file=sys.stderr)

        for i in range(N - K + 1, N):
            if S[i] == 0:
                ans = 'IMPOSSIBLE'
                break
        else:
            ans = cnt

        print('Case #{}: {}'.format(tc + 1, ans))


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

if __name__ == '__main__':
    solve()