#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys


def solve(a, b):
    intersection = list(set(a) & set(b))
    equals = len(intersection)
    
    if equals == 0:
        return 'Volunteer cheated!'
    elif equals == 1:
        return str(intersection[0])
    
    return 'Bad magician!'


def main():
    cases = int(sys.stdin.readline().strip())
    for case in xrange(cases):
        first_answer = int(sys.stdin.readline().strip())
        first_rows = [
            map(int, sys.stdin.readline().strip().split(' ')),
            map(int, sys.stdin.readline().strip().split(' ')),
            map(int, sys.stdin.readline().strip().split(' ')),
            map(int, sys.stdin.readline().strip().split(' '))
        ]
        first_row = first_rows[first_answer - 1]
        
        second_answer = int(sys.stdin.readline().strip())
        second_rows = [
            map(int, sys.stdin.readline().strip().split(' ')),
            map(int, sys.stdin.readline().strip().split(' ')),
            map(int, sys.stdin.readline().strip().split(' ')),
            map(int, sys.stdin.readline().strip().split(' '))
        ]
        second_row = second_rows[second_answer - 1]
        
        print 'Case #%d:' % (case + 1), solve(first_row, second_row)
    return 0


if __name__ == '__main__':
    sys.exit(main())

