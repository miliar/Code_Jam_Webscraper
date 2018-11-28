#!/usr/bin/python3

from common import *

# square root of i, rounded down
def int_sqrt(i):
    if i <= 1:
        return i

    # Easier version:
    # low = 0
    # high = i + 1
    # Faster version:

    log4 = 0
    power4 = 1
    while power4 < i:
        log4 += 1
        power4 *= 4
    high = (2 ** log4) + 1
    low = (2 ** (log4 - 1))

    # Binary search
    while low + 1 < high:
        # The answer is in the range [low, high)
        mid = (low + high) // 2
        mid2 = mid * mid
        if mid2 == i:
            return mid
        if mid2 < i:
            low = mid
        else:
            high = mid
    return low

def num_digits(i):
    n = 0
    while i > 0:
        n += 1
        i = i // 10
    return n

# Returns whether the square of the palindrome is also a palindrome, and
# lies in the correct interval [a, b].
# The palindrome "12344321" is represented by digits = [1, 2, 3, 4].
def is_valid_even(digits, a = None, b = None):
    # Is the square a palindrome? Calculate sum of squares of the digits.
    ss = 0
    for d in digits:
        ss += 2 * d * d
    if ss >= 10:
        return False

    if a is None:
        return True

    num = 0
    for d in digits:
        num *= 10
        num += d
    for i in range(len(digits)):
        num *= 10
        num += digits[len(digits) - 1 - i]

    num = num * num
    return num >= a and num <= b

# Returns whether the square of the palindrome is also a palindrome, and
# lies in the correct interval [a, b].
# The palindrome "1234321" is represented by digits = [1, 2, 3, 4].
def is_valid_odd(digits, a = None, b = None):
    # Is the square a palindrome? Calculate sum of squares of the digits.
    ss = 0
    for d in digits:
        ss += 2 * d * d
    ss -= digits[-1] * digits[-1]
    if ss >= 10:
        return False

    if a is None:
        return True

    num = 0
    for d in digits:
        num *= 10
        num += d
    for i in range(1, len(digits)):
        num *= 10
        num += digits[len(digits) - 1 - i]

    num = num * num
    return num >= a and num <= b

def num_valid_in_range(aa, bb):
    a = int_sqrt(aa)
    b = int_sqrt(bb) + 1
    # Find all palindromes in range [a, b]
    n_digits_a = num_digits(a)
    n_digits_b = num_digits(b)
    # print (aa, bb, a, b, n_digits_a, n_digits_b)

    # These ranges of digits are inclusive
    even_low = (n_digits_a + 1) // 2
    even_high = (n_digits_b) // 2
    odd_low = (n_digits_a + 2) // 2
    odd_high = (n_digits_b + 1) // 2

    num_valid = 0
    # First do even palindromes
    for e_digits in range(even_low, even_high + 1):
        # print (e_digits, "even digits")
        digits = [0] * e_digits
        digits[0] = 1
        while True:
            if is_valid_even(digits, aa, bb):
                # print ("Even: ", digits)
                num_valid += 1
            # get next palindrome
            for i in range(0, len(digits)):
                if digits[len(digits) - 1 - i] == 9:
                    digits[len(digits) - 1 - i] = 0
                else:
                    digits[len(digits) - 1 - i] += 1
                    break
            if digits[0] == 0:
                break
    # Then do odd palindromes
    for o_digits in range(odd_low, odd_high + 1):
        # print (o_digits, "odd digits")
        digits = [0] * o_digits
        digits[0] = 1
        while True:
            if is_valid_odd(digits, aa, bb):
                # print ("Odd: ", digits)
                num_valid += 1
            # get next palindrome
            for i in range(0, len(digits)):
                if digits[len(digits) - 1 - i] == 9:
                    digits[len(digits) - 1 - i] = 0
                else:
                    digits[len(digits) - 1 - i] += 1
                    break
            if digits[0] == 0:
                break
    return num_valid

def testcase(x):
    a, b = readintegers()
    ans = num_valid_in_range(a, b)
    writeline("Case #%d: %d" % (x, ans))

run_tests(testcase)
