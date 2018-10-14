from __future__ import print_function

import fractions
import sys

def calc(N_str):
    digits = [int(ch) for ch in N_str]
    n = len(digits)
    last_9 = n  # None yet.
    for i in range(n-1, 0, -1):  # Exclude 0.
        if digits[i-1] > digits[i]:
            digits[i - 1] -= 1
            for j in range(i, last_9):
                digits[j] = 9
            last_9 = i
    if digits[0] == 0:
        del digits[0]
    return ''.join(map(str, digits))

def main():
    f = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "rt")

    T = int(f.readline().strip())

    for case_id in range(1, T+1):
        N_str = f.readline().strip()

        r = calc(N_str)

        print('Case #{}: {}'.format(case_id, r))

if __name__ == '__main__':
    main()
    # do_stuff()
