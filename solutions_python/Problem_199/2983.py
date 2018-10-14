# Google Code Jam 2017
# Qualification Round
# Problem B. Tidy Numbers

import numpy as np

t = int(input())  # read a line with a single integer
for case in range(1, t + 1):
    S, K = input().split(" ")
    S = np.array([c == '+' for c in S])
    N = len(S)
    K = int(K)
    flips = 0
    for i in range(N - K + 1):
        if not S[i]:
            S[i:i+K] = np.logical_not(S[i:i+K])
            flips += 1
    if S.all():
        print("Case #{0}: {1}".format(case, flips))
    else:
        print("Case #{0}: IMPOSSIBLE".format(case))

# --- HOW TO USE ---
# python test.py < input > output

