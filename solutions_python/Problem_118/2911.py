#!/usr/bin/env python3

# Copyright (c) 2013 Vincent Cheng <Vincentc1208@gmail.com>
# Licensed under the GNU GPLv3: http://www.gnu.org/licenses/gpl-3.0-standalone.html

# Note: only works for integers up to the value of python's sys.maxsize,
# usually 2**31 - 1 on a 32-bit platform and 2**63 - 1 on a 64-bit platform.

import math

# Filenames go here
in_file = 'C-small-attempt0.in'
out_file = 'output.txt'

output = []
DEBUG = True

def is_palindrome(num):
    return repr(num) == (repr(num))[::-1]

def is_square(num):
    n = math.sqrt(num)
    return abs(int(n) - n) < 1e-15

with open(in_file, 'r') as f:
    for line in f:
        count = 0
        if DEBUG: print(line)
        lsplit = line.split()
        if DEBUG: print(lsplit)
        if len(lsplit) == 2:
            begin = int(lsplit[0])
            if DEBUG: print(begin)
            end = int(lsplit[1])
            if DEBUG: print(end)
            for i in range(begin, end+1):
                # Optimization: i has to be of odd length to be a palindrome
                if len(repr(i)) % 2 == 1:
                    if is_palindrome(i) and is_square(i):
                        if is_palindrome(int(math.sqrt(i))):
                            count += 1
                            if DEBUG: print(i)
            output.append(count)

if DEBUG: print(output)
            
with open(out_file, 'w+') as f:
    index = 1
    for i in output:
        f.write('Case #' + repr(index) + ': ' + repr(i) + '\n')
        index += 1
