import numpy as np


t = int(input())
for c in range(1, t + 1):
    s, k = input().split()
    s = np.array(list(map(lambda x: x == '+', s)))
    k = int(k)

    r = 0
    for i in range(len(s)):
        if i <= len(s) - k and not s[i]:
            r += 1
            s[i:i+k] = np.logical_not(s[i:i+k])
        if not s[i]:
            r = -1
            break
    print('Case #{}: {}'.format(c, ('IMPOSSIBLE', r)[r >= 0]))
