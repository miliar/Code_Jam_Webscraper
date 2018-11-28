
# -*- coding: utf-8 -*-

import itertools
import sys

def is_tidy(n):
    last = 0
    for s in str(n):
        if last > int(s):
            return False
        last = int(s)
    return True


T = int(input())
for t in range(T):
    N = int(input())
    for n in range(N, 0, -1):
        if is_tidy(n):
            result = n
            break

    print("Case #" + str(t + 1) + ": " + str(result))
