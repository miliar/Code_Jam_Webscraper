#!/usr/bin/env python3

import fileinput
import random

def is_tidy(n):
    for i, c in enumerate(str(n)[:-1]):
        if c > str(n)[i+1]:
            return False
    return True


def solve(number):
    digits = [int(c) for c in str(number)]

    # find first non-tidy digit
    for first_invalid, d in enumerate(digits):
        if first_invalid+1 < len(digits) and d > digits[first_invalid+1]:
            break
    else:
        # input was already tidy
        return number

    # find last digit that can be tidily decremented
    decr_index = first_invalid
    while decr_index > 0:
        if digits[decr_index] > digits[decr_index-1]:
            digits[decr_index] = max(digits[decr_index-1], digits[decr_index]-1)
            for i in range(decr_index+1, len(digits)):
                digits[i] = 9
            return int(''.join(str(d) for d in digits))
        decr_index -= 1
    
    # decrement first digit and set rest to 9s
    digits = [digits[0]-1] + [9] * (len(digits)-1)
    return int(''.join(str(d) for d in digits))


def test_samples():
    assert solve(132) == 129
    assert solve(1000) == 999
    assert solve(7) == 7
    assert solve(111111111111111110) == 99999999999999999


def test_corners():
    assert solve(0) == 0
    assert solve(123) == 123
    assert solve(987) == 899


def test_solve_annoying():
    assert solve(11111222244444222200002229999000) == 11111222239999999999999999999999


def test_random():
    for _ in range(100):
        ex = random.randint(0, 100000000)
        result = solve(ex)
        assert result <= ex
        assert is_tidy(result)


def main():
    n = int(input())
    for i, line in enumerate(fileinput.input()):
        highest = solve(int(line))
        assert is_tidy(highest), '{} not tidy'.format(highest)
        assert highest <= int(line)
        print('Case #{}: {}'.format(i+1, highest))

    assert i == n-1, 'read wrong number of cases'


if __name__ == '__main__':
    main()
