#!/usr/bin/env python3

def is_palindrom(x):
    number = str(x)
    return number == number[::-1]

palindroms = {}
for x in range(1, 10 ** 7 + 1):
    square = x * x
    if is_palindrom(x) and is_palindrom(square):
        palindroms[square] = True

n = int(input())
for case in range(n):
    low, high = map(int, input().split())
    count = 0
    for palindrom in palindroms.keys():
        if low <= palindrom <= high:
            count += 1
    print('Case #{0}: {1}'.format(case + 1, count))
