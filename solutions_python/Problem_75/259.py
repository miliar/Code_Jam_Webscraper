#!/usr/bin/env python
# encoding: utf-8

import sys

def parse_elements(fileDescriptor):
    # Returns a dict of joinable elems, opposit elements, and the list elements
    f = fileDescriptor
    line = (f.readline()).split(' ')
    index = 0
    comb_dict = {}
    opp_dict = {}
    # Number of combinations
    c = int(line[index])
    index += 1

    for i in xrange(index, index+c):
        add_combinations(line[index], comb_dict)
    # Number of opposed
    index += c
    d = int(line[index])
    index += 1

    for i in xrange(index, index+d):
        add_opposed(line[index], opp_dict)

    index += d
    # Length of casts
    n = int(line[index])
    index += 1
    l = list(line[index])
    # Take off EOL
    l.pop(-1)

    return comb_dict, opp_dict, l

def add_combinations(string, comb_dict):
    assert(len(string) == 3)
    if not comb_dict.has_key(string[0]):
        comb_dict[string[0]] = []
    comb_dict[string[0]].append((string[1], string[2]))

    if string[0] != string[1]:
        if not comb_dict.has_key(string[1]):
            comb_dict[string[1]] = []
        comb_dict[string[1]].append((string[0], string[2]))

def add_opposed(string, opp_dict):
    assert(len(string) == 2)
    if not opp_dict.has_key(string[0]):
        opp_dict[string[0]] = []
    if not opp_dict.has_key(string[1]):
        opp_dict[string[1]] = []

    opp_dict[string[0]].append(string[1])
    opp_dict[string[1]].append(string[0])


def can_combine(sequence, index, comb_dict):
    # Se puede combinar un elem con el sig
    result = None

    if index < len(sequence)-1:
        # The las element can't be combined with a next one
        if comb_dict.has_key(sequence[index]):
            combinationList = comb_dict[sequence[index]]

            for comb in combinationList:
                if comb[0] == sequence[index+1]:
                    result = comb[1]
                break
    return result


def apply_opp(sequence, index, opp_dict, comb_dict):
    assert(opp_dict.has_key(sequence[index]))

    opp = -1
    result = False

    oppList = opp_dict[sequence[index]]
    for i in xrange(index+1, len(sequence)):
        if sequence[i] in oppList:
            if not can_combine(sequence, i-1, comb_dict):
                opp = i
                break

    if opp != -1:
        # I have found two opp elems
        i = 0
        while i <= opp:
            sequence.pop(0)
            i += 1
        result = True

    return result


def step(sequence, index, comb_dict, opp_dict):
    # I always need at least 2 elems
    assert(index < len(sequence) - 1)
    result = True

    comb = can_combine(sequence, index, comb_dict)
    if comb:
        sequence.pop(index)
        sequence.pop(index)
        sequence.insert(index, comb)
    else:
        # It's an opposite
        if opp_dict.has_key(sequence[index]):
            if apply_opp(sequence, index, opp_dict, comb_dict):
                result = False
    return result

def interact_elems(sequence, comb_dict, opp_dict):
    index = 0

    while index < len(sequence) - 1:
        r = step(sequence, index, comb_dict, opp_dict)
        if not r:
            index = 0
        else:
            index += 1

def solve(fileName):
    f = open(fileName, "r")
    fsol = open("solution.txt", "w")

    # Number of testcases
    t = int(f.readline())

    for i in xrange(t):
        comb, opp, l = parse_elements(f)
        interact_elems(l, comb, opp)
        fsol.write("Case #%d: " %(i+1))
        pprint(l, fsol)

def pprint(l, fsol):
    fsol.write('[')
    if l:
        for i in xrange(len(l)-1):
            fsol.write(str(l[i]) + ', ')
        # Las elem
        fsol.write(str(l[len(l)-1]))
    fsol.write(']')
    fsol.write('\n')



