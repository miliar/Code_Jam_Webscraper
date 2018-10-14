from sys import stdin

T = int(next(stdin))

for t in range(1, T+1):
    D, N = map(int, next(stdin).strip().split(" "))
    MAX = 0
    for _ in range(N):
        K, S = map(int, next(stdin).strip().split(" "))
        MAX = max(MAX, (D-K) / S)
    print("Case #{0}: {1:.6f}".format(t, D / MAX))
