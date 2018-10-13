#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import math


def readData():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        for test in f:
            yield map(int, test.split(' '))


def writeData(data):
    with open('output.txt', 'w') as fout:
        fout.write('\n'.join(data))


def isPolyndrom(number):
    return number == number[::-1]


def solution():
    answer = []
    for case, l in enumerate(readData()):
        a, b = l
        count = 0
        for number in xrange(a, b + 1):
            if isPolyndrom(str(number)) and math.sqrt(number).is_integer() and isPolyndrom(str(int(math.sqrt(number)))):
                count += 1
        answer.append('Case #{0}: {1}'.format(case + 1, count))

    writeData(answer)


if __name__ == "__main__":
    solution()
