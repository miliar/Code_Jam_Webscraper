#!/usr/bin/env python3

def to_digits(n):
    assert n is not None

    return [int(c) for c in str(n)]

def to_num(digits):
    assert digits is not None

    s = ''.join([str(d) for d in digits])
    return int(s)

def fail_tidy_start(digits):
    assert digits is not None

    low = digits[0]
    for i, d in enumerate(digits[1:], start=1):
        if d < low:
            return i
        low = max(low, d)

    return None

def solve(n):
    assert n is not None

    digits = to_digits(n)

    while True:
        at = fail_tidy_start(digits)
        if at is None:
            break
        assert at > 0

        digits[at-1] -= 1

        len_rest = len(digits) - at
        digits[at:] = [9] * len_rest

    return to_num(digits)

T = int(input())
for i in range(T):
    N = input()
    N = int(N)
    result = solve(N)
    print(f'Case #{i+1}: {result}')
