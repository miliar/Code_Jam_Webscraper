#!/usr/bin/env python
# coding=utf-8

import sys


def solve(first_answer, second_answer, first_arrangement, second_arrangement):
    set_1 = set(first_arrangement[first_answer-1])
    set_2 = set(second_arrangement[second_answer-1])
    inter = set_1 & set_2
    if len(inter) == 1:
        return inter.pop()
    elif len(inter) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'


def main():
    with open(sys.argv[1]) as f:
        num_problems = int(f.readline().strip())
        for i in range(num_problems):
            first_answer = int(f.readline().strip())
            first_arrangement = [[int(x) for x in f.readline().strip().split()] for n in range(4)]
            second_answer = int(f.readline().strip())
            second_arrangement = [[int(x) for x in f.readline().strip().split()] for n in range(4)]
            res = solve(first_answer, second_answer, first_arrangement, second_arrangement)
            print('Case #{}: {}'.format(i+1, res))


if __name__ == '__main__':
    main()
