#!/usr/bin/env python

from __future__ import print_function, division

import math
import os
import os.path
import sys


inFile = open(sys.argv[1], "rt")
outFile = open(sys.argv[2], "wt")

CHAR_MAP = {'a': 'y',
            'b': 'h',
            'c': 'e',
            'd': 's',
            'e': 'o',
            'f': 'c',
            'g': 'v',
            'h': 'x',
            'i': 'd',
            'j': 'u',
            'k': 'i',
            'l': 'g',
            'm': 'l',
            'n': 'b',
            'o': 'k',
            'p': 'r',
            'r': 't',
            's': 'n',
            't': 'w',
            'u': 'j',
            'v': 'p',
            'w': 'f',
            'x': 'm',
            'y': 'a',
            'q': 'z',
            'z': 'q',
            ' ': ' '}


def main():
    numLines = int(inFile.readline())

    for i in xrange(numLines):
        inText = inFile.readline().strip()
        outChars = [CHAR_MAP[c] for c in inText]
        outText = "".join(outChars)

        outFile.write("Case #{0:d}: {1}\n".format(i+1, outText))


if __name__ == "__main__": main()
