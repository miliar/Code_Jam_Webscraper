#!/usr/bin/env python

import sys
file = open(sys.argv[1])
num_tests = int(file.readline()[:-1])
for X in range(1, num_tests+1):
    string = file.readline()[:-1]
    base = len (set(string))
    if base == 1:
        base = 2
    char_val = {}
    char_val[string[0]] = 1
    for char in string:
        if char not in char_val.keys():
            i = 0
            while i in char_val.values():
                i += 1
            char_val[char] = i
    num = ''
    for char in string:
        num = num + str(char_val[char])
    number = int(num, base)
    print "Case #%d: %d" % (X, number)

