#!/usr/bin/env python
# -*- coding: utf-8 -*-

def to_list(number):
    ret = list()
    while 0 != number:
        ret.insert(0, number%10)
        number = number/10
    return ret

def to_int(line):
    ret = 0
    l = len(line) - 1
    for idx in range(0, len(line), 1):
        ret += line[idx] * (10 ** (l-idx))
    return ret

def solve(cipher):
    ret = -1
    for i in range(int(cipher)+1):
        line = to_list(i)
        line.sort()
        x = to_int(line)
        ret = max(ret, x)
    return ret

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
