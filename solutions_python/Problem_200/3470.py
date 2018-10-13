#!/bin/env python

def integer(args):
    result = [str(arg) for arg in args]
    return int("".join(result))

def last_tidy_number(n):
    s = str(n)
    t = [int(c) for c in s]
    end = len(s) - 1

    i = 0
    while i < end:
        if t[i + 1] < t[i]:
            break
        i += 1
    else:
        # Didn't break out of loop.
        # So this is a tidy number itself.
        return n

    # T[i] won't be zero since the digit
    # on its right was less than it, ie,
    # T[i+1] < T[i].
    t[i] -= 1

    if t[i] == 0:
        if i == 0:
            # Handle cases like 10, 100, 1000, ...
            return integer([9] * (len(t) - 1))
        else:
            # Converted 1 to 0. Everything on the
            # right can only be a 0.
            arg = t[:i+1] + ([0] * len(t[i+1:]))
            return last_tidy_number(integer(arg))

    result1 = t[:i+1]
    result2 = [9] * (len(t[i+1:]))
    return last_tidy_number(integer(result1 + result2))

def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = int(raw_input())
        result = last_tidy_number(n)
        print "Case #{}: {}".format(i, result)

if __name__ == "__main__":
    main()
