#!/bin/python
import os, sys

filename = "A-small-attempt0"

mapping = {
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
  'z': 'q'
}

infile = open("%s.in" % filename,"rb")
outfile = open("%s.out" % filename, "wb")
T = int(infile.readline())
for index in xrange(T):
  t = ''.join(mapping.get(x,x) for x in infile.readline().rstrip())
  outfile.write("Case #%d: %s\n" % (index+1, t))
