#!/usr/bin/env python
# Google Code Jam Entry
# Round1C - A - 
#
# Copyright (C) 2009 Robert Wallis 2009-09-13

import sys
import threading
import time
from os import path

if len(sys.argv) <= 1:
    print("Please type the name of the input [name].in.txt")
    exit()
prefix = sys.argv[1]
infile = open(prefix+".in.txt", "r")
outfile = open(prefix+time.strftime("%H%M%S")+".out.txt", "w+")

# based on (no pun intended) http://code.activestate.com/recipes/576435/


def base_to_i(chars, string):
    map_dict = {}
    base = len(chars)
    for c in range(base):
        map_dict[c] = chars[c]
        map_dict[chars[c]] = c
    x = [a for a in string]
    x.reverse()
    value = 0
    for i in range(len(x)):
        c = x[i]
        value += (map_dict[c] * pow(base,i))
    return value

try:
    for case in range(1, int(infile.readline())+1):
        alien = infile.readline().strip()
        print(alien)
        possible = set()
        chars = []
        for c in alien:
            if c not in possible:
                possible.add(c)
                chars.append(c)
        if len(chars) == 1:
            chars.append('0')
        z = chars[1]
        chars[1] = chars[0]
        chars[0] = z
        print chars
        number = base_to_i(chars, alien)
        
        answer = number
        output = 'Case #%d: %s\n' % (case, answer)
        outfile.write(output)
        sys.stdout.write(output)
finally:
    infile.close()
    outfile.flush()
    outfile.close()

