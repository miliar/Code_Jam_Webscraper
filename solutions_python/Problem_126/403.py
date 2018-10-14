#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

def vowel(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

def consonant(c):
    return not vowel(c)

def solve(name, nvalue):
    substrs = set()

    a = 0
    L = len(name)

    while a + nvalue <= L:
        if all(map(consonant, name[a:a+nvalue])):
            for i in xrange(0,a+1):
                for j in range(a+nvalue,L+1):
                    substrs.add((i,j))

        a += 1


    return len(substrs)


if __name__ == "__main__":
    input_data = [line for line in sys.stdin.readlines()]

    num_tests = int(input_data.pop(0).strip())

    for i in range(0,num_tests):
        [name, nvalue] = input_data.pop(0).strip().split(" ")
        nvalue = int(nvalue)

        print "Case #%d: %d" % (i+1, solve(name, nvalue))

