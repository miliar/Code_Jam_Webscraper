#!/usr/bin/env python3

import sys

charMap = {
'a': 'y',
'c': 'e',
'b': 'h',
'e': 'o',
'd': 's',
'g': 'v',
'f': 'c',
'i': 'd',
'h': 'x',
'k': 'i',
'j': 'u',
'm': 'l',
'l': 'g',
'o': 'k',
'n': 'b',
'q': 'z',
'p': 'r',
's': 'n',
'r': 't',
'u': 'j',
't': 'w',
'w': 'f',
'v': 'p',
'y': 'a',
'x': 'm',
'z': 'q',
' ': ' ',
}

def translate(s):
	return ''.join([charMap[x] for x in s])

numcases = int(sys.stdin.readline())
for i in range(numcases):
	print("Case #%d: %s" % (i+1, translate(sys.stdin.readline().strip())))
