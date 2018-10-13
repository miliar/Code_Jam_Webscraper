import sys

T = int(sys.stdin.readline())


for case in range(1, T + 1):
    (S, K) = sys.stdin.readline().split()
    K = int(K)
    n = len(S)

    flips = 0
    flipped = [False for i in range(K)]

    for i in range(n - K + 1):
        isOn = (S[i] == '+') != flipped[0]

        if not isOn:
            flips += 1
            flipped = [not x for x in flipped[1:]] + [False]
        else:
            flipped = flipped[1:] + [False]

    final = [(x == '+') != flipped[i] for (i, x) in enumerate(S[-(K-1):])]
    result = flips if all(final) else "IMPOSSIBLE"

    print("Case #{}: {}".format(case, result))