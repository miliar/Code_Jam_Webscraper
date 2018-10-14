#!/usr/bin/python

translation_table = {
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

def translate(s):
    return ''.join([translation_table[c] for c in s])

i = 0
for l in file('A-small-attempt0.in', 'r'):
    l = l.strip()
    if i > 0:
        print 'Case #%d: %s' % (i, translate(l))
    i = i + 1
