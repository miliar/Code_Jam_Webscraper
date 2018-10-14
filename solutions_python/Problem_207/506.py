# Google Code Jam
# Round 1B 2017
# Problem B. Stable Neigh-bors

import numpy as np
from collections import deque, Counter

t = int(input())  # read a line with a single integer
for case in range(1, t + 1):
    N, R, O, Y, G, B, V = map(int, input().split())
    assert O + G + V == 0
    assert R + Y + B == N
    if max(R, Y, B) > N//2:
        print("Case #{0}: IMPOSSIBLE".format(case))
    else:
        pattern = ['']*N
        seq = [i for i in range(N) if i%2 == 0] + [i for i in range(N) if i%2 == 1]
        seq = deque(seq)
        if max(R,Y,B) == R:
            for i in range(R):
                pattern[seq.popleft()] = 'R'
            for i in range(Y):
                pattern[seq.popleft()] = 'Y'
            for i in range(B):
                pattern[seq.popleft()] = 'B'
        elif max(R,Y,B) == Y:
            for i in range(Y):
                pattern[seq.popleft()] = 'Y'
            for i in range(R):
                pattern[seq.popleft()] = 'R'
            for i in range(B):
                pattern[seq.popleft()] = 'B'
        else:
            if max(R,Y,B) == B:
                for i in range(B):
                    pattern[seq.popleft()] = 'B'
                for i in range(Y):
                    pattern[seq.popleft()] = 'Y'
                for i in range(R):
                    pattern[seq.popleft()] = 'R'

        result = ''.join(pattern)
        print("Case #{0}: {1}".format(case, result))

# --- HOW TO USE ---
# python test.py < input > output
