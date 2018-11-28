#!/usr/bin/env python

import sys
from string import *

count = 0
total_lines = 0

decoding_table = {'\n': '', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}

#lines = ['our language is impossible to understand',
#        'there are twenty six factorial possibilities',
#        'so it is okay if you want to just give up']

for line in sys.stdin.readlines():
    if total_lines == 0:
        total_lines = int(line)
        count += 1
    else:
        decoded = strip(''.join([decoding_table[letter] for letter in line]))
        print('Case #%d: %s'%(count, decoded))
        count += 1


