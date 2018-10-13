#!/usr/bin/env python3

from functools import reduce

def digits(n):
    while n:
        yield n % 10
        n //= 10

def solve(n):
    d = list(digits(n))
    l = len(d)

    i = 0
    while i < l:
        if not all(map(lambda x: d[i] >= x, d[i+1:])):
            d[i] = 9
            d[i+1] -= 1
            for j in range(i):
                d[j] = 9
            i = 0
        else:
            i += 1

    return reduce(lambda x, y: x*10+y, reversed(d))

def main():
    T = int(input())

    for i in range(T):
        result = solve(int(input()))

        print('Case #{0}: {1}'.format(i+1, result))

if __name__ == '__main__':
    main()
