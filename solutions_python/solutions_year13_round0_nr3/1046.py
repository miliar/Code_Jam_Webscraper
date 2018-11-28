from math import floor, ceil
import datetime

__author__ = 'danolsen'

def is_palindrome(num):
    str_num = str(num)
    return (str_num == str_num[::-1])

f = open('pal_input.txt', 'r')
test_cases = f.readline()
test_cases = int(test_cases.strip())

for i in range(0, test_cases, 1):
    a = datetime.datetime.now()
    numbers = f.readline().strip().split()
    start = long(numbers[0])
    end = long(numbers[1])

    start_square = long(floor(start**.5))
    end_square = long(floor(end**.5))

    # print '%d (%d) - %d (%d)' % (start_square, start, end_square, end)

    # print start, end

    counter = 0
    j = start_square

    while j <= end_square:
        if is_palindrome(j):
            square_j = j**2
            if square_j >= start and square_j <= end and j**2 and is_palindrome(square_j):
            # if is_palindrome(long(j**.5)):
                counter += 1
        j += 1



    print 'Case #%d: %d' % (i + 1, counter)
    # b = datetime.datetime.now()
    # c = b - a
    # print '%d.%d' % (c.seconds, c.microseconds)