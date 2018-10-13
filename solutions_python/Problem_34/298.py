#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def mix(first, second):
    answer = []
    if first == []:
        return second
    elif second == []:
        return first
    for i, ei in enumerate(first):
        for j, ej in enumerate(second):
            answer.append(first[i] + second[j])
    return answer

def parse(pattern):
    parenthesis = False
    interpretations = []
    for character in pattern:
        if character == '(':
            parenthesis = True
            temp = []
        elif character == ')':
            parenthesis = False
            interpretations.append(temp)
        else:
            if parenthesis:
                temp.append(character)
            else:
                interpretations.append(character)
    return interpretations

def count_possibilities(dictionary, pattern):
    valid = 0
    interpretations = parse(pattern)
    for word in dictionary:
        ok = True
        for i,character in enumerate(word):
            if character not in interpretations[i]:
                ok = False
        if ok:
            valid += 1
    return valid

if __name__ == '__main__':
    dictionary = []
    L, D, N = [int(i) for i in sys.stdin.readline().strip().split()]

    for i in range(D):
        dictionary.append(sys.stdin.readline().strip())
    for i in range(N):
        result = count_possibilities(dictionary,
                sys.stdin.readline().strip())
        print "Case #%d: %d" % (i + 1, int(result))

