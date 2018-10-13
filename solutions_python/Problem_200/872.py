#!/usr/bin/python3

import sys

def istidy(i):
    """Takes a positive integer and returns whether or not it is 'tidy'."""
    i = int(i)
    if i < 0:
        return False
    istr = str(i)
    largest_digit = '0'
    for digit in istr:
        if largest_digit > digit:
            return False
        else:
            largest_digit = digit
    return True

def bf_prev_tidy_int(i):
    """Determines the largest 'tidy' number <= the passed in positive integer.

    This function does this by counting backwards until it finds a
    tidy number.  This may potentially be very slow for large numbers.
    So this is a 'brute force' algorithm for testing.
    """
    i = int(i)
    if i < 0:
        raise RuntimeError("{} must be a positive integer!".format(i))
    for tnum in range(i, -1, -1):
        if istidy(tnum):
            return tnum
    assert False

def prev_tidy_int(i):
    """Takes a positive integer and returns largest tidy number <= the integer."""
    i = int(i)
    if i < 0:
        raise RuntimeError("{} must be a positive integer!".format(i))
    istr = str(i)
    largest_digit = '0'
    idx = 0
    c = ''
    for idx, c in enumerate(istr):
        if c < largest_digit:
            break
        else:
            largest_digit = c
    if largest_digit == c:
        return i
    else:
        assert idx > 0
        ilst = list(istr[0:idx]) + ['9'] * len(istr[idx:])
        idx = idx - 1
        while idx > 0:
            if ilst[idx] == '0':
                ilst[idx] = '9'
            else:
                ilst[idx] = chr(ord(ilst[idx]) - 1)
                if ilst[idx] >= ilst[idx - 1]:
                    return int(''.join(ilst))
                else:
                    ilst[idx] = '9'
            idx = idx - 1
        if ilst[0] != '1':
            ilst[0] = chr(ord(ilst[idx]) - 1)
        else:
            ilst = ilst[1:]
        return int(''.join(ilst))

def process_stdin():
    numnums = int(sys.stdin.readline())
    for case in range(1, numnums + 1):
        i = int(sys.stdin.readline())
        print("Case #{}: {}".format(case, prev_tidy_int(i)))

if __name__ == '__main__':
    process_stdin()
