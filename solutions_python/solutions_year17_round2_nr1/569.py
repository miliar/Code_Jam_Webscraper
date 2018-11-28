# Google Code Jam
# Round 1B 2017
# Problem A. Steed 2: Cruise Control

import numpy as np

t = int(input())  # read a line with a single integer
for case in range(1, t + 1):
    D, N = map(int, input().split())
    horses = np.zeros((N, 2))
    for i in range(N): horses[i] = [int(c) for c in input().split()]
    tmax = np.max((D - horses[:,0])/horses[:,1])
    speed = D/tmax
    print("Case #{0}: {1:.6f}".format(case, speed))

# --- HOW TO USE ---
# python test.py < input > output

