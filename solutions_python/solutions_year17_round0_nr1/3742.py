from sys import stdin

T = int(stdin.readline())

def flip(A, p, K):
    for i in range(p, p + K):
        A[i] = not A[i]

for t in range(T):
    cakes, K = stdin.readline().split()
    cakes = [p == "+" for p in cakes]
    K = int(K)

    flips = 0
    for i in range(len(cakes) - K + 1):
        if not cakes[i]:
            flip(cakes, i, K)
            flips += 1

    if not all(cakes[i] for i in range(len(cakes) - K + 1, len(cakes))):
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: {flips}")
