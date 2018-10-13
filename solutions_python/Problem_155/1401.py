#!/usr/bin/env python3

T = int(input())

for n in range(T):
    digits = input().split()[1]
    clapping = 0
    extra = 0
    for i in range(len(digits)):
        digit = int(digits[i])
        if digit > 0 and clapping < i:
            extra += i - clapping
            clapping = i
        clapping += digit
    print('Case #{0}: {1}'.format(n + 1, extra))
