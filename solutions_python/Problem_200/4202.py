#!/usr/bin/python


def calculate(number):
    digits = number_to_digits(number)
    while True:
        if not is_tidy(digits):
            wrong = find_wrong_number(digits)
            digits[wrong-1] = digits[wrong-1] - 1
            digits[wrong:] = [9] * (len(digits)-wrong)
        else:
            return digits_to_number(digits)


def number_to_digits(number):
    return [int(i) for i in str(number)]


def digits_to_number(digits):
    return int(''.join(str(i) for i in digits))


def find_wrong_number(digits):
    for i in range(0, len(digits)+1):
        sub_digits = digits[0:i]
        if not sub_digits == sorted(list(sub_digits)):
            return i-1


def is_tidy(digits):
    sort = sorted(list(digits))
    return digits == sort


t = int(raw_input())
for i in xrange(1, t + 1):
    row = raw_input()
    result = calculate(int(row))
    print "Case #{}: {}".format(i, result)
