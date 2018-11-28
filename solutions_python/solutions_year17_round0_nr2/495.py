#! /usr/bin/env python3
import sys

T = int(sys.stdin.readline().strip())
for i, line in enumerate(sys.stdin.readlines()):
    N = line.strip()
    digits = [int(d) for d in N]
    first_nine_index = len(digits)
    for index in range(len(digits)-1, 0, -1):
        if digits[index] < digits[index-1]:
            # digits[index-1] couldn't have been 0, so no problem decreasing it
            digits[index-1] -= 1
            first_nine_index = index
    print(
        'Case #{}: {}'.format(
            i+1,
            ''.join(
                [str(d if di < first_nine_index else 9)
                 for di, d in enumerate(digits)]
            ).lstrip('0')))
