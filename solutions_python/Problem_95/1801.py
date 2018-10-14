#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from string import maketrans

if __name__ == '__main__':
    table = {
             'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v',
             'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l',
             'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't',
             'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm',
             'z': 'q', 'q': 'z'
        }

    count = int(raw_input())

    for index in xrange(count):
        line = raw_input()
        translated = ''
        for symbol in line:
            if symbol in table:
                translated += table[symbol]
            else:
                translated += symbol
        print 'Case #%d: %s' % (index + 1, translated)

    sys.exit()
