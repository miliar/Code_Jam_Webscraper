import math


def fair_and_square_numbers(a, b):
    sqrt, n = first_square(a, b)
    step = 2*sqrt + 1
    if not sqrt:
        return 0
    numbers = 0
    while n <= b:
        if is_palindrome(n) and is_palindrome(sqrt):
            numbers += 1
        n += step
        sqrt += 1
        step += 2
    return numbers


def first_square(a, b):
    while a <= b:
        sqrt = int(math.sqrt(a))
        if sqrt*sqrt == a:
            return sqrt, a
        a += 1
    return False, a


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


cases = int(input())
for i in range(1, cases+1):
    limits = input().split(' ')
    a = int(limits[0])
    b = int(limits[1])
    print("Case #" + str(i) + ":", fair_and_square_numbers(a, b))
