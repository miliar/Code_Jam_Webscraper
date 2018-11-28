#!/usr/bin/python3

import itertools, sys

def gf2div(dividend, divisor):
    """Does a Galois field division in a Galois field of characteristic 2."""
    divisor = tuple(itertools.dropwhile(lambda x: not x,
                                        ((x and 1 or 0) for x in divisor)))
    dividend = list(itertools.dropwhile(lambda x: not x,
                                        ((x and 1 or 0) for x in dividend)))
    quotient = []
    while len(divisor) <= len(dividend):
        if dividend[0]:
            quotient.append(1)
            for i, bit in enumerate(divisor):
                dividend[i] = dividend[i] ^ bit
            dividend = dividend[1:]
        while (len(dividend) > 0) and (not dividend[0]):
            if len(dividend) >= len(divisor):
                quotient.append(0)
            dividend = dividend[1:]
    return (quotient, dividend)

def read_pancakes():
    cases = int(sys.stdin.readline())
    for count in range(1, cases + 1):
        pancakes = sys.stdin.readline().strip()
        pancakes, flipperbits = pancakes.split()
        flipperbits = (1,) * int(flipperbits)
        pancakes = tuple((1 if c == '-' else 0) for c in pancakes)
        quot, rem = gf2div(pancakes, flipperbits)
        if len(rem) > 0:
            print("Case #{}: IMPOSSIBLE".format(count))
        else:
            print("Case #{}: {}".format(count, sum(quot)))

if __name__ == '__main__':
    read_pancakes()
