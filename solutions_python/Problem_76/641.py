#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math

MAXLEN = math.floor((6 * math.log(10)) / math.log(2)) + 1

def solve(case):
    bag = case
    bag.sort()
    
    cnt = [0] * MAXLEN
    for candy in bag:
        bitw = math.floor(math.log(candy) / math.log(2)) + 1
        for w in range(bitw):
            mask = 1 << w
            if candy & mask > 0:
                cnt[w] += 1

    for c in cnt:
        if c % 2 != 0:
            result = "NO"
            break
    else:
        sean = 0
        for candy in bag[1:]:
            sean += candy
        result = str(sean)
        
    return result

def patrick_sum(a, b):    
    return [(b1 ^ b2) for (b1, b2) in zip(a, b)]

def patrick_sum_dec(a, b):
    weight = 1
    sum = 0
    while a != 0 or b != 0:
        bit1 = a % 2
        bit2 = b % 2
        sum += ((bit1 + bit2) % 2) * weight
        weight *= 2
        a = int(a / 2)
        b = int(b / 2)

    return sum

def readfile(file):
    with open(file, "r") as f:
        cases = []
        T = int(f.readline())

        line = f.readline()
        while line != "":
            N = int(line)
            numbers = [int(n) for n in f.readline().split()]
            if N != len(numbers):
                print("Wrong data: " + line)
            cases.append(numbers)
            line = f.readline()

    if len(cases) != T:
        print("Wrong number of data read")
        sys.exit(1)
    
    return(cases)

#
# main
#
if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "sample.in"

cases = readfile(file)

with open(file + ".output", "w") as output:
    n = 1
    for case in cases:
        result = solve(case)
        msg = "Case #%d: %s" % (n, result)
        print(msg)
        output.write(msg + "\n")
        n += 1
