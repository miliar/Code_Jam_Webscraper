#!/usr/bin/env python

MAPPING = {}
MAPPING[' '] = ' '
MAPPING['a'] = 'y'
MAPPING['b'] = 'h'
MAPPING['c'] = 'e'
MAPPING['d'] = 's'
MAPPING['e'] = 'o'
MAPPING['f'] = 'c'
MAPPING['g'] = 'v'
MAPPING['h'] = 'x'
MAPPING['i'] = 'd'
MAPPING['j'] = 'u'
MAPPING['k'] = 'i'
MAPPING['l'] = 'g'
MAPPING['m'] = 'l'
MAPPING['n'] = 'b'
MAPPING['o'] = 'k'
MAPPING['p'] = 'r'
MAPPING['r'] = 't'
MAPPING['s'] = 'n'
MAPPING['t'] = 'w'
MAPPING['u'] = 'j'
MAPPING['v'] = 'p'
MAPPING['w'] = 'f'
MAPPING['x'] = 'm'
MAPPING['y'] = 'a'
MAPPING['z'] = 'q'
MAPPING['q'] = 'z'

def remap(string):
    return ''.join([MAPPING[i] for i in string])

def main():
    T = int(raw_input().strip())
    for i in range(T):
        in_str = raw_input()
        print "Case #%d: %s" % (i + 1, remap(in_str))

if __name__ == '__main__':
    main()

