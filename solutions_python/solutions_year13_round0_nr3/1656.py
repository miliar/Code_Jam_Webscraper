#!/bin/env python

import math

DEBUG = False

data = []

def genrate_square_palindrome(number):
    # palindrome check
    palin1 = str(number)
    len_palin1 = len(palin1)
    for i in range(len_palin1 / 2):
        if palin1[i] != palin1[-(i + 1)]:
            return None

    # square palindrome check
    square = number * number
    palin2 = str(square)
    len_palin2 = len(palin2)
    for i in range(len_palin2 / 2):
        if palin2[i] != palin2[-(i + 1)]:
            return None

    return square

def solve1(A, B):
    result = []
    st = int(math.sqrt(A))
    ed = int(math.sqrt(B)) + 1
    for i in range(st, ed):
        ret = genrate_square_palindrome(i)
        if ret != None and ret >= A and ret <= B:
            result.append(ret)
    if DEBUG:
        print result
    return len(result)

def solve(A, B):
    result = []
    for i in data:
        if A <= i and i <= B:
            result.append(i)
        elif i > B:
            break
    return len(result)

index = 1
max_index = int(math.sqrt(10**14)) + 1
while True:
    ret = genrate_square_palindrome(index)
    index += 1
    if ret != None:
        data.append(ret)
    if index > max_index:
        break

tc = int(raw_input())

for tc_index in range(tc):
    (A, B) = map(int, raw_input().split())
    print "Case #%d: %s" % (tc_index + 1, solve(A, B))
