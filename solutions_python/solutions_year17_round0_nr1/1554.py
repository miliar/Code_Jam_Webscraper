#!/usr/bin/env python3

def read_case():
    s, k = input().split()
    return [face == '+' for face in s], int(k)

for i in range(1, int(input()) + 1):
    print('Case #{}: '.format(i), end='')
    s, k = read_case()
    flip_count = 0
    for j in range(len(s) - k + 1):
        if s[j]: continue
        flip_count += 1
        for c in range(j, j + k):
            s[c] ^= True
    print(flip_count if all(s) else 'IMPOSSIBLE')
