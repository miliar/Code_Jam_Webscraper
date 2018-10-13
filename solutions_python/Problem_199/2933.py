from __future__ import print_function
import numpy as np
import math

cast = lambda x: True if x == '+' else False

def pancakes(row, k):

    if len(row) == 0:
        return 0
    if len(row) < k and False in row:
        return 'IMPOSSIBLE'
    flips = 0
    for i in range(len(row)-k+1):
        if not row[i]:
            row[i:i+k] ^= True
            flips+=1
    if not False in row:
        return flips
    else:
        return 'IMPOSSIBLE'




test_cases = int(raw_input())
for case in range(test_cases):
    line = raw_input()
    row, k = line.split(' ')
    k = int(k)
    row = np.array([cast(x) for x in row])
    print('Case #{}: '.format(case+1), pancakes(row, k))






