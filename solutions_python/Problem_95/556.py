#!/usr/bin/env python
'''
Juan Manuel Caicedo
cavorite.com
'''

import sys

def translate(line):
    chars = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 
        'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 
        'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 
        't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

    return ''.join([chars[c] for c in line])


def main():
    lines = sys.stdin

    cases = int(lines.next())
    for i in xrange(1, cases+1):
        l = lines.next()
        normal = translate(l.strip())
        print 'Case #%d: %s' % (i, normal)

if __name__ == '__main__':
    main()

