
import sys


def nflips(S, K):
    n = 0
    for i in range(len(S) - K + 1):
        if not S[i]:
            S[i:i+K] = [not v for v in S[i:i+K]]
            n += 1
    if all(S):
        return n
    return None


def solve(lines):
    T = int(next(lines))
    for t in range(1, T + 1):
        S, K = next(lines).split()
        S = [s == "+" for s in S]
        K = int(K)
        a = nflips(S, K)
        if a is None:
            a = "IMPOSSIBLE"
        print(f"Case #{t}: {a}")


solve(sys.stdin)
