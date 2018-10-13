#!/usr/bin/env python

import sys
import itertools

""" googleres to normal english """
translation_map = {
        'a': 'y',
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
        'q': 'z',
        'r': 't',
        's': 'n',
        't': 'w',
        'u': 'j',
        'v': 'p',
        'w': 'f',
        'x': 'm',
        'y': 'a',
        'z': 'q',
        ' ': ' '
        }


def open_input(file):
    try:
        f = open(file, "r")
        return f
    except:
        print "can not open ", file
        sys.exit(1)

def translate(line):
    ret = ''
    for c in line:
        ret += translation_map[c]
    return ret

def solve(input):
    """ T = # test case """
    T = int(input.readline())

    """ line = googlerese string """
    for i in range(T):
        line = input.readline().rstrip()
        print "Case #{0}: {1}".format(i+1, translate(line))

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(open_input(sys.argv[1]))
    else:
        print 'require input'
        sys.exit(1)
