#!/usr/bin/env python

import numpy as np

T = int(input().strip())
for t in range(T):
    S,K = input().strip().split()
    k = int(K)
    binary = np.array([(0 if x == '-' else 1) for x in S])
    size = len(S)
    ans = 0
    for i in range(size):
        if binary[i:i+1] == 0:
            if size - i < k:
                ans = 'IMPOSSIBLE'
                break
            else:
                binary[i:i+k] = 1-binary[i:i+k]
                ans+=1


    print("Case #%d: %s" % (t+1, str(ans)))
