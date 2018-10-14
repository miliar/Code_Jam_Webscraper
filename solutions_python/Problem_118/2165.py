#! /usr/bin/env python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', 
                    action='store_true',
                    default=False,
                    dest='largeFile',
                    help='Use large practice input instead of small one.')

fairSquareNumbers = set([1, 9, 121])

def isPalindrone(number):
    number = str(number)
    return number == number[::-1]

def result(start, end):
    count = 0
    for number in xrange(start, end+1):
        if number in fairSquareNumbers:
            count += 1
        else:
            if isPalindrone(number):
                sqrt = number**0.5
                if sqrt == int(sqrt) and isPalindrone(int(sqrt)):
                    fairSquareNumbers.add(number)
                    count += 1
    return count

if __name__ == '__main__':
    args = vars(parser.parse_args())
    filename = 'C-small-attempt0.in' if not args['largeFile'] else 'C-large.in'
    try:
        contents = open(filename).read().splitlines()
    except:
        raise

    totalCases = int(contents[0])
    row = 1
    for case in xrange (1, totalCases+1):
        start, end = (int(n) for n in contents[row].split())
        print 'Case #' + str(case) + ': ' + str(result(start, end))
        row += 1

