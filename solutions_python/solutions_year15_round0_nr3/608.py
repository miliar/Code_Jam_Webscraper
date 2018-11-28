#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""See http://martin-thoma.com for more mini code samples."""


def quadopt(a, b):
    if a == '1':
        return b
    elif b == '1':
        return a

    if a == 'i':
        if b == 'i':
            return '-1'
        elif b == 'j':
            return 'k'
        elif b == 'k':
            return '-j'
    elif a == 'j':
        if b == 'i':
            return '-k'
        elif b == 'j':
            return '-1'
        elif b == 'k':
            return 'i'
    elif a == 'k':
        if b == 'i':
            return 'j'
        elif b == 'j':
            return '-i'
        elif b == 'k':
            return '-1'


def solve(chars, X):
    curr_char = '1'
    is_neg = False
    got_i = False
    got_j = False
    got_k = False
    for char in chars*X:
        next_char = quadopt(curr_char, char)
        if next_char.startswith('-'):
            is_neg = not is_neg
            next_char = next_char[1:]
        if not is_neg and next_char == 'i' and not got_i:
            got_i = True
            curr_char = '1'
        elif not is_neg and next_char == 'j' and got_i and not got_j:
            got_j = True
            curr_char = '1'
        elif not is_neg and next_char == 'k' and got_i and got_j and not got_k:
            got_k = True
            curr_char = '1'
        else:
            curr_char = next_char
    #print([got_i, got_j, got_k, is_neg, curr_char])
    if got_i and got_j and got_k and curr_char == '1' and (not is_neg):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    testcases = int(raw_input())

    for caseNr in range(1, testcases+1):
        L, X = [int(el) for el in raw_input().split(" ")]
        chars = raw_input()
        print("Case #%i: %s" % (caseNr, solve(chars, X)))
