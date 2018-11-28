#!/bin/python


def find_max_digit(number):
    result = 0
    while number:
        result = max(result, number%10)
        number = number/10
    return result


def proc():
    result = ''
    number = int(raw_input())
    while (number >= 10):
        now = number % 10
        number = number / 10
        max_digit = find_max_digit(number)
        if max_digit > now:
            result = '9' * len(result)
            now = 9
            number -= 1
        result = str(now) + result

    if (number > 0):
        result = str(number) + result
    return result




if __name__ == '__main__':
    T = int(raw_input())
    for t in xrange(1, T+1):
        print 'Case #{}: {}'.format(t, proc())
