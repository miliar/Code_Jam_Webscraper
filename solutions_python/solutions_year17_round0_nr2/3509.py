#!/usr/bin/env python3

import sys

def read():
    return sys.stdin.readline().strip()

def tidy_numbers(n):
    if n == 1:
        for i in range(1, 10):
            yield str(i)
    else:
        for m in tidy_numbers(n-1):
            last_digit = int(m[-1])
            for i in range(last_digit, 10):
                yield m + str(i)

def all_tidy_numbers(start_length):
    for length in range(start_length, 20):
        for num in tidy_numbers(length):
            yield num

def largest_below(n):
    num_digits = len(str(n))
    Max = 0
    start_length = max(num_digits-1, 1)

    for num in all_tidy_numbers(start_length):
        if int(num) > n:
            break
        else:
            Max = int(num)

    return Max

def main():
    num_cases = int(read())
    for i in range(num_cases):
        n = int(read())
        print("Case #{}: {}".format(i+1, largest_below(n)))
        sys.stdout.flush()

if __name__ == '__main__':
    main()

