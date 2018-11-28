#!/usr/bin/python
import sys

infile = open(sys.argv[1], 'r')

numCases = int(infile.readline())

charMap = {}
charMap['a'] = 'y'
charMap['b'] = 'h'
charMap['c'] = 'e'
charMap['d'] = 's'
charMap['e'] = 'o'
charMap['f'] = 'c'
charMap['g'] = 'v'
charMap['h'] = 'x'
charMap['i'] = 'd'
charMap['j'] = 'u'
charMap['k'] = 'i'
charMap['l'] = 'g'
charMap['m'] = 'l'
charMap['n'] = 'b'
charMap['o'] = 'k'
charMap['p'] = 'r'
charMap['q'] = 'z'
charMap['r'] = 't'
charMap['s'] = 'n'
charMap['t'] = 'w'
charMap['u'] = 'j'
charMap['v'] = 'p'
charMap['w'] = 'f'
charMap['x'] = 'm'
charMap['y'] = 'a'
charMap['z'] = 'q'
charMap[' '] = ' '

for i in range(numCases):
    line = infile.readline().strip()
    newline = ''
    for char in line:
        newline += charMap[char]
    print "Case #%d: %s" % (i+1, newline)
