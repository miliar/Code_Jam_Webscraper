#!/usr/bin/python

import sys

mapping = {
    ' ' : ' ',
    'a' : 'y',
    'b' : 'h',
    'c' : 'e',
    'd' : 's',
    'e' : 'o',
    'f' : 'c',
    'g' : 'v',
    'h' : 'x',
    'i' : 'd',
    'j' : 'u',
    'k' : 'i',
    'l' : 'g',
    'm' : 'l',
    'n' : 'b',
    'o' : 'k',
    'p' : 'r',
    'q' : 'z',
    'r' : 't',
    's' : 'n',
    't' : 'w',
    'u' : 'j',
    'v' : 'p',
    'w' : 'f',
    'x' : 'm',
    'y' : 'a',
    'z' : 'q',
}

def solve(text):
    return ''.join([mapping[c] for c in text])

input = [line.strip() for line in sys.stdin]

for index in range(1, int(input[0]) + 1):
    print 'Case #%d: %s' % (index, solve(input[index]))
