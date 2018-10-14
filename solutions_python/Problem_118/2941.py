__author__ = 'nick'
import sys
import math

def process_input(filename):
    f = open(filename, 'r')
    cases = int(f.readline())

    for i in range(0, cases):
        line = f.readline()
        points = line.split(' ')
        start = int(points[0])
        end = int(points[1])
        sqPalInRange = 0

        for j in range(start, end+1):
            if is_palindrome(str(j)) and is_palindrome(str(get_sqrt(j))):
                sqPalInRange += 1

        print('Case #'+str(i+1)+': '+str(sqPalInRange))

def is_palindrome(line):
    return line == line[::-1]

def get_sqrt(value):
    sqrt = math.sqrt(value)
    if int(sqrt) * int(sqrt) == value:
        return int(sqrt)
    return sqrt

if __name__ == '__main__':
    if len(sys.argv) > 1:
        process_input(sys.argv[1])