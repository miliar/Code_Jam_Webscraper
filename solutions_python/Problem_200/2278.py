
import sys
import math


def solution(K):
    if len(K) == 1:
        return K

    for i in range(len(K) - 1):
        if K[i] > K[i+1]:
            K = solution(K[:i] + str(int(K[i]) - 1)) + "9" * (len(K) - i - 1)
            break
    return str(int(K))


def solve(lines):
    T = int(next(lines))
    for t in range(1, T + 1):
        K = next(lines).strip()
        a = solution(K)
        print(f"Case #{t}: {a}")


solve(sys.stdin)
