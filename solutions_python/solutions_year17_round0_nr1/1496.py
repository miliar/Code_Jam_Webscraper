#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python solve.py < input.txt > result.txt
def flip(pancakes, index, size):
    if index > (len(pancakes)-size):
        index = len(pancakes)-size-1
    for x in range(size):
        if pancakes[index+x] == '-':
           pancakes[index+x] = '+'
        else:
            pancakes[index+x] = '-'

def solve(nbr):
    n_and_k = nbr.split(" ");
    pancakes = list(n_and_k[0])
    size = int(n_and_k[1])
    i = 0
    flips = 0;
    while i != len(pancakes):

        if pancakes[i] == '-':

            flips += 1
            flip(pancakes, i, size)
        i += 1
    if ''.join(pancakes).find("-") != -1:
        return "IMPOSSIBLE"
    else:
        return flips


if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
