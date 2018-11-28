#!/usr/bin/env python3

def solve(n):
    start = -1
    for i, (j, k) in enumerate(zip(n, n[1:])):
        if j > k:
            break
        elif j < k:
            start = i
    else:
        return n

    return (n[:start + 1] + str(int(n[start + 1]) - 1) + '9' * (len(n) - start - 2)).lstrip('0')

for i in range(int(input())):
    print('Case #{}: {}'.format(i + 1, solve(input())))
