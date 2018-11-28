import sys

def solve():
    T = int(sys.stdin.readline())

    for tc in range(T):
        D, N = map(int, sys.stdin.readline().split())
        t = 0

        for i in range(N):
            K, S = map(int, sys.stdin.readline().split())
            t = max(t, (D - K) / S)

        ans = D / t
        
        print('Case #{}: {}'.format(tc + 1, ans))


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

if __name__ == '__main__':
    solve()