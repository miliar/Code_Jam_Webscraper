from __future__ import print_function
import numpy as np

def tidy_number(N):

    digits = 0
    strN = str(N)
    digits = len(strN)

    #Special case
    if N < 10:
        return N
    elif N ^ 10**(digits-1) == 0:
        return N-1
    top = np.array([int(x) for x in strN])
    hi = [0, 1, top[0]]
    for i in range(digits-1):
        if top[i] > hi[2]:
            hi = [i, i+1, top[i]]
        elif top[i] == hi[2]:
            hi[1] = i

        if top[i] > top[i+1]:
            top[hi[0]] -= 1
            top[hi[0]+1:] = 9
            break

    return int("".join(str(e) for e in top))

test_cases = int(input())
for case in range(test_cases):
    num = int(input())
    print('Case #{}: '.format(case+1), tidy_number(num))






