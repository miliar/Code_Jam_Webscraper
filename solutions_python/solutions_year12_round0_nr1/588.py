#!/usr/bin/python

import sys

reverse_google = {
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
    ' ' : ' '
}


lines = sys.stdin.readlines()
for t, input_ in enumerate(lines[1:], 1):
    input_ = input_.strip()
    answer = ''.join(map(lambda c: reverse_google[c], input_))
    print "Case #%d: %s" % (t, answer)

