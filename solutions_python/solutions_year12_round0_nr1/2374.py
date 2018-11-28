#!/usr/bin/python

import sys

l = {
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
'x': 'm',
'y': 'a',
'w': 'f',
'z': 'q',
' ': ' ' }

f = open(sys.argv[1], 'r')
cases = int(f.readline())
case = 0

for line in f.readlines():
  case += 1
  #do something
  output = "".join(l[c] for c in line if c != '\n')

  print("Case #{0}: {1}".format(case,output))

